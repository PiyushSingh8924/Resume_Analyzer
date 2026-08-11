from db import collection


def save_analysis(candidate_info, score, resume_skills, job_skills):

    document = {
        "candidate_name": candidate_info["name"],
        "email": candidate_info["email"],
        "phone": candidate_info["phone"],
        "linkedin": candidate_info["linkedin"],
        "github": candidate_info["github"],
        "ats_score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills
    }

    collection.insert_one(document)