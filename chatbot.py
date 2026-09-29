import json
from pathlib import Path
from typing import Dict, List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text

DEFAULT_THRESHOLD = 0.28


class FAQChatbot:
    def __init__(self, faq_path: str | Path, threshold: float = DEFAULT_THRESHOLD):
        self.faq_path = Path(faq_path)
        self.threshold = threshold
        self.faqs: List[Dict[str, str]] = self._load_faqs()
        self.questions = [item["question"] for item in self.faqs]
        self.processed_questions = [preprocess_text(q) for q in self.questions]

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True
        )
        self.faq_matrix = self.vectorizer.fit_transform(self.processed_questions)

    def _load_faqs(self) -> List[Dict[str, str]]:
        with self.faq_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list) or not data:
            raise ValueError("FAQ file must contain a non-empty list.")

        for item in data:
            if "question" not in item or "answer" not in item:
                raise ValueError("Each FAQ must contain 'question' and 'answer'.")

        return data

    def get_response(self, user_input: str) -> Tuple[str, float, str | None]:
        cleaned = preprocess_text(user_input)

        if not cleaned:
            return (
                "Please type a question so I can help you.",
                0.0,
                None,
            )

        user_vector = self.vectorizer.transform([cleaned])
        similarities = cosine_similarity(user_vector, self.faq_matrix).flatten()

        best_index = int(similarities.argmax())
        best_score = float(similarities[best_index])
        best_faq = self.faqs[best_index]

        if best_score < self.threshold:
            return (
                "I couldn't find a confident FAQ match. Please rephrase your question or ask about CodeAlpha, submission, certificates, GitHub, or how this chatbot works.",
                best_score,
                None,
            )

        return best_faq["answer"], best_score, best_faq["question"]
