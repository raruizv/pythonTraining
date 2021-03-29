# Programacion estructurada, guia ejercicios UDistrital
import math
# from dataclasses import dataclass
'''
Ejercicio 1
    Escribir un programa que muestre en pantalla un saludo

print("Hola camaradas!")
'''
'''
Ejercicio 2
    Escribir un programa que sume dos valores: a=7, b=4

print("Tenemos a = 7 y b = 4")
a = 7
b = 4
print("La suma de a y b es {}".format(a+b))
'''
'''
Ejercicio 3
    Escribir un programa que lea dos valores y los sume

print("Operacion suma, dos operandos. Favor aguarde...")
sumando_1 = int(input("Ingrese entero positivo. Sera primer termino\n"))
sumando_2 = int(input("Ingrese entero positivo. Sera segundo termino\n"))
print("La suma de los terminos ingresados es: {}".format(sumando_1+sumando_2))
'''
'''
Ejercicio 4
    Escribir un programa que sume, reste, multiplique y divida dos valores:
    x=10, y=2

print("Tenemos x = 10 y y = 2")
x = 10
y = 2
print("La suma de x y 'y' es {}".format(x+y))
print("La resta de x y 'y' es {}".format(x-y))
print("La multiplicacion de x y 'y' es {}".format(x*y))
print("La division de x y 'y' es {}".format(x/y))
'''
'''
Ejercicio 5
    Escribir un programa que sume, reste, multiplique y divida dos numeros
    leidos desde teclado

print("Operaciones matematicas. Favor aguarde...")
termOne=int(input("Ingrese entero positivo:\n"))
termTwo=int(input("Ingrese entero positivo. Segundo termino:\n"))
print("La suma de {} y {} es {}".format(termOne, termTwo, termOne+termTwo))
print("La resta de {} y {} es {}".format(termOne, termTwo, termOne-termTwo))
print("El producto de {} y {} es {}".format(termOne, termTwo, termOne*termTwo))
print("El cociente de {} y {} es {}".format(termOne, termTwo, termOne/termTwo))
'''
'''
Ejercicio 6
    Escribir un programa que calcule el area de un rectangulo de lado1=3 y
    lado2=4. Area del rectangulo=lado1*lado2

print("Lados del rectangulo, (lado 1 = 3, lado 2 = 4)")
ladoUno=3
ladoDos=4
print("El area del rectangulo es {}".format(ladoUno*ladoDos))
'''
'''
Ejercicio 7
    Modificar el ejercicio anterior en los cuales lo valores de lo lados sean
    suministrados por el usuario

print("Area del rectangulo. Favor aguarde...")
ladoUno=float(input("Ingrese uno de los lados del rectangulo:\n"))
ladoDos=float(input("Ingrese el lado restante:\n"))
print("El area del rectangulo es {}".format(ladoUno*ladoDos))
'''
'''
Ejercicio 8
    Escribir un programa que calcule el area de un triangulo, capta los valores
    de base y altura por consola. Area del triangulo=(base*altura)/2

print("Area del triangulo. Favor aguarde...")
base = float(input("Ingrese base de la figura:\n"))
altura = float(input("Ingrese altura de la figura\n"))
areaTrigl = print("El area del triangulo es: {}".format(base*altura))
'''

'''
Ejercicio 9
    Escribir un programa que calcule la longitud y el area de una
    circunferencia, capturando el valor del radio. Longitud de la
    circunferencia = 2*PI*radio, Area de la circunferencia = PI*radio^2

# import math

print("Circunferencia. Favor aguarde...")
radioCircle = float(input("Ingres radio de la circunferencia:\n"))
longitud = 2*radioCircle*math.pi
areaCircle = math.pi*radioCircle**2

print("La longitud de de la circunfrencia es: {}".format(longitud))
print("El area de la circunferencia es: {}".format(areaCircle))
'''

'''
Ejercicio 10
    Escribir un programa que calcule la longitud de un proyectil que
    recorre 'x'(Km) en 't' (minutos). Expresar el resultado en
    metros/segundo.
'''

'''
Ejercicio 11
    Escribir un programa que calcule el volumen de una esfera de radio = r
    Volumen esfera = 4/3 * PI * radio^3

print("Esfera. Favor aguarde...")
radioEsf = float(input("Ingrese radio de la esfera:\n"))
volumenEsf = 4/3 * math.pi * radioEsf**3

print("El volumen de la esfera es: {}".format(volumenEsf))
'''

