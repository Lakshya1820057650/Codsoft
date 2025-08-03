import tkinter as tk
from tkinter import scrolledtext
import re
import datetime
import random

# Lexi's brain
def get_response(user_input):
    user_input = user_input.lower().strip()

    if re.search(r"\b(exit|bye|quit|goodbye)\b", user_input):
        return "Goodbye! It was lovely chatting with you. Take care! 👋"

    elif re.search(r"\b(hello|hi|hey|greetings|yo|sup)\b", user_input):
        return random.choice([
            "Hey there! 😊",
            "Hello! How can I help you today?",
            "Hi! Ready to chat?",
            "Greetings, friend! 👋"
        ])

    elif re.search(r"\b(who are you|what are you|your name|tell me about yourself)\b", user_input):
        return "I'm Lexi 🤖, your friendly rule-based chatbot! I love jokes, timekeeping, and casual chats."

    elif re.search(r"\b(help|support|assist|what can you do)\b", user_input):
        return (
            "Here's what I can help with:\n"
            "- Tell you the current time 🕒\n"
            "- Share a joke 😂\n"
            "- Chat casually 💬\n"
            "- Say goodbye when you're done 👋"
        )

    elif re.search(r"\b(time|clock|current time|what time is it)\b", user_input):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now} ⏰"

    elif re.search(r"\b(joke|funny|laugh|make me laugh)\b", user_input):
        return random.choice([
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
            "Parallel lines have so much in common… it’s a shame they’ll never meet.",
            "Why did the math book look sad? Because it had too many problems.",
            "I told my computer I needed a break, and now it won’t stop sending me KitKat ads."
        ])

    elif re.search(r"\b(how are you|how do you feel|what's up)\b", user_input):
        return "I'm just a bunch of code, but I'm feeling logically fantastic today! 😄"

    elif re.search(r"\b(weather|rain|sunny|forecast|temperature)\b", user_input):
        return "I can't check the weather, but I hope it's nice where you are! ☀️"

    else:
        return random.choice([
            "Hmm... I didn't quite get that. Try asking something else or type 'help' for options.",
            "I'm not sure I understand. Want to hear a joke instead?",
            "Interesting... but I might need more context. Try rephrasing?",
            "Lexi's still learning! Can you ask that a different way?"
        ])

# GUI setup
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = get_response(user_input)
    chat_window.insert(tk.END, f"Lexi 🤖: {response}\n\n")
    entry.delete(0, tk.END)
    chat_window.see(tk.END)
    if "goodbye" in response.lower():
        root.after(2000, root.destroy)

root = tk.Tk()
root.title("Lexi 🤖 Chatbot")
root.geometry("500x500")
root.resizable(False, False)

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Lexi 🤖: Hi! I'm Lexi, your chatbot companion. Type 'exit' to end our chat.\n\n")

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.LEFT)

root.mainloop()