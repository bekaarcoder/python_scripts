import PyPDF2

with open('twopage.pdf', 'rb') as file:
  reader = PyPDF2.PdfFileReader(file)
  page = reader.getPage(0)
  page.rotateClockwise(90)
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)
  with open('rotate.pdf', 'wb') as new_file:
    writer.write(new_file)