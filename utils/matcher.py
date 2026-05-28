import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

# Load dataset
dataset = pd.read_csv("dataset/Resume.csv")

# Convert to string
dataset["Resume"] = dataset["Resume"].astype(str)

dataset["Category"] = dataset["Category"].astype(str)

# Training data
X = dataset["Resume"]

y = dataset["Category"]

# ML Pipeline
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(stop_words="english")
    ),
    (
        "classifier",
        MultinomialNB()
    )
])

# Train model
model.fit(X, y)

# Common skills
skills_list = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "nlp",
    "streamlit",
    "flask",
    "django",
    "data analysis"
]


def calculate_similarity(resume, job_description):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([
        resume,
        job_description
    ])

    similarity = cosine_similarity(vectors)[0][1]

    return similarity * 100


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:

            found_skills.append(skill)

    return found_skills


def predict_category(resume_text):

    prediction = model.predict([resume_text])

    return prediction[0]