'''
Ejercicio 12
    Escribir un programa que evalue la siguiente expresión
    (a+7*c)/(b+2-a)+2*b

print("Expresiones algebraicas (1).Favor aguarde...")
a = int(input("Ingrese valor entero. Este es 'a':\n"))
b = int(input("Ingrese valor entero. Este es 'b':\n"))
c = int(input("Ingrese valor entero. Este es 'c':\n"))
algebraPhr = (a+7*c)/(b+2-a)+2*b

print("Los valores: a = {}, b = {}, c = {}".format(a, b, c))
print("(a+7*c)/(b+2-a)+2*b = {}".format(algebraPhr))

'''
'''
Ejercicio 13
    Escribir un programa que evalue la siguiente expresion
    (a+5)*3/2*b-b

print("Expresiones algebraicas (2).Favor aguarde...")
a = int(input("Ingrese valor entero. Este es 'a':\n"))
b = int(input("Ingrese valor entero. Este es 'b':\n"))
algebraPhr = (a+5)*3/2*b-b

print("Los valores: a = {}, b = {}".format(a, b))
print("(a+5)*3/2*b-b es: {}".format(algebraPhr))
'''
'''
Ejercicio 14
    Escribir un programa que evalue la siguiente expresion
    (-b+raiz cuadrada(b^2-4*a*c))/(2*a)
'''
'''
Ejercicio 15
    Escribir un programa que calcule las raices de una ecuación de
    segundo grado
    (-b+raiz cuadrada(b^2-4*a*c))/(2*a)
    (-b-raiz cuadrada(b^2-4*a*c))/(2*a)
'''
'''
Ejercicio 16
    Escribir un programa que calcule la hipotenusa de un rectangulo

print("Triangulo rectangulo. Favor aguarde..")
catetoUno = float(input("Ingrese valor para un primer cateto:\n"))
catetoDos = float(input("Ingrese valor para un segundo cateto:\n"))

hipotenusa = math.sqrt(catetoUno**2+catetoDos**2)

print("El valor de la hipotenusa es de: {}".format(hipotenusa))
'''

'''
Ejercicio 17
    Escribir un programa que calcula el equivalente en grado Fahrenheit
    o Celsius de un temperatura 't'. Celsius/5 = (Fahrenheit - 32)/9

print("Conversion de unidades físicas, temperatura.Favor aguarde...")
tempFahrenheit = float(input("Ingrese temperatura en Fahrenheit\n"))
tempCelsius = float((tempFahrenheit - 32)*5)/9

print("La temperatura en Fahrenheit {}".format(tempFahrenheit))
print("es equivalente en Celsius a {}".format(tempCelsius))
'''

'''
Ejercicio 18
    Escribir un programa que calcule el numero de horas, minutos, y
    segundos que hay en 3700
print("Conversion de 3700 segundos a hh:min:seg. Favor aguarde")
tiempo = 3700
tiempoHrs = int(tiempo / 3600)
restoHrs = int(tiempo % 3600)
tiempoMin = int(restoHrs / 60)
tiempoSeg = int(restoHrs % 60)

print("3700 segundos es equivalente a {} hora(s), ".format(tiempoHrs))
print("{} minuto(s), {} segundo(s)".format(tiempoMin, tiempoSeg))
'''
'''
Ejercicio 19
    Escribir un programa que calcule el interes producido por un capital
    de 'x'(pesos), al cabo de un año depositado a una tasa 'y'% mensual

print("Rendimiento financiero, tasa mensual durante un (1) año")
print("Favor aguarde...")
capital = float(input("Ingrese capital inicial en pesos($):\n"))
tasaMes = float(input("Ingrese tasa mensual como porcentaje (%):\n"))

interes = capital * tasaMes/100
print("El rendimiento en un año del capital inicial COP$ {}".format(capital))
print("con una tasa mensual de {} %".format(tasaMes))
print("COP$ {}".format(interes))
'''

