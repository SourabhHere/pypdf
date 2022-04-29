'''
Purpose: merge 2 or more pdfs as one
Author: Sourabh Katoch
'''
import sys
from PyPDF2 import PdfFileMerger

print(sys.argv)

def pdf_merge(pdflist):
    '''
    function for merging pdfs given as list of pdf files
    '''
    merger = PdfFileMerger()

    for pdf in pdflist:
        merger.append(pdf)

    merger.write('merged-output.pdf')
    merger.close()


pdf_list = sys.argv[1:]

try:
    pdf_merge(pdf_list)
except Exception as err:
    print(f'following error occured while trying to run script {err}')
