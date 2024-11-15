[Tema04](../index.md)

# PR0404: Ejercicios con diccionarios

--- 
[PR0404](https://vgonzalez165.github.io/apuntes_sge/ut04_python/pr0404_diccionarios.html)
Haremos un par de ejercicios con diccionarios.

1. ### Ejercicio 1 Buscando el valor de un diccionario
Crea un diccionario de frutas y precios. Permite al usuario ingresar el nombre de una fruta y muestra su precio si existe en el diccionario, o un mensaje de que no está disponible en caso contrario.

```python
entrada = input("Introduce la fruta que quieras conocer: ")

productos = {"Fresa" : 4.50, "Mandarina" : 8.90, "Tomate" : 7.50}

if(entrada in productos):
    print(entrada + str(productos(entrada)))
else:
    print("No se encuentra la fruta solicitada")
```

2. ### Ejercicio 2 Contar elementos en un diccionario
Suponiendo un diccionario con al siguiente estructura, crea un programa que calcule cuántas categorías hay, cuántos productos tiene cada categoría y cuántos productos hay en total.

```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

print(len(productos))

for producto in productos:
    print(producto + ": " + str(len(productos.get(producto))) + " elementos")
```

3. ### Ejercicio 3 Contador de frecuencias de palabras
Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra.

```python
entrada = input("Introduce tu frase: ")

entrada_split = entrada.split()

palabras = {}

for palabra in entrada_split:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

print(str(palabras))
```

4. ### Ejercicio 4 Diccionario de listas
Supón un diccionario donde cada clave es una asignatura y el valor correspondiente una lista de estudiantes matriculados, tal como se muestra en el diccionario de ejemplo. Crea un programa que tenga un menú con tres opciones:
     Listar estudiantes matriculados en una asignatura, Matricular un estudiante en una asignatura, Dar de baja un estudiante de una asignatura.

```python
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
encontrado = False

print("1. Listar estudiantes matricula")
print("2. Matricular estudiante en una asignatura")
print("3. Dar de baja a un estudiante")

def listar_alumnos(lista):
    asignatura = input("Elige una asignatura:")
    asignatura_correcta = False
    alumnos = ""
    while not asignatura_correcta:
        if asignatura in lista:
            alumnos = str(lista[asignatura])
            asignatura_correcta = True
        else:
            asignatura = input("Elige una asignatura: ")
    return alumnos

def matricular_alumno(lista):
    asignatura = input("Elige una asignatura: ")
    alumno = input("Elije el nombre del alumno")
    asignatura_correcta = False
    while not asignatura_correcta:
        if asignatura in lista:
            asignaturas[asignatura].append(alumno)
            asignatura_correcta = True
        else:
            asignatura = input("Elige una asignatura: ")
            alumno = input("Elije el nombre del alumno")

    return alumno + " ha sido añanido a " + asignatura

def dar_de_baja(lista):
    asignatura = input("Elige una asignatura: ")
    alumno = input("Elije el nombre del alumno")
    asignatura_correcta = False
    while not asignatura_correcta:
        if asignatura in lista:
            if alumno in asignaturas[asignatura]:
                asignaturas[asignatura].remove(alumno)
                asignatura_correcta = True
            else:
                asignatura = input("Elige una asignatura: ")
                alumno = input("Elije el nombre del alumno")
        else:
            asignatura = input("Elige una asignatura: ")
            alumno = input("Elije el nombre del alumno")

    return alumno + " ha sido añanido a " + asignatura

respuesta = ""
while not encontrado:
    opcion = input("Por favor elige una opción: ")
    if opcion == "1":
        respuesta = listar_alumnos(asignaturas)
        encontrado = True
    elif opcion == "2":
        respuesta = matricular_alumno(asignaturas)
        encontrado = True
    elif opcion == "3":
        respuesta = dar_de_baja(asignaturas)
        encontrado = True
    else:
        encontrado = False


print(respuesta)
```

5. ### Ejercicio 5 Diccionario invertido
Escribe una función que tome un diccionario y devuelva otro con las claves y valores intercambiados (lo que antes eran valores ahora son claves, y viceversa).

```python
nombres = {"pepe": 1, "mario": 2, "anya": 3, "juan" :5}

def diccionario_invertido(dic):
    invertido = {v: k for k, v in dic.items()}
    return invertido



invertido = diccionario_invertido(nombres)
print(invertido)
```

6. ### Ejercicio 6 Combinar dos diccionarios
Escribe un programa que tome dos diccionarios de productos y precios, y combine los productos comunes sumando sus precios, sin duplicar los elementos únicos.

```python
productos1 = {"manzanas" : 3, "platanos" : 2, "uvas" : 5}
productos2 = {"manzanas" : 4, "naranjas" : 3, "uvas" : 2}

def combinar_diccionarios(dic1, dic2):
    combinado = dic1.copy()  
    for producto, precio in dic2.items():
        if producto in combinado:
            combinado[producto] += precio 
        else:
            combinado[producto] = precio
    return combinado

resultado = combinar_diccionarios(productos1, productos2)
print(resultado)  
```