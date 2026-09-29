# CodeAlpha FAQ Chatbot

A simple NLP-based FAQ chatbot created for **CodeAlpha Artificial Intelligence Internship — Task 2**.

## Project Objective

The application stores a collection of frequently asked questions and answers, preprocesses user input using NLP, and finds the closest FAQ using **TF-IDF vectorization** and **cosine similarity**.

It does **not** use ChatGPT or any external AI API.

## Features

- FAQ dataset stored in JSON
- NLP text preprocessing
- NLTK Snowball stemming
- TF-IDF vectorization
- Unigram + bigram features
- Cosine similarity matching
- Confidence threshold for unknown questions
- Desktop chat interface using Tkinter
- Offline execution
- CLI mode included
- Easy-to-edit FAQ dataset

## Project Structure

```text
CodeAlpha_FAQChatbot/
├── app.py
├── chatbot.py
├── cli.py
├── preprocess.py
├── requirements.txt
├── .gitignore
├── data/
│   └── faqs.json
└── tests/
    └── test_chatbot.py
```

## How It Works

1. The user types a question.
2. The input is converted to lowercase and cleaned.
3. Words are stemmed using NLTK.
4. Stored FAQ questions are converted to TF-IDF vectors.
5. The user question is converted using the same vectorizer.
6. Cosine similarity compares the user vector with all FAQ vectors.
7. The chatbot returns the answer belonging to the highest-scoring FAQ.
8. If the score is below the confidence threshold, the chatbot asks the user to rephrase.

## Installation

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the GUI

```bash
python app.py
```

## Run in the Terminal

```bash
python cli.py
```

## Add More FAQs

Edit:

```text
data/faqs.json
```

Each record uses this format:

```json
{
  "question": "Your question?",
  "answer": "Your answer."
}
```

Restart the application after modifying the FAQ dataset.

## Core Technologies

- Python
- Tkinter
- NLTK
- scikit-learn
- TF-IDF
- Cosine Similarity

## Example

**User**

```text
Where should I upload my project?
```

**Bot**

```text
Upload your complete source code to GitHub in a repository named using the format CodeAlpha_ProjectName.
```

## CodeAlpha Task 2 Requirements Covered

- FAQ collection: ✅
- NLP preprocessing: ✅
- Similarity matching: ✅
- Best matching answer: ✅
- Chat UI: ✅

## Suggested GitHub Repository Name

```text
CodeAlpha_FAQChatbot
```

## Author

Ayman Boufounas

Built for the CodeAlpha Artificial Intelligence Internship.
