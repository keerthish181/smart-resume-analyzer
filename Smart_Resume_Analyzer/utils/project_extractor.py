import re

def extract_projects(text):
    text = text.replace("\r", "")
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    projects = []
    capture = False
    buffer = []

    for line in lines:
        if re.search(r"(projects?|filmography|works|portfolio)", line, re.I):
            capture = True
            continue

        if capture and re.search(
            r"(skills|education|internship|experience|certification)",
            line,
            re.I
        ):
            break

        if capture:
            buffer.append(line)

    if not buffer:
        return []

    i = 0
    while i < len(buffer):
        title = buffer[i]
        desc = []

        # Collect next 1–2 lines as description/role
        if i + 1 < len(buffer) and not re.match(r"^[A-Z].*\(\d{2}/\d{4}\)", buffer[i + 1]):
            desc.append(buffer[i + 1])

        if i + 2 < len(buffer) and len(buffer[i + 2]) < 80:
            desc.append(buffer[i + 2])

        description = generate_description(title, desc)

        projects.append({
            "title": title.title(),
            "description": description
        })

        i += 2

    return projects


def generate_description(title, raw_desc):
    title_lower = title.lower()

    # 🎬 CINEMA / CREATIVE
    if any(word in title_lower for word in ["film", "docu", "cinema", "short", "movie"]):
        role = ", ".join(raw_desc) if raw_desc else "Creative contributor"
        return (
            f"Worked on the project **{title}** as {role}. "
            "Handled creative planning, execution, and visual storytelling. "
            "Involved in pre-production, production, and post-production workflows."
        )

    # 💻 TECH PROJECT
    if any(word in title_lower for word in ["system", "app", "analyzer", "platform"]):
        return (
            f"Developed the project **{title}** using frontend and backend technologies. "
            "Implemented core application logic, data handling, and user interaction features."
        )

    # 📊 GENERAL
    return (
        f"Completed the project **{title}**, contributing to planning, execution, "
        "and successful delivery of project objectives."
    )
