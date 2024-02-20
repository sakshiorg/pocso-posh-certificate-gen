from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
import csv,os


rakshins = []
file = open("../Assets/rakshins-pocso.csv", "r", encoding = 'utf-8')
data = csv.reader(file)
for rakshin in data:
    rakshins.append(rakshin)


for i in rakshins:
    rname, rclg, rdate, rloc = i[1], i[2], i[3], i[4]
    if not os.path.exists(rname+".pdf"):
        pdfname = (rname+".pdf")
        c = canvas.Canvas(pdfname, pagesize = (862.5, 600))
        c.setTitle(rname+"'s Certificate One")
        c.drawImage("../Assets/cert-1.png", 0, 0, width = 862.5, height = 600)
        pdfmetrics.registerFont(TTFont('Allura', '../Assets/allura.ttf'))

        c.setFillColor(Color(0, 0, 0, alpha = 1))

        c.scale(1, 1)
        c.setFont("Allura", 40)
        c.drawCentredString(431.25, 290, rname)

        c.setFont("Helvetica", 10)
        c.drawString(66, 93, rdate)
        c.drawString(90, 71.4, rclg+", "+rloc)

        c.showPage()
        c.save()
        
        print(rname + " certificate generated.")

