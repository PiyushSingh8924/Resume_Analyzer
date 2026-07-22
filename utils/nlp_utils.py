import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess(text):

    text = text.lower()

    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()

    stop_words = set(stopwords.words("english"))

    filtered = []

    for word in words:
        if word not in stop_words:
            filtered.append(word)

    return " ".join(filtered)
    