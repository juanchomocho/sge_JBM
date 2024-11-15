[Tema04](../index.md)

# PR0405: Ejercicios de programación funcional

--- 
[PR0405](https://vgonzalez165.github.io/apuntes_sge/ut04_python/pr0405_programacion_funcional.html)
Haremos un par de ejercicios con utilizando la programación funcional.

1. ### Ejercicio 1 Buscando el valor de un diccionario
Usa filter para obtener solo los números pares de una lista de enteros.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares) 
```

2. ### Ejercicio 2 Mapeo de temperaturas
Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.

```python
celsius = [0, 20, 37, 100]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit) 
```

3. ### Ejercicio 3 Suma acumulativa
Utiliza reduce para obtener la suma acumulativa de una lista de números.

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

suma_acumulativa = reduce(lambda x, y: x + y, numeros)

print(suma_acumulativa)
```

4. ### Ejercicio 4 Palabras con cierta longitud
Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas.

```python
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

palabras_largas = filter(lambda palabra: len(palabra) > 5, palabras)


resultado = list(map(lambda palabra: palabra.upper(), palabras_largas))

print(resultado)
```

5. ### Ejercicio 5 Multiplicación de pares
Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

pares = filter(lambda x: x % 2 == 0, numeros)

producto = reduce(lambda x, y: x * y, pares)

print(producto)
```

6. ### Ejercicio 6 Combinar operaciones en listas anidadas
Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.

```python
from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

numeros_aplanados = reduce(lambda x, y: x + y, numeros)

positivos = filter(lambda x: x > 0, numeros_aplanados)

suma_positivos = reduce(lambda x, y: x + y, positivos)

print(suma_positivos)
```