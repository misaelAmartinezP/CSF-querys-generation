import aspose.words as aw
import os
from os import path

def conviertePDFaTXT(archivo, nombreAr, directorio):#convertir el archivo dpf a txt 
        doc = aw.Document(archivo)
        print("Generando el .txt")
        dir=(directorio+"/"+nombreAr)
        print(dir)
        doc.save( dir +".txt")
        print("Documento Generado")
def borrar(nombreAr,directorio): #depuracion de lineas del pdf para quedar los campos dE: RFC, RAZON SOCIAL, CODIGO POSTAL, NOMBRE DE VIALIDAD, NUMERO INTERIOR, TIPO DE VIALIDAD, NUMERO EXTERIOR, NOMBRE COLONIA, REGIMEN 
    archivoTxt= os.path.join(directorio + "/" + nombreAr +".txt")
    l1 = []
    with open(archivoTxt, 'r') as fp:
        l1 = fp.readlines()
    with open(archivoTxt, 'w') as fp:
        for number, line in enumerate(l1):
           if number in [4,5,6,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,59,66,67,68,69]:
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
                        rfc=line.split(' ')
                        fp.write(rfc[0]+"\n")
                        print(line)
               if number == 5: #razon social
                    print(number, line)
                    print(len(line))
                    raSo=line.partition('Nombre,')
                    if ('Nombre,' in raSo):
                        print(raSo[0]+"\n")
                        fp.write(raSo[0]+"\n")
                    elif (len(line)!=35):
                        fp.write(line)
                        print(line)
               if number ==  6:
                   print(number, line)
                   print(len(line))
                   idCIF=line.partition('idCIF:')
                   if('idCIF:' in idCIF):
                        print("no se imprime la linea")
                   elif(len(line)!=38):#razon social con cadena encimado de 'Nombre'
                        raSo=line.split(' ')
                        raSoArr=[]
                        for i in raSo:
                            if (i != 'Nombre,'):
                                raSoArr.append(i)
                            elif (i=='Nombre,'):
                                break
                        fp.write(" ".join(raSoArr)+"\n")
                        print(" ".join(raSoArr)+"\n")
               if number == 40:#codigo postal y nombre de vialidad
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line) == 21): #division del codigo postal
                             cp=line.partition("PÃ¡gina")
                             if('PÃ¡gina' in cp):
                                 print("excepcion no se imprime")
                             else:
                                 cp=line.split(':')
                                 fp.write(cp[1])
                             print(cp[1])
                      elif(len(line) >=22): #tipo vialidad
                              tipVial=line.partition('Tipo de Vialidad:') 
                              print(tipVial)
                              tipoVialStrAux=tipVial[0]
                              print(tipoVialStrAux)
                              if ('Tipo de Vialidad:' in tipVial):
                                  tipVialAux=tipoVialStrAux.replace('Tipo de Vialidad:', " ")
                                  tipVialidad=list(tipVial)
                                  tipVialidadStr=" ".join(tipVialidad)
                                  cp=tipoVialStrAux.partition('CÃ³digo Postal:')
                                  print("tupla la siguiente linea")
                                  print(cp)
                                  fp.write(cp[2]+"\n") #guarda cp
                                  fp.write(tipVialidad[2]+"\n")#guarda tipo de vialidad
                                  print(cp[2]+"\n")
                                  print(tipVialidad[2]+"\n")
                              else: 
                                  print(line)
                                  fp.write(line)
               if number == 41:#nombre de vialidad y numero exterior
                    print(number,line)
                    print(len(line))
                    if (len(line)!=1):
                         nomVial=line.partition('NÃºmero Exterior:')
                         if('NÃºmero Exterior:' in nomVial):
                             nomVialAuxStr=" ".join(nomVial)
                             nomVialAuxRep=nomVialAuxStr.replace('Nombre de Vialidad:', " ")
                             nomVialAux=nomVialAuxRep.partition('NÃºmero Exterior:')
                             if('NÃºmero Exterior:' in nomVialAux):
                                 print(nomVialAux[0]+"\n"+nomVialAux[2]+"\n")
                                 fp.write(nomVialAux[0]+"\n"+nomVialAux[2]+"\n")#guarda numero exterior 
               if number == 42:#
                   print(number,line)
                   print(len(line))
                   if (len(line)!=1):
                        divLin=line.partition('Nombre de la Colonia:')
                        print(divLin)
                        divLinAux=divLin[0]
                        print(divLin)
                        numInt="".join(divLinAux+" NULL \n")
                        numIntAux=numInt.partition('NÃºmero Interior:')
                        print(numIntAux)
                        fp.write(numIntAux[2])
                        print(numIntAux[2])
                        divLinAuxNom=divLin[1]
                        nomCol="".join(divLinAuxNom+" NULL \n")
                        print(nomCol)
                        nomColAux=nomCol.partition('Nombre de la Colonia:')
                        fp.write(nomColAux[2])
                        print(nomColAux[2])
               if number == 43:#codigo postal y nombre de vialidad
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line) == 21): #division del codigo postal
                             cp=line.partition("PÃ¡gina")
                             if('PÃ¡gina' in cp):
                                 print("excepcion no se imprime")
                             else:
                                 cp=line.split(':')
                                 fp.write(cp[1])
                             print(cp[1])
               if number == 44: #nombre de la vialidad y codigo postal
                     print(number, line)
                     print(len(line))
                     nomVial=line.partition('NÃºmero Interior:')
                     if('NÃºmero Interior:' in nomVial):
                         print(nomVial)
                         nomVialStr=str(nomVial[0])
                         nomVialStr=nomVialStr.partition('Nombre de Vialidad:')
                         print(nomVialStr)
                         if('Nombre de Vialidad:' in nomVialStr):
                             print(nomVialStr[2]+"\n")
                             fp.write(nomVialStr[2]+"\n")
                         print(nomVial[2]+"\n")
                         fp.write(nomVial[2]+"\n")
               if number == 45: #codigo postal
                     print(number, line)
                     print(len(line))
                     if (len(line)!=1):
                         eliEntF=line.partition('Nombre de la Entidad Federativa:')
                         if ('Nombre de la Entidad Federativa:' in eliEntF):
                             print("informacion no util")
                         else:
                             if (len(line) == 21):#division del codigo postal 
                                 cp=line.split(':')
                                 fp.write(cp[1]+"\n")
                                 print(cp[1]+"\n")
                             else:
                                 fp.write(line)
                                 print(line)
               if number == 46: #codigo postal y nombre de vialidad 
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                        eliEmail=line.partition('Correo ElectrÃ³nico:')
                        if ('Correo ElectrÃ³nico:' in eliEmail):
                            print("informacion no util")
                        else:
                          if (len(line) == 21): #division del codigo postal 
                                 cp=line.split(':')
                                 fp.write(cp[1])
                                 print(cp[1])
                          elif(len(line) >=22): #numero interior
                                  numInt=line.partition('NÃºmero Interior:') 
                                  if ('NÃºmero Interior:' in numInt):
                                      numIntl=list(cp)
                                      print(numIntl)
                                      fp.write(numIntl[0]+"\n") #guarda nombre de vialidad 
                                      fp.write(numIntl[1]+" "+numIntl[2])#guarda numero interior
                                      print(numIntl[0])
                                      print(numIntl[1]+" "+numIntl[2])
                                  else: 
                                      print(line)
                                      fp.write(line)
               if number == 47:#codigo postal y nombre de vialidad
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                        if (len(line) == 21): #division del codigo postal 
                             cp=line.split(':')
                             fp.write(cp[1])
                             print(cp[1])
                        if(len(line) >=22): #numero interior
                              numInt=line.partition('NÃºmero Interior:')
                              if ('NÃºmero Interior:' in numInt):
                                  print("true")
                                  numIntl=list(numInt)
                                  print(numIntl)
                                  fp.write(numIntl[0]+"\n")
                                  fp.write(numIntl[1]+" "+numInt[2])#guarda numero interior
                                  print(numIntl[0]+"\n")
                                  print(numIntl[1]+" "+numIntl[2])
                              else:
                                    nomVia=line.partition('Nombre de Vialidad:')
                                    if('Nombre de Vialidad:' in nomVia):
                                        print(line)
                                        fp.write(line)
               if number == 48:#nombre de vialidad, quitar linea nombre entidad federativa 
                    print(number,line)
                    print(len(line))
                    if (len(line)!=1):
                        if(len(line) >=22): #numero interior
                              numInt=line.partition('NÃºmero Interior:')
                              if ('NÃºmero Interior:' in numInt):
                                  print("true")
                                  numIntl=list(numInt)
                                  print(numIntl)
                                  fp.write(numIntl[0]+"\n") #guarda nombre de vialidad 
                                  fp.write(numIntl[1]+" "+numIntl[2])#guarda numero interior
                                  print(numIntl[0])
                                  print(numIntl[1]+" "+numIntl[2])
                              else:
                                  nomLoc=line.partition('Nombre de la Localidad:')
                                  if('Nombre de la Localidad:' in nomLoc):
                                        print("nombre de la localidad no se guarda")
               if number == 49:# quitar linea nombre entidad federativa 
                    print(number,line)
                    nomLoc=line.partition('Nombre de la Localidad:')
                    if('Nombre de la Localidad:' in nomLoc):#nombre de la localidad no se guarda en el txt
                        print("nombre de la localidad no se guarda")
                    else: 
                        nomEnt=line.partition('Nombre de la Entidad Federativa:')
                        if('Nombre de la Entidad Federativa:' in nomEnt):#nombre de la entidad no se guarda en el txt
                             print("no se imprime nombre de la entidad federativa")
                        else:
                            telfijo=line.partition('Tel. Fijo Lada:')#tel fijo no se guarda
                            if('Tel. Fijo Lada:' in telfijo):
                                print("no se imprime el telefono fijo")
                            elif('Tel. Fijo Lada:' not in telfijo):
                                eliCreate=line.partition('Aspose.Words.')
                                if('Aspose.Words.' in eliCreate):
                                    print("informacion no util")
                            else:
                                fp.write(line)
                                print(line)
               if number == 50:#quitar linea nombre entidad federativa 
                    print(number,line)
                    nomEnt=line.partition('Nombre de la Entidad Federativa:')
                    if('Nombre de la Localidad:' in nomEnt):#nombre de la localidad no se guarda en el txt
                         print("nombre de la entidad no se guarda")
                    elif('Nombre de la Localidad:' not in nomEnt):
                        entid=line.partition('Nombre de la Entidad Federativa:')
                        if('Nombre de la Entidad Federativa:' in entid):#nombre de la entidad no se guarda en el txt
                             print("no se imprime nombre de la entidad federativa")
                        elif('Nombre de la Entidad Federativa:' not in entid):
                            eliPag=line.partition('PÃ¡gina')
                            if('PÃ¡gina' in eliPag):
                                print("informacion no util")
                        else:
                            telfijo=line.partition('Tel. Fijo Lada:')#tel fijo no se guarda
                            if('Tel. Fijo Lada:' in telfijo):
                                print("no se imprime el telefono fijo") 
                            else:
                                fp.write(line)
                                print(line)
                    else:
                        tipoVialid=line.partition('Tipo de Vialidad:')
                        if ('Tipo de Vialidad:' in tipoVialid):
                            tipoViaL=list(tipoVialid)
                            print(tipoViaL)
                            fp.write(tipoViaL[1]+" "+tipoViaL[2])#guarda tipo de vialidad 
               if number == 51:
                    print(number,line)
                    tipoVialid=line.partition('Tipo de Vialidad:')
                    if ('Tipo de Vialidad:' in tipoVialid):
                         tipoViaL=list(tipoVialid)
                         print(tipoViaL)
                         tipoVialStrAux=" ".join (tipoViaL)
                         if('NÃºmero Exterior:' in tipoVialStrAux):#caso en donde numero exterior y tipo de vialidad estan en la misma linea 
                             print("impresos pero no guardados")
                             avNomExt=tipoVialStrAux.replace('Tipo de Vialidad:', " ")
                             avNomExtAux=avNomExt.partition('NÃºmero Exterior:')
                             print(avNomExtAux)
                             print(avNomExtAux[0]+"\n"+avNomExtAux[2]+"\n")
                             fp.write(avNomExtAux[0]+"\n")
                             fp.write(avNomExtAux[2]+"\n")
                         else:
                             print("no paso")
                             fp.write(tipoViaL[1]+" "+tipoViaL[2])#guarda tipo de vialidad
                    elif('NÃºmero Exterior:' not in tipoVialid):
                         nomExt=line.partition('NÃºmero Exterior:')
                         if ('NÃºmero Exterior:' in nomExt):
                             print(nomExt)
                             fp.write(line)
               if number == 52:
                    print(number,line)
                    tipoVialid=line.partition('Tipo de Vialidad:')
                    if ('Tipo de Vialidad:' in tipoVialid):
                         tipoViaL=list(tipoVialid)
                         print(tipoViaL)
                         tipoVialStrAux=" ".join (tipoViaL)
                         if('NÃºmero Exterior:' in tipoVialStrAux):#caso en donde numero exterior y tipo de vialidad estan en la misma linea 
                             print("impresos pero no guardados")
                             avNomExt=tipoVialStrAux.replace('Tipo de Vialidad:', " ")
                             avNomExtAux=avNomExt.partition('NÃºmero Exterior:')
                             print(avNomExtAux)
                             print(avNomExtAux[0]+"\n"+avNomExtAux[2]+"\n")
                             fp.write(avNomExtAux[0]+"\n")
                             fp.write(avNomExtAux[2]+"\n")
                         else:
                             print("no paso")
                             fp.write(tipoViaL[1]+" "+tipoViaL[2])#guarda tipo de vialidad
                    elif('NÃºmero Exterior:' not in tipoVialid):
                         nomExt=line.partition('NÃºmero Exterior:')
                         if ('NÃºmero Exterior:' in nomExt):
                             print(nomExt)
                             fp.write(line)
                         else:
                             nomCol=line.partition('Nombre del Municipio o DemarcaciÃ³n Territorial:')#guardar numero exterior
                             if ('Nombre del Municipio o DemarcaciÃ³n Territorial:' in nomCol):
                                 print(numExt[0]+"\n")
                                 fp.write(numExt[0]+"\n")
                             elif('Nombre del Municipio o DemarcaciÃ³n Territorial:' not in nomCol):
                                print(line)
                                fp.write(line)
               if number == 53:
                    print(number,line)
                    nomMun=line.partition('Nombre del Municipio o DemarcaciÃ³n Territorial:')#guardar numero exterior
                    if ('Nombre del Municipio o DemarcaciÃ³n Territorial:' in nomMun):
                         print(nomMun[0]+"\n")
                         fp.write(nomMun[0]+"\n")
                    elif('Nombre del Municipio o DemarcaciÃ³n Territorial:' not in nomMun):
                        nomCol=line.partition('Nombre de la Colonia:')
                        print(nomCol)
                        if('Nombre de la Colonia:' in nomCol):# nombre de la colonia
                            print(nomCol[1]+" "+nomCol[2]+"\n")
                            fp.write(nomCol[1]+" "+nomCol[2]+"\n")
                        else:
                             numExt=line.partition('NÃºmero Exterior:')#numero exterior
                             if ('NÃºmero Exterior:' in numExt):
                                 print(numExt)
                                 print(numExt[1]+" "+numExt[2]+"\n")
                                 fp.write(numExt[1]+" "+numExt[2]+"\n")
               if number == 54:
                    print(number,line)
                    nomMun=line.partition('Nombre del Municipio o DemarcaciÃ³n Territorial:')#guardar numero exterior
                    if ('Nombre del Municipio o DemarcaciÃ³n Territorial:' in nomMun):
                         print(nomMun[0]+"\n")
                         fp.write(nomMun[0]+"\n")
                    elif('Nombre del Municipio o DemarcaciÃ³n Territorial:' not in nomMun):#eliminar nombre del municipio
                        corEli=line.partition('Correo ElectrÃ³nico:')
                        if('Correo ElectrÃ³nico:' in corEli):#eliminar correo
                            print("esta linea no se imprime")
                        elif('Correo ElectrÃ³nico:' not in corEli):
                            entCall=line.partition('Entre Calle:')
                            if('Entre Calle:' in entCall): #eliminar entre calle
                                print("Esta linea no se imprime")
                            elif('Entre Calle:' not in entCall):
                                eliActEco=line.partition('Actividades EconÃ³micas:')
                                if('Actividades EconÃ³micas:' in eliActEco):
                                    print("informacion no util")
                            else:
                                print(line)
                                fp.write(line)
               if number ==59:
                    print(number,line)
                    reg=line.partition('Personas Morales con Fines no Lucrativos')#regimen
                    print(reg)
                    if ('Personas Morales con Fines no Lucrativos' in reg):
                         print(reg[1]+"\n")
                         fp.write(reg[1]+"\n")
               if number ==66:
                    print(number,line)
                    reg=line.partition('RÃ©gimen General de Ley Personas Morales')#regimen
                    print(reg)
                    if ('RÃ©gimen General de Ley Personas Morales' in reg):
                         print(reg[1]+"\n")
                         fp.write(reg[1]+"\n")
               if number == 67:
                    print(number,line)
                    reg=line.partition('RÃ©gimen General de Ley Personas Morales')#regimen
                    print(reg)
                    if ('RÃ©gimen General de Ley Personas Morales' in reg):
                         print(reg[1]+"\n")
                         fp.write(reg[1]+"\n")
               if number == 68:
                    print(number,line)
                    reg=line.partition('RÃ©gimen General de Ley Personas Morales')#regimen
                    print(reg)
                    if ('RÃ©gimen General de Ley Personas Morales' in reg):
                         print(reg[1]+"\n")
                         fp.write(reg[1]+"\n")
               if number == 69:
                    print(number,line)
                    reg=line.partition('RÃ©gimen General de Ley Personas Morales')#regimen
                    print(reg)
                    if ('RÃ©gimen General de Ley Personas Morales' in reg):
                         print(reg[1]+"\n")
                         fp.write(reg[1]+"\n")
               #fp.write(line)
                

