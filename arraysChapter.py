# Guia UDistrital, programacion basica (capitulo arreglos)

# import math
import random
import numpy as np
'''
Ejercicio 53
    Escribir un programa que llene un arreglo con los numeros enteros
    comprendidos entre 4 y 14

listSimple = []

for idx in range(11):
    listSimple.append(idx+4)
print(listSimple)
'''
'''
Ejercicio 54
    Escribir un programa que llene un arreglo con los numeros pares
    comprendidos entre 1 y 100
listSimple = []

for idx in range(100):
    if idx % 2 == 0:
        listSimple.append(idx+2)
print(listSimple)
'''
'''
Ejercicio 55
    Escribir un programa que llene un arreglo con los numeros comprendidos
    entre 0 y 100 divisibles por 3

listSimple = []

for idx in range(100):
    if idx % 3 == 0:
        listSimple.append(idx+3)
print(listSimple)
'''
'''
Ejercicio 56
    Escribir un programa que llene un arreglo con cinco numeros enteros
    consecutivos y haga una copia de este arreglo en otro

listToFill = []
copyList = []

enteroUsr = int(input("Ingrese un numero entero de su eleccion:\n"))
listToFill.insert(0, enteroUsr)

for idx in range(1, 5):
    listToFill.append(idx+enteroUsr)
copyList = listToFill.copy()

print(listToFill)
print(copyList)
'''
'''
Ejercicio 57
    Escribir un programa que llene un arreglo de 10 numeros enteros
    comprendidos entre 50 y 100 y copie en otro arreglo esos numeros
    multiplicados por 0.5

rdmArrayEnteros = []
pdtCopyArray = []
for item in range(10):
    rdmArrayEnteros.append(random.randrange(50, 100))

print(rdmArrayEnteros)

for item in range(len(rdmArrayEnteros)):
    rdmArrayEnteros[item] *= 0.5

pdtCopyArray = rdmArrayEnteros.copy()

print(pdtCopyArray)
'''
'''
Ejercicio 58
    Escribir un programa que llene un arreglo con los veinte primeros
    numeros pares y calcule su suma

veintenaList = []
sumaArray = 0

for itm in range(1, 41):
    if itm % 2 == 0:
        veintenaList.append(itm)

for itm in range(len(veintenaList)):
    sumaArray += veintenaList[itm]

print(veintenaList)
print(sumaArray)
'''
'''
Ejercicio 59
    Escribir un programa que solicite cinco (5) numeros, los almacene en un
    arreglo y luego calcule la media aritmetica de esos numeros

fiveArray = []
sumArray = 0

for idx in range(5):
    itm = int(input("Ingrese valor numerico, natural:\t"))
    fiveArray.append(itm)

for idx in range(len(fiveArray)):
    sumArray += fiveArray[idx]

mediaArray = sumArray / len(fiveArray)

print(fiveArray)
print(sumArray)
print(mediaArray)
'''
'''
Ejercicio 60
    Escribir un programa que tras asignar los numeros 23, 45, 68, 99,
    10, 15 y 4 en un arreglo, determine la posición del arreglo en la
    que se encuentra el maximo valor
# solucion adaptada de https:// tutotialesprogramacionya.com7
array_60 = []
for count in range(7):
    itm = int(input("Ingrese valor numerico:\t"))
    array_60.append(itm)
max_value = array_60[0]
position = 0
for idx in range(1, len(array_60)):
    if max_value < array_60[idx]:
        max_value = array_60[idx]
        position = idx
print(position)
'''
'''
Ejercicio 61
    Escribir un programa que tras asignar los numeros -2, 5, 8, -9, 10,
    15 y -4 a un arreglo, calcule independiente, la suma de los elementos
    positivos y negativos

array_61 = []
sumPositivos = 0
sumNegativos = 0

for idx in range(7):
    element = int(input("Ingrese valor entero: "))
    array_61.append(element)
for idx in range(len(array_61)):
    if array_61[idx] < 0:
        sumNegativos += array_61[idx]
    else:
        sumPositivos += array_61[idx]
print("La suma los elementos negativos es {}".format(sumNegativos))
print("La suma los elementos positivos es {}".format(sumPositivos))
'''
'''
Ejercicio 62
    Escribir un programa que tras asignar 10 numeros leidos desde teclado
    a un arreglo, determine las posiciones del arreglo en que se encuentran
    el maximo y el minimo valor

# Lista vacia
array_62 = []

# Inserción de los diez elementos deseados
for indice in range(10):
    elemntArr = int(input("Ingrese valor entero: "))
    array_62.append(elemntArr)

# Presumamos que una lista cuenta con apenas (1) elemento
positionMin = 0
positionMax = 0
min_value = array_62[0]
max_value = array_62[0]

for indice in range(1, len(array_62)):
    if array_62[indice] < min_value:
        min_value = array_62[indice]
        positionMin = indice
    elif array_62[indice] > max_value:
        max_value = array_62[indice]
        positionMax = indice

print("La posicion del max. valor es {}".format(positionMax))
print("La posicion del min. valor es {}".format(positionMin))
'''
'''
Ejercicio 63
    Escribir un programa que imprima la media de los elementos que se
    encuentran en las posiciones pares; como asi mismo, en las posiciones
    impares en un arreglo de 20 lugares

array_63 = []
sumaPar = 0
sumaImp = 0

for indice in range(20):
    array_63.append(random.randrange(-50, 50))

for indice in range(len(array_63)):
    if indice % 2 == 0:
        sumaPar += array_63[indice]
    else:
        sumaImp += array_63[indice]
mediaPar = sumaPar / 10
mediaImp = sumaImp / 10

print(array_63)
print("La media de las posiciones pares es {}".format(mediaPar))
print("La media de las posiciones impares es {}".format(mediaImp))
'''
'''
Ejercicio 64
    Escribir un programa que determine la posicion de la siguiente
    matriz en la que se encuentra el valor maximo

            | 32 | 56 | 50 |
            | 49 | 99 | 12 |
            | 78 | 57 | 89 |

array_64 = np.array([[32, 56, 50], [49, 99, 12], [78, 57, 89]])

maximo = array_64[0, 0]
listPos = [0, 0]
for filas in range(len(array_64)):
    for columnas in range(len(array_64)):
        if array_64[filas, columnas] > maximo:
            maximo = array_64[filas, columnas]
            listPos = [filas, columnas]

print("La posicion del mayor elemento es {}".format(listPos))
'''
'''
Ejercicio 65
    Escribir un programa que sume, en forma independiente, los elementos
    positivos y negativos de la siguiente matriz
                        | -2 | 56 | 50 |
                        | 44 | -12| -42|
                        | 70 | 57 | -86|

array_65 = np.array([[-2, 56, 50], [44, -12, -42], [70, 57, -86]])
sumaPos = 0
sumaNeg = 0

for rows in range(len(array_65)):
    for colums in range(len(array_65)):
        if array_65[rows][colums] < 0:
            sumaNeg += array_65[rows][colums]
        elif array_65[rows][colums] > 0:
            sumaPos += array_65[rows][colums]
        else:
            pass
print("La suma de los elementos negativos es {}".format(sumaNeg))
print("La suma de los elementos positivos es {}".format(sumaPos))
'''
'''
Ejercicio 66
    Escribir un programa que multilplique por (2) los elementos
    de la siguiente matriz
                        | 5 | 6 | 13|
                        | 14| 2 | 4 |
                        | 21| 7 | 6 |

array_66 = np.array([[5, 6, 13], [14, 2, 4], [21, 7, 6]])
print(array_66, "\n")

for rows in range(len(array_66)):
    for colums in range(len(array_66)):
        array_66[rows][colums] *= 2

print(array_66)
'''
'''
Ejercicio 67
    Escribir un programa que llene la primera fila de una matriz de 3
    filas por 10 columnas con numeros aleatorios entre 1 y 20, la segunda
    fila con los cuadrados de los datos de la primera fila y la tercera
    fila con la suma de la primera y la segunda

rdmList_67 = []
row = []
sum = []

for indice in range(10):
    rdmList_67.append(random.randrange(1, 20))

row = rdmList_67.copy()
sum = rdmList_67.copy()

for indice in range(10):
    row[indice] **= 2

for indice in range(10):
    sum[indice] += row[indice]

firstRow = np.array(rdmList_67)
secondRow = np.array(row)
thirdRow = np.array(sum)

psedoMatrix = np.concatenate((firstRow, secondRow, thirdRow))
matriz = psedoMatrix.reshape(3, 10)

print(matriz)
'''
'''
Ejercicio 68
    Escribir un programa que sume los datos de cada una de las filas
    de la siguiente matriz; el resultado se almacenara en la ultima
    posicion de cada fila
                        | 5 | 6 | 7 | 9 |   |
                        | 11| 8 | 2 |   |   |

firstList = [5, 6, 7, 9]
secondList = [11, 8, 2]
sumList_f = 0
sumList_s = 0

print(firstList)
print(secondList)

for fRow in range(3, 4):
    firstList.append("")

for sRow in range(2, 4):
    secondList.append("")

print(firstList)
print(secondList)

for fRow in range(len(firstList)):
    if isinstance(firstList[fRow], int):
        sumList_f += firstList[fRow]
    elif isinstance(firstList[fRow], str):
        firstList.pop(fRow)
        firstList.insert(fRow, sumList_f)
        sumList_f += firstList[fRow]

for sRow in range(len(secondList)):
    if isinstance(secondList[sRow], int):
        sumList_s += secondList[sRow]
    elif isinstance(secondList[sRow], str):
        secondList.pop(sRow)
        secondList.insert(sRow, sumList_s)
        sumList_s += secondList[sRow]

fRow_Matx = np.array(firstList)
sRow_Matx = np.array(secondList)

draftMatx = np.concatenate((fRow_Matx, sRow_Matx))
matx_68 = draftMatx.reshape(2, 5)

print(matx_68)
'''

