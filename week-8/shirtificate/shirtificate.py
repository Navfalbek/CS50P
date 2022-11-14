"""
In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate 
in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.

The format of the PDF should be A4, which is 210mm wide by 297mm tall.

The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.

The shirt’s image should be centered horizontally.

The user’s name should be on top of the shirt, in white text.

"""


from fpdf import FPDF


pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
pdf.add_page()
pdf.set_font("helvetica", size = 36)
pdf.cell(75)
pdf.cell(50, 20, "CS50 Shirtificate", align = "C")
pdf.ln(40)
pdf.image("shirtificate.png", x = 1, y = 40)
pdf.set_font("helvetica", size = 28)
pdf.set_text_color(r = 255, g = 255, b = 255)
pdf.cell(77)
name = str(input("Name: "))
pdf.cell(40, 120, f"{name} took CS50", align = "C")

pdf.output("navfal's shirtificate.pdf")