def numeroLineasNueve(nombreAr, directorio):
        archivoTxt= os.path.join(directorio+"/" + nombreAr +".txt")
        l1 = []
        with open(archivoTxt, 'r') as fp:
            l1 = fp.readlines()
        with open(archivoTxt, 'w') as fp:
            for number, line in enumerate(l1):
                print(number,line, len(line))
                if (len(line)!=1):
                    fp.write(line)


def campoListo(nombreAr, directorio):
        archivoTxt= os.path.join(directorio + "/" + nombreAr +".txt")
        l1 = []
        with open(archivoTxt, 'r') as fp:
            l1 = fp.readlines()
        with open(archivoTxt, 'w') as fp:
            for number, line in enumerate(l1):
                print(number,line)
                if number in [0,1,2,3,4,5,6,7,8]:
                       if number == 0:#rfc
                           fp.write(line)
                       if number == 1:#razon social
                           fp.write(line)
                       if number == 2:#codigo postal
                           fp.write(line)
                       if number == 3:#nombre de vialidad
                            nomVial=line.partition('Nombre de Vialidad:')
                            print("entro en la funcion campo listo")
                            print(nomVial)
                            if ('Nombre de Vialidad:' in nomVial):
                                 print(nomVial[2]+"\n")
                                 fp.write(nomVial[2]+"\n")
                            else: 
                                print(nomVial)
                                fp.write(nomVial[0])
                       if number == 4:#numero interior
                            numInt=line.partition('NÃºmero Interior:')
                            print(numInt)
                            if ('NÃºmero Interior:' in numInt):
                                 print(numInt[2]+"\n")
                                 fp.write(numInt[2]+"\n")
                            else:
                                fp.write(numInt[0]+"\n")
                       if number == 5:#tipo de vialidad
                            tipVial=line.partition('Tipo de Vialidad:')
                            print(numInt)
                            if ('Tipo de Vialidad:' in tipVial):
                                 print(tipVial[2]+"\n")
                                 fp.write(tipVial[2]+"\n")
                            elif('Tipo de Vialidad:' not in tipVial):
                                print(tipVial[0]+"\n")
                                fp.write(tipVial[0]+"\n")
                       if number == 6:#numero exterior
                            numExt=line.partition('NÃºmero Exterior:')
                            print(numExt)
                            if ('NÃºmero Exterior:' in numExt):
                                 print(numExt[2]+"\n")
                                 fp.write(numExt[2]+"\n")
                            elif('NÃºmero Exterior:' not in numExt):
                                print(numExt[0]+"\n")
                                fp.write(numExt[0]+"\n")
                       if number == 7:#nombre de la colonia 
                            nomCol=line.partition('Nombre de la Colonia:')
                            print(nomCol)
                            if ('Nombre de la Colonia:' in nomCol):
                                 print(nomCol[2]+"\n")
                                 fp.write(nomCol[2]+"\n")
                            elif ('Nombre de la Colonia:' not in nomCol):
                                 print(nomCol[0]+"\n")
                                 fp.write(nomCol[0]+"\n")
                       if number == 8:#regimen 
                            numExt=line.partition('RÃ©gimen General de Ley Personas Morales')
                            print(numExt)
                            if ('RÃ©gimen General de Ley Personas Morales' in numExt):
                                 print(numExt[1]+"\n")
                                 fp.write(numExt[1]+"\n")
                            else:
                                reg=line.partition('Personas Morales con Fines no Lucrativos')
                                print(reg)
                                if ('Personas Morales con Fines no Lucrativos' in reg):
                                     print(reg[1]+"\n")
                                     fp.write(reg[1]+"\n")

                    


