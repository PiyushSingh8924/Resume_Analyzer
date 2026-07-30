from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(
    clean_resume,
    clean_job,
    resume_skills,
    job_skills
):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2)
    )

    vectors = vectorizer.fit_transform(
        [
            clean_resume,
            clean_job
        ]
    )

    text_similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0] * 100

    matched_skills = list(
        set(resume_skills)
        &
        set(job_skills)
    )

    if len(job_skills) == 0:
        skill_score = 0
    else:
        skill_score = (
            len(matched_skills)
            /
            len(job_skills)
        ) * 100

    final_score = (
        text_similarity * 0.4
        +
        skill_score * 0.6
    )

    important_skills = [
        "python",
        "flask",
        "mysql",
        "sql",
        "git",
        "html",
        "css"
    ]

    bonus = 0

    for skill in important_skills:
        if skill in resume_skills and skill in job_skills:
            bonus += 2

    final_score += bonus

    final_score = min(final_score, 100)


    return (
        round(final_score,2),
        matched_skills
    )