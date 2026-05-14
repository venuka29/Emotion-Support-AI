import random

class ResponseBuilder:

    def __init__(self):
        self.responses = {
            "greeting": [
                "Hi 😊 how are you feeling today?",
                "Hello ❤️ I'm here for you.",
                "Hey 😊 tell me what's on your mind."
            ],

            "sad": [
                "I’m really sorry to hear that 💔 what happened?",
                "That sounds really tough... I’m here with you.",
                "You don’t have to go through this alone ❤️",
                "I’m listening… take your time.",
                "That must be really hard for you."
            ],

            "happy": [
                "That’s amazing 😊 tell me more!",
                "I’m really happy for you ❤️",
                "That’s wonderful to hear!",
                "You deserve that happiness 😊",
                "That made me smile too!"
            ],

            "love": [
                "That sounds really beautiful ❤️",
                "Love is a powerful feeling 😊 tell me more.",
                "That’s really sweet ❤️",
                "I’m happy for you.",
                "That sounds meaningful ❤️"
            ],

            "anxiety": [
                "Take a deep breath 🌿 you’re safe here.",
                "I understand you’re overwhelmed 😔",
                "Let’s slow things down together.",
                "You’re stronger than you think ❤️",
                "One step at a time."
            ],

            "anger": [
                "I understand you're upset 😔",
                "Do you want to talk about what happened?",
                "It’s okay to feel angry.",
                "Take a moment to breathe.",
                "I’m here to listen."
            ],

            "lonely": [
                "You’re not alone ❤️ I’m here with you.",
                "That sounds really lonely 💔",
                "I’m listening if you want to talk.",
                "You matter ❤️",
                "I’m right here with you."
            ],

            "unknown": [
                "I’m listening ❤️ tell me more.",
                "Go on… I’m here.",
                "I understand. Keep going.",
                "Tell me more about that.",
                "I’m here for you."
            ],

            "no_reply": [
                "No worries ❤️ I’m here if you need me.",
                "It’s okay 😊 take your time.",
                "I’ll be here whenever you’re ready.",
                "No problem ❤️ I understand.",
                "Alright 😊 I’m here."
            ]
        }

    def get(self, intent):
        return random.choice(self.responses.get(intent, self.responses["unknown"]))