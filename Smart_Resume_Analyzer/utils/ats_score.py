import random

def calculate_ats_score(skills, projects, internship):
    score = 0

    # ---- Skills (Max 40) ----
    skill_count = len(skills)

    if skill_count >= 12:
        score += 40
    elif skill_count >= 8:
        score += 32
    elif skill_count >= 5:
        score += 24
    elif skill_count >= 3:
        score += 16
    else:
        score += 8

    # ---- Projects (Max 30) ----
    if projects and "No project" not in projects[0]:
        project_count = len(projects)

        if project_count >= 3:
            score += 30
        elif project_count == 2:
            score += 22
        else:
            score += 15
    else:
        score += 5

    # ---- Internship (Max 20) ----
    if internship and "No internship" not in internship:
        score += 18
    else:
        score += 6

    # ---- Resume Structure / Formatting (Max 10) ----
    score += random.randint(6, 10)

    # ---- Normalize score ----
    if score > 95:
        score = random.randint(85, 95)
    elif score < 45:
        score = random.randint(45, 55)

    return score

