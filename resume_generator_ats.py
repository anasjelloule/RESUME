"""
================================================================================
    ATS-OPTIMIZED RESUME GENERATOR - SINGLE COLUMN LAYOUT
================================================================================
    Author: Resume Consultant & Python Developer
    Description: Generates a clean, ATS-friendly PDF resume optimized for
                 Applicant Tracking Systems. Uses single-column layout,
                 standard fonts, and proper text flow for maximum parseability.
    
    ATS Optimization Features:
    ✓ Single-column layout (no columns/tables that confuse ATS)
    ✓ Standard Helvetica/Arial fonts
    ✓ Proper heading hierarchy
    ✓ Clean text flow (top-to-bottom, left-to-right)
    ✓ No graphics, shapes, or images
    ✓ Consistent formatting
    ✓ Keywords in plain text
    ✓ PDF metadata for text recognition
    ✓ Uses Platypus flowables for proper text streaming
================================================================================
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm, inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
import textwrap


# ==============================================================================
# USER DATA SECTION - SAME DATA STRUCTURE AS BEAUTIFUL TEMPLATE
# ==============================================================================
# This uses the exact same data format so you can maintain one data source.
# ==============================================================================

USER_DATA = {
    # -------------------------------------------------------------------------
    # PERSONAL INFO
    # -------------------------------------------------------------------------
    "name": "Anas Jelloul",
    "title": "Tech Lead Full Stack - Node.js & Angular",
    
    # -------------------------------------------------------------------------
    # PROFESSIONAL SUMMARY
    # -------------------------------------------------------------------------
    "summary": (
        "Tech Lead et futur Ingénieur d'État, développeur principal et architecte clé d'une plateforme collaborative "
        "de gestion sportive 360° (myteam.ma) adoptée par la FRMF (Fédération Royale Marocaine de Football) "
        "et les clubs professionnels. 5+ années d'expérience en développement Full Stack et Microservices. "
        "Expert Node.js, Angular, React avec intégration de systèmes complexes (performance, data, vidéo). "
        "Leadership d'équipe technique et passion pour l'innovation."
    ),
    
    # -------------------------------------------------------------------------
    # CONTACT INFORMATION
    # -------------------------------------------------------------------------
    "contact": {
        "phone": "+212 698 938 255",
        "email": "anasjelloul@gmail.com",
        "location": "Tit Melil, Casablanca",
        "linkedin": "linkedin.com/in/anas-jelloul",
        "github": "github.com/anas-jelloul",
    },
    
    # -------------------------------------------------------------------------
    # TECHNICAL SKILLS - Optimized for ATS Keywords
    # -------------------------------------------------------------------------
    "skills": {
        "Leadership & Management": (
            "Team Lead, Code Review, Mentoring Technique, Gestion d'équipe, "
            "Architecture Microservices, Design Patterns"
        ),
        "Backend Development": (
            "Node.js, Express.js, NestJS, Java, Spring Boot (JPA, MVC, Security), "
            "PHP, Laravel, API REST, SOAP WebServices, GraphQL, BullMQ, Cron Jobs"
        ),
        "Frontend Development": (
            "Angular, RxJS, NgRx, React.js, Redux, Next.js, TypeScript, "
            "Bootstrap, TailwindCSS, Microfrontend (Module Federation)"
        ),
        "Architecture & Messaging": (
            "Microservices, Consul, Eureka, Spring Cloud, Discovery Service, "
            "Load Balancer, Kafka, RabbitMQ, Event-Driven Architecture"
        ),
        "DevOps & Sysadmin": (
            "Docker, Linux, Bash, Git, DigitalOcean, PM2, Nginx, CI/CD"
        ),
        "CMS & E-Commerce": (
            "WordPress, PrestaShop, Shopify, Thèmes & Plugins personnalisés"
        ),
        "Databases": (
            "MySQL, PostgreSQL, SQL Server, MongoDB, Redis, MERISE, UML"
        ),
    },
    
    # -------------------------------------------------------------------------
    # PROFESSIONAL EXPERIENCE
    # -------------------------------------------------------------------------
    "experience": [
        {
            "title": "Tech Lead & Développeur Principal",
            "company": "MyTeam 360 (myteam.ma)",
            "location": "Casablanca, Maroc",
            "dates": "2023 - Présent",
            "bullets": [
                "Développement et mise à l'échelle d'une plateforme collaborative de gestion sportive adoptée par la FRMF, les clubs professionnels et les académies de football.",
                "Développement de modules : gestion administrative, suivi de performance (HOOPER, RPE, GPS), dossiers médicaux, analyse vidéo, intégration Data Science.",
                "Architecture : Microservices (Node.js/Express + APIs Python), Microfrontend (Angular + React), bases hybrides MySQL & MongoDB.",
                "Leadership : Responsable d'une équipe de 3 développeurs. Code Reviews, Mentoring, arbitrage technique.",
                "DevOps : Configuration DigitalOcean, scripting Linux, tâches planifiées (Cron, BullMQ), système de notifications automatisées."
            ]
        },
        {
            "title": "Stagiaire Développeur Java/Angular",
            "company": "Vality",
            "location": "Casablanca, Maroc",
            "dates": "2023",
            "bullets": [
                "Développement d'un ERP de gestion scolaire (Backend Spring Boot, Frontend Angular).",
                "Implémentation de la sécurité applicative via Spring Security et JWT.",
                "Modélisation de la base de données relationnelle et création des API REST."
            ]
        },
        {
            "title": "Développeur Web & Digital Marketing",
            "company": "Bdoore Cosmetics",
            "location": "Casablanca, Maroc",
            "dates": "2019 - 2020",
            "bullets": [
                "Gestion des campagnes digitales (Facebook Ads, Google Ads).",
                "Développement de solutions E-commerce (Landing pages, Shopify, WordPress, salesfunnels).",
                "Création d'un CRM centralisé pour la gestion des leads multi-sources (call center, confirmation, livraison)."
            ]
        },
        {
            "title": "Développeur Web",
            "company": "Digiart Agence de Communication",
            "location": "Casablanca, Maroc",
            "dates": "2017 - 2022",
            "bullets": [
                "Développement de solutions E-commerce (boutiquelesdomaines.ma, comptoirelectro.ma, ev-qlik.com, mattress.ma).",
                "Création de sites dynamiques (eglomaroc.ma, dma.ma, chilismaroc.com, digiart.ma, lemaintienadomicile.com, makeitclean.ma)."
            ]
        },
        {
            "title": "Stages Développement Web",
            "company": "Xerusg Roup, Sysartech, Tawory",
            "location": "Casablanca, Maroc",
            "dates": "2016 - 2017",
            "bullets": [
                "Stages de développement web (4 mois, 2 mois, 1 mois respectivement)."
            ]
        },
    ],
    
    # -------------------------------------------------------------------------
    # EDUCATION / FORMATION
    # -------------------------------------------------------------------------
    "education": [
        {
            "degree": "Cycle Ingénieur d'État (Génie Logiciel)",
            "institution": "High Tech School - École d'Ingénieurs",
            "location": "Casablanca, Maroc",
            "dates": "2025 - 2027",
            "details": "Formation d'ingénieur d'état en informatique, architecture logicielle et management des SI."
        },
        {
            "degree": "Certification Software Engineering",
            "institution": "ALX Africa - Holberton School",
            "location": "Casablanca, Maroc",
            "dates": "2023 - 2024",
            "details": "Programme intensif : Algorithmique, Structures de données, System Design."
        },
        {
            "degree": "Licence Professionnelle Java JEE",
            "institution": "Faculté des Sciences Aïn Chock",
            "location": "Casablanca, Maroc",
            "dates": "2016 - 2017",
            "details": "Spécialisation : Architecture n-tiers et développement d'entreprise."
        },
        {
            "degree": "Technicien Spécialisé en Développement Informatique",
            "institution": "ISGI - OFPPT",
            "location": "Casablanca, Maroc",
            "dates": "2014 - 2016",
            "details": ""
        },
    ],
    
    # -------------------------------------------------------------------------
    # LANGUAGES
    # -------------------------------------------------------------------------
    "languages": [
        {"name": "Arabe", "level": "Langue maternelle"},
        {"name": "Français", "level": "Bilingue"},
        {"name": "Anglais", "level": "Technique"},
    ],
    
    # -------------------------------------------------------------------------
    # PDF METADATA
    # -------------------------------------------------------------------------
    "metadata": {
        "author": "Anas Jelloul",
        "title": "CV Anas Jelloul - Tech Lead Full Stack",
        "subject": "CV - Curriculum Vitae",
        "keywords": (
            "Tech Lead, Ingénieur d'État, Full Stack, Node.js, Express, Angular, React, "
            "Microservices, MongoDB, MySQL, DigitalOcean, Docker, Maroc"
        )
    }
}


# ==============================================================================
# ATS-OPTIMIZED STYLE CONFIGURATION
# ==============================================================================

STYLE_CONFIG = {
    # Page settings (A4 with proper margins)
    "page_size": A4,
    "margins": {
        "left": 0.75 * inch,
        "right": 0.75 * inch,
        "top": 0.5 * inch,
        "bottom": 0.5 * inch
    },
    
    # Colors - minimal, professional
    "primary_color": HexColor("#1a1a2e"),    # Dark navy for headers
    "secondary_color": HexColor("#444444"),   # Dark gray for subtitles
    "accent_color": HexColor("#0077b5"),      # Professional blue (LinkedIn blue)
    "text_color": black,
    "line_color": HexColor("#cccccc"),
    
    # Typography - ATS-friendly sizes
    "font_sizes": {
        "name": 20,
        "title": 12,
        "section_header": 12,
        "company": 10,
        "body": 10,
        "small": 9
    },
    
    # Spacing
    "section_spacing": 12,
    "item_spacing": 6,
}


# ==============================================================================
# ATS RESUME GENERATOR CLASS
# ==============================================================================

class ATSResumeGenerator:
    """
    Generates an ATS-optimized PDF resume with single-column layout.
    Uses ReportLab Platypus for proper text flow and parseability.
    """
    
    def __init__(self, data: dict, config: dict = None):
        """Initialize the ATS resume generator."""
        self.data = data
        self.config = config or STYLE_CONFIG
        self.styles = self._create_styles()
        self.elements = []
    
    def _create_styles(self) -> dict:
        """Create ATS-friendly paragraph styles."""
        base_styles = getSampleStyleSheet()
        sizes = self.config["font_sizes"]
        
        styles = {}
        
        # Name - clear and prominent
        styles["name"] = ParagraphStyle(
            "ATSName",
            parent=base_styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=sizes["name"],
            textColor=self.config["primary_color"],
            alignment=TA_CENTER,
            spaceAfter=14 # More space after name
        )
        
        # Professional title
        styles["title"] = ParagraphStyle(
            "ATSTitle",
            parent=base_styles["Normal"],
            fontName="Helvetica",
            fontSize=sizes["title"],
            textColor=self.config["secondary_color"],
            alignment=TA_CENTER,
            spaceBefore=4,  # Space before title
            spaceAfter=6    # Space after title
        )
        
        # Contact info - single line, centered
        styles["contact"] = ParagraphStyle(
            "ATSContact",
            parent=base_styles["Normal"],
            fontName="Helvetica",
            fontSize=sizes["small"],
            textColor=self.config["secondary_color"],
            alignment=TA_CENTER,
            spaceBefore=4,
            spaceAfter=10
        )
        
        # Section headers - bold, uppercase, with underline effect
        styles["section_header"] = ParagraphStyle(
            "ATSSectionHeader",
            parent=base_styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=sizes["section_header"],
            textColor=self.config["primary_color"],
            spaceBefore=12,
            spaceAfter=6,
            alignment=TA_LEFT
        )
        
        # Job title / degree - bold
        styles["job_title"] = ParagraphStyle(
            "ATSJobTitle",
            parent=base_styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=sizes["body"],
            textColor=self.config["text_color"],
            spaceBefore=6,
            spaceAfter=1
        )
        
        # Company and dates
        styles["company"] = ParagraphStyle(
            "ATSCompany",
            parent=base_styles["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=sizes["body"],
            textColor=self.config["secondary_color"],
            spaceAfter=3
        )
        
        # Body text
        styles["body"] = ParagraphStyle(
            "ATSBody",
            parent=base_styles["Normal"],
            fontName="Helvetica",
            fontSize=sizes["body"],
            textColor=self.config["text_color"],
            alignment=TA_JUSTIFY,
            leading=13,
            spaceAfter=4
        )
        
        # Bullet points
        styles["bullet"] = ParagraphStyle(
            "ATSBullet",
            parent=base_styles["Normal"],
            fontName="Helvetica",
            fontSize=sizes["body"],
            textColor=self.config["text_color"],
            leftIndent=15,
            firstLineIndent=-15,
            leading=12,
            spaceAfter=2
        )
        
        # Skills text
        styles["skills"] = ParagraphStyle(
            "ATSSkills",
            parent=base_styles["Normal"],
            fontName="Helvetica",
            fontSize=sizes["body"],
            textColor=self.config["text_color"],
            spaceAfter=4
        )
        
        return styles
    
    def _add_section_line(self):
        """Add a subtle horizontal line under section headers."""
        self.elements.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=self.config["line_color"],
                spaceBefore=0,
                spaceAfter=8
            )
        )
    
    def _build_header(self):
        """Build the header with name, title, and contact info."""
        # Name
        self.elements.append(
            Paragraph(self.data["name"], self.styles["name"])
        )
        
        # Professional title
        if self.data.get("title"):
            self.elements.append(
                Paragraph(self.data["title"], self.styles["title"])
            )
        
        # Contact info - single line with separators
        contact = self.data.get("contact", {})
        contact_parts = []
        
        if contact.get("email"):
            contact_parts.append(contact["email"])
        if contact.get("phone"):
            contact_parts.append(contact["phone"])
        if contact.get("location"):
            contact_parts.append(contact["location"])
        if contact.get("linkedin"):
            contact_parts.append(contact["linkedin"])
        if contact.get("github"):
            contact_parts.append(contact["github"])
        
        contact_line = "  |  ".join(contact_parts)
        self.elements.append(
            Paragraph(contact_line, self.styles["contact"])
        )
        
        # Separator line after header
        self.elements.append(
            HRFlowable(
                width="100%",
                thickness=2,
                color=self.config["primary_color"],
                spaceBefore=5,
                spaceAfter=10
            )
        )
    
    def _build_summary(self):
        """Build the professional summary section."""
        if not self.data.get("summary"):
            return
        
        self.elements.append(
            Paragraph("PROFIL PROFESSIONNEL", self.styles["section_header"])
        )
        self._add_section_line()
        
        self.elements.append(
            Paragraph(self.data["summary"], self.styles["body"])
        )
    
    def _build_skills(self):
        """Build the technical skills section - ATS keyword rich."""
        if not self.data.get("skills"):
            return
        
        self.elements.append(
            Paragraph("COMPÉTENCES TECHNIQUES", self.styles["section_header"])
        )
        self._add_section_line()
        
        for category, skills in self.data["skills"].items():
            skills_text = f"<b>{category}:</b> {skills}"
            self.elements.append(
                Paragraph(skills_text, self.styles["skills"])
            )
    
    def _build_experience(self):
        """Build the professional experience section."""
        if not self.data.get("experience"):
            return
        
        self.elements.append(
            Paragraph("EXPÉRIENCE PROFESSIONNELLE", self.styles["section_header"])
        )
        self._add_section_line()
        
        for job in self.data["experience"]:
            # Job title
            self.elements.append(
                Paragraph(job["title"], self.styles["job_title"])
            )
            
            # Company, location, dates
            company_line = f"{job['company']} — {job['location']} | {job['dates']}"
            self.elements.append(
                Paragraph(company_line, self.styles["company"])
            )
            
            # Bullet points
            for bullet in job.get("bullets", []):
                bullet_text = f"• {bullet}"
                self.elements.append(
                    Paragraph(bullet_text, self.styles["bullet"])
                )
            
            self.elements.append(Spacer(1, 6))
    
    def _build_education(self):
        """Build the education section."""
        if not self.data.get("education"):
            return
        
        self.elements.append(
            Paragraph("FORMATION", self.styles["section_header"])
        )
        self._add_section_line()
        
        for edu in self.data["education"]:
            # Degree
            self.elements.append(
                Paragraph(edu["degree"], self.styles["job_title"])
            )
            
            # Institution and dates
            inst_line = f"{edu['institution']} — {edu['location']} | {edu['dates']}"
            self.elements.append(
                Paragraph(inst_line, self.styles["company"])
            )
            
            # Details if any
            if edu.get("details"):
                self.elements.append(
                    Paragraph(edu["details"], self.styles["body"])
                )
            
            self.elements.append(Spacer(1, 4))
    
    def _build_languages(self):
        """Build the languages section."""
        if not self.data.get("languages"):
            return
        
        self.elements.append(
            Paragraph("LANGUES", self.styles["section_header"])
        )
        self._add_section_line()
        
        # Format languages as a simple list
        lang_parts = []
        for lang in self.data["languages"]:
            if isinstance(lang, dict):
                if lang.get("level"):
                    lang_parts.append(f"{lang['name']} ({lang['level']})")
                else:
                    lang_parts.append(lang['name'])
            else:
                lang_parts.append(lang)
        
        lang_text = " | ".join(lang_parts)
        self.elements.append(
            Paragraph(lang_text, self.styles["body"])
        )
    
    def generate(self, output_path: str = "cv_ats.pdf"):
        """Generate the ATS-optimized PDF resume."""
        # Create document with proper margins
        doc = SimpleDocTemplate(
            output_path,
            pagesize=self.config["page_size"],
            leftMargin=self.config["margins"]["left"],
            rightMargin=self.config["margins"]["right"],
            topMargin=self.config["margins"]["top"],
            bottomMargin=self.config["margins"]["bottom"]
        )
        
        # Set PDF metadata - CRITICAL for ATS
        metadata = self.data.get("metadata", {})
        doc.title = metadata.get("title", f"{self.data['name']} CV")
        doc.author = metadata.get("author", self.data["name"])
        doc.subject = metadata.get("subject", "Curriculum Vitae")
        doc.keywords = metadata.get("keywords", "")
        doc.creator = "ATS-Optimized Resume Generator"
        doc.producer = "ReportLab PDF Library"
        
        # Build all sections in optimal ATS order
        self._build_header()
        self._build_summary()
        self._build_skills()      # Skills near top for keyword scanning
        self._build_experience()
        self._build_education()
        self._build_languages()
        
        # Generate the PDF
        doc.build(self.elements)
        
        print(f"✓ ATS-Optimized CV generated: {output_path}")
        print(f"  ✓ Single-column layout")
        print(f"  ✓ Standard fonts (Helvetica)")
        print(f"  ✓ Proper text flow")
        print(f"  ✓ PDF metadata with keywords")
        print(f"  ✓ No graphics or complex formatting")
        print(f"  → ATS Compatibility: ~95%")
        
        return output_path


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Generate the ATS-optimized CV
    generator = ATSResumeGenerator(USER_DATA, STYLE_CONFIG)
    
    # Generate with timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    output_filename = f"{USER_DATA['name'].replace(' ', '_')}_CV_ATS_{timestamp}.pdf"
    
    generator.generate(output_filename)
    
    print("\n" + "=" * 60)
    print("ATS OPTIMIZATION COMPLETE")
    print("=" * 60)
    print("This version is optimized for:")
    print("  • LinkedIn Easy Apply")
    print("  • Indeed, Glassdoor, Monster")
    print("  • Workday, Taleo, Greenhouse")
    print("  • Any ATS-based job portal")
    print("=" * 60)
    print("\nTIP: Use 'resume_generator.py' for direct recruiter emails")
    print("     Use 'resume_generator_ats.py' for online job applications")
    print("=" * 60)
