import time

class ChatbotBase:
    def __init__(self, name="Emotion AI"):
        self.name = name
        self.active = True

    def greeting(self):
        print("\nBot:", f"Hi 😊 I am {self.name}. I’m here to listen to you.\n")

    def farewell(self):
        print("\nBot: Take care ❤️ I’m always here if you need me.\n")

    def conversation_is_active(self):
        return self.active

    def stop(self):
        self.active = False

    # ✨ human-like typing effect
    def type_effect(self, message):
        for char in message:
            print(char, end="", flush=True)
            time.sleep(0.02)
        print()