
from PyPDF2 import PdfFileReader
import os


def ConviertePDFaTXT(a):
    with open(a, "rb") as filehandle:
        pdf = PdfFileReader(filehandle)
        print("Leyendo Paginas de la CSF")
        os.system("Pause")
        print("**************************************")
        page1 = pdf.getPage(0)
        page2 = pdf.getPage(1)
        #print(page1)
        #print(page2)
        print("Guardando Valores de la CSF")
        os.system("Pause")
        print("**************************************")
        guardaRFC=page1.extractText()
        guardaRFC1=page2.extractText()
        #print ("monstando los valores de CSF")
        #print(guardaRFC)
        #print(guardaRFC1)
        print("Generando archivo .txt")
        print("**************************************")
        print ("Guardando los datos de CSF hoja 1")
        file1=open(r"C:\Users\mmartinez\Documents\Tapi America Constancia de Situacion Fiscal 14-11-22.txt","w")
        file1.writelines(guardaRFC)
        print("**************************************")
        print ("Guardando los datos de CSF hoja 2")
        file1=open(r"C:\Users\mmartinez\Documents\Tapi America Constancia de Situacion Fiscal 14-11-22.txt","a")
        file1.writelines(guardaRFC1)
        print("**************************************")
        print("Archivo .TXT creado")
        print("**************************************")
        os.system("Pause")
        return file1

def depurarInformacion(file1):
    print("Depurando campos del  CSF que no sean de utilidad")
    print("**************************************")
    print("\n *depurando* \n")
    file1=open(r"C:\Users\mmartinez\Documents\Tapi America Constancia de Situacion Fiscal 14-11-22.txt","w")
    print("**************************************")
    print("Tratamiento de cadenas")
    print("**************************************")
    print("Validacion de cadenas")
    print("**************************************")
    print("Archivo .TXT depurado ")
    print("**************************************")

def Inicio():
    print ("Este herramienta convierte de pdf a txt \nRealiza la extraccion de datos de una CSF \nPosteriormente arroja la sentencia SQL para realizar un update/insert")
    os.system("Pause \n")
    print("**************************************")
    a = "C:/Users/mmartinez/Documents/Tapi America Constancia de Situacion Fiscal 14-11-22.pdf"
    ConviertePDFaTXT(a)
    b = "C:/Users/mmartinez/Documents/Tapi America Constancia de Situacion Fiscal 14-11-22.txt" 
    depurarInformacion(a)
    
Inicio()