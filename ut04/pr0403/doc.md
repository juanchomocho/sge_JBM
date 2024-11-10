[Tema04](../index.md)

# PR0403: Ejercicios con listas

--- 
[PR0403](https://vgonzalez165.github.io/apuntes_sge/ut04_python/pr0403_listas.html)
Haremos un par de ejercicios con listas.

1. ### Ejercicio 1.1 Operaciones con listas: Ordenando elementos
Mostrar los nombres ordenados alfabéticamente en orden inverso.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nombres.sort(reverse=True)

print(nombres)
```

2. ### Ejercicio 1.1 Operaciones con listas: Contando elementos
Contar el número de nombres que comienzan con la letra a.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

numero_palabras_a = 0

for nombre in nombres:
    if nombre[0] == "Á" or nombre[0] == "A":
        numero_palabras_a += 1

print(numero_palabras_a)
```

3. ### Ejercicio 1.1 Operaciones con listas: Buscar un elementos
Pregunte al usuario su nombre y le indique si está en la lista, y en caso afirmativo, en qué posición está.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nombre_usuario = input("Introduzca su nombre por favor: ")

if nombre_usuario in nombres:
    posicion = nombres.index(nombre_usuario)
    print("Tu nombre es: " + nombre_usuario)
    print("La posición de tu nombre es: " + str(posicion + 1))
else:
    print("Tu nombre no está en la lista, fuera")
```

4. ### Ejercicio 1.1 Operaciones con listas: Primeros elementos
Pregunte al usuario su nombre y le muestre el listado de todos los nombres que se encuentran delante del suyo.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nombre_usuario = input("Introduzca su nombre por favor: ")

if nombre_usuario in nombres:
    posicion = nombres.index(nombre_usuario)
    print("Tu nombre es: " + nombre_usuario)
    print("Estos nombres están por delante tuyo: " + str(nombres[posicion:]))
else:
    print("Tu nombre no está en la lista, fuera")
```

5. ### Ejercicio 1.1 Operaciones con listas: Obtener número de nombres de una longitud
Pregunte al usuario un número y le diga cuántos nombres hay en la lista con la misma longitud que el número indicado.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

longitud = int(input("Dime la longitud deseada: "))

numero_palabras = 0

for nombre in nombres:
    if len(nombre) == longitud:
        numero_palabras += 1

print(str(numero_palabras))
```

6. ### Ejercicio 1.1 Operaciones con listas: Nombres cortos
Muestre todos los nombres cuya longitud sea igual o inferior a 4 caracteres.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nuevas_palabras = []

for nombre in nombres:
    if len(nombre) <= 4:
        nuevas_palabras.append(nombre)

print(str(nuevas_palabras))
```

7. ### Ejercicio 1.1 Operaciones con listas: Número de vocales
Indique cuántas veces se repite cada una de las vocales entre todos los nombres (ignorando mayúsculas y minúsculas).

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

letras = {}

letras["a"] = 0
letras["e"] = 0
letras["i"] = 0
letras["o"] = 0
letras["u"] = 0

for nombre in nombres:
    for letra in nombre:
        if letra.lower() in letras:
            letras[letra.lower()] += 1

print(str(letras))
```

8. ### Ejercicio 1.1 Operaciones con listas: Número de letras
Imprima el número de veces que se repite cada letra del abecedario entre todos los elementos de la lista.

```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

letras = {}

for i in range(26):
    letras[chr(i+97)] = 0

for nombre in nombres:
    for letra in nombre:
        if letra.lower() in letras:
            letras[letra.lower()] += 1

print(str(letras))
```


9. ### Ejercicio 2.1 Más ejercicios con listas: Sumar elementos de una lista
Dada una lista de números, escribe un programa que calcule y muestre la suma de todos sus elementos.

```python
numeros = [1, 54, 21, 23, 523, 2, 4, 6, 1, 6, 2, 48, 98, 5]

print(len(numeros))
```

10. ### Ejercicio 2.2 Más ejercicios con listas: Contar elementos específicos
Dada una lista de palabras, permite al usuario ingresar una palabra y cuenta cuántas veces aparece en la lista.

```python
palabras = ["bomba", "tombola", "meem", "meem", "gut", "bomba", "bomba", "bomba", "tombola", "meem", "meem", "gut"]

entrada = input("Ecoge una palabra: ")

contador = 0

for palabra in palabras:
    if entrada == palabra:
        contador += 1

print(contador)
```

11. ### Ejercicio 2.3 Más ejercicios con listas: Eliminar duplicados
Dada una lista de números, elimina todos los elementos duplicados y muestra la lista con solo valores únicos.

```python
lista = [3, 4, 2, 1, 2, 3]
lista = list(set(lista))
print(lista)
```

12. ### Ejercicio 2.4 Más ejercicios con listas: Máximo y mínimo
Escribe una función que tome una lista de números y devuelva el valor máximo y mínimo de la lista.

```python
lista = [1, 3, 2, 65, 23, 12, 645, 87, 43 ,213 ,34]

def coger_mayor_menor(numeros):
    numeros = list(sorted(numeros))

    numero_mayor = numeros[0]
    numero_menor = numeros[len(numeros) - 1]

    return numero_mayor, numero_menor

numero_grande, numero_chico = coger_mayor_menor(lista)

print("El numero mas pequeño es: " + str(numero_chico))
print("El numero mas grande es: " + str(numero_grande))
```

13. ### Ejercicio 2.5 Más ejercicios con listas: Filtrar números pares
Dada una lista de números, genera una nueva lista que contenga solo los números pares.

```python
numeros_todos = [12, 23 , 4, 1, 2, 32, 4, 64, 3, 12, 5, 7,3 ,2 ,34, 64]
numeros_pares = []

for numero in numeros_todos:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    
print(str(numeros_pares))
```

14. ### Ejercicio 2.6 Más ejercicios con listas: Revertir una lista
Escribe una función que tome una lista y devuelva una nueva lista con los elementos en orden inverso, sin utilizar el método .reverse().

```python
entrada = [2, 3, "ford", "gato", 'loco', 98]

def revertir_lista(lista):
    lista_revertida = []
    for elemento in lista[::-1]:
        lista_revertida.append(elemento)

    return lista_revertida

print(revertir_lista(entrada))
```

15. ### Ejercicio 2.7 Más ejercicios con listas: Concatenar listas
Dadas dos listas de números, crea una función que devuelva una tercera lista que contenga los elementos de ambas listas intercalados.

```python
entrada1 = ["mono", "macaco", "monaco", "rey", "ladrillo"]
entrada2 = ["castillo", "cigarrillo", "raton", "stat", "teclado"]

def concaternar_listas(lista1, lista2):
    lista_resultado = []
    tamano_lista_mas_larga = len(entrada1) if len(entrada1) < len(entrada2) else len(entrada2)
    for i in range(tamano_lista_mas_larga):
        lista_resultado.append(lista1[i])
        lista_resultado.append(lista2[i])

    return lista_resultado

print(concaternar_listas(entrada1, entrada2))
```

16. ### Ejercicio 2.8 Más ejercicios con listas: Encuentra elementos comunes
Escribe un programa que tome dos listas y devuelva una nueva lista con los elementos que son comunes en ambas.

```python
lista1 = [12, 21, 43, 3, 21, 2, 35, 62]
lista2 = [12, 5, 3, 21, 24, 3, 2, 34, 62]

lista_resultado = list(set.intersection(set(lista1), set(lista2)))
print(str(lista_resultado))
```

17. ### Ejercicio 2.9 Más ejercicios con listas: Dividir una lista
Dada una lista de números, crea dos listas: una con los números mayores o iguales a la media y otra con los números menores a la media.

```python
lista_total = [1, 2, 1, 2, 4, 5, 62, 2,2,4, 87, 3]
lista_menores = []
lista_mayores = []

total = 0
for numero in lista_total:
    total += numero

avg = total // len(lista_total)

for numero in lista_total:
    if numero < avg:
        lista_menores.append(numero)
    else:
        lista_mayores.append(numero)

print(lista_menores)
print(lista_mayores)
```

18. ### Ejercicio 2.10 Más ejercicios con listas: Lista de listas
Crea una lista de listas que represente una matriz de números y escribe una función que devuelva la suma de cada fila y columna.

```python
lista_listas = [[2, 4, 4], [5, 2, 7], [9, 2, 6]]

suma_filas = []
suma_columnas = []

for lista in lista_listas:
    suma = 0
    for numero in lista:
        suma += numero
    suma_filas.append(suma)


for columna in range(len(lista_listas)):
    suma = 0
    for lista in lista_listas:
        suma += lista[columna]
    suma_columnas.append(suma)

print(suma_filas)
print(suma_columnas)
```
