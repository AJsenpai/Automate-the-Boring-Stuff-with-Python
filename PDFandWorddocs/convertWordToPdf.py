# This script runs on Windows only, and you must have Word installed.
import win32com.client  # pipenv install pywin32==224
import os
import docx

wordFileName = "mydoc.docx"
pdfFileName = "sample.pdf"
os.chdir("c:/Users/Jai/Desktop/Docs")
doc = docx.Document()
doc.save(wordFileName)
wdFormatPDF = 17  # word's numeric code for PDF
wordObj = win32com.client.Dispatch("Word.Application")

docObj = wordObj.Documents.Open(f"c:/Users/Jai/Desktop/Docs/{wordFileName}")
docObj.SaveAs(pdfFileName, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
