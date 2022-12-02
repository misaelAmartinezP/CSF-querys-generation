
from PyPDF2 import PdfFileReader

pdf_document = "C:/Users/mmartinez/Documents/Tapi America Constancia de Situacion Fiscal 14-11-22.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    page1 = pdf.getPage(0)
    print(page1)
    guardaRFC=page1.extractText()
    print ("monstando los valores de CSF")
    print(guardaRFC)
    print ("Guardando los datos de CSF")
    file1=open(r"C:\Users\mmartinez\Documents\Tapi America Constancia de Situacion Fiscal 14-11-22.txt","w")
    file1.writelines(guardaRFC)

