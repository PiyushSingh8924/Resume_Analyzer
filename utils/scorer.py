from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, jd):

    docs = [resume, jd]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(docs)

    score = cosine_similarity(matrix)[0][1]

    return round(score * 100, 2)