'''
Ejercicio 20
    Escribir un programa que calcule el equivalente en pies de una
    longitud 'x' en metros sabiendo que un metro es igual a 39.37
    pulgadas y 12 pulgadas a 1 pie

print("Conversion metros a pies. Favor aguarde..")
longitudUsr = float(input("Ingrese longitud en metros:\n"))
conversionPulg = longitudUsr*39.37
conversionPie = conversionPulg/12

print("La longitud 'x' en (mt) es quivalente a {} pies".format(conversionPie))
'''
'''
Ejercicio 21
    Escribir un programa que calcule el area de un rectangulo a partir de sus
    coordenadas (x1, y1) (x2, y2)

# Al manipular coordenadas con enteros se obtienen tambien valores negativos
# Se requiere implementar la funcion valor absoluto para calcular el area
distancia_x = 0
distancia_y = 0
abscisa_1 = int(input("Ingrese coordenada x1:\n"))
ordenada_1 = int(input("Ingrese coordenada y1:\n"))
abscisa_2 = int(input("Ingrese coordenada x2:\n"))
ordenada_2 = int(input("Ingrese coordenada y2:\n"))

if abscisa_1 == abscisa_2 or ordenada_1 == ordenada_2:
    print("Es inconsistente elaborar un rectagulo con estas coordenadas")
else:
    distancia_x = abscisa_2 - abscisa_1
    distancia_y = ordenada_2 - ordenada_1

areaRectgl = math.fabs(distancia_x * distancia_y)
print("El area del rectangulo es {}".format(areaRectgl))
'''
'''
Ejercicio 22
    Escribir un programa que lea dos numeros enteros A y B, y obtenga los
    valores de la divison entera de A dividido en b y el residuo de esta

print("Terminos de la division. Favor aguarde")
a = int(input("Ingrese valor entero. Es dividendo 'a':\n"))
b = int(input("Ingrese valor entero. Es divisor 'b':\n"))
cociente = int(a/b)
resto = a % b

print("El cociente de la division entre {} y {}".format(a, b))
print("es {} y el residuo es {}".format(cociente, resto))
'''
'''
Ejercicio 23
    Escribir un programa que convierta un numero de segundos en su
    equivalente en minutos y segundos

print("Conversion de 't' segundos a min:seg. Favor aguarde")
tiempo = int(input("Ingrese numero de segundos de su eleccion:\n"))
tiempoMin = int(tiempo / 60)
tiempoSeg = int(tiempo % 60)

print("{} segundos es equivalente a".format(tiempo))
print("{} minuto(s), {} segundo(s)".format(tiempoMin, tiempoSeg))
'''
'''
Ejercicio 24
    Escribir un programa que determine si un numero introducido por
    consola es positivo o negativo

print("Numeros enteros. Favor aguarde...")
integerUsr = int(input("Ingrese valor entero:\n"))
if integerUsr < 0:
    print("El entero es negativo")
else:
    print("El entero es positivo")
'''
'''
Ejercicio 25
    escribir un programa que determine si se han ingresado en orden
    creciente tres numeros por el usuario
print("Orden creciente de enteros. Favor aguarde...")
intUsr_a = input("Ingrese entero de su eleccion:\n")
intUsr_b = input("Ingrese entero de su eleccion:\n")
intUsr_c = input("Ingrese entero de su eleccion:\n")

if intUsr_a < intUsr_b and intUsr_a < intUsr_c:
    if intUsr_b < intUsr_c:
        print("Los numeros fueron ingresados en orden creciente")
    else:
        print("Los numeros fueron ingresados en orden arbitrario")
else:
    print("Los numeros fueron ingresados en orden arbitrario")
'''
'''
Ejercicio 26
    escribir un programa que determine si por consola un numero
    ingresado es par o impar

print("Par o impar?. Favor aguarde...")
ingresoUsr = int(input("Ingrese entero positivo:\n"))
if ingresoUsr % 2 == 0:
    print("El numero es par!")
else:
    print("El numero es impar!")
'''
'''
Ejercicio 27
    escribir un programa que determine si por consola un numero
    es mayor o menor a 100

print("Mayor o menor a 100. Favor aguarde...")
ingresoUsr = int(input("Ingrese numero real:\n"))
if ingresoUsr < 100:
    print("El valor ingresado es menor a 100")
else:
    print("El valor ingresado es mayor a 100")
'''
'''
Ejercicio 28
    escribir un program que dado un numero del 1 al 7 escriba el
    correspondiente dia de la semana

print("Escriba un numero del 1 al 7, cualquiera de ellos")
ingresoUsr = int(input("corresponde a un dia de la semana\n"))

if ingresoUsr == 1:
    print("El dia es lunes")
elif ingresoUsr == 2:
    print("El dia es martes")
elif ingresoUsr == 3:
    print("El dia es miercoles")
elif ingresoUsr == 4:
    print("El dia es jueves")
elif ingresoUsr == 5:
    print("El dia es viernes")
elif ingresoUsr == 6:
    print("El dia es sabado")
elif ingresoUsr == 7:
    print("El dia es domingo")
else:
    print("Valor fuera de rango para la rutina")
'''
'''
Ejercicio 29
    escribir un programa que lea un caracter e indique si es o
    no vocal

print("Es vocal o consonante?. Favor aguarde...")
charUsr = str(input("Ingrese caracter del alfabeto:\n"))

if charUsr == 'a' or charUsr == 'e':
    print("{} es vocal".format(charUsr))
elif (charUsr == 'i' or charUsr == 'o') or charUsr == 'u':
    print("{} es vocal".format(charUsr))
else:
    print("{} es consonante".format(charUsr))
'''
'''
Ejercicio 30
    escribir un programa que por consola dos numeros ingresados,
    en tanto el primero es mayor al segundo los intercambie

enteroUsr_frst = int(input("Ingrese numero entero. Es variable 'a':\n"))
enteroUsr_scnd = int(input("Ingrese numero entero. Es variable 'b':\n"))

if enteroUsr_frst > enteroUsr_scnd:
    aux_oper = enteroUsr_frst
    enteroUsr_frst = enteroUsr_scnd
    enteroUsr_scnd = aux_oper
    print("Ahora 'a' es {} y b es {}".format(enteroUsr_frst, enteroUsr_scnd))
else:
    print("No hay motivo para intercambiar")
'''

