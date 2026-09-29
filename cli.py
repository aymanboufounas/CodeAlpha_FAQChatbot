from pathlib import Path
from chatbot import FAQChatbot

def main():
    bot = FAQChatbot(Path(__file__).parent / "data" / "faqs.json")
    print("CodeAlpha FAQ Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break
        answer, score, matched = bot.get_response(user_input)
        print(f"Bot: {answer}")
        print(f"[score={score:.2f}" + (f", match={matched}" if matched else "") + "]")

if __name__ == "__main__":
    main()
