from flask import Flask, render_template, request
import os

from utils.resume_parser import extract_text
from utils.nlp_utils import preprocess
from utils.scorer import calculate_score
from utils.info_extractor import extract_info
from utils.skill_extractor import extract_skills
from utils.database import save_analysis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(filepath)

    text = extract_text(filepath)

    print("\nResume Text:\n")
    print(text)

    candidate_info = extract_info(text)

    print(candidate_info)

    job_description = request.form["job_description"]

    resume_skills = extract_skills(text)
    job_skills = extract_skills(job_description)

    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)

    clean_resume = preprocess(text)
    clean_job = preprocess(job_description)

    score, matched_skills = calculate_score(
    clean_resume,
    resume_skills,
    job_skills
    )

    save_analysis(
        candidate_info,
        score,
        resume_skills,
        job_skills
    )

    missing_skills = list(
    set(job_skills)
    -
    set(resume_skills)
    )

    return render_template(
    "result.html",
    score=score,
    candidate_info=candidate_info,
    resume_skills=resume_skills,
    job_skills=job_skills,
    matched_skills=matched_skills,
    missing_skills=missing_skills
)

if __name__ == "__main__":
    app.run(debug=True, port=5001)