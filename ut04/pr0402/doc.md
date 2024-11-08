[Tema04](../index.md)

# PR0402: Ejercicios de cadenas

--- 
[PR0402](https://vgonzalez165.github.io/apuntes_sge/ut04_python/pr0402_cadenas.html)
Haremos un par de ejercicios con cadenas.

1. ### Ejercicio 1: Contar vocales y consonantes
Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.

```python
entrada = input("Introduce la cadena: ")

def recibir(cadena):
    consonantes = 0
    volcales = 0
    for i in cadena:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            volcales += 1
        else:
            consonantes += 1
    return volcales, consonantes

a, b = recibir(entrada)

print("Vocales " + str(a))
print("Consoantes: " + str(b))
```

2. ### Ejercicio 2: Invertir una cadena
Crea un programa que invierta una cadena.

```python
entrada = input("Introduce tu cadena: ")

print(entrada[::-1])
```

3. ### Ejercicio 3: Verificar palíndromo
Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).

```python
entrada = input("Introduce tu cadena: ")

respuesta = ""

if len(entrada) % 2 == 0:
    primera_mitad = entrada[:len(entrada)//2]
    segunda_mitad = entrada[len(entrada)//2:]
else:
    primera_mitad = entrada[:len(entrada)//2]
    segunda_mitad = entrada[len(entrada)//2 + 1:]

if primera_mitad == segunda_mitad[::-1]:
    respuesta = entrada + " si es un palindromo"
else:
    respuesta = entrada + " no es un palindromo"

print(str(respuesta))
```

4. ### Ejercicio 4: Contar palabras
Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios.

```python
entrada = input("Introduce la entrada: ")

def contar_palabras(cadena):
    cadena_partida = cadena.split(" ")

    contador = 0

    for i in cadena_partida:
        contador += 1

    return contador

contado = contar_palabras(entrada)


print("Tienes " + str(contado) + " palabras")
```

5. ### Ejercicio 5: Eliminar caracteres repetidos
Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.

```python
entrada = input("Introduce tu entrada: ")

letras_encontradas = []

def eliminar_duplicados(cadena):
    resultado = ""
    for cara in cadena:
        if(not cara in letras_encontradas):
            letras_encontradas.extend(cara)
        
    
    return letras_encontradas

print(str(eliminar_duplicados(entrada)))
```

6. ### Ejercicio 6: Mayusculas y minusculas
Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.

```python
entrada = input("Introduce tu palabra: ")

entrada = entrada.swapcase()

print(entrada)
```

7. ### Ejercicio 7: Invertir palabras de una cadena
Escribe un programa que invierta el orden de las palabras de una cadena, manteniendo las palabras originales intactas.

```python
entrada = input("Introduce tu cadena de palabras")

palabras = entrada.split(" ")

palabras.reverse()

print(palabras)
```

8. ### Ejercicio 8: Anagrama
Crea un programa que verifique si dos cadenas son anagramas. Se considera que dos palabras son anagramas si tienen las mismas letras en diferente orden, por ejemplo, lácteo y coleta.

```python
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if sorted(palabra1) == sorted(palabra2):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")
```

9. ### Ejercicio 9: Frecuencia de caracteres
Crea una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada carácter.

```python
entrada = input("Introduce tu palabra")

def contar_palabras(letras):
    dic = {}
    palabra = tuple(letras)
    for cara in palabra:
        if cara in dic:
            dic[cara] += 1
        else:
            dic[cara] = 1
    print(dic)

contar_palabras(entrada)
```

10. ### Ejercicio 10: Quitar caracteres alfanumericos
Escribe un programa que elimine todos los caracteres no alfanuméricos (como signos de puntuación) de una cadena.

```python
entrada = input("Escribe tu cadena: ")

palabra_nueva = ""

for cara in entrada:
    if cara.isalnum():
        palabra_nueva += cara

print(palabra_nueva)
```

11. ### Ejercicio 11: Transformar a camelCase
Escribe un programa que transforme una cadena de palabras separadas por espacios o guiones en formato camelCase (la primera letra de cada palabra, excepto la primera, debe ser mayúscula y no debe haber espacios ni guiones).

