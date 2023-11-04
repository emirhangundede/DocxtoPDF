from pdf2docx import Converter

pdf_file='PDFDeneme.pdf'
docx_file='Sample.docx'

cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()



