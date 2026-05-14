# ❤️ Emotional Support AI Chatbot

## 📌 Overview
This project is a Python-based **Emotional Support AI Chatbot** that simulates human-like supportive conversations.  
It detects user emotions and responds with empathetic, continuous dialogue.

The system is fully offline and built using rule-based Natural Language Processing (NLP) techniques.  
No external APIs or LLM services are used.

---

## 💡 Features

- Emotion detection:
  - Sad
  - Happy
  - Love
  - Anxiety
  - Anger
  - Loneliness

- Human-like conversation flow
- Context-aware replies (remembers previous emotion)
- Name recognition (e.g., "my name is ...")
- Natural follow-up responses
- Typing animation effect for realism
- Fully offline chatbot (no APIs)

---

## 📁 Project Structure

emotion_ai/
│── main.py                  # Run this file
│── emotion_chatbot.py       # Core chatbot logic
│── chatbot_base.py          # Base chatbot class
│── intent_recognizer.py     # Emotion detection logic
│── response_builder.py      # Response system
│── text_processor.py        # Text cleaning utilities

