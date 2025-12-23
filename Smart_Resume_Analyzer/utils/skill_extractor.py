SKILLS = [
    # IT / CSE
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "machine learning", "data analysis", "flask", "django",
    "react", "node", "aws", "azure",

    # Mechanical
    "autocad", "solidworks", "ansys", "catia", "manufacturing",
    "thermodynamics", "hvac",

    # Civil
    "staad pro", "etabs", "surveying", "construction management",

    # ECE / EEE
    "embedded systems", "vlsi", "iot", "plc", "matlab",

    # Arts / Commerce
    "accounting", "tally", "business analysis", "marketing",
    "content writing", "ms excel", "finance"
]

def extract_skills(text):
    text = text.lower()
    found = set()

    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return list(found)
