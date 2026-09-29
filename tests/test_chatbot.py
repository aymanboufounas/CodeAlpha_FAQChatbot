from pathlib import Path
from chatbot import FAQChatbot

def test_known_question():
    bot = FAQChatbot(Path(__file__).parents[1] / "data" / "faqs.json")
    answer, score, matched = bot.get_response("Where do I upload my code?")
    assert score > 0
    assert matched is not None
    assert "GitHub" in answer

def test_unknown_question():
    bot = FAQChatbot(Path(__file__).parents[1] / "data" / "faqs.json")
    answer, score, matched = bot.get_response("How is the weather on Mars today?")
    assert matched is None
