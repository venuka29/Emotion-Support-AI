from chatbot_base import ChatbotBase
from intent_recognizer import IntentRecognizer
from response_builder import ResponseBuilder


class EmotionChatbot(ChatbotBase):

    def __init__(self):
        super().__init__("Emotion Support AI")
        self.intent = IntentRecognizer()
        self.responses = ResponseBuilder()

        # MEMORY SYSTEM
        self.last_intent = None
        self.user_name = ""

    def run(self):
        self.greeting()

        while self.conversation_is_active():

            user = input("Me: ").strip()
            low = user.lower()

            if low in ["bye", "exit", "quit"]:
                self.farewell()
                break

            # NAME MEMORY
            if "my name is" in low:
                self.user_name = user.split("is")[-1].strip().capitalize()
                self.type_bot(f"Nice to meet you {self.user_name} ❤️")
                continue

            intent = self.intent.detect(user)

            reply = self.generate_reply(user, intent)

            self.type_bot(reply)

            self.last_intent = intent

    # ❤️ CORE CONTINUITY ENGINE
    def generate_reply(self, user, intent):

        low = user.lower().strip()

        # SHORT ANSWERS HANDLING
        if low in ["no", "no thanks", "nah"]:
            return self.responses.get("no_reply")

        if low in ["yes", "yeah", "ok", "okay"]:
            return "Alright 😊 I’m listening."

        # GREETING FLOW
        if intent == "greeting":
            return self.responses.get("greeting")

        # EMOTIONS
        if intent == "sad":
            return self.responses.get("sad")

        if intent == "happy":
            return self.responses.get("happy")

        if intent == "love":
            return self.responses.get("love")

        if intent == "anxiety":
            return self.responses.get("anxiety")

        if intent == "anger":
            return self.responses.get("anger")

        if intent == "lonely":
            return self.responses.get("lonely")

        # CONTEXT FOLLOW-UP (IMPORTANT HUMAN BEHAVIOR)
        if self.last_intent == "sad":
            return "Do you want to talk more about it? ❤️"

        if self.last_intent in ["anxiety", "anger"]:
            return "Take your time… I’m here ❤️"

        if self.last_intent == "happy":
            return "That’s nice 😊 what else happened?"

        return self.responses.get("unknown")

    def type_bot(self, message):
        import time
        print("Bot:", end=" ", flush=True)
        for c in message:
            print(c, end="", flush=True)
            time.sleep(0.02)
        print()