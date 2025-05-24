import wikipedia
from termcolor import colored

def ai_wiki():
    print(colored("Futuristic Wiki AI Interface", "cyan", attrs=["bold"]))
    while True:
        query = input(colored("Enter topic (or 'exit'): ", "green"))
        if query.lower() in ["exit", "quit"]:
            break
        try:
            summary = wikipedia.summary(query, sentences=3)
            print(colored("\nResponse:\n", "blue", attrs=["bold"]))
            print(colored(summary, "white"))
        except Exception as e:
            print(colored("Error: " + str(e), "red"))

ai_wiki()
import random

def ai_wiki():
    greetings = [
        "Welcome back, curious mind.",
        "Online. Ready to explore.",
        "Activated. Feed me knowledge.",
        "Hello, seeker of facts.",
        "System live. Awaiting input."
    ]
    print(colored(random.choice(greetings), "magenta", attrs=["bold"]))