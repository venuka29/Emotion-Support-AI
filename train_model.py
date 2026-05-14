import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Training Emotional AI Model...")

df = pd.read_csv("data.csv")

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=300)
model.fit(X_vec, y)

with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained successfully ✔")