def detect_domain(text):
    text = text.lower()

    domains = {
        # ================= ENGINEERING =================
        "Computer Science / IT": [
            "python", "java", "c++", "html", "css", "javascript",
            "sql", "flask", "django", "software", "developer",
            "machine learning", "data science", "artificial intelligence", "ai"
        ],

        "Electronics & Communication (ECE)": [
            "ece", "embedded", "vlsi", "verilog", "matlab",
            "signal processing", "communication systems", "microcontroller"
        ],

        "Electrical & Electronics (EEE)": [
            "eee", "electrical", "power systems", "electrical machines",
            "control systems", "transformer", "substation"
        ],

        "Mechanical Engineering": [
            "mechanical", "autocad", "solidworks", "ansys",
            "manufacturing", "thermal", "cnc"
        ],

        "Civil Engineering": [
            "civil", "construction", "structural", "surveying",
            "autocad civil", "estimation"
        ],

        # ================= COMMERCE / MANAGEMENT =================
        "Commerce / B.Com": [
            "b.com", "commerce", "accounting", "tally",
            "gst", "taxation", "auditing", "balance sheet"
        ],

        "Management / BBA / MBA": [
            "bba", "mba", "management", "business",
            "operations", "strategy", "leadership", "business analysis"
        ],

        "Economics / Finance": [
            "economics", "finance", "investment",
            "banking", "equity", "trading", "financial analysis"
        ],

        # ================= ARTS / SCIENCE =================
        "Arts / Humanities": [
            "arts", "history", "political science",
            "sociology", "psychology", "philosophy", "literature"
        ],

        "Science": [
            "physics", "chemistry", "biology",
            "mathematics", "laboratory", "research"
        ],

        # ================= CREATIVE / MEDIA =================
        "Cinema / Film Studies": [
            "cinema", "film", "filmmaking", "direction",
            "screenplay", "short film", "movie"
        ],

        "Photography / Photo Editing": [
            "photography", "photo editing", "photoshop",
            "lightroom", "dslr", "camera"
        ],

        "Video Editing / VFX": [
            "video editing", "vfx", "after effects",
            "premiere pro", "cinematography", "final cut"
        ],

        "Animation / Gaming": [
            "animation", "blender", "maya",
            "3d modeling", "gaming", "unity", "unreal engine"
        ],

        # ================= CYBER / DIGITAL =================
        "Cybersecurity": [
            "cybersecurity", "ethical hacking",
            "penetration testing", "network security", "kali", "linux"
        ],

        "Digital Marketing / Media": [
            "digital marketing", "seo", "social media",
            "content creation", "branding"
        ]
    }

    scores = {}
    for domain, keywords in domains.items():
        scores[domain] = sum(1 for k in keywords if k in text)

    best_domain = max(scores, key=scores.get)

    if scores[best_domain] == 0:
        return "General / Multi-domain"

    return best_domain

