import PyPDF2
import sys

files = sys.argv[1:]

def pdf_combine(file_list):
  merger = PyPDF2.PdfFileMerger()
  for file in file_list:
    print(file)
    merger.append(file)
  merger.write('merged.pdf')

pdf_combine(files)