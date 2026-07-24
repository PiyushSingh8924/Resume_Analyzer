from db import connection

cursor = connection.cursor()

def save_analysis(candidate_info, score, resume_skills, job_skills):

    query = """
    INSERT INTO resume_analysis
    (
        candidate_name,
        email,
        phone,
        linkedin,
        github,
        ats_score,
        resume_skills,
        job_skills
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        candidate_info["name"],
        candidate_info["email"],
        candidate_info["phone"],
        candidate_info["linkedin"],
        candidate_info["github"],
        score,
        ", ".join(resume_skills),
        ", ".join(job_skills)
    )

    cursor.execute(query, values)
    connection.commit()