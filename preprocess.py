import re
from nltk.stem import SnowballStemmer

_stemmer = SnowballStemmer("english")

def preprocess_text(text: str) -> str:
    """
    Convert text into a normalized form suitable for FAQ matching.

    Steps:
    1. lowercase
    2. keep alphabetic/numeric tokens
    3. remove very short noise tokens
    4. stem English words
    """
    text = text.lower().strip()
    tokens = re.findall(r"[a-z0-9']+", text)
    cleaned = []
    for token in tokens:
        token = token.strip("'")
        if not token:
            continue
        if len(token) == 1 and token not in {"i", "a"}:
            continue
        cleaned.append(_stemmer.stem(token))
    return " ".join(cleaned)
