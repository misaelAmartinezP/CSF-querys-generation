
from PyPDF2 import PdfFileReader
import os

def ConviertePDFaTXT(archivo, nombreAr):
    with open(archivo, "rb") as filehandle:
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
        file1=open(r"archivo","w")    
        file1.writelines(guardaRFC)
        print("**************************************")
        print ("Guardando los datos de CSF hoja 2")
        file1=open(nombreAr.txt,"ra")
        file1.writelines(guardaRFC1)
        print("**************************************")
        print("Archivo .TXT creado")
        print("**************************************")
        os.system("Pause")
        return file1


def Inicio():
    print ("Este herramienta convierte de pdf a txt \nRealiza la extraccion de datos de una CSF \nPosteriormente arroja la sentencia SQL para realizar un update/insert \n")
    os.system("Pause")
    nombreAr = input("introduzca el nombre del archivo que se encuentra en la direccion: C:/Users/mmartinez/Documents/")
    #aqui se deberia cambiar la ruta dependiendo de la computadora y en donde se tengan las CSF
    print("**************************************")
    #print (archivoIn)
    archivo =  os.path.join("C:/Users/mmartinez/Documents/" + nombreAr +".pdf")
    ConviertePDFaTXT(archivo, nombreAr)
    #print(archivo)


Inicio()