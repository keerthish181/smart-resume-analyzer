def recommend_training(skill_gap):

    course_map = {
        "dsa": "Data Structures & Algorithms – Udemy",
        "system design": "System Design Fundamentals – Coursera",
        "sql": "SQL for Data Analysis – Coursera",
        "python": "Python for Everybody – Coursera",
        "tally": "Tally with GST – Udemy",
        "gst": "GST Practitioner Course – Udemy",
        "financial modeling": "Financial Modeling – Coursera",
        "excel": "Advanced Excel – Udemy",
        "editing": "Video Editing Masterclass – Udemy",
        "storytelling": "Creative Storytelling – Coursera"
    }

    courses = []

    for s in skill_gap:
        if s in course_map:
            courses.append(course_map[s])

    if not courses:
        return [
            "Professional Communication Skills",
            "Industry Readiness Program",
            "Career Development Training"
        ]

    return courses[:3]

