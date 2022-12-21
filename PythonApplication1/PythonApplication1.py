

import aspose.words as aw
import os


def conviertePDFaTXT(archivo, nombreAr):
        doc = aw.Document(archivo)
        print("Generando el .txt")
        doc.save("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt")
        print("Documento Generado")

def borrar(nombreAr):
    archivoTxt= os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt")
    l1 = []
    with open(archivoTxt, 'r') as fp:
        l1 = fp.readlines()
    with open(archivoTxt, 'w') as fp:
        for number, line in enumerate(l1):
           if number in [4,5,6,45,46,47,48,50,51,52,53,54,67,69]:
               if number == 4:
                    if (len(line) == 12):
                         fp.write(line)
                    elif(len(line)==13):
                         fp.write(line)
                    elif(len(line)>=14):
                        x=line.split(' ')
                        fp.write(x[0]+"\n")
               if number == 5:
                    if (len(line)!=35):
                        fp.write(line)
               if number ==  6:
                     if (1==1):
                         x=line.split(' ')
                         print(x)
                         fp.write(x[0]+""+ x[1]+"\n")
               if number == 45:
                     if (1==1):
                        fp.write(line)
               if number == 46:
                     if (1==1):
                        fp.write(line)
               if number == 47:
                    if (1==1):
                        fp.write(line)
               if number == 48:
                    if (1==1):
                        fp.write(line)
               if number == 50:
                    if (1==1):
                        fp.write(line)
               if number == 51:
                    if (1==1):
                        fp.write(line)
               if number == 52:
                    if (1==1):
                        fp.write(line)
               if number == 53:
                    if (1==1):
                        fp.write(line)
               if number == 54:
                    if (1==1):
                        fp.write(line)
               if number == 67:
                    if (1==1):
                        fp.write(line)
               if number == 69:
                    if (1==1):
                        fp.write(line)
               #fp.write(line)
    os.system("Pause")
  


def inicio():
        nombreAr = input("introduzca el nombre del archivo que se encuentra en la direccion: C:/Users/mmartinez/Documents/CSF/")
        archivo =  os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".pdf")
        conviertePDFaTXT(archivo,nombreAr)
        borrar(nombreAr)

inicio()