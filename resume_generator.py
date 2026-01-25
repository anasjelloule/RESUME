"""
================================================================================
    PROFESSIONAL CV GENERATOR - TWO-COLUMN LAYOUT WITH SIDEBAR
================================================================================
    Replicates a modern two-column CV design with:
    - Dark sidebar on the right (contact, skills, languages, hobbies)
    - Teal/cyan gradient header with profile photo
    - Timeline-style experience and education sections
    - Professional French CV format
================================================================================
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import os
import textwrap


# ==============================================================================
# USER DATA SECTION - UPDATE YOUR INFORMATION HERE
# ==============================================================================

USER_DATA = {
    # -------------------------------------------------------------------------
    # PERSONAL INFO
    # -------------------------------------------------------------------------
    "name": "Anas Jelloul",
    "title": "Tech Lead Full Stack | Node.js & Angular",
    "photo": "d:\\ANAS\\CV\\profile.png",  # Profile photo
    
    # -------------------------------------------------------------------------
    # PROFESSIONAL SUMMARY (Executive Pitch)
    # -------------------------------------------------------------------------
    "summary": (
        "Tech Lead et Futur Ingénieur d'État. Architecte et développeur principal d'une plateforme collaborative "
        "de gestion sportive 360° (myteam.ma) adoptée par la FRMF et les clubs professionnels marocains. "
        "Expert en architecture Microservices (Node.js, Angular, React) et intégration de systèmes "
        "complexes (performance, data, vidéo). Leadership d'équipe et passion pour l'innovation technologique."
    ),
    
    # -------------------------------------------------------------------------
    # CONTACT INFORMATION (Sidebar)
    # -------------------------------------------------------------------------
    "contact": {
        "phone": "+212 698 938 255",
        "email": "anasjelloul@gmail.com",
        "location": "Casablanca, Maroc"
    },
    
    # -------------------------------------------------------------------------
    # EXPERIENCES - Timeline format
    # -------------------------------------------------------------------------
    "experiences": [
        {"year": "2023-", "title": "Tech Lead & Développeur Principal", "company": "MyTeam 360 (myteam.ma)", "details": (
            "• Produit : Conception et développement complet d'une plateforme collaborative de gestion sportive adoptée par la FRMF, les clubs professionnels et les académies de football.\n"
            "• Modules : Gestion administrative, suivi de performance (HOOPER, RPE, GPS), dossiers médicaux, analyse vidéo et intégration Data Science.\n"
            "• Architecture : Microservices (Node.js/Express + APIs Python), Microfrontend (Angular + React), bases hybrides MySQL & MongoDB.\n"
            "• Leadership : Responsable d'une équipe de 3 développeurs. Code Reviews, Mentoring, arbitrage technique.\n"
            "• DevOps : Configuration DigitalOcean, scripting Linux, tâches planifiées (Cron, BullMQ), notifications automatisées."
        )},
        {"year": "2023", "title": "Stagiaire Développeur Java/Angular", "company": "Vality", "details": (
            "• Développement d'un ERP de gestion scolaire (Backend Spring Boot / Frontend Angular).\n"
            "• Implémentation de la sécurité applicative (Spring Security, JWT)."
        )},
        {"year": "2019-20", "title": "Développeur Web & Digital Marketing", "company": "Bdoore Cosmetics", "details": (
            "• Gestion des campagnes digitales (Facebook Ads, Google Ads).\n"
            "• Développement de solutions E-commerce (Landing pages, Shopify, WordPress).\n"
            "• Création d'un CRM centralisé pour la gestion des leads multi-sources (call center, confirmation, livraison)."
        )},
        {"year": "2017-22", "title": "Développeur Web", "company": "Digiart Agence", "details": (
            "• Développement de solutions E-commerce (boutiquelesdomaines.ma, comptoirelectro.ma, ev-qlik.com, mattress.ma).\n"
            "• Création de sites dynamiques (eglomaroc.ma, dma.ma, chilismaroc.com, digiart.ma, lemaintienadomicile.com)."
        )},
        {"year": "2016-17", "title": "Stages Développement Web", "company": "Xerusg Roup, Sysartech, Tawory", "details": ""}
    ],
    
    # -------------------------------------------------------------------------
    # FORMATION / EDUCATION
    # -------------------------------------------------------------------------
    "formation": [
        {"year": "2025-27", "title": "Cycle Ingénieur d'État (Génie Logiciel)", "institution": "High Tech School - École d'Ingénieurs", "details": "Formation d'excellence en ingénierie informatique et management des SI."},
        {"year": "2023-24", "title": "Certification Software Engineering", "institution": "ALX Africa - Holberton School", "details": "Programme intensif : Algorithmique avancée et System Design."},
        {"year": "2016-17", "title": "Licence Pro. Java JEE", "institution": "Faculté des Sciences Aïn Chock", "details": "Architecture logicielle distribuée."},
        {"year": "2014-16", "title": "Technicien Spécialisé (TDI)", "institution": "ISGI - OFPPT", "details": ""}
    ],
    
    # -------------------------------------------------------------------------
    # COMPETENCES / SKILLS (Sidebar)
    # -------------------------------------------------------------------------
    "competences": {
        "LEADERSHIP": [
            "Gestion d'équipe (3+ devs)",
            "Code Review & Mentoring",
            "Architecture Microservices"
        ],
        "BACKEND": [
            "Node.js, Express, NestJS",
            "Java, Spring Boot (JPA, MVC)",
            "PHP, Laravel"
        ],
        "FRONTEND": [
            "Angular, React, Redux, Next.js",
            "TypeScript, Bootstrap, Tailwind",
            "Microfrontend (Module Federation)"
        ],
        "ARCHITECTURE & API": [
            "Microservices, Consul, Eureka",
            "REST API, SOAP, GraphQL",
            "Kafka, RabbitMQ"
        ],
        "DEVOPS": [
            "Docker, Linux, Bash, Git",
            "DigitalOcean, PM2, Nginx",
            "CI/CD (notions: K8s, Jenkins)"
        ],
        "CMS & E-COMMERCE": [
            "WordPress, PrestaShop, Shopify",
            "Création thèmes & plugins"
        ],
        "DATABASES": [
            "MySQL, PostgreSQL, SQL Server",
            "MongoDB, Redis, MERISE/UML"
        ],
        "DESIGN PATTERNS": [
            "MVC, Singleton, Strategy",
            "Builder, Observer, Factory"
        ]
    },
    
    # -------------------------------------------------------------------------
    # LOISIRS / HOBBIES
    # -------------------------------------------------------------------------
    "loisirs": [
        "Veille Technologique (IA, Cloud)",
        "Hackathons & Coding Challenges",
        "Voyages & Culture",
        "Engagement Associatif"
    ],
    
    # -------------------------------------------------------------------------
    # LANGUES / LANGUAGES
    # -------------------------------------------------------------------------
    "langues": [
        {"name": "Arabe", "level": "Natif"},
        {"name": "Français", "level": "Bilingue"},
        {"name": "Anglais", "level": "Technique"},
    ],
    
    # -------------------------------------------------------------------------
    # PDF METADATA
    # -------------------------------------------------------------------------
    "metadata": {
        "author": "Anas Jelloul",
        "title": "CV Anas Jelloul - Tech Lead Full Stack",
        "subject": "Curriculum Vitae",
        "keywords": "Tech Lead, Ingénieur d'État, Full Stack, Node.js, Angular, React, Microservices, Maroc"
    }
}


# ==============================================================================
# STYLE CONFIGURATION
# ==============================================================================

STYLE_CONFIG = {
    # Page settings (A4)
    "page_width": A4[0],  # 595.27 points
    "page_height": A4[1],  # 841.89 points
    
    # Layout proportions
    "sidebar_width": 180,  # points (about 63mm)
    "main_width": A4[0] - 180,  # remaining width for main content
    
    # Colors - matching your CV
    "header_gradient_start": HexColor("#0097a7"),  # Teal/cyan
    "header_gradient_end": HexColor("#00838f"),    # Darker teal
    "sidebar_bg": HexColor("#1a1a2e"),             # Dark navy/charcoal
    "accent_color": HexColor("#00bcd4"),           # Cyan accent
    "accent_dark": HexColor("#0097a7"),            # Darker cyan
    "text_dark": HexColor("#333333"),              # Dark gray text
    "text_light": white,                           # White text
    "text_muted": HexColor("#666666"),             # Muted gray
    "timeline_line": HexColor("#e0e0e0"),          # Light gray timeline
    
    # Header settings
    "header_height": 140,
    "photo_size": 80,
    
    # Typography sizes
    "name_size": 24,
    "title_size": 14,
    "summary_size": 8,
    "section_header_size": 14,
    "body_size": 9,
    "small_size": 8,
    
    # Spacing
    "margin": 0,  # No margin for full-bleed design
    "section_spacing": 15,
    "item_spacing": 8,
}


# ==============================================================================
# CV GENERATOR CLASS
# ==============================================================================

class CVGenerator:
    """
    Generates a professional two-column CV with sidebar design.
    Uses ReportLab canvas for precise positioning and styling.
    """
    
    def __init__(self, data: dict, config: dict = None):
        """Initialize the CV generator with user data and config."""
        self.data = data
        self.config = config or STYLE_CONFIG
        self.width = self.config["page_width"]
        self.height = self.config["page_height"]
        self.sidebar_width = self.config["sidebar_width"]
        self.main_width = self.config["main_width"]
        
    def _draw_header(self, c: canvas.Canvas):
        """
        Draw the header section with gradient background and profile info.
        Includes photo circle, name, title, and summary.
        """
        header_height = self.config["header_height"]
        
        # Draw gradient-like header background (solid teal for simplicity)
        # For true gradient, we'd need multiple rectangles
        c.setFillColor(self.config["header_gradient_start"])
        c.rect(0, self.height - header_height, self.main_width, header_height, fill=1, stroke=0)
        
        # Photo placeholder circle
        photo_size = self.config["photo_size"]
        photo_x = 50
        photo_y = self.height - header_height / 2
        
        # Draw white circle border for photo
        c.setFillColor(white)
        c.circle(photo_x, photo_y, photo_size / 2 + 3, fill=1, stroke=0)
        
        # Draw photo or placeholder
        if self.data.get("photo") and os.path.exists(self.data["photo"]):
            # Load and draw the actual photo
            try:
                img = ImageReader(self.data["photo"])
                # Clip to circle would require more complex masking
                c.drawImage(img, photo_x - photo_size/2, photo_y - photo_size/2, 
                           photo_size, photo_size, mask='auto')
            except:
                # Fallback to gray circle
                c.setFillColor(HexColor("#cccccc"))
                c.circle(photo_x, photo_y, photo_size / 2, fill=1, stroke=0)
        else:
            # Gray placeholder circle
            c.setFillColor(HexColor("#aaaaaa"))
            c.circle(photo_x, photo_y, photo_size / 2, fill=1, stroke=0)
            # Add person icon placeholder
            c.setFillColor(HexColor("#888888"))
            c.circle(photo_x, photo_y + 10, 12, fill=1, stroke=0)  # Head
            c.ellipse(photo_x - 20, photo_y - 25, photo_x + 20, photo_y, fill=1, stroke=0)  # Body
        
        # Name
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", self.config["name_size"])
        name_x = photo_x + photo_size / 2 + 30
        c.drawString(name_x, self.height - 45, self.data["name"])
        
        # Title
        c.setFont("Helvetica", self.config["title_size"])
        c.drawString(name_x, self.height - 65, self.data["title"])
        
        # Summary text - wrapped
        c.setFont("Helvetica", self.config["summary_size"])
        summary = self.data.get("summary", "")
        max_width = self.main_width - name_x - 20
        
        # Simple text wrapping
        y_pos = self.height - 82
        lines = self._wrap_text(summary, max_width, self.config["summary_size"])
        for line in lines[:5]:  # Limit to 5 lines in header
            c.drawString(name_x, y_pos, line)
            y_pos -= 11
    
    def _draw_sidebar(self, c: canvas.Canvas):
        """
        Draw the dark sidebar with contact, skills, hobbies, and languages.
        """
        # Sidebar background - full height
        c.setFillColor(self.config["sidebar_bg"])
        c.rect(self.main_width, 0, self.sidebar_width, self.height, fill=1, stroke=0)
        
        # Starting Y position for sidebar content
        y_pos = self.height - 30
        sidebar_x = self.main_width + 15
        content_width = self.sidebar_width - 30
        
        # =====================================================================
        # CONTACT SECTION
        # =====================================================================
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(sidebar_x, y_pos, "CONTACT")
        y_pos -= 25
        
        contact = self.data.get("contact", {})
        c.setFont("Helvetica", 9)
        
        # Phone
        if contact.get("phone"):
            # Draw cyan circle icon
            c.setFillColor(self.config["accent_color"])
            c.circle(sidebar_x + 8, y_pos + 3, 8, fill=1, stroke=0)
            c.setFillColor(self.config["sidebar_bg"])
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(sidebar_x + 8, y_pos, "📞")
            c.setFillColor(white)
            c.setFont("Helvetica", 8)
            c.drawString(sidebar_x + 22, y_pos, contact["phone"])
            y_pos -= 18
        
        # Email
        if contact.get("email"):
            c.setFillColor(self.config["accent_color"])
            c.circle(sidebar_x + 8, y_pos + 3, 8, fill=1, stroke=0)
            c.setFillColor(white)
            c.setFont("Helvetica", 8)
            c.drawString(sidebar_x + 22, y_pos, contact["email"])
            y_pos -= 18
        
        # Location
        if contact.get("location"):
            c.setFillColor(self.config["accent_color"])
            c.circle(sidebar_x + 8, y_pos + 3, 8, fill=1, stroke=0)
            c.setFillColor(white)
            c.setFont("Helvetica", 8)
            c.drawString(sidebar_x + 22, y_pos, contact["location"])
            y_pos -= 30
        
        # =====================================================================
        # COMPETENCES SECTION
        # =====================================================================
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(sidebar_x, y_pos, "COMPÉTENCES")
        y_pos -= 20
        
        c.setFont("Helvetica", 7)
        competences = self.data.get("competences", {})
        
        for category, skills in competences.items():
            # Category header
            c.setFillColor(white)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(sidebar_x, y_pos, f"{category} :")
            y_pos -= 11
            
            # Skills
            c.setFont("Helvetica", 7)
            c.setFillColor(HexColor("#cccccc"))
            for skill in skills:
                # Wrap long skill text
                wrapped = self._wrap_text(skill, content_width - 5, 7)
                for line in wrapped:
                    c.drawString(sidebar_x + 5, y_pos, line)
                    y_pos -= 9
            y_pos -= 3
        
        y_pos -= 10
        
        # =====================================================================
        # LOISIRS SECTION
        # =====================================================================
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(sidebar_x, y_pos, "LOISIRS")
        y_pos -= 18
        
        c.setFont("Helvetica", 8)
        c.setFillColor(HexColor("#cccccc"))
        for hobby in self.data.get("loisirs", []):
            wrapped = self._wrap_text(hobby, content_width, 8)
            for line in wrapped:
                c.drawString(sidebar_x, y_pos, line)
                y_pos -= 11
        
        y_pos -= 15
        
        # =====================================================================
        # LANGUES SECTION
        # =====================================================================
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(sidebar_x, y_pos, "LANGUES")
        y_pos -= 25
        
        # Draw language pills/badges
        langues = self.data.get("langues", [])
        pill_x = sidebar_x
        
        for lang in langues:
            lang_name = lang["name"] if isinstance(lang, dict) else lang
            
            # Pill dimensions
            pill_width = 45
            pill_height = 22
            
            # Draw pill outline (cyan border)
            c.setStrokeColor(self.config["accent_color"])
            c.setLineWidth(1.5)
            c.roundRect(pill_x, y_pos - pill_height + 5, pill_width, pill_height, 10, fill=0, stroke=1)
            
            # Draw text
            c.setFillColor(white)
            c.setFont("Helvetica", 8)
            c.drawCentredString(pill_x + pill_width / 2, y_pos - 8, lang_name)
            
            pill_x += pill_width + 8
            
            # Wrap to next line if needed
            if pill_x + pill_width > self.main_width + self.sidebar_width - 15:
                pill_x = sidebar_x
                y_pos -= pill_height + 10
    
    def _draw_experiences(self, c: canvas.Canvas, start_y: float) -> float:
        """
        Draw the experiences section with timeline format.
        Returns the Y position after drawing.
        """
        y_pos = start_y
        margin_left = 25
        timeline_x = margin_left + 35  # Position of the timeline dots
        content_x = timeline_x + 25    # Position where content starts
        
        # Section header
        c.setFillColor(self.config["text_dark"])
        c.setFont("Helvetica-Bold", self.config["section_header_size"])
        c.drawString(margin_left, y_pos, "EXPÉRIENCES")
        y_pos -= 25
        
        # Draw timeline line (vertical)
        experiences = self.data.get("experiences", [])
        if experiences:
            line_start_y = y_pos + 5
            line_end_y = y_pos - (len(experiences) * 35) - 50
            c.setStrokeColor(self.config["timeline_line"])
            c.setLineWidth(1)
            c.line(timeline_x, line_start_y, timeline_x, line_end_y)
        
        # Draw each experience
        for exp in experiences:
            # Year on the left
            c.setFillColor(self.config["text_dark"])
            c.setFont("Helvetica", 9)
            c.drawRightString(timeline_x - 12, y_pos, exp["year"])
            
            # Cyan dot on timeline
            c.setFillColor(self.config["accent_color"])
            c.circle(timeline_x, y_pos + 3, 5, fill=1, stroke=0)
            
            # Title (bold)
            c.setFillColor(self.config["text_dark"])
            c.setFont("Helvetica-Bold", 9)
            c.drawString(content_x, y_pos, exp["title"])
            y_pos -= 12
            
            # Company
            if exp.get("company"):
                c.setFillColor(self.config["text_muted"])
                c.setFont("Helvetica-Oblique", 8)
                c.drawString(content_x, y_pos, exp["company"])
                y_pos -= 12
            
            # Details (if any)
            if exp.get("details"):
                c.setFillColor(self.config["text_dark"])
                c.setFont("Helvetica", 8)
                max_width = self.main_width - content_x - 20
                
                # Handle multi-paragraph details
                paragraphs = exp["details"].split("\n\n")
                for para in paragraphs:
                    lines = self._wrap_text(para.replace("\n", " "), max_width, 8)
                    for line in lines:
                        c.drawString(content_x, y_pos, line)
                        y_pos -= 10
                    y_pos -= 3
            
            y_pos -= 8
        
        return y_pos
    
    def _draw_formation(self, c: canvas.Canvas, start_y: float) -> float:
        """
        Draw the formation/education section with timeline format.
        Returns the Y position after drawing.
        """
        y_pos = start_y
        margin_left = 25
        timeline_x = margin_left + 35
        content_x = timeline_x + 25
        
        # Section header
        c.setFillColor(self.config["text_dark"])
        c.setFont("Helvetica-Bold", self.config["section_header_size"])
        c.drawString(margin_left, y_pos, "FORMATION")
        y_pos -= 25
        
        # Draw timeline line
        formation = self.data.get("formation", [])
        if formation:
            line_start_y = y_pos + 5
            line_end_y = y_pos - (len(formation) * 30)
            c.setStrokeColor(self.config["timeline_line"])
            c.setLineWidth(1)
            c.line(timeline_x, line_start_y, timeline_x, line_end_y)
        
        # Draw each education entry
        for edu in formation:
            # Year
            c.setFillColor(self.config["text_dark"])
            c.setFont("Helvetica", 9)
            c.drawRightString(timeline_x - 12, y_pos, edu["year"])
            
            # Cyan dot
            c.setFillColor(self.config["accent_color"])
            c.circle(timeline_x, y_pos + 3, 5, fill=1, stroke=0)
            
            # Title
            c.setFillColor(self.config["text_dark"])
            c.setFont("Helvetica-Bold", 9)
            c.drawString(content_x, y_pos, edu["title"])
            y_pos -= 12
            
            # Institution
            if edu.get("institution"):
                c.setFillColor(self.config["text_muted"])
                c.setFont("Helvetica-Oblique", 8)
                c.drawString(content_x, y_pos, edu["institution"])
                y_pos -= 12
            
            y_pos -= 8
        
        return y_pos
    
    def _wrap_text(self, text: str, max_width: float, font_size: float) -> list:
        """
        Wrap text to fit within a maximum width.
        Uses approximate character width calculation.
        """
        if not text:
            return []
        
        # Approximate characters per line based on font size
        # Helvetica is roughly 0.5 * font_size per character on average
        char_width = font_size * 0.45
        chars_per_line = int(max_width / char_width)
        
        # Use textwrap for proper word wrapping
        wrapped = textwrap.wrap(text, width=chars_per_line)
        return wrapped
    
    def generate(self, output_path: str = "cv_output.pdf"):
        """
        Generate the complete CV PDF.
        """
        # Create canvas
        c = canvas.Canvas(output_path, pagesize=A4)
        
        # Set PDF metadata for ATS compatibility
        metadata = self.data.get("metadata", {})
        c.setTitle(metadata.get("title", f"{self.data['name']} CV"))
        c.setAuthor(metadata.get("author", self.data["name"]))
        c.setSubject(metadata.get("subject", "Curriculum Vitae"))
        c.setKeywords(metadata.get("keywords", ""))
        c.setCreator("Professional CV Generator")
        
        # Draw all sections
        self._draw_sidebar(c)
        self._draw_header(c)
        
        # Main content starts below header
        content_y = self.height - self.config["header_height"] - 30
        
        # Draw experiences
        content_y = self._draw_experiences(c, content_y)
        
        # Draw formation
        content_y = self._draw_formation(c, content_y - 20)
        
        # Save the PDF
        c.save()
        
        print(f"✓ CV successfully generated: {output_path}")
        print(f"  • Design: Two-column with dark sidebar")
        print(f"  • Accent color: Teal/Cyan")
        print(f"  • Sections: Header, Expériences, Formation, Contact, Compétences, Loisirs, Langues")
        print(f"  • PDF metadata enabled for ATS compatibility")
        
        return output_path


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Generate the CV
    generator = CVGenerator(USER_DATA, STYLE_CONFIG)
    
    # Generate with timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    output_filename = f"{USER_DATA['name'].replace(' ', '_')}_CV_{timestamp}.pdf"
    
    generator.generate(output_filename)
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Update USER_DATA with your actual information")
    print("2. Add your profile photo path to 'photo' field")
    print("3. Run: python resume_generator.py")
    print("=" * 60)
