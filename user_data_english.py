# ==============================================================================
# ENGLISH USER DATA - For CV Generators
# ==============================================================================
# Copy this data into resume_generator.py or resume_generator_ats.py
# to generate English versions of your CVs.
# ==============================================================================

USER_DATA_EN = {
    # -------------------------------------------------------------------------
    # PERSONAL INFO
    # -------------------------------------------------------------------------
    "name": "Anas Jelloul",
    "title": "Tech Lead Full Stack | Node.js & Angular",
    "photo": "d:\\ANAS\\CV\\profile.png",
    
    # -------------------------------------------------------------------------
    # PROFESSIONAL SUMMARY
    # -------------------------------------------------------------------------
    "summary": (
        "Tech Lead and Future State Engineer. Architect and lead developer of a 360° collaborative "
        "sports management platform (myteam.ma) adopted by the FRMF (Royal Moroccan Football Federation) "
        "and professional clubs. Expert in Microservices architecture (Node.js, Angular, React) and "
        "complex systems integration (performance, data, video). Team leadership with a passion for tech innovation."
    ),
    
    # -------------------------------------------------------------------------
    # CONTACT INFORMATION
    # -------------------------------------------------------------------------
    "contact": {
        "phone": "+212 698 938 255",
        "email": "anasjelloule@gmail.com",
        "location": "Tit Melil, Casablanca, Morocco",
        "linkedin": "linkedin.com/in/anas-jelloul-758747137/",
        "github": "github.com/anasjelloule",
    },
    
    # -------------------------------------------------------------------------
    # EXPERIENCES
    # -------------------------------------------------------------------------
    "experiences": [
        {"year": "2023-", "title": "Tech Lead & Lead Developer", "company": "MyTeam 360 (myteam.ma)", "details": (
            "• Product: Designed and built a complete collaborative sports management platform adopted by FRMF, professional clubs, and football academies.\n"
            "• Modules: Administrative management, performance tracking (HOOPER, RPE, GPS), medical records, video analysis, and Data Science integration.\n"
            "• Architecture: Microservices (Node.js/Express + Python APIs), Microfrontend (Angular + React), hybrid databases MySQL & MongoDB.\n"
            "• Leadership: Managing a team of 3 developers. Code Reviews, Mentoring, technical decision-making.\n"
            "• DevOps: DigitalOcean configuration, Linux scripting, scheduled tasks (Cron, BullMQ), automated notifications."
        )},
        {"year": "2023", "title": "Java/Angular Developer Intern", "company": "Vality", "details": (
            "• Developed a school management ERP (Spring Boot backend / Angular frontend).\n"
            "• Implemented application security (Spring Security, JWT)."
        )},
        {"year": "2019-20", "title": "Web Developer & Digital Marketing", "company": "Bdoore Cosmetics", "details": (
            "• Managed digital campaigns (Facebook Ads, Google Ads).\n"
            "• Developed E-commerce solutions (Landing pages, Shopify, WordPress).\n"
            "• Built a centralized CRM for multi-source lead management (call center, confirmation, delivery)."
        )},
        {"year": "2017-22", "title": "Web Developer", "company": "Digiart Agency", "details": (
            "• Developed E-commerce solutions (boutiquelesdomaines.ma, comptoirelectro.ma, ev-qlik.com, mattress.ma).\n"
            "• Created dynamic websites (eglomaroc.ma, dma.ma, chilismaroc.com, digiart.ma, lemaintienadomicile.com)."
        )},
        {"year": "2016-17", "title": "Web Development Internships", "company": "Xerusg Roup, Sysartech, Tawory", "details": ""}
    ],
    
    # -------------------------------------------------------------------------
    # EDUCATION
    # -------------------------------------------------------------------------
    "formation": [
        {"year": "2025-27", "title": "State Engineering Degree (Software Engineering)", "institution": "High Tech School - Engineering School", "details": "Excellence program in computer engineering and IT management."},
        {"year": "2023-24", "title": "Software Engineering Certification", "institution": "ALX Africa - Holberton School", "details": "Intensive program: Advanced algorithms and System Design."},
        {"year": "2016-17", "title": "Professional License Java JEE", "institution": "Faculty of Sciences Aïn Chock", "details": "Distributed software architecture."},
        {"year": "2014-16", "title": "Specialized Technician (IT Development)", "institution": "ISGI - OFPPT", "details": ""}
    ],
    
    # For ATS version
    "education": [
        {
            "degree": "State Engineering Degree (Software Engineering)",
            "institution": "High Tech School - Engineering School",
            "location": "Casablanca, Morocco",
            "dates": "2025 - 2027",
            "details": "State engineering program in computer science, software architecture, and IT management."
        },
        {
            "degree": "Software Engineering Certification",
            "institution": "ALX Africa - Holberton School",
            "location": "Casablanca, Morocco",
            "dates": "2023 - 2024",
            "details": "Intensive program: Algorithms, Data Structures, System Design."
        },
        {
            "degree": "Professional License Java JEE",
            "institution": "Faculty of Sciences Aïn Chock",
            "location": "Casablanca, Morocco",
            "dates": "2016 - 2017",
            "details": "Specialization: N-tier architecture and enterprise development."
        },
        {
            "degree": "Specialized Technician in IT Development",
            "institution": "ISGI - OFPPT",
            "location": "Casablanca, Morocco",
            "dates": "2014 - 2016",
            "details": ""
        },
    ],
    
    # -------------------------------------------------------------------------
    # SKILLS
    # -------------------------------------------------------------------------
    "competences": {
        "LEADERSHIP": [
            "Team Management (3+ devs)",
            "Code Review & Mentoring",
            "Microservices Architecture"
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
            "CI/CD (basics: K8s, Jenkins)"
        ],
        "CMS & E-COMMERCE": [
            "WordPress, PrestaShop, Shopify",
            "Custom themes & plugins"
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
    
    # For ATS version
    "skills": {
        "Leadership & Management": (
            "Team Lead, Code Review, Technical Mentoring, Team Management, "
            "Microservices Architecture, Design Patterns"
        ),
        "Backend Development": (
            "Node.js, Express.js, NestJS, Java, Spring Boot (JPA, MVC, Security), "
            "PHP, Laravel, REST API, SOAP WebServices, GraphQL, BullMQ, Cron Jobs"
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
            "WordPress, PrestaShop, Shopify, Custom Themes & Plugins"
        ),
        "Databases": (
            "MySQL, PostgreSQL, SQL Server, MongoDB, Redis, MERISE, UML"
        ),
    },
    
    # For ATS version - experience format
    "experience": [
        {
            "title": "Tech Lead & Lead Developer",
            "company": "MyTeam 360 (myteam.ma)",
            "location": "Casablanca, Morocco",
            "dates": "2023 - Present",
            "bullets": [
                "Designed and developed a complete collaborative sports management platform adopted by FRMF (Royal Moroccan Football Federation), professional clubs, and academies.",
                "Built modules: administrative management, performance tracking (HOOPER, RPE, GPS), medical records, video analysis, Data Science integration.",
                "Architecture: Microservices (Node.js/Express + Python APIs), Microfrontend (Angular + React), hybrid databases MySQL & MongoDB.",
                "Leadership: Managing a team of 3 developers. Code Reviews, Mentoring, technical decision-making.",
                "DevOps: DigitalOcean configuration, Linux scripting, scheduled tasks (Cron, BullMQ), automated notifications system."
            ]
        },
        {
            "title": "Java/Angular Developer Intern",
            "company": "Vality",
            "location": "Casablanca, Morocco",
            "dates": "2023",
            "bullets": [
                "Developed a school management ERP (Spring Boot backend, Angular frontend).",
                "Implemented application security via Spring Security and JWT.",
                "Designed relational database model and created REST APIs."
            ]
        },
        {
            "title": "Web Developer & Digital Marketing",
            "company": "Bdoore Cosmetics",
            "location": "Casablanca, Morocco",
            "dates": "2019 - 2020",
            "bullets": [
                "Managed digital campaigns (Facebook Ads, Google Ads).",
                "Developed E-commerce solutions (Landing pages, Shopify, WordPress, salesfunnels).",
                "Built a centralized CRM for multi-source lead management (call center, confirmation, delivery)."
            ]
        },
        {
            "title": "Web Developer",
            "company": "Digiart Communication Agency",
            "location": "Casablanca, Morocco",
            "dates": "2017 - 2022",
            "bullets": [
                "Developed E-commerce solutions (boutiquelesdomaines.ma, comptoirelectro.ma, ev-qlik.com, mattress.ma).",
                "Created dynamic websites (eglomaroc.ma, dma.ma, chilismaroc.com, digiart.ma, lemaintienadomicile.com, makeitclean.ma)."
            ]
        },
        {
            "title": "Web Development Internships",
            "company": "Xerusg Roup, Sysartech, Tawory",
            "location": "Casablanca, Morocco",
            "dates": "2016 - 2017",
            "bullets": [
                "Web development internships (4 months, 2 months, 1 month respectively)."
            ]
        },
    ],
    
    # -------------------------------------------------------------------------
    # HOBBIES
    # -------------------------------------------------------------------------
    "loisirs": [
        "Tech Watch (AI, Cloud)",
        "Hackathons & Coding Challenges",
        "Travel & Culture",
        "Community Involvement"
    ],
    
    # -------------------------------------------------------------------------
    # LANGUAGES
    # -------------------------------------------------------------------------
    "langues": [
        {"name": "Arabic", "level": "Native"},
        {"name": "French", "level": "Bilingual"},
        {"name": "English", "level": "Technical"},
    ],
    
    "languages": [
        {"name": "Arabic", "level": "Native"},
        {"name": "French", "level": "Bilingual"},
        {"name": "English", "level": "Technical"},
    ],
    
    # -------------------------------------------------------------------------
    # PDF METADATA
    # -------------------------------------------------------------------------
    "metadata": {
        "author": "Anas Jelloul",
        "title": "CV Anas Jelloul - Tech Lead Full Stack",
        "subject": "CV - Curriculum Vitae",
        "keywords": (
            "Tech Lead, State Engineer, Full Stack, Node.js, Express, Angular, React, "
            "Microservices, MongoDB, MySQL, DigitalOcean, Docker, Morocco"
        )
    }
}


# ==============================================================================
# HOW TO USE
# ==============================================================================
# 1. Open resume_generator.py or resume_generator_ats.py
# 2. Replace USER_DATA = {...} with USER_DATA = USER_DATA_EN (after importing)
#    OR copy-paste the contents directly
# 3. Run: python resume_generator.py
# ==============================================================================
