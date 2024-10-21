import os

if os.path.exists("spam_classifier.pkl"):
    os.remove("spam_classifier.pkl")
if os.path.exists("vectorizer.pkl"):
    os.remove("vectorizer.pkl")