'''
Ejercicio 31
    escribir un programa que dado un importe bruto de una factura por consola,
    determine el importe neto segun los siguientes criterios.
    Importe bruto menor de 20.000 -> sin descuento
    Importe bruto mayor de 20.000 -> 15% de descuento

print("Facturación con descuentos. Favor aguarde...")
importeUsr = float(input("Ingrese importe bruto por verificar descuentos:\n"))
if importeUsr > 20000:
    print("El importe bruto es de $ {}".format(importeUsr))
    importeUsr -= importeUsr*0.15
    print("El importe neto es de $ {}".format(importeUsr))
else:
    print("No aplica para descuento")
    print("El importe neto es de $ {}".format(importeUsr))
'''
'''
Ejercicio 32
    Escribir un programa que por consola una hora ingresada en formato
    (hh:min:segundos) indique cual sera el tiempo dentro de un segundo

print("Ingrese un tiempo en formato (hh:mm:ss)")
horaUsr = int(input("Ingrese hora(entre 0 y 23):\n"))
minUsr = int(input("Ingrese minutos(entre 0 y 59):\n"))
secUsr = int(input("Ingrese segundos(entre 0 y 59):\n"))

if secUsr < 59 and minUsr < 59:
    secUsr += 1
elif secUsr == 59 and minUsr < 59:
    secUsr = 0
    minUsr += 1
elif (secUsr == 59 and minUsr == 59) and horaUsr < 23:
    secUsr = 0
    minUsr = 0
    horaUsr += 1
elif (secUsr == 59 and minUsr == 59) and horaUsr == 23:
    secUsr = 0
    minUsr = 0
    horaUsr = 0
else:
    print("Formato equivocado de ingreso")

print("La hora es {}:{}:{}".format(horaUsr, minUsr, secUsr))
'''
'''
Ejercicio 33
    Escribir un programa que realice un bucle con while y muestre en
    pantalla los naturales del 1 al 10

print("El listado de los primeros 10 naturales con 'while':\n")
natural = 1
while natural < 11:
    print(natural)
    natural += 1
'''
'''
Ejercicio 34
    Escribir un programa que realice un bucle con do while y muestre
    en pantalla los naturales del 1 al 10
'''
# Estructura de repeticion do while no esta en python, ver solución
# en java

