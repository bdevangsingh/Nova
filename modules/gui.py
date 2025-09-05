# File: modules/gui.py
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading
import queue
import time
from modules.nlp import generate_response

class GPTChatGUI:
    def __init__(self, bot_name: str):
        self.bot_name = bot_name
        self.response_queue = queue.Queue()

        self.root = tk.Tk()
        self.root.title(f"{bot_name} Chat")
        self._build_ui()
        self.root.after(100, self._process_responses)

    def _build_ui(self):
        self.text_area = scrolledtext.ScrolledText(self.root, state="disabled", font=("Segoe UI", 12))
        self.text_area.pack(padx=10, pady=10, fill="both", expand=True)

        self.entry = tk.Entry(self.root, font=("Segoe UI", 12))
        self.entry.pack(padx=10, pady=(0, 10), fill="x")
        self.entry.bind("<Return>", self._on_send)

    def _append_message(self, sender, message):
        self.text_area.configure(state="normal")
        self.text_area.insert("end", f"{sender}: {message}\n")
        self.text_area.configure(state="disabled")
        self.text_area.see("end")

    def _on_send(self, event=None):
        user_text = self.entry.get().strip()
        if user_text:
            self.entry.delete(0, "end")
            self._append_message("You", user_text)
            threading.Thread(target=self._get_bot_response, args=(user_text,), daemon=True).start()

    def _get_bot_response(self, user_text):
        response = generate_response(user_text)
        self.response_queue.put(response)

    def _process_responses(self):
        try:
            while True:
                response = self.response_queue.get_nowait()
                self._append_message(self.bot_name, response)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self._process_responses)

    def run(self):
        self._append_message(self.bot_name, "Hi! I'm NOVA, your assistant. How can I help you today?")
        self.root.mainloop()
