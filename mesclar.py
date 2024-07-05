import PyPDF2
import os

merger = PyPDF2.PdfMerger()

archives_list = os.listdir()
archives_list.sort()
print(archives_list)

for archives in archives_list:
    if ".pdf" in archives:
        merger.append(archives)

merger.write("PDF Mesclado.pdf")
