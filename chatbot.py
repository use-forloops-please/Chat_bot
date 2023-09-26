import openai
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

openai.api_key = "Add your own key to make this chat bot work"

def chat_with_bot():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    
    messages_text.config(state=tk.NORMAL)
    messages_text.insert(tk.END, "You: " + user_input + "\n", "user")
    messages_text.insert(tk.END, "\n", "newline")
    messages_text.config(state=tk.DISABLED)
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    
    bot_response = chat_with_bot_api(messages)
    
    messages_text.config(state=tk.NORMAL)
    messages_text.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
    messages_text.insert(tk.END, "\n", "newline")
    messages_text.config(state=tk.DISABLED)

def chat_with_bot_api(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# Create the main window
root = tk.Tk()
root.title("Chatbot GUI")

# Set background and foreground colors
root.configure(bg='blue')

# Create a text widget to display messages
messages_text = Text(root, wrap=tk.WORD, state=tk.DISABLED)
messages_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Set colors for user and bot messages
messages_text.tag_configure("user", foreground="red")
messages_text.tag_configure("bot", foreground="blue")
messages_text.tag_configure("newline", spacing1=5)

# Create a scrollbar for the text widget
scrollbar = Scrollbar(root, command=messages_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages_text.config(yscrollcommand=scrollbar.set)

# Create an entry widget for user input
user_entry = Entry(root)
user_entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Create a button to send user input
send_button = Button(root, text="Send", command=chat_with_bot)
send_button.pack()

# Start the GUI main loop
root.mainloop()

