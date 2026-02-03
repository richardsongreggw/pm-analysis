#!/usr/bin/env python3
"""
Generate PDF Business Case Report with FamilySearch Branding
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

# FamilySearch Brand Colors
FS_GREEN = colors.HexColor('#87b940')
FS_DARK = colors.HexColor('#333536')
FS_CORAL = colors.HexColor('#f16458')
FS_GREY_LIGHT = colors.HexColor('#F6F6F6')
FS_GREY = colors.HexColor('#76797C')

class FSCanvas(canvas.Canvas):
    """Custom canvas with page numbers"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page_num, page in enumerate(self.pages, 1):
            self.__dict__.update(page)
            self.draw_page_number(page_num, page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_num, page_count):
        self.setFont("Helvetica", 9)
        self.setFillColor(FS_GREY)
        self.drawRightString(7.5*inch, 0.5*inch, f"{page_num} of {page_count}")

def create_pdf_report():
    # Setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_file = os.path.join(project_dir, "presentations", "sibling_feature_business_case_report.pdf")
    doc = SimpleDocTemplate(output_file, pagesize=letter,
                           leftMargin=1*inch, rightMargin=1*inch,
                           topMargin=1*inch, bottomMargin=1*inch)

    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=FS_GREEN,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=40
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=FS_DARK,
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=FS_GREEN,
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )

    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=FS_DARK,
        spaceAfter=12,
        fontName='Helvetica'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=FS_DARK,
        spaceAfter=12,
        fontName='Helvetica',
        leading=16
    )

    quote_style = ParagraphStyle(
        'Quote',
        parent=styles['Normal'],
        fontSize=11,
        textColor=FS_DARK,
        fontName='Helvetica-Oblique',
        leftIndent=20,
        rightIndent=20,
        spaceAfter=6,
        leading=16
    )

    # Title Page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("Sibling Feature<br/>Business Case", title_style))
    story.append(Paragraph("Adding Sibling View to Mobile Pedigree", subtitle_style))
    story.append(Spacer(1, 0.5*inch))

    # Three Pillars
    pillars_data = [
        ["1.", "Market Standard", "All competitors have it"],
        ["2.", "Customer Voice", "Users are asking for it"],
        ["3.", "Proven Value", "49% of engaged users use it"]
    ]

    pillars_table = Table(pillars_data, colWidths=[0.5*inch, 2*inch, 3*inch])
    pillars_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0,0), (0,-1), FS_GREEN),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 18),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 13),
        ('FONTSIZE', (2,0), (2,-1), 11),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(pillars_table)
    story.append(PageBreak())

    # Section 1: Market Standard
    story.append(Paragraph("1. Market Standard", heading_style))
    story.append(Paragraph("We're Behind Competitors", subheading_style))

    competitors_data = [
        ["✓", "Ancestry", "Has sibling view in mobile pedigree"],
        ["✓", "MyHeritage", "Has sibling view in mobile pedigree"],
        ["✓", "FindMyPast", "Has sibling view in mobile pedigree"],
        ["✗", "FamilySearch", "Requires navigation away from pedigree"],
    ]

    competitors_table = Table(competitors_data, colWidths=[0.4*inch, 1.5*inch, 4.5*inch])
    competitors_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0,0), (0,2), FS_GREEN),
        ('TEXTCOLOR', (0,3), (0,3), FS_CORAL),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 14),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 11),
        ('FONTSIZE', (2,0), (2,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(competitors_table)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("<b><font color='#f16458'>This is table stakes, not innovation.</font></b>", body_style))
    story.append(Spacer(1, 0.3*inch))

    # Add competitor screenshots if they exist
    screenshots_dir = os.path.join(project_dir, "data", "screenshots", "competitors")
    screenshot_files = [
        ("ancestry-app-sibling-view.png", "Ancestry Mobile App"),
        ("myheritage-app-sibling-view.png", "MyHeritage Mobile App"),
        ("findmypast-app-sibling-view.png", "FindMyPast Mobile App")
    ]

    for filename, caption in screenshot_files:
        filepath = os.path.join(screenshots_dir, filename)
        if os.path.exists(filepath):
            try:
                img = Image(filepath, width=3*inch, height=5*inch, kind='proportional')
                story.append(img)
                story.append(Paragraph(f"<i>{caption}</i>", body_style))
                story.append(Spacer(1, 0.2*inch))
            except:
                pass

    story.append(PageBreak())

    # Section 2: Customer Voice
    story.append(Paragraph("2. Customer Voice", heading_style))
    story.append(Paragraph("What Android Users Are Saying", subheading_style))

    story.append(Paragraph("<b>Featured Customer Quotes:</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    quotes = [
        ("I believe that the app should make sm option for providing half siblings", "May 2023, 3 stars"),
        ("I hope they add a feature where I can see the siblings of a person in the family tree diagram.", "May 2025, 4 stars"),
        ("I find it frustrating that I don't see my siblings even though they are listed under my parents.", "July 2025, 4 stars"),
        ("Love it! But please address these 3 issues: 1. Suggest the spouse's immediate family members when attaching people from records! They're often present in baptism records where both sets of grandparents are named and a sibling of one of the spouses is often a godparent...", "September 2022, 4 stars"),
        ("website is better. search results are useless, coming up with unrelated matches that are 100 years out. doesn't show siblings, can't add. use the website", "July 2025, 1 star"),
        ("Why can't I add my children? It's also not allowing me to add my aunts/uncles and cousins...", "November 2024, 3 stars")
    ]

    for quote, meta in quotes:
        story.append(Paragraph(f'"{quote}"', quote_style))
        story.append(Paragraph(f"<i><font color='#76797C' size=9>Google Play Review, {meta}</font></i>", body_style))
        story.append(Spacer(1, 0.15*inch))

    # Summary note with smaller font
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=9,
        textColor=FS_GREY,
        fontName='Helvetica',
        leading=12
    )

    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>Summary:</b> 23 Android reviews (0.53% of reviews with text) explicitly mention sibling/family viewing over 3 years (2023-2025). <i>Note: iOS App Store feedback not available for analysis.</i>", note_style))
    story.append(PageBreak())

    # Section 3: Proven Value
    story.append(Paragraph("3. Proven Value", heading_style))
    story.append(Paragraph("Web Users Actively Engage With This Feature", subheading_style))

    story.append(Spacer(1, 0.3*inch))

    # Big stat
    big_stat_style = ParagraphStyle(
        'BigStat',
        parent=styles['Normal'],
        fontSize=48,
        textColor=FS_GREEN,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=58,
        spaceAfter=12
    )

    stat_desc_style = ParagraphStyle(
        'StatDesc',
        parent=styles['Normal'],
        fontSize=12,
        textColor=FS_DARK,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    stat_detail_style = ParagraphStyle(
        'StatDetail',
        parent=styles['Normal'],
        fontSize=11,
        textColor=FS_DARK,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    story.append(Paragraph("49%", big_stat_style))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("of engaged users toggle siblings", stat_desc_style))
    story.append(Spacer(1, 0.08*inch))
    story.append(Paragraph("(514,746 of 1,047,944 who toggled ancestors)", stat_detail_style))
    story.append(Spacer(1, 0.25*inch))

    # Divider line
    divider_table = Table([['']], colWidths=[6.5*inch])
    divider_table.setStyle(TableStyle([
        ('LINEABOVE', (0,0), (-1,0), 2, colors.HexColor('#CACDCD')),
        ('TOPPADDING', (0,0), (0,0), 20),
    ]))
    story.append(divider_table)
    story.append(Spacer(1, 0.2*inch))

    # Secondary stat
    secondary_stat_style = ParagraphStyle(
        'SecondaryStat',
        parent=styles['Normal'],
        fontSize=32,
        textColor=FS_GREEN,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=40,
        spaceAfter=12
    )

    story.append(Paragraph("38%", secondary_stat_style))
    story.append(Spacer(1, 0.12*inch))
    story.append(Paragraph("of all pedigree users toggle siblings", stat_desc_style))
    story.append(Spacer(1, 0.08*inch))
    story.append(Paragraph("(593,667 users over 90 days)", stat_detail_style))

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<i><font color='#76797C' size=9>Source: Adobe Analytics, Nov 5, 2025 – Feb 2, 2026 (1.56M pedigree views)</font></i>", body_style))
    story.append(PageBreak())

    # Section 4: Recommendation
    story.append(Paragraph("Recommendation", heading_style))
    story.append(Spacer(1, 0.2*inch))

    # Recommendation box with proper styling
    rec_text_style = ParagraphStyle(
        'RecText',
        parent=styles['Normal'],
        fontSize=18,
        textColor=colors.white,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=24
    )

    rec_paragraph = Paragraph("Add sibling affordance to mobile pedigree view", rec_text_style)
    rec_table = Table([[rec_paragraph]], colWidths=[6.5*inch])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), FS_GREEN),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 30),
        ('BOTTOMPADDING', (0,0), (-1,-1), 30),
        ('ROUNDEDCORNERS', [12, 12, 12, 12]),
    ]))
    story.append(rec_table)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("<b>Rationale:</b>", subheading_style))
    rationale_points = [
        "✓ Achieves competitive parity with Ancestry, MyHeritage, FindMyPast",
        "✓ Addresses explicit customer requests (3 years of Android feedback)",
        "✓ Leverages proven high-engagement feature (49% of engaged users)",
        "✓ Closes UX consistency gap between web and mobile platforms"
    ]
    for point in rationale_points:
        story.append(Paragraph(point, body_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Expected Impact:</b>", subheading_style))
    impact_points = [
        "→ Improved user satisfaction",
        "→ Increased mobile engagement (based on 49% web engagement rate)",
        "→ Reduced competitive disadvantage"
    ]
    for point in impact_points:
        story.append(Paragraph(f"<font color='#87b940'>{point}</font>", body_style))

    # Build PDF
    doc.build(story, canvasmaker=FSCanvas)
    print(f"PDF report generated: {output_file}")

if __name__ == "__main__":
    create_pdf_report()
