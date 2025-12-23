import fitz  # PyMuPDF
import re

def extract_resume_text(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text


def extract_projects(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    projects = []

    project_keywords = [
        "project", "system", "application", "tool", "platform",
        "website", "analysis", "management", "dashboard", "app",
        "film", "short film", "documentary"
    ]

    current_project = None

    for line in lines:
        lower = line.lower()

        # Detect project title
        if any(k in lower for k in project_keywords) and len(line) < 80:
            if current_project:
                projects.append(current_project)

            current_project = {
                "title": line.strip(),
                "description": []
            }

        elif current_project:
            # Add description lines
            if len(line) > 15:
                current_project["description"].append(line)

    if current_project:
        projects.append(current_project)

    # Post-process descriptions
    final_projects = []
    for p in projects:
        desc = " ".join(p["description"]).strip()

        if not desc:
            desc = (
                "Developed and implemented the project using relevant tools, "
                "focusing on core logic, problem solving, and real-world application."
            )

        final_projects.append({
            "title": p["title"],
            "description": desc
        })

    return final_projects
