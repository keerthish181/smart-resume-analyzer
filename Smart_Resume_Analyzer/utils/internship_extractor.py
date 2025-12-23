def extract_internship(text):
    text = text.lower()
    lines = text.splitlines()

    capture = False
    details = []

    for line in lines:
        line = line.strip()

        if "internship" in line or "intern" in line or "training" in line:
            capture = True
            continue

        if capture and any(
            key in line for key in
            ["project", "education", "skills", "certification"]
        ):
            break

        if capture and len(line) > 3:
            details.append(line)

    if details:
        role = details[0].title()
        company = details[1].title() if len(details) > 1 else "Company not specified"
        return f"{role} at {company}"

    return "No internship details detected"

