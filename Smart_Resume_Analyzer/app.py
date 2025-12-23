from flask import Flask, render_template, request
import os

from utils.resume_parser import extract_resume_text, extract_projects
from utils.skill_extractor import extract_skills
from utils.internship_extractor import extract_internship
from utils.domain_detector import detect_domain
from utils.job_recommender import recommend_jobs
from utils.training_recommender import recommend_training
from utils.ats_score import calculate_ats_score
from utils.report_generator import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["resume"]
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_resume_text(file_path)

        skills = extract_skills(text)
        projects = extract_projects(text)
        internship = extract_internship(text)
        domain = detect_domain(text)

        jobs = recommend_jobs(skills, domain, len(projects), internship)

        for job in jobs:
            job["courses"] = recommend_training(job.get("skill_gap", []))

        ats_score = calculate_ats_score(skills, projects, internship)

        report_path = generate_pdf({
            "domain": domain,
            "ats": ats_score,
            "jobs": jobs
        })

        return render_template(
            "result.html",
            skills=skills,
            projects=projects,
            internship=internship,
            domain=domain,
            jobs=jobs,
            ats_score=ats_score,
            report_path=report_path
        )

    except Exception as e:
        return f"Error processing resume: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
