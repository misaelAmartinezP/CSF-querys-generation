
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
        archivoTxt= "C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt"
        file1=open(archivoTxt,"w")    
        file1.writelines(guardaRFC)
        print("**************************************")
        print ("Guardando los datos de CSF hoja 2")
        file1=open(archivoTxt,"a")
        file1.writelines(guardaRFC1)
        print("**************************************")
        print("Archivo .TXT creado")
        print("**************************************")
        os.system("Pause")


def borrar(nombreAr):
    archivoTxt= os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt")
    l1 = []
    with open(archivoTxt, 'r') as fp:
        l1 = fp.readlines()
    with open(archivoTxt, 'w') as fp:
        for number, line in enumerate(l1):
           if number in [2,4,5,24,25,26,27,28,44]:
               if number == 2:
                    if (len(line) == 11 or 12):
                         fp.write(line)
               if number == 4:
                    if (1==1):
                        fp.write(line)
               if number ==  5:
                    if (len(line) !=30):
                        fp.write(line)
               if number == 24:
                    if (1==1):
                        fp.write(line)
               if number == 25:
                    if (1==1):
                        fp.write(line)
               if number == 26:
                    if (1==1):
                        fp.write(line)
               if number == 27:
                    if (1==1):
                        fp.write(line)
               if number == 28:
                    if (1==1):
                        fp.write(line)

               #fp.write(line)
    os.system("Pause")
  


def Inicio():
    print ("Este herramienta convierte de pdf a txt \nRealiza la extraccion de datos de una CSF \nPosteriormente arroja la sentencia SQL para realizar un update/insert \n")
    os.system("Pause")
    nombreAr = input("introduzca el nombre del archivo que se encuentra en la direccion: C:/Users/mmartinez/Documents/CSF/")
    #aqui se deberia cambiar la ruta dependiendo de la computadora y en donde se tengan las CSF
    print("**************************************")
    archivo =  os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".pdf")
    ConviertePDFaTXT(archivo, nombreAr)
    print("**************************************")
    print("Parceando informacion")
    borrar(nombreAr)
    #separaPalabras(nombreAr)

Inicio()