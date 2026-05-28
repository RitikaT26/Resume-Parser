import re
import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def preprocess_text(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = text.split()

    filtered_words = []

    for word in words:

        if word not in stop_words:

            filtered_words.append(word)

    return " ".join(filtered_words)