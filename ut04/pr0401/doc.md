[Tema04](../index.md)

# PR0401: Ejercicios básicos en Python

--- 
[PR0401](https://vgonzalez165.github.io/apuntes_sge/ut04_python/pr0401_ejercicios_basicos.html)
Haremos un par de ejercicios de python para comprender un par de conceptos basicos.

1. ### Ejercicio 1: Lectura de un número válido
Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.

```python
entrada = input("Introduce un numero: ")

while(not entrada.isdigit()):
    entrada = input("Introduce un numero: ")

print("Gracias por elejir un numero")
```

2. ### Ejercicio 2: Tabla de multiplicar
Crea un programa que solicite un número **n** y un valor **k** y que muestre por la terminal los primeros **k** elementos de la tabla de multiplicar de **n**.

```python
a = int(input("Pon un numero "))
b = int(input("Cuantas veces lo multiplicamos? "))

for num in range(b):
    print(str(a) + " * " + str(num + 1) + " = " + str(a*(num + 1)))
```

3. ### Ejercicio 3: Triángulo de asteriscos
Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.

```python
base = int(input("Introduce la base del triangulo: "))

for numero in range(base):
    print("*" * (numero + 1))
```

4. ### Ejercicio 4: Pirámide de asteriscos
Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número par.

```python
base = int(input("Introduce la base del triangulo: "))


for numero in range(1, (base + 1), 2):
    espacios = (base - numero) // 2
    linea = " " * espacios
    print(linea + "*" * (numero))
```

5. ### Ejercicio5:
Crea un programa que pida al usuario que introduzca 5 números y luego le diga cuál es el mayor y el menor de todos ellos de la forma: *El número **mayor** es **mayor** y el **menor** es **menor***

```python
import math

numero_menor = math.inf
numero_mayor = -math.inf

for num in range(5):
    numero_nuevo = int(input("Introduzca un numero: "))
    if(numero_menor > numero_nuevo):
        numero_menor = numero_nuevo
    if(numero_mayor < numero_nuevo):
        numero_mayor = numero_nuevo

print("El numreo mayor es: " + str(numero_mayor))
print("El numero menor es: " + str(numero_menor))
```

6. ### Ejercicio6: Conversión de unidades
Crea un programa que convierta entre diferentes unidades de longitud *(milímetros, centímetros, metros y kilómetros)*. El usuario introducirá primero la **cantidad**, luego la **unidad de medida** en que está y finalmente la **unidad de medida** a la que se va a convertir.

```python
cantidad = int(input("introduce la unidad a la que quieres cambiar"))
unidad_inicial = input("Introduce la unidad de miedida inicial")
unidad_final = input("Introduce la unidad de medida final")

match unidad_final:
    case "mm":
        cantidad = (
            (cantidad * (10 ** 1)) if unidad_inicial == "cm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "m" else
            (cantidad * (10 ** 6)) if unidad_inicial == "km" else
            cantidad
        )
    case "cm":
        cantidad = (
            (cantidad * (10 ** -1)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 2)) if unidad_inicial == "m" else
            (cantidad * (10 ** 5)) if unidad_inicial == "km" else
            cantidad
        )
    case "m":
        cantidad = (
            (cantidad * (10 ** -2)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "mm" else
            (cantidad * (10 ** 3)) if unidad_inicial == "km" else
            cantidad
        )
    case "km":
        cantidad = (
            (cantidad * (10 ** -5)) if unidad_inicial == "cm" else
            (cantidad * (10 ** -3)) if unidad_inicial == "m" else
            (cantidad * (10 ** -6)) if unidad_inicial == "mm" else
            cantidad
        )

cantidad = round(cantidad)

print("Tu medida es: " + str(cantidad) + str(unidad_final))
```

7. ### Ejercicio7: Acierta el número

Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo.

```python
from random import *

numero_aleatorio = randint(0, 100)
encontrado = False

while not encontrado:
    numero_elegido = int(input("Elije un numero: "))
    if numero_aleatorio > numero_elegido:
        print("no, tu numero es demasiado pequeño")
    elif numero_aleatorio < numero_elegido:
        print("no, tu numero es demasiado grande")
    else:
        print("correcto, tu numero es " + str(numero_aleatorio))
```

8. ### Ejercicio8: Piedra, papel o tijeras
Crea un programa que implemente el clásico juego de piedra, papel, tijeras, lagarto y spock.
Ganará el primero que gane 5 manos.

```python
from random import *

eleciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]

enemigo_victorias = 0
player_victorias = 0
while(not (enemigo_victorias == 5 or player_victorias == 5)):
    player_eleccion = input("Elije piedra, papel tijeras, lagarto o spock: ")
    enemigo_eleccion = choice(eleciones)
    match (enemigo_eleccion):
        case "piedra":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "papel":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "tijeras":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "lagarto":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "spock":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
    print("Victorias de player " + str(player_victorias))
    print("Victorias de enemigo: " + str(enemigo_victorias))
        
if(enemigo_victorias == 5):
    print("Enemigo gana")
else:
    print("Player gana")
```

9. ### Ejercicio9: Secuencia de Fibonacci
Crea un programa que genere los primeros **n** números de la secuencia de Fibonacci.

```python
numeros = [0, 1]

n = int(input("Cuantos numeros de la cadena de fibbonacci quieres que te muestre?: "))

for i in range(2, n):
    siguiente = numeros[i-1] + numeros[i-2]
    numeros.append(siguiente)

if n > 2:
    print(numeros)
elif n == 2:
    print("0, 1")
elif n == 1:
    print("0")
else:
    print("no puedes imprimir 0 numeros")
```