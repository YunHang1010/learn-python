# combinePdfs.py - COmbines all the PDFs in the current working directory into
# into a single PDF

import PyPDF2,os

pdfFiles = []
for filename in os.listdir('filepath'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        
pdfOutput = open('outputfilename.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()