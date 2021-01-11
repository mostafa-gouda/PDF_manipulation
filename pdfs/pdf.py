import PyPDF2
import sys


# with open("twopage.pdf", "rb") as pdf:
# reader = PyPDF2.PdfFileReader(pdf)
# page1 = reader.getPage(0)
# page1.rotateClockwise(90)
# writer = PyPDF2.PdfFileWriter()
# writer.addPage(page1)
# with open("tilt.pdf", "wb") as pdf2:
#     writer.write(pdf2)


# def mergePDFs(*args):
#     writer = PyPDF2.PdfFileWriter()
#     for pdf in args:
#         with open(pdf, "rb") as file1:
#             pdf1 = PyPDF2.PdfFileReader(file1)
#             with open("merge.pdf", "wb") as file:
#                 for page in pdf1.pages:
#                     writer.addPage(page)
#                     writer.write(file)
#
#
# pdf_names = sys.argv[1:]
# mergePDFs(*pdf_names)

# def watermark(pdf, wtr):
#     pdf1 = PyPDF2.PdfFileReader(open(pdf, "rb"))
#     wtr1 = PyPDF2.PdfFileReader(open(wtr, "rb"))
#     writer = PyPDF2.PdfFileWriter()
#     with open(f"{pdf.replace('.pdf','')}_wtr.pdf", "wb") as output:
#         for i in range(pdf1.numPages):
#             page = pdf1.getPage(i)
#             page.mergePage(wtr1.getPage(0))
#             writer.addPage(page)
#             writer.write(output)
#
#
# watermark("twopage.pdf", "wtr.pdf")
