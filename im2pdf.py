#!/usr/bin/env python
# this puts a simple image into a pdf in landscape mode
# using reportlab
# you can just omit the landscape() call if you don't want landscape.

# as you should know A4 pdf is 597.276 x 841.89
# and allowing for a tiny margin, you should aim for an image of size 838x594 (in point units).

# this will make the image almost take up the whole
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
c2 = canvas.Canvas('myfile1.pdf', pagesize=landscape(A4))
# c2.drawImage("dpg2.png", 50,50)
c2.drawImage("r3.png", 2, 2)
c2.showPage()
c2.save()
