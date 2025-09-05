
# File: modules/nlp.py
import random

_PREDEFINED_RESPONSES = {
    "hello": ["Hi there! 👋", "Hello! How can I help you today?"],
    "help": ["I'm here to assist you. What do you need help with?"],
    "bye": ["Goodbye! Take care!", "See you later!"],
    "how are you": ["I'm just code, but I'm doing great! How about you?"],
    "what is your name": ["I'm NOVA, your smart assistant."]
}


# Simulate GPT-like logic for small talk and helpfulness
def generate_response(text: str) -> str:
    text = text.lower()

    for key in _PREDEFINED_RESPONSES:
        if key in text:
            return random.choice(_PREDEFINED_RESPONSES[key])

    # Basic reasoning/answering
    if "calculate" in text or any(op in text for op in ["+", "-", "*", "/"]):
        try:
            result = eval(text.split("calculate")[-1].strip())
            return f"The result is {result}."
        except:
            return "Sorry, I couldn't calculate that."

    if "what is" in text:
        return f"That's an interesting question. Here's what I found: [Simulated GPT-like thoughtful answer]."

    return random.choice([
        "That's a great point. Let me think about it...",
        "I'm not sure, but I'd love to learn more.",
        "Can you explain more so I can understand better?"
    ])


# File: modules/__init__.py
# Leave empty or add common imports if needed