'''
Ejercicio 35
    Escribir un programa que realice un bucle con for y muestre en
    pantalla los naturales del 1 al 10

print("El listado de los primeros 10 naturales con 'for':\n")
for natural in range(1, 11):
    print(natural)
'''
'''
Ejercicio 36
    Escribir un programa que visualice en pantalla los numeros pares
    entre 1 y 25

print("El listado de los numeros pares hasta 25:\n")
for natural in range(2, 26, 2):
    print(natural)
'''
'''
Ejercicio 37
    Escribir un programa que visualice en pantalla los numeros multiplos
    de 5 comprendidos entre 1 y 100

print("Multiplos de 5 hasta 100")
for natural in range(5, 101, 5):
    print(natural)
'''
'''
Ejercicio 38
    Escribir un programa que sume los numeros compredidos entre 1 y 10

natural = 1
sumaNat = 0
while natural < 11:
    sumaNat += natural
print("La suma de los primeros 10 naturales es:")
print(sumaNat)
'''
'''
Ejercicio 39
    Escribir un programa que genere la tabla de multiplicar de un numero
    ingresado por consola

print("Tablas de multiplicar. Favor aguarde...")
naturalUsr = int(input("Ingrese factor:\n"))
cuenta = 1
print("Tabla de {}".format(naturalUsr))
while cuenta < 11:
    productoTabla = naturalUsr * cuenta
    print("{} x {} = {}".format(naturalUsr, cuenta, productoTabla))
    cuenta += 1
'''
'''
Ejercicio 40
    Escribir un programa que realice la pregunta ¿Desea continuar S/N? y no
    deje de hacerla hasta que el usuario teclee N

print("¿Desea continuar S/N?")
choiceUsr = str(input())
while choiceUsr != 'n':
    print("¿Desea continuar S/N?")
    choiceUsr = str(input())
'''
'''
Ejercicio 41
    Escribir un programa que calcule cuantos años tarda en duplicarse un
    capital depositado al 5 % de interes anual

timeMonth = 1
interestRate = 1/240
capital = 0
interest = 0
timeYear = 0

print("Ingrese capital inicial en COP$:\n")
capital = float(input())
throwput = capital*2

while capital <= throwput:
    interest = capital * interestRate * timeMonth
    print("El capital es: COP$ {}".format(capital))
    print("Va mes {} de inversion".format(timeMonth))
    timeMonth += 1
    capital += interest
timeYear = timeMonth / 12

print("El tiempo requerido para doblar la inversion es {}".format(timeYear))
'''

'''
Ejercicio 42
    Escribir un programa que calcule la suma de los numeros hasta un numero
    dado (ingresado por consola)

suma = 0
print("Suma de enteros con centinela. Favor aguarde...")
valueUsr = int(input("Ingrese valor entero. -1 para terminar:\n"))
while valueUsr != -1:
    suma += valueUsr
    print("La suma es de: {}".format(suma))
    valueUsr = int(input("Ingrese valor entero:\n")
'''
'''
Ejercicio 43
    Escribir un programa que pida un numero y si el ingresado por consola
    es menor de 100 vuelva a solicitarlo

print("El entero es menor a 100?. Favor aguarde")
enteroUsr = int(input("Ingrese un numero entero de su eleccion:\n"))
while enteroUsr < 100:
    enteroUsr = int(input("Ingrese un numero entero de su eleccion:\n"))
else:
    print("El entero ingresado es igual o mayor a 100")
'''
'''
Ejercicio 44
    Escribir un programa que calcule el factorial de un numero

choiceUsr = int(input("Calcular el factorial de:\n"))
factorial = 1
output = 0
while choiceUsr > 0:
    factorial *= choiceUsr
    choiceUsr -= 1
    output += 1
else:
    pass
print("El factorial de {} es: {}".format(output, factorial))
'''
'''
Ejercicio 45
    Escribir un programa que calcule la media de 5 numeros ingresados por
    consola

print("Media de cinco (5) valores. Favor aguarde...")

contador = 0
auxSuma = 0
cuentaMedia = 0

for contador in range(5):
    ingresoUsr = int(input("Ingrese valor numerico.\n"))
    auxSuma = ingresoUsr
    cuentaMedia += auxSuma

print("El numerador para la media es: {}".format(cuentaMedia))
media = cuentaMedia/5
print("La media de los valores numericos es: {}".format(media))
'''

