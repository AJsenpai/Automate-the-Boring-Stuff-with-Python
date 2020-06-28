# combinePdfs.py - Combines all the PDFs in the current working directory into into a single PDF.

import PyPDF2, os

# get all the pdf file name
pdfFiles = []
os.chdir("c:/Users/Jai/Desktop/Docs/myPDF")
# print(os.path.abspath("."))
for filename in os.listdir():
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pdf files and combine them
for pdf in pdfFiles:
    pdf = os.path.abspath(pdf)
    print(pdf)
    pdfFileObj = open(pdf, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # pdfWriter.addPage(pdfReader.getPage(0))
    for pageNum in range(1, pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

# save the resultant pdf to a new pdf file
with open("fusion.pdf", "wb") as fused:
    pdfWriter.write(fused)
print("done!!")
