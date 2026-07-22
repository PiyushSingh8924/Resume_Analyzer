from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_text
from utils.nlp_utils import preprocess
from utils.scorer import calculate_score

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

    job_description = request.form["job_description"]

    clean_resume = preprocess(text)

    clean_job = preprocess(job_description)

    score = calculate_score(
        clean_resume,
        clean_job
    )

    return render_template(
    "result.html",
    score=score
)
if __name__ == "__main__":
    app.run(debug=True,port=5001)