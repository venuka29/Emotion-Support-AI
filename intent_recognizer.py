class IntentRecognizer:

    def detect(self, text):
        text = text.lower()

        if any(w in text for w in ["hi", "hello", "hey"]):
            return "greeting"

        if any(w in text for w in ["sad", "depressed", "cry", "upset", "hurt"]):
            return "sad"

        if any(w in text for w in ["happy", "good", "great", "awesome", "nice"]):
            return "happy"

        if any(w in text for w in ["love", "care", "miss", "crush"]):
            return "love"

        if any(w in text for w in ["stress", "anxious", "worried", "panic"]):
            return "anxiety"

        if any(w in text for w in ["angry", "mad", "furious", "annoyed"]):
            return "anger"

        if any(w in text for w in ["lonely", "alone", "nobody"]):
            return "lonely"

        if "my name is" in text:
            return "name"

        return "unknown"