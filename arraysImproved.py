import numpy as np
import random as rdm
'''
Ejercicio 64
    Escribir un programa que determine la posicion de la siguiente matriz
    en la que se encuentra el valor maximo

FILAS_TAM = 3
COLUMNAS_TAM = 3
array_64 = []
maxPos = [0, 0]

for iRow in range(FILAS_TAM):
    array_64.append([])
    for jColumn in range(COLUMNAS_TAM):
        item = int(input("Ingrese valor entero:\n"))
        array_64[iRow].append(item)
    print("\n")

maxItem = array_64[0][0]

for iRow in range(len(array_64)):
    for jColumn in range(len(array_64[iRow])):
        if array_64[iRow][jColumn] > maxItem:
            maxItem = array_64[iRow][jColumn]
            maxPos = [iRow, jColumn]

matrix_64 = np.asmatrix(array_64)
for iRow in matrix_64:
    for jColumn in iRow:
        print(jColumn)

print("La posicion del mayor elemento es {}".format(maxPos))
'''
'''
Ejercicio 65
    Escribir un programa que sume, en forma independiente, los elementos
    positivos y negativos de la siguiente matriz
                        | -2| 56| 50|
                        | 44|-12|-42|
                        | 70| 57|-86|

FILAS_TAM = 3
COLUMNAS_TAM = 3
array_65 = []
sumaPos = 0
sumaNeg = 0

for iRow in range(FILAS_TAM):
    array_65.append([])
    for jColumn in range(COLUMNAS_TAM):
        item = int(input("Ingrese valor entero:\n"))
        array_65[iRow].append(item)
    print("\n")

for iRow in range(len(array_65)):
    for jColumn in range(len(array_65[iRow])):
        if array_65[iRow][jColumn] < 0:
            sumaNeg += array_65[iRow][jColumn]
        elif array_65[iRow][jColumn] > 0:
            sumaPos += array_65[iRow][jColumn]
        else:
            pass

matrix_65 = np.asmatrix(array_65)
for iRow in matrix_65:
    for jColumn in iRow:
        print(jColumn)

print("La suma de los valores negativos es {}".format(sumaNeg))
print("La suma de los valores positivos es {}".format(sumaPos))
'''
'''
Ejercicio 66
    Escribir un programa que multiplique por dos (2) los elementos de la
    siguiente matriz
                    | 5 | 6 | 13|
                    | 14| 2 | 4 |
                    | 21| 7 | 6 |
FILAS_TAM = 3
COLUMNAS_TAM = 3
array_66 = []

for iRow in range(FILAS_TAM):
    array_66.append([])
    for jColumn in range(COLUMNAS_TAM):
        item = int(input("Ingrese valor entero:\n"))
        array_66[iRow].append(item)
    print("\n")

for iRow in range(len(array_66)):
    for jColumn in range(len(array_66[iRow])):
        array_66[iRow][jColumn] *= 2

matrix_66 = np.asmatrix(array_66)
for iRow in matrix_66:
    for jColumn in iRow:
        print(jColumn)
'''
'''
Ejercicio 67
    Escribir un programa que llene la primera fila de una matriz de 3
    filas por 10 columnas con numeros aleatorios entre 1 y 20, la segunda
    fila con los cuadrados de los datos de la primera fila; y la tecera
    fila con la suma de la primera y la segunda

FILAS_TAM = 3
COLUMNAS_TAM = 10
array_67 = []

for iRow in range(FILAS_TAM):
    array_67.append([])
    for jColumn in range(COLUMNAS_TAM):
        if iRow == 0:
            randomNum = rdm.randrange(1, 20)
            array_67[iRow].append(randomNum)
        elif iRow >= 1:
            array_67[iRow].append(0)

for iRow in range(len(array_67)):
    for jColumn in range(len(array_67[iRow])):
        if iRow == 1:
            copyItem = array_67[0][jColumn]
            array_67[iRow].pop(jColumn)
            array_67[iRow].insert(jColumn, copyItem)
            array_67[iRow][jColumn] **= 2
        if iRow == 2:
            zeroRow = array_67[0][jColumn]
            oneRow = array_67[1][jColumn]
            array_67[iRow][jColumn] = zeroRow + oneRow

matrix_67 = np.asmatrix(array_67)
for iRow in matrix_67:
    for jColumn in iRow:
        print(jColumn)
'''
'''
Ejercicio 68
    Escribir un programa que sume los datos de cada una de las filas
    de la siguiente matriz, el resultado se almacenará en la ultima
    posicion de cada fila
                            | 5 | 6 | 7 | 9 |  |
                            |11 | 8 | 2 |   |  |

FILAS_TAM = 2
COLUMNAS_TAM = 5
array_68 = []
elmntSum = 0

for iRow in range(FILAS_TAM):
    array_68.append([])
    for jColumn in range(COLUMNAS_TAM):
        if iRow == 0 and jColumn <= 3:
            element = int(input("Ingrese valor entero:\n"))
            array_68[iRow].append(element)
        elif iRow == 1 and jColumn <= 2:
            element = int(input("Ingrese valor entero:\n"))
            array_68[iRow].append(element)
        else:
            array_68[iRow].append(0)
    print("\n")

for iRow in range(len(array_68)):
    for jColumn in range(len(array_68[iRow])):
        if array_68[iRow][jColumn] > 0:
            elmntSum += array_68[iRow][jColumn]
        else:
            array_68[iRow].pop(jColumn)
            array_68[iRow].insert(jColumn, elmntSum)
            elmntSum += array_68[iRow][jColumn]
    elmntSum = 0

matrix_68 = np.asmatrix(array_68)
for iRow in matrix_68:
    for jColumn in iRow:
        print(jColumn)
'''
'''
Ejercicio 69
    Una solucion que sume los datos de cada una de las columnas de la
    siguiente matriz; el resultado se almacenara en la ultima posición
    de cada columna:
                    ____________
                    | 5 | 6 |13 |
                    |14 | 2 | 4 |
                    |21 | 7 | 6 |
                    |12 | 9 | 5 |
                    |___|___|___|

FILAS_TAM = 5
COLUMNAS_TAM = 3
array_69 = []
acumSuma = 0

for iRow in range(FILAS_TAM):
    array_69.append([])
    for jColumn in range(COLUMNAS_TAM):
        if iRow <= 3:
            element = int(input("Ingrese entero positivo, segun enunciado: "))
            array_69[iRow].append(element)
        else:
            array_69[iRow].append(0)
    print("\n")

for iRow in range(len(array_69[iRow])):
    for jColumn in range(len(array_69)):
        if array_69[jColumn][iRow] > 0:
            acumSuma += array_69[jColumn][iRow]
        elif array_69[jColumn][iRow] == 0:
            array_69[jColumn][iRow] = acumSuma
    acumSuma = 0

matrix_69 = np.asmatrix(array_69)

for iRow in matrix_69:
    for jColumn in iRow:
        print(jColumn)
'''
'''
Ejercicio 70
    Una solución que sume los resultados de cada una de las filas y de las
    columnas de la siguiente matriz; el resultado de cada suma se almacenara
    en la ultima posicion de la fila o columna correspondiente. Ademas suma
    total de todos los elementos de la matriz se almacenara en el elemento de
    la esquina inferior derecha de la matriz:
                        | 2 | 9 |11 |   |
                        | 1 |12 | 4 |   |
                        |21 |17 | 8 |   |
                        | 2 |39 | 5 |   |
                        |   |   |   |   |

FILAS_TAM = 5
COLUMNAS_TAM = 4
array_70 = []
acumSuma = 0
initialSum = 0

for iRow in range(FILAS_TAM):
    array_70.append([])
    for jColumn in range(COLUMNAS_TAM):
        if iRow <= 3 and jColumn <= 2:
            item = int(input("Ingrese entero positivo, segun enunciado: "))
            array_70[iRow].append(item)
        else:
            array_70[iRow].append(0)
    print("\n")

for iRow in range(len(array_70) - 1):
    for jColumn in range(len(array_70[iRow])):
        if array_70[iRow][jColumn] > 0:
            acumSuma += array_70[iRow][jColumn]
        elif array_70[iRow][jColumn] == 0:
            array_70[iRow][jColumn] = acumSuma
    acumSuma = 0

for iRow in range(len(array_70[iRow]) - 1):
    for jColumn in range(len(array_70)):
        if array_70[jColumn][iRow] > 0:
            acumSuma += array_70[jColumn][iRow]
        elif array_70[jColumn][iRow] == 0:
            array_70[jColumn][iRow] = acumSuma
    acumSuma = 0

for iRow in range(len(array_70) - 1):
    for jColumn in range(len(array_70[iRow]) - 1):
        initialSum += array_70[iRow][jColumn]

for iRow in range(len(array_70) - 1, len(array_70) - 2, -1):
    for jColumn in range(len(array_70[iRow]) - 1, len(array_70[iRow]) - 2, -1):
        array_70[iRow][jColumn] = initialSum

matrix_70 = np.asmatrix(array_70)

for iRow in matrix_70:
    for jColumn in iRow:
        print(jColumn)
'''
'''
Ejercicio 71
    Escribir un programa que divida todos los elementos de una matriz
    M(3, 4) por elemento situado en la posición 2, 2

FILAS_TAM = 3
COLUMNAS_TAM = 4
array_71 = []

for iRow in range(FILAS_TAM):
    array_71.append([])
    for jColmn in range(COLUMNAS_TAM):
        item = int(input("Ingrese valor entero: "))
        array_71[iRow].append(item)
    print("\n")

matrix_71 = np.asmatrix(array_71)
for iRow in matrix_71:
    for jColmn in iRow:
        print(jColmn)
print("\n")

escalar = array_71[2][2]

try:
    for iRow in range(len(array_71)):
        for jColmn in range(len(array_71[iRow])):
            array_71[iRow][jColmn] /= float(escalar)
            array_71[iRow][jColmn] = format(array_71[iRow][jColmn], '.2f')
except ZeroDivisionError:
    print("El elemento divisor es cero! No es posible realizar la operacion")

matrix_71 = np.asmatrix(array_71)
for iRow in matrix_71:
    for jColmn in iRow:
        print(jColmn)
'''
'''
Ejercicio 72
    Escribir un programa que almacene en un arreglo los numeros primos
    comprendidos entre 1 y 100

array_71 = []
cont = 2
esPrimo = 1

for item in range(2, 16):
    array_71.append(item)

for item in range(len(array_71)):
    while cont**2 <= array_71[item] and esPrimo:
        if array_71[item] % cont == 0:
            esPrimo = 0
    cont += 1

    if bool(esPrimo) is False:
        array_71.pop(item)
    else:
        pass

print(array_71)
'''
'''
Ejercicio 73
    Escribir un programa que genera la matriz traspuesta de una matriz
    M(3, 4). La matriz traspuesta de M(f, c) se obtiene intercambiando
    filas por columnas y viceversa; el resultado se tiene que almacenar
    en una nueva matriz M_TRANS(c, f)
'''
FILAS_TAM = 3
COLUMNAS_TAM = 4
array_73 = []

for iRow in range(FILAS_TAM):
    array_73.append([])
    for jColmn in range(COLUMNAS_TAM):
        item = int(input("Ingrese valor entero: "))
        array_73[iRow].append(item)
    print("\n")

matrix_73 = np.asmatrix(array_73)
for iRow in matrix_73:
    for jColmn in iRow:
        print(jColmn)
print("\n")

'''
Ejercicio 75
    Escribir un programa que sume dos matrices bidimensionales. La matrices
    para que puedan sumarse deben tener las mismas dimensiones
'''
'''
Ejercicio 85
    Escribir un programa que sume los valores que hay por encima de la
    diagonal principal de una matriz M(4, 4). Los valores se deben asignar
    aleatoriamente
'''
