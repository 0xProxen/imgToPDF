from fpdf import FPDF
import os
pdf = FPDF()

for image in os.listdir("images"):
    pdf.add_page()
    pdf.image('images/'+image,x = None,y = None)

pdf.output(name="images.pdf",dest= "F")