def query(nombreAr, directorio):
        archivoTxt= os.path.join(directorio+ "/" + nombreAr +".txt")
        l1 = []
        with open(archivoTxt, 'r') as fp:
            l1 = fp.readlines()
        with open(archivoTxt, 'w') as fp:
               print("insert in to AcProveedores values( "+ l1[0]+" ,"+l1[1]+" ,"+l1[2]+" ,"+l1[3]+l1[6]+l1[4]+" ,"+l1[5]+" ,"+l1[7]+" ,"+l1[8]+");")
               fp.write("insert into AcProveedores values( " + l1[0]+" ,"+l1[1]+" ,"+l1[2]+" ,"+l1[3]+l1[6]+l1[4]+" ,"+l1[5]+" ,"+l1[7]+" ,"+l1[8]+");") 


def inicio():#funcion en donde se introduce la ruta del archivo y el nombre del archivo 
        dir=input("introduzca el directorio donde se encuentran los archivos:")
        directorio=dir.replace("\\", "/")
        #print(directorio)
        nombreAr = input("introduzca el nombre del archivo:")
        archivo =  os.path.join(directorio + "/" + nombreAr +".pdf")
        conviertePDFaTXT(archivo,nombreAr, directorio)
        os.system("pause")
        borrar(nombreAr, directorio)
        numeroLineasNueve(nombreAr, directorio)
        campoListo(nombreAr, directorio)
        numeroLineasNueve(nombreAr, directorio)
        os.system("pause")
        query(nombreAr, directorio)

        

inicio()#inicio del programa