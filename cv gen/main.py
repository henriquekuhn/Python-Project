from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Henrique Cafruni Kuhn', 0, 1, 'C')
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, 'Software Test & Validation | Software Engineer | IoT | R&D | Embedded Systems | Microelectronics', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        body = body.encode('latin-1', 'replace').decode('latin-1')
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, body):
        self.chapter_title(title)
        self.chapter_body(body)

# Create instance of FPDF class
pdf = PDF()
pdf.add_page()

# Add contact information
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Email: henriqueckuhn@gmail.com', 0, 1)
pdf.cell(0, 10, 'Phone: +55 51 99160-02840', 0, 1)
pdf.cell(0, 10, 'Location: Porto Alegre, RS, Brazil', 0, 1)
pdf.cell(0, 10, 'LinkedIn: linkedin.com/in/henriqueckuhn', 0, 1)
pdf.cell(0, 10, 'GitHub: github.com/henriquekuhn', 0, 1)
pdf.ln(10)

# Add experience section
experience_text = """\
Research and Development Engineer
Itt Chip - Unisinos
Sao Leopoldo, Jan 2024 - Present
- Developed a database application in Python utilizing SQLAlchemy to manage data from SiP development and mass production platforms.
- Planned, developed, and documented test platforms (functional, performance, characterization, and pre-compliance) and created automated tests using Python, C, National Instruments (PXI, LabView, and TestStand), and Rohde and Schwarz tools.
- Developed IoT embedded C applications for LoRa/Bluetooth and NB-IoT Low Energy devices.

Senior Advanced R&D Engineer
HTMicron Semiconductors S.A
Sao Leopoldo, Apr 2021 - Nov 2023
- Planned, developed, and documented test platforms (functional, performance, characterization, and pre-compliance) and created automated tests using Python, C, National Instruments (PXI, LabView, and TestStand), and Rohde and Schwarz tools.
- Developed automated mass production test platforms using National Instruments tools.
- Created IoT embedded C applications for LoRa/Bluetooth Low Energy devices.

Research - IoT Project for Semiconductor Factory
Itt Chip - Unisinos
Sao Leopoldo, Mar 2018 - Apr 2021
- Studied and developed IoT hardware to monitor environment and process variables for a semiconductor factory, integrating analog and digital sensors, microcontrollers, and 6LowPan communication.
- Developed APIs for digital sensors, test platforms, and applications using C, Python, and uPython.
- Designed products, enclosures, and cabinets using SolidWorks.

Project Analyst
Racional Tecnologia
Porto Alegre, Dec 2017 - Mar 2018
- Planned security systems (cameras, sensors, etc.) for condominiums.
- Conducted field activities involving the installation of automation panels, infrastructure, and sensors.
- Designed hardware to reduce panel installation time and enhance confidence.
"""
pdf.add_section('Experience', experience_text)

# Add education section
education_text = """\
M.Sc. in Electrical Engineering
Universidade do Vale do Rio dos Sinos
Sao Leopoldo, RS, Brazil, 2018 - 2020
- Developed a non-intrusive sensor of electromagnetic fields in Three-Phase Motors for predicting mechanical and electrical failures.

B.Sc. in Control and Automation Engineering
Pontificia Universidade Catolica do Rio Grande do Sul
Porto Alegre, RS, Brazil, 2009 - 2016
- Developed an autonomous temperature control system for the brewing process in microbreweries. Modeled a Proportional-Integral system and programmed an ATMEGA328p Microcontroller in C to control a thermal resistor.

Exchange B.Sc in Computer and Electronics Engineering
Galway-Mayo Institute of Technology
Galway, Ireland, 2013 - 2014
- Conducted research, design, and development of a biosimulator for bronchoscopy training, presented at the International Bronchoscopy Workshop in Galway, Ireland.
"""
pdf.add_section('Education', education_text)

# Add skills section
skills_text = """\
Programming Languages: Python, C, C++, uPython
Tools & Technologies: Git, Matlab, National Instruments TestStand, National Instruments LabView, SAP, SolidWorks, AutoCAD, Altium
Specializations: Embedded Systems, IoT, R&D, Software Testing & Validation
"""
pdf.add_section('Skills', skills_text)

# Add languages section
languages_text = """\
Portuguese: Native
English: Advanced
Spanish: Intermediate
"""
pdf.add_section('Languages', languages_text)

# Output the PDF
pdf.output('Henrique_Kuhn_CV.pdf')
