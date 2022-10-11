from pdf2docx import Converter
pdf = "sample-table.pdf"
docx = "sample-doc.docx"
cv = Converter(pdf)
cv.convert(docx)
cv.close()