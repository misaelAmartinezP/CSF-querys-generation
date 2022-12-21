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
               if number == 4: #RFC
                    if (len(line) == 12):
                         fp.write(line)
                    elif(len(line)== 13):
                         fp.write(line)
                    elif(len(line)>=14):
                        x=line.split(' ')
                        fp.write(x[0]+"\n")
               if number == 5: #razon social
                    if (len(line)!=35):
                        fp.write(line)
               if number ==  6:
                   if(len(line)!=38):
                        x=line.split(' ')
                        arr=[]
                        for i in x:
                            if (i != 'Nombre,'):
                                arr.append(i)
                            elif (i=='Nombre,'):
                                break
                        fp.write(" ".join(arr)+"\n")
               if number == 45: #codigo postal
                     if (len(line)!=1):
                         if (len(line) == 21):
                             x=line.split(':')
                             fp.write(x[1])
                         else:
                             fp.write(line)
               if number == 46: #codigo postal y tipo de vialidad 
                    if (len(line)!=1):
                      if (len(line) == 21): #division del codigo postal 
                             x=line.split(':')
                             print(x)
                             fp.write(x[1])
                      else:
                             fp.write(line)
               if number == 47:#codigo postal y tipo de vialidad
                    if (len(line)!=1):
                      if (len(line) == 21):
                             x=line.split(':')
                             print(x)
                             fp.write(x[1])
                      else:
                             fp.write(line)
               if number == 48:#tipo de vialidad
                    if (len(line)!=1):
                      if (len(line) == 21):
                             x=line.split(':')
                             print(x)
                             fp.write(x[1])
                      else:
                             fp.write(line)
               if number == 50:#
                    if (1==1):
                        fp.write(line)
               if number == 51:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 52:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 53:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 54:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 67:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 69:
                    print(number,line)
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