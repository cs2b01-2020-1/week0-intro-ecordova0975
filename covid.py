from io import *

lista_archivos = ["AY274119.txt","AY278488.2.txt","MN908947.txt","MN988668.txt","MN988669.txt"]

def seleccionar_menor(arch1,arch2):
    if len(arch1) == len(arch2):
        if len(arch1[len(arch1)-1]) <  len(arch2[len(arch2)-1]):
            min_arch = arch1
        else:
            min_arch = arch2
    elif len(arch1) < len(arch2):
        min_arch = arch1
    else:
        min_arch = arch2
    return min_arch

def get_similarity(_arch1,_arch2):
    similarity = 0
    total = 0
    pivot = seleccionar_menor(_arch1,_arch2)
    for i in range(0,len(pivot)):
        for j in range(0,len(pivot[len(pivot)-1])):
            if _arch1[i][j] == _arch2[i][j]:
                similarity+=1
        total +=1
    similarity = 100*(similarity/total)
    return round(similarity,2)

print()
print("\t\tAnalizando los genomas:")
print()
for i in range(0,10):
    if i < 4:
        archivo1 = open(lista_archivos[0],"r")
        archivo2 = open(lista_archivos[i+1],"r")
        print("Comparando..."+str(lista_archivos[0])+"(1) y "+str(lista_archivos[i+1])+"("+str(i+2)+")")
    elif i >=4 and i < 7:
        archivo1 = open(lista_archivos[1], "r")
        archivo2 = open(lista_archivos[i-2], "r")
        print("Comparando..." +str(lista_archivos[1])+"(2) y "+str(lista_archivos[i-2])+"("+str(i-1)+")")
    elif i==7 or i==8:
        archivo1 = open(lista_archivos[2],"r")
        archivo2 = open(lista_archivos[i-4],"r")
        print("Comparando..." + str(lista_archivos[2]) + "(3) y " + str(lista_archivos[i - 4]) + "(" + str(i - 3) + ")")
    elif i == 9:
        archivo1 = open(lista_archivos[3], "r")
        archivo2 = open(lista_archivos[4], "r")
        print("Comparando..." + str(lista_archivos[3]) + "(4) y " + str(lista_archivos[4]) + "(5)")
    a1 = archivo1.read()
    a2 = archivo2.read()
    print("\t"+str(get_similarity(a1,a2))+"%")
    archivo1.close()
    archivo2.close()







