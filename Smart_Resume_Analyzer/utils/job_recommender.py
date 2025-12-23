def recommend_jobs(skills, domain, project_count, internship):

    skills = set(s.lower() for s in skills)
    jobs = []

    # ---------- COMPUTER SCIENCE / IT ----------
    if domain == "Computer Science / IT":

        if {"python", "flask", "django"} & skills:
            jobs.append({
                "title": "Backend Python Developer",
                "salary_india": "₹6 – 14 LPA",
                "salary_abroad": "$75k – $120k",
                "cities": "Bangalore, Hyderabad, Pune",
                "companies": "Google, Amazon, Zoho, Startups",
                "training": "Direct job possible",
                "skill_gap": list({"system design", "api security"} - skills)
            })

        if {"html", "css", "javascript"} & skills:
            jobs.append({
                "title": "Frontend Web Developer",
                "salary_india": "₹5 – 12 LPA",
                "salary_abroad": "$65k – $110k",
                "cities": "Chennai, Bangalore",
                "companies": "Infosys, TCS, Accenture",
                "training": "Framework training recommended",
                "skill_gap": list({"react", "ui optimization"} - skills)
            })

        if {"machine learning", "data science"} & skills:
            jobs.append({
                "title": "Machine Learning Engineer",
                "salary_india": "₹8 – 18 LPA",
                "salary_abroad": "$90k – $140k",
                "cities": "Bangalore, Pune",
                "companies": "Microsoft, IBM, NVIDIA",
                "training": "Advanced ML training required",
                "skill_gap": list({"deep learning", "model deployment"} - skills)
            })

        jobs.append({
            "title": "Cloud / DevOps Engineer",
            "salary_india": "₹7 – 16 LPA",
            "salary_abroad": "$80k – $130k",
            "cities": "Bangalore, Hyderabad",
            "companies": "AWS, Azure, Google Cloud",
            "training": "Cloud certification required",
            "skill_gap": list({"docker", "kubernetes"} - skills)
        })

    # ---------- CYBERSECURITY ----------
    elif domain == "Cybersecurity":
        jobs.append({
            "title": "Cyber Security Analyst",
            "salary_india": "₹6 – 15 LPA",
            "salary_abroad": "$80k – $130k",
            "cities": "Bangalore, Delhi",
            "companies": "Cisco, IBM, EY",
            "training": "Ethical hacking certification recommended",
            "skill_gap": list({"penetration testing", "soc tools"} - skills)
        })

    # ---------- COMMERCE ----------
    elif domain == "Commerce / B.Com":
        jobs.extend([
            {
                "title": "Chartered Accountant (CA Track)",
                "salary_india": "₹8 – 20 LPA",
                "salary_abroad": "$90k – $150k",
                "cities": "Mumbai, Chennai",
                "companies": "Big4 Firms",
                "training": "CA / CMA qualification required",
                "skill_gap": ["advanced accounting"]
            },
            {
                "title": "GST & Tax Consultant",
                "salary_india": "₹5 – 10 LPA",
                "salary_abroad": "$60k – $100k",
                "cities": "Coimbatore, Bangalore",
                "companies": "Tax Firms, Corporates",
                "training": "GST certification required",
                "skill_gap": ["gst filing"]
            }
        ])

    # ---------- ARTS / HUMANITIES ----------
    elif domain == "Arts / Humanities":
        jobs.extend([
            {
                "title": "Content Writer / Editor",
                "salary_india": "₹3 – 6 LPA",
                "salary_abroad": "$40k – $70k",
                "cities": "Remote, Chennai",
                "companies": "Media Houses",
                "training": "Portfolio required",
                "skill_gap": ["seo writing"]
            },
            {
                "title": "Public Relations Executive",
                "salary_india": "₹4 – 8 LPA",
                "salary_abroad": "$50k – $90k",
                "cities": "Mumbai, Delhi",
                "companies": "PR Agencies",
                "training": "Communication training recommended",
                "skill_gap": ["media handling"]
            }
        ])

    # ---------- CINEMA / MEDIA ----------
    elif domain in ["Cinema / Film Studies", "Video Editing / VFX"]:
        jobs.append({
            "title": "Video Editor / VFX Artist",
            "salary_india": "₹4 – 12 LPA",
            "salary_abroad": "$50k – $100k",
            "cities": "Chennai, Mumbai",
            "companies": "Film Studios",
            "training": "Industry tool mastery required",
            "skill_gap": ["after effects", "color grading"]
        })

    # ---------- CIVIL ----------
    elif domain == "Civil Engineering":
        jobs.append({
            "title": "Site Engineer",
            "salary_india": "₹4 – 9 LPA",
            "salary_abroad": "$60k – $100k",
            "cities": "Middle East, India",
            "companies": "L&T, Shapoorji",
            "training": "AutoCAD & site management required",
            "skill_gap": ["project management"]
        })

    # ---------- DEFENCE / ARMY ----------
    elif domain == "General / Multi-domain":
        jobs.append({
            "title": "Indian Armed Forces (Officer Entry)",
            "salary_india": "₹5 – 10 LPA",
            "salary_abroad": "N/A",
            "cities": "Across India",
            "companies": "Indian Army, Navy, Air Force",
            "training": "SSB & physical training required",
            "skill_gap": []
        })

    # ---------- FALLBACK ----------
    if not jobs:
        jobs.append({
            "title": "Graduate Trainee",
            "salary_india": "₹3 – 5 LPA",
            "salary_abroad": "$40k – $70k",
            "cities": "All major cities",
            "companies": "MNCs & Startups",
            "training": "Industry readiness training",
            "skill_gap": []
        })

    return jobs
