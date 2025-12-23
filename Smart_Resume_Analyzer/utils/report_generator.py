import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(data):
    reports_dir = "static/reports"
    os.makedirs(reports_dir, exist_ok=True)

    file_path = os.path.join(reports_dir, "career_report.pdf")

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Career Guidance Report")

    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Detected Domain: {data.get('domain')}")

    y -= 20
    c.drawString(50, y, f"ATS Score: {data.get('ats')}%")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Recommended Jobs:")

    y -= 20
    c.setFont("Helvetica", 10)

    for job in data.get("jobs", []):
        c.drawString(60, y, f"- {job['title']}")
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()

   
    return "/static/reports/career_report.pdf"