'''
Ejercicio 46
    Escribir un programa que calcule la media de 'x' cantidad de numeros
    ingresados por consola

print("Media de valores cantidad arbitraria. Favor aguarde...")

contador = 0
auxSuma = 0
cuentaMedia = 0
valoresMedia = int(input("Cuantos valores empleará en la cuenta\n"))

for contador in range(valoresMedia):
    ingresoUsr = int(input("Ingrese valor numerico.\n"))
    auxSuma = ingresoUsr
    cuentaMedia += auxSuma

print("El numerador para la media es: {}".format(cuentaMedia))
media = cuentaMedia/valoresMedia
print("La media de los valores numericos es: {}".format(media))
'''
'''
Ejercicio 47
    Escribir un programa que calcule la media de numeros ingresados por consola
    hasta que el ingresado sea cero (0)

print("Media de valores, cantidad progresiva anclada a un centinela.")
print("Favor aguarde...")

contador = 0
auxSuma = 0
cuentaMedia = 0
valoresMedia = 1
print("Ingrese valor numerico")
ingresoUsr = int(input("Para terminar la cuenta cero (0):\n"))

while ingresoUsr != 0:
    if ingresoUsr == 0:
        break
    auxSuma = ingresoUsr
    cuentaMedia += auxSuma
    print("El numerador para la media es: {}".format(cuentaMedia))
    media = cuentaMedia/valoresMedia
    valoresMedia += 1
    print("La media de los valores numericos es: {}".format(media))
    print("Ingrese valor numerico")
    ingresoUsr = int(input("Para terminar la cuenta cero (0):\n"))
else:
    pass
'''
'''
Ejercicio 48
    Escribir un programa que determine si un numero es primo o no. Un numero es
    primo si solo es divisible por si mismo y por la unidad

cont = 0
esPrimo = bool(True)

print("Evaluar si 'es' numero primo o 'no'. Favor aguarde...")
valorUsr = int(input("Ingrese valor numerico\n"))

for cont in range(2, (cont < valorUsr) and esPrimo):
    if valorUsr % cont == 0:
        esPrimo = False
if esPrimo:
    print("{} es numero primo\n".format(valorUsr))
else:
    print("{} no es numero primo\n".format(valorUsr))

# Salida inconsistente, ver solucion en java
'''
'''
Ejercicio 49
    Escribir un programa que escriba los numeros comprendidos entre 1 y 1000.
    El programa los presentara en grupos de 20, solicitando al usuario si
    quiere o no continuar al siguiente grupo


print("Enteros positivos por grupos de veinte (20). Favor aguarde...")
asw = str('si')
listNatural = int(1)
tope = int(1000)
paso = int(20)

while asw != 'no' and listNatural < tope:
    print(listNatural)
    if listNatural % paso == 0 and listNatural != tope:
        print("Desea continuar al sgte. grupo?\t")
        asw = input()
    listNatural += 1
'''
'''
Ejercicio 50
    Escribir un programa que calcule, independientemente, la suma y la
    media de los numeros impares y pares comprendidos entre 1 y 200

sumaPar = 0
listaPar = 0
sumaImp = 0
listImp = 0
for listaNaturales in range(1, 201):
    if listaNaturales % 2 == 0:
        sumaPar += listaNaturales
        listaPar += 1
    else:
        sumaImp += listaNaturales
        listImp += 1
listaNaturales += 1

mediaPar = sumaPar / listaPar
mediaImp = sumaImp / listImp
print("La suma de los valores pares de 1 a 200 es {}".format(sumaPar))
print("La media de esta suma de pares es {}".format(mediaPar))
print("La suma de los valores impares de 1 a 200 es {}".format(sumaImp))
print("La media de esta suma de impares es {}".format(mediaImp))
'''
'''
Ejercicio 51
    Escribir un programa que calcule la suma de los cuadrados de los cien
    (100) primeros numeros enteros

sumaCuadrado = 0
for indiceEnteros in range(1, 201):
    indiceEnteros = indiceEnteros**2
    sumaCuadrado += indiceEnteros
indiceEnteros += 1

print("La suma de los cuadrados para los primeros")
print("cien (100) valores enteros positivos es {}".format(sumaCuadrado))
'''
'''
Ejercicio 52
    Escribir un programa donde 10 valores ingresados por consola, sume
    solo aquellos que sean negativos

listaEspera = 1
sumaNegativos = 0

valorUsr = int(input("Ingrese valor entero:\n"))
while listaEspera <= 9:
    if valorUsr < 0:
        sumaNegativos += valorUsr
    valorUsr = int(input("Ingrese valor entero:\n"))
    listaEspera += 1

print("La suma de los valores negativos")
print("ingresados es {}".format(sumaNegativos))
'''