```python
entrada = input("Escribe tu cadena: ")

palabra_nueva = ""
encontrado = False

for cara in entrada:
    if  cara != ' 'and cara != '-':
        if encontrado:
            palabra_nueva += cara.upper()
            encontrado = False
        else:
            palabra_nueva += cara
    else:
        encontrado =True


print(palabra_nueva)
```

12. ### Ejercicio 12: Codificación RLE (Run-Length Enconding)
Escribe una función que implemente la codificación por longitud de ejecución (RLE), que consiste en comprimir una cadena representando las secuencias consecutivas de caracteres iguales con el carácter seguido de la cantidad de repeticiones.

```python
entrada = input("Escribe tu palabra: ")


def transformal_a_rle(cadena):
    rle = ""
    cara_anterior = ""
    contador = 1
    for cara in cadena:
        if cara_anterior == "":
            cara_anterior = cara
            rle += cara
        elif (cara == cara_anterior):
            contador += 1
        else:
            rle += str(contador) + cara
            contador = 1
            cara_anterior = cara
    rle += str(contador)
    return rle

print(transformal_a_rle(entrada))
```

13. ### Ejercicio 13: Decodificar RLE
Crea una función que decodifique una cadena que ha sido comprimida usando el método RLE.

```python
entrada = input("Introduce tu palabra: ")

caracter = ""

cadena_traducida = ""

for char in entrada:
    if char.isdigit():
        cadena_traducida += caracter * int(char)
    else:
        caracter = char

print(cadena_traducida)
```

14. ### Ejercicio 14: Formateo de cadenas con plantillas
Escribe un programa que tome una plantilla de cadena y un diccionario, y reemplace los marcadores en la plantilla por los valores correspondientes en el diccionario.

```python
print("Escribe tu nombre para obtener la siguiente linea: ")
print("Hola: {nombre}")

entrada = input("")
dict = {"nombre" : entrada}

print("Hola: " + dict["nombre"])
```

15. ### Ejercicio 15: Comparar cadenas con valor ASCII
Escribe una función que compare dos cadenas sumando el valor ASCII de cada carácter y devuelva cuál tiene un mayor valor total. Para este ejercicio ten en cuenta que la función integrada ord() devuelve el valor ASCII de un carácter

```python
entrada = input("mete tu palabra: ")

def get_ascci_value(cadena):
    contador = 0
    for char in cadena:
        contador += ord(char)
    return contador


print(entrada + " " + str(get_ascci_value(entrada)))
```

16. ### Ejercicio 16: Contar la longitud de palabra más larga
Escribe un programa que reciba una cadena y devuelva la longitud de la palabra más larga

```python
entrada = input("Escribe tu cadena: ")
palabras = entrada.split(" ")

maxima_longitud = 0
palabra_mas_larga = ""

for palabra in palabras:
    if len(palabra) > maxima_longitud:
        palabra_mas_larga = palabra

print(palabra_mas_larga)
```

17. ### Ejercicio 17: Formatear numero con separador de miles
Escribe una función que tome un número de forma de cadena y le agregue separadores de miles.

```python
entrada = input("Mete un numero: ")



def poner_puntos(cadena):
    contador = len(cadena)
    cadena_traducida = ""
    for i in range(len(cadena)):
        if(contador % 3 == 0):
            cadena_traducida += "."
        cadena_traducida += cadena[i]
        contador -= 1
    return cadena_traducida

print(poner_puntos(entrada))
```

18. ### Ejercicio 18: Rotar caracteres de una cadena
Escribe una función que rote una cadena hacia la izquierda un número dado de veces.

```python
entrada = input("Escribe tu palabra: ")
numero_rotacion = int(input("Escribe el numero de rotaciones: "))

def swap(cadena, num_rotaciones):
    num_rotaciones %= len(cadena)
    return cadena[num_rotaciones:] + cadena[:num_rotaciones]


print(swap(entrada, numero_rotacion))
```