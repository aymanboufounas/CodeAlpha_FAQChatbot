import tkinter as tk
from tkinter import ttk
from pathlib import Path
from datetime import datetime

from chatbot import FAQChatbot

APP_BG = "#0f172a"
PANEL_BG = "#111827"
CHAT_BG = "#0b1220"
INPUT_BG = "#1f2937"
TEXT = "#e5e7eb"
MUTED = "#94a3b8"
ACCENT = "#22c55e"
USER = "#2563eb"
BOT = "#374151"
ERROR = "#ef4444"


class FAQChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CodeAlpha FAQ Chatbot")
        self.geometry("900x650")
        self.minsize(720, 520)
        self.configure(bg=APP_BG)

        faq_file = Path(__file__).parent / "data" / "faqs.json"
        self.bot = FAQChatbot(faq_file)

        self._build_styles()
        self._build_ui()
        self._add_message(
            "bot",
            "Hello! 👋 I'm the CodeAlpha FAQ Assistant.\nAsk me about internship tasks, GitHub submission, certificates, or how this chatbot works."
        )

    def _build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Send.TButton",
            background=ACCENT,
            foreground="#052e16",
            font=("Segoe UI", 11, "bold"),
            borderwidth=0,
            padding=(18, 10)
        )
        style.map("Send.TButton", background=[("active", "#4ade80")])

    def _build_ui(self):
        header = tk.Frame(self, bg=PANEL_BG, height=90)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🤖  CodeAlpha FAQ Chatbot",
            bg=PANEL_BG,
            fg=TEXT,
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", padx=24, pady=(16, 0))

        tk.Label(
            header,
            text="NLP • TF-IDF • Cosine Similarity • Offline",
            bg=PANEL_BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=26, pady=(3, 0))

        body = tk.Frame(self, bg=APP_BG)
        body.pack(fill="both", expand=True, padx=18, pady=18)

        self.chat = tk.Text(
            body,
            bg=CHAT_BG,
            fg=TEXT,
            insertbackground=TEXT,
            wrap="word",
            relief="flat",
            font=("Segoe UI", 11),
            padx=18,
            pady=18,
            state="disabled",
            spacing1=2,
            spacing3=10
        )
        self.chat.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(body, command=self.chat.yview)
        scrollbar.pack(side="right", fill="y")
        self.chat.configure(yscrollcommand=scrollbar.set)

        self.chat.tag_configure("user_name", foreground="#60a5fa", font=("Segoe UI", 10, "bold"))
        self.chat.tag_configure("bot_name", foreground="#4ade80", font=("Segoe UI", 10, "bold"))
        self.chat.tag_configure("message", foreground=TEXT, font=("Segoe UI", 11))
        self.chat.tag_configure("meta", foreground=MUTED, font=("Segoe UI", 8))

        bottom = tk.Frame(self, bg=APP_BG)
        bottom.pack(fill="x", padx=18, pady=(0, 18))

        self.entry = tk.Entry(
            bottom,
            bg=INPUT_BG,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            font=("Segoe UI", 12)
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=11, padx=(0, 10))
        self.entry.bind("<Return>", self._send_event)
        self.entry.focus_set()

        send_btn = ttk.Button(
            bottom,
            text="Send",
            style="Send.TButton",
            command=self.send_message
        )
        send_btn.pack(side="right")

        hint = tk.Label(
            self,
            text="Try: “How do I submit my task?”  •  “Does it work offline?”  •  “What is cosine similarity?”",
            bg=APP_BG,
            fg=MUTED,
            font=("Segoe UI", 9)
        )
        hint.pack(pady=(0, 12))

    def _send_event(self, _event):
        self.send_message()

    def send_message(self):
        message = self.entry.get().strip()
        if not message:
            return

        self.entry.delete(0, "end")
        self._add_message("user", message)

        response, score, matched_question = self.bot.get_response(message)

        metadata = f"Similarity: {score:.2f}"
        if matched_question:
            metadata += f"  •  Matched FAQ: {matched_question}"

        self._add_message("bot", response, metadata)

    def _add_message(self, sender: str, message: str, metadata: str | None = None):
        self.chat.configure(state="normal")

        timestamp = datetime.now().strftime("%H:%M")
        if sender == "user":
            self.chat.insert("end", f"You  {timestamp}\n", "user_name")
        else:
            self.chat.insert("end", f"Bot  {timestamp}\n", "bot_name")

        self.chat.insert("end", message + "\n", "message")

        if metadata:
            self.chat.insert("end", metadata + "\n", "meta")

        self.chat.insert("end", "\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")


if __name__ == "__main__":
    app = FAQChatApp()
    app.mainloop()