'''
Ejercicio 69
    Escribir un programa que sume los datos de cada una de las columnas
    de la siguiente matriz; el resultado se almacenará en la última
    posición de cada columna
                         ___________
                        | 5 | 6 | 13|
                        | 14| 2 | 4 |
                        | 21| 7 | 6 |
                        |_12|_9_|_5_|


matrix_69 = np.array([[5, 6, 13], [14, 2, 4], [21, 7, 6], [12, 9, 5]])
sumList = []
posZero = 0
posOne = 0
posTwo = 0


for iRow in range(len(matrix_69)):
    posZero += matrix_69[iRow, 0]
    posOne += matrix_69[iRow, 1]
    posTwo += matrix_69[iRow, 2]

sumList.insert(0, posZero)
sumList.append(posOne)
sumList.append(posTwo)

draftMtx_69 = matrix_69.reshape(-1)

draftMtx_69 = np.concatenate((draftMtx_69, sumList))
matrix_69 = draftMtx_69.reshape(5, 3)
print(matrix_69)
'''
'''
Ejercicio 70
Escribir un programa que sume los elementos de cada una de las filas y de
las columnas de la siguiente matriz; el resultado de cada suma se
almacenara en la ultima posición de de fila o columna correspondiente.
Ademas la suma total de todos los elementos de la matrizse almacenará
en el elemento de la esquina inferior derecha de la matriz

                        | 2 | 9 | 11|   |
                        | 1 | 12| 4 |   |
                        | 21| 17| 8 |   |
                        | 2 | 39| 5 |   |
                        |   |   |   |   |
'''
draftMtx_70 = np.array([[2, 9, 11], [1, 12, 4], [21, 17, 8], [2, 39, 5]])
'''
sumsRow = []
sumsColumn = []
sumRowZero = 0
sumRowOne = 0
sumRowTwo = 0
sumRowthree = 0
sumColumnZero = 0
sumColumnOne = 0
sumColumnTwo = 0
sumColumnThree = 0
allSumItems = 0

for iRow in range(len(matrix_70)):
    sumRowZero += matrix_70[iRow, 0]
    sumRowOne += matrix_70[iRow, 1]
    sumRowTwo += matrix_70[iRow, 2]

for jColumn in range(len(matrix_70[iRow])):
    sumColumnZero += matrix_70[0, jColumn]
    sumColumnOne += matrix_70[1, jColumn]
    sumColumnTwo += matrix_70[2, jColumn]
    sumColumnThree += matrix_70[3, jColumn]


for iRow in range(len(matrix_70)):
    for jColumn in range(len(matrix_70[iRow])):
        allSumItems += matrix_70[iRow, jColumn]

sumsRow.insert(0, sumRowZero)
sumsRow.append(sumRowOne)
sumsRow.append(sumRowTwo)
sumsRow.append(allSumItems)

sumsColumn.insert(0, sumColumnZero)
sumsColumn.append(sumColumnOne)
sumsColumn.append(sumColumnTwo)
sumsColumn.append(sumColumnThree)

print(sumsColumn)
print(sumsRow)
'''
print(draftMtx_70)

'''
En este punto de desarrollo, se hace un alto en el camino y se comprende que
los enunciados - problema necesitan implementarse de otra manera
'''
