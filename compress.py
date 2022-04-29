'''
Purpose: compressing the pdfs
Author: Sourabh Katoch
'''
import sys
import PyPDF2

try:
    reader = PyPDF2.PdfFileReader(sys.argv[1])
    writer = PyPDF2.PdfFileWriter()

    for page in reader.pages:
        page.compressContentStreams()
        writer.addPage(page)


    with open('compressed'+sys.argv[1], "wb") as f:
        writer.write(f)
except Exception as err:
    print(f'the program requires path of pdf file. returning with Error {err}')
