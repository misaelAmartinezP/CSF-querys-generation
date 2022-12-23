import aspose.words as aw
import os

def conviertePDFaTXT(archivo, nombreAr):#convertir el archivo dpf a txt 
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
           if number in [4,5,6,45,46,47,48,49,50,51,52,53,54,67,69]:
               if number == 4: #RFC
                    print(number, line)
                    print(len(line))
                    if (len(line) == 12):#corroborar longitud del RFC
                         fp.write(line)
                         print(line)
                    elif(len(line)== 13):
                         fp.write(line)
                         print(line)
                    elif(len(line)>=14):
                        x=line.split(' ')
                        fp.write(x[0]+"\n")
                        print(line)
               if number == 5: #razon social
                    print(number, line)
                    print(len(line))
                    if (len(line)!=35):
                        fp.write(line)
                        print(line)
               if number ==  6:
                   print(number, line)
                   print(len(line))
                   if(len(line)!=38):#razon social con cadena encimado de 'Nombre'
                        x=line.split(' ')
                        arr=[]
                        for i in x:
                            if (i != 'Nombre,'):
                                arr.append(i)
                            elif (i=='Nombre,'):
                                break
                        fp.write(" ".join(arr)+"\n")
                        print(" ".join(arr)+"\n")
               if number == 45: #codigo postal
                     print(number, line)
                     print(len(line))
                     if (len(line)!=1):
                         if (len(line) == 21):
                             x=line.split(':')
                             fp.write(x[1])
                             print(line)
                         else:
                             fp.write(line)
                             print(line)
               if number == 46: #codigo postal y nombre de vialidad 
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line) == 21): #division del codigo postal 
                             x=line.split(':')
                             fp.write(x[1])
                             print(x[1])
                      elif(len(line) >=22): #numero interior
                              x=line.partition('NÃºmero Interior:') 
                              x1=list(x)
                              print(x1)
                              fp.write(x1[0]+"\n") #guarda nombre de vialidad 
                              fp.write(x1[1]+" "+x1[2])#guarda numero interior
                              print(x1[0])
                              print(x1[1]+" "+x1[2])
                    else:
                            x=line.partition
               if number == 47:#codigo postal y nombre de vialidad
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line) == 21):#division del codigo postal
                             x=line.split(':')
                             fp.write(x[1])
                             print(x[1])
                      elif(len(line) >=22): #numero interior
                              x=line.partition('NÃºmero Interior:') 
                              x1=list(x)
                              print(x1)
                              fp.write(x1[0]+"\n") #guarda nombre de vialidad 
                              fp.write(x1[1]+" "+x1[2])#guarda numero interior
                              print(x1[0])
                              print(x1[1]+" "+x1[2])
                    else:
                            x=line.partition
               if number == 48:#nombre de vialidad
                    print(number,line)
                    print(len(line))
                    if (len(line)!=1):
                        if(len(line) >=22): #numero interior
                              x=line.partition('NÃºmero Interior:') 
                              x1=list(x)
                              print(x1)
                              fp.write(x1[0]+"\n") #guarda nombre de vialidad 
                              fp.write(x1[1]+" "+x1[2])#guarda numero interior
                              print(x1[0])
                              print(x1[1]+" "+x1[2])
                    else:
                            x=line.partition
               if number == 49:#
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 50:#
                    print(number, line)
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


def inicio():#funcion en donde se introduce la ruta del archivo y el nombre del archivo 
        nombreAr = input("introduzca el nombre del archivo que se encuentra en la direccion: C:/Users/mmartinez/Documents/CSF/")
        archivo =  os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".pdf")
        conviertePDFaTXT(archivo,nombreAr)
        borrar(nombreAr)

inicio()#inici del programa