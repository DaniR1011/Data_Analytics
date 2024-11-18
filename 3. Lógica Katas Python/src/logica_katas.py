# Ejercicios Katas Python -> Daniel Recio.

#### 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(cadena):
 """
    Calcula la frecuencia de cada letra que componen el diccionario.
    
    Parámetros:
    cadena: contiene el listado de las palabras.
    
    Retorna:
    list: Una lista de valores con la frecuencia de cada palabra.
 """
 repetidas = {}
# Con el .replace eliminamos los espacios que pueden existir entre las letras
 for letra in cadena.replace(" ", ""):
        if letra in repetidas:
            repetidas[letra] += 1
        else:
            repetidas[letra] = 1
 return repetidas

# Ejemplo de la función
cadena = "ejemplo repetidas"
repetidas = frecuencia_letras(cadena)
print(repetidas)

#### 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
"""
    Calcula el doble de cada valor dada una lista de valores.
    
    Parámetros:
    map(): Multiplica por dos cada valor.
    
    Retorna:
    list: Una lista de valores que son el doble de los valores insertados.
"""
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))

# Ejemplo de la función
print(resultado)

#### 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def resultado_palabras(palabras, palabra_objetivo):
 """
    Calcula a través de una palabra objetivo, las palabras de la lista que contengan esa palabra objetivo.
    
    Parámetros:
    palabras (list): Listado de palabras.
    palabra_objetivo (str): Palabra objetivo a repetir.
    
    Retorna:
    list: Una lista de palabras que se repiten, respecto de la palabra objetivo.
 """
 return [palabra for palabra in palabras if palabra_objetivo in palabra]

# Ejemplo de la función
palabras = ["jardin", "jardinero", "jardineria", "hoja", "arbol", "jarron"]
objetivo = "jard"
resultado = resultado_palabras(palabras, objetivo)
print(resultado)

#### 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""
    Calcula la diferencia entre los valores de las dos listas.
    
    Parámetros:
    listaA (list): Contiene los valores de la primera lista.
    listaB (list): Contiene los valores de la segunda lista.
    
    Retorna:
    list: Una lista de valores que contiene la diferencia de valores entre ellas.
"""
listaA = [4, 3, 2]
listaB = [3, 1, 0]

# Usamos map con lambda para restar los elementos de cada lista
resultado = list(map(lambda x, y: x - y, listaA, listaB))

# Ejemplo de la función
print(resultado)

#### 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def calcular_nota(notas, aprobado = 5):
 """
    Calcula la media de unos valores, si es mayor o igual a 5 aprobado, y en caso contrario, suspenso.
    
    Parámetros:
    notas (list): Contiene la lista con los valores obtenidos.
    aprobado (int): Determina que el aprobado debe ser mayor o igual a 5.
    
    Retorna:
    list: Una lista de valores con la media de los valores y determinando si está aprobado o suspenso.
 """
 media = sum(notas) / len(notas) if notas else 0
 estado = "aprobado" if media >= aprobado else "suspenso"
 return (media, estado)

# Ejemplo de la función
notas = [3, 10, 3, 4, 6]
resultado = calcular_nota(notas)
print(resultado)

#### 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def calculo_factorial(x):
 """
    Calcula el factorial de un número.
    
    Parámetros:
    x (int): El valor a partir del cual se calcula el factorial.
    
    Retorna:
    int: Un número con el factorial calculado.
 """
 if x == 0 or x == 1:
     return 1
 else:
     return x * calculo_factorial(x - 1)

# Ejemplo de la función
numero = 8
resultado = calculo_factorial(numero)
print(resultado)

#### 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""
    Convierte una lista de tuplas en una lista de strings.
    
    Parámetros:
    map(): Convierte el valor a string.
    
    Retorna:
    list: Una lista de valores convertidos a string.
"""
tuplas = [(1, 2), (2, 3), (3, 'hola')]
# Usamos map con lambda para convertir cada tupla en un string
resultado = list(map(lambda tupla: f"({tupla[0]}, {tupla[1]})", tuplas))

# Ejemplo de la función
print(resultado)

#### 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir_numeros(num1, num2):
 """
    Calcula la división entre dos números.
    
    Parámetros:
    num1 (int): Valor del primer número ingresado.
    num2 (int): Valor del segundo número ingresado.
    
    Retorna:
    int: El valor final que sea la división entre el primero y el segundo. 
    Teniendo en cuenta valores no numéricos o dividir entre 0.
 """
 try:
        resultado = num1 / num2
# Utilizamos el ZeroDivisionError si el usuario añade un 0, debido a que la división causaría error
 except ZeroDivisionError:
        print("❌ No se puede dividir por 0")
# Utilizamos el ValueError si el usuario ingresa valores no numéricos
 except ValueError:
        print("❌ Ingresa valores numéricos")
# Si los dos casos anteriores no se cumplen, significa que la división se realizó correctamente
 else:
        print(f"La división se realizó correctamente, el resultado es: {resultado}")

# Ejemplo de la función
print(dividir_numeros(10,4))

#### 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
def filtrar_mascotas(mascotas):
 """
    Calcula la lista de mascotas, excluyendo las prohibidas.
    
    Parámetros:
    mascotas (list): Contiene el listado de mascotas.
    
    Retorna:
    list: Una lista de valores excluyendo las mascotas prohibidas.
 """
 mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Definimos las mascotas permitidas, y utilizamos un filter donde no aparezcan las mascotas prohibidas. Volvemos a utilizar lambda para generar dos condiciones sobre mascotas.
 mascotas_permitidas = list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas))
 print(mascotas_permitidas)

# Ejemplo de la función
 mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Serpiente Pitón"]
 resultado = filtrar_mascotas(mascotas)
 print(resultado)

#### 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(numeros):
 """
    Calcula el promedio de una lista de valores.
    
    Parámetros:
    numeros (list): Contiene el listado de valores.
    
    Retorna:
    list: Una lista de valores con el promedio calculado.
 """
 try:
        if not numeros:
# Excepción si la lista está vacía
            raise Exception("La lista está vacía. Por favor completa la lista con valores.")
        promedio = sum(numeros) / len(numeros)
        return promedio

 except Exception as error:
        # Manejar el error y mostrar el mensaje si se lanza una excepción
        print(f"❌ Error: {error}")

# Ejemplo de la función
numeros = [1, 2, 3, 4, 6]
print("El promedio de los valores es: ", calcular_promedio(numeros))

#### 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def introduce_edad(edad):
 """
    Calcula la edad del usuario, tras el valor ingresado.
    
    Parámetros:
    edad (int): El valor de la edad.
    
    Retorna:
    int: El cálculo de la edad según el valor ingresado y sus respectivas excepciones.
 """
 try:
        edad = int(edad)
# Comprobar que la edad esté en el rango solicitado
        if edad < 0 or edad > 120:
            raise ValueError("❌ Error. La edad debe estar entre 0 y 120.")
        print(f"Tienes: {edad} años.")
# Manejar el error si el valor es no numérico o está fuera del rango permitido
 except ValueError as error:
        print(f"Error: {error}")

# Ejemplo de la función
print(introduce_edad(132))

#### 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
 """
    Calcula la longitud de cada palabra dada una frase.
    
    Parámetros:
    frase (str): Contiene la frase con las palabras a calcular.
    
    Retorna:
    list: Una lista con la longitud de las palabras que forman la frase.
 """
# Usamos map con lambda para obtener la longitud de cada palabra
 return list(map(lambda palabra: len(palabra), frase.split()))

# Ejemplo de la función
frase = "La longitud de esta frase"
resultado = longitud_palabras(frase)
print(resultado)

#### 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()
def generar_tuplas_caracteres(caracteres):
 """
    Genera una lista de tuplas con las letras en mayúsculas y minúscula sin que se repitan.
    
    Parámetros:
    caracteres (list): Conjunto de caracteres.
    
    Retorna:
    list: Una lista de tuplas, con los valores en mayus y minus sin que estén repetidos.
 """
 caracteres_unicos = set(caracter.lower() for caracter in caracteres)
# Aplicamos map para obtener las tuplas de mayúscula y minúscula
 resultado = list(map(lambda x: (x.upper(), x.lower()), caracteres_unicos))
 return resultado

# Ejemplo de la función
letras = ['a', 'b', 'A', 'c', 'B', 'C']
print(generar_tuplas_caracteres(letras))

#### 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_primera_letra(palabras, primera_letra):
 """
    Calcula las palabras que comienzan por una letra elegida.
    
    Parámetros:
    palabras (list): Contiene las palabras.
    primera_letra (str): Letra inicial elegida.
    
    Retorna:
    list: Una lista de palabras que empiezan por la letra elegida.
 """
# Usamos filter() para obtener las palabras que comienzan con la letra especificada, gracias a startswith
 resultado = list(filter(lambda palabra: palabra.startswith(primera_letra), palabras))
 return resultado

# Ejemplo de la función
lista_palabras = ["dinero", "dedo", "doble", "dejar", "hola", "adios"]
print(palabras_primera_letra(lista_palabras, "d"))

#### 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def sumar_tres(numeros):
 """
    Calcula cada número elegido más 3.
    
    Parámetros:
    numeros (list): Lista de números a sumar.
    
    Retorna:
    list: Una lista de valores que son la suma del propio valor más 3.
 """
 return list(map(lambda x: x + 3, numeros))

# Ejemplo de la función
numeros = [2, 4, 6, 8, 10]
print(sumar_tres(numeros))

#### 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas_n(frase, n):
 """
    Calcula las palabras que son más largas que el parámetro n.
    
    Parámetros:
    frase (str): Contiene la cadena de texto.
    n (int): Parámetro el cual mide la longitud de las palabras.
    
    Retorna:
    list: Una lista de palabras de longitud mayor a n.
 """
 palabras = frase.split()
# Con filter definimos que las palabras tienen que tener mayor len que n
 resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
 return resultado

# Ejemplo de la función
frase = "Palabras de mayor longitud que n"
n = 4
print(palabras_mas_largas_n(frase, n))

#### 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
# Reduce se encuentra en el módulo functools, por lo que primero se debe importar
from functools import reduce
def numero_digitos(digitos):
 """
    Calcula el número correspondiente a patir de una lista de dígitos.
    
    Parámetros:
    digitos (list): Listado de dígitos.
    
    Retorna:
    int: El valor que corresponde al número completo.
 """
 return reduce(lambda x, y: x * 10 + y, digitos)

# Ejemplo de la función
lista_digitos = [9,4,6,5,2]
print(numero_digitos(lista_digitos))

#### 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def calcular_aprobados(estudiantes):
 """
    Calcula los estudiante con calificación mayor o igual a 90.
    
    Parámetros:
    estudiantes (list): Contiene la información de los estudiantes.
    
    Retorna:
    list: Una lista de valores con los estudiantes que han obtenido 90 o más.
 """
 return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))

# Listado de alumnos
estudiantes = [
    {"nombre": "Daniel", "edad": 20, "calificacion": 85},
    {"nombre": "Jaime", "edad": 20, "calificacion": 92},
    {"nombre": "Pablo", "edad": 20, "calificacion": 88},
    {"nombre": "Luisa", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 20, "calificacion": 90}
]

# Ejemplo de la función
estudiantes_aprobados = calcular_aprobados(estudiantes)
print(estudiantes_aprobados)

#### 19. Crea una función lambda que filtre los números impares de una lista dada.
def numeros_impares(numeros):
 """
    Calcula los números impares.
    
    Parámetros:
    numeros (list): Contiene el listado de números.
    
    Retorna:
    list: Una lista con los valores impares.
 """
 return list(filter(lambda x: x % 2 != 0, numeros))

# Ejemplo de la función
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros_impares(numeros))

#### 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_enteros(elementos):
 """
    Obtiene de una lista de integer y string, solo valores int.
    
    Parámetros:
    elementos (list): Listado de elementos.
    
    Retorna:
    list: Una lista de valores que solo incluye valores int.
 """
 return list(filter(lambda x: isinstance(x, int), elementos))

# Ejemplo de la función
elementos = [0, 1, 2, 3, 4, "ejemplo", "int"]
print(filtrar_enteros(elementos))

#### 21. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def calcular_aprobados(estudiantes):
 """
    Calcula los estudiante con calificación mayor o igual a 90.
    
    Parámetros:
    estudiantes (list): Contiene la información de los estudiantes.
    
    Retorna:
    list: Una lista de valores con los estudiantes que han obtenido 90 o más.
 """
 return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))

# Listado de alumnos
estudiantes = [
    {"nombre": "Daniel", "edad": 20, "calificacion": 85},
    {"nombre": "Jaime", "edad": 20, "calificacion": 92},
    {"nombre": "Pablo", "edad": 20, "calificacion": 88},
    {"nombre": "Luisa", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 20, "calificacion": 90}
]

# Ejemplo de la función
estudiantes_aprobados = calcular_aprobados(estudiantes)
print(estudiantes_aprobados)

#### 22. Crea una función que calcule el cubo de un número dado mediante una función lambda
def calcular_cubo_numero(numero):
 """
    Calcula el cubo mediante la función lambda.
    
    Parámetros:
    numero (int): Número elegido.
    
    Retorna:
    int: Calcula el valor al cubo, del número elegido.
 """
 cubo = lambda x: x ** 3
 return cubo(numero)

# Ejemplo de la función
print(calcular_cubo_numero(5))

#### 23. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
# De nuevo importamos reduce desde functools, puesto que es una función que se almacena allí
from functools import reduce
def mult_numeros(numeros):
 """
    Calcula el producto total de los valores de la lista.
    
    Parámetros:
    numeros (list): Listado de valores.
    
    Retorna:
    int: Valor del producto de los números elegidos.
 """
 return reduce(lambda x, y: x * y, numeros)

# Ejemplo de la función
numeros = [1, 2, 3, 4]
print(mult_numeros(numeros))

#### 24. Concatena una lista de palabras. Usa la función reduce().
# Importamos reduce
from functools import reduce
def sumar_palabras(palabras):
 """
    Concatena una lista de palabras.
    
    Parámetros:
    palabras (list): Contiene el listado de palabras.
    
    Retorna:
    str: Un string con las palabras concatenadas.
 """
 return reduce(lambda x, y: x + y, palabras)

# Ejemplo de la función
palabras = ["Ejemplo", " ", "de", " ", "suma", " ", "de", " ", "palabras"]
print(sumar_palabras(palabras))

#### 25. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
# Importamos reduce
from functools import reduce
def resta_valores(valores):
 """
    Calcula la diferencia de los valores de la lista.
    
    Parámetros:
    valores (int): La diferencia de los valores.
    
    Retorna:
    int: El valor de la diferencia de los valores de la lista.
 """
 return reduce(lambda x, y: x - y, valores)

# Ejemplo de la función
valores = [10, 3, 2, 1]
print(resta_valores(valores))

#### 26. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def calcular_longitud(cadena):
 """
    Calcula los caracteres de una cadena de texto.
    
    Parámetros:
    cadena (list): Lista con los caracteres.
    
    Retorna:
    int: Devuelve el valor de la longitud de la cadena de texto.
 """
 return len(cadena)

# Ejemplo de la función
cadena = "Longitud de esta cadena"
print(calcular_longitud(cadena))

#### 27. Crea una función lambda que calcule el resto de la división entre dos números dados.
calcular_resto = lambda a, b: a % b
"""
    Calcula el resto de la división entre dos números.
    
    Parámetros:
    a (int): Primer número
    b (int): Segundo número
    
    Retorna:
    int: El resto de la división de los números.
 """

# Ejemplo de la función
print(calcular_resto(10,2))

#### 28. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista):
 """
    Calcula el promedio de una lista de números.
    
    Parámetros:
    lista (list): Listado de los números.
    
    Retorna:
    int: El promedio de la lista de los números.
 """
 if not lista:
   return 0
 return sum(lista) / len(lista)

# Ejemplo de la función
numeros = [1, 2, 3, 4]
print(calcular_promedio(numeros))

#### 29. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_elemento_repetido(lista):
    """
    Calcula el primer elemento duplicado.
    
    Parámetros:
    lista (list): Listado de elementos.
    
    Retorna:
    str: Devuelve el primer elemento duplicado.
    """
    vistos = set()
    for elemento in lista:
# Con esta condición devuelve el primer elemento repetido
        if elemento in vistos:
            return elemento
# Aquí verificamos si está duplicado, y si no lo está, lo devuelve a la lista y sigue buscando
        vistos.add(elemento)
# Aquí verificamos toda la lista y no ha encontrado ningún duplicado
    return print("❌ No se ha encontrado ningún elemento duplicado")

# Ejemplo de la función
lista = [0, 1, 2, 3, 0, 1, 4]
print(primer_elemento_repetido(lista))

#### 30. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar_caracteres(caracteres):
    """
    Transforma una variable en texto, y enmascara todos los caracteres excepto los últimos 4.
    
    Parámetros:
    caracteres (list): Contiene la cadena de caracteres.
    
    Retorna:
    str: Cadena de texto con los últimos 4 valores sin enmascarar.
    """
    caracteres_str = str(caracteres)
# Definimos que todos los caracteres sean # excepto los 4 últimos, y que a su vez muestre por pantalla los 4 últimos caracteres
    enmascarado = "#" * (len(caracteres_str) - 4) + caracteres_str[-4:]
    return enmascarado

# Ejemplo de la función
resultado = enmascarar_caracteres(123456700)
print(resultado)

#### 31. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def calcular_anagramas(x, y):
 """
    Calcula si dos palabras son anagramas.
    
    Parámetros:
    x (str): Primera palabra.
    y (str): Segunda palabra.
    
    Retorna:
    bool: Retorna el booleano para ver si son anagramas o no.
 """
 return sorted(x.lower()) == sorted(y.lower())

# Ejemplo de la función
resultado = calcular_anagramas("Daniel", "Pedro")
print(resultado)

#### 32. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre(nombres, nombre_a_buscar):
    """
    Busca si un nombre se encuentra en una lista de nombres.
    
    Parámetros:
    nombres (list): Contiene la lista de nombres.
    nombre_a_buscar (str): Nombre a buscar.
    
    Retorna:
    bool: Retorna un booleano que confirma si el nombre fue encontrado.
    """
    try:
        nombres = [nombre.strip() for nombre in nombres]
# Con esta condición nos aseguramos que el nombre existe en la lista
        if nombre_a_buscar in nombres:
            print(f"✅ El nombre '{nombre_a_buscar}' pertenece al listado.")
        else:
# Con esta otra condición definimos que el nombre no se encuentra en la lista
            raise ValueError(f"❌ El nombre '{nombre_a_buscar}' no pertenece al listado.")
# Except forma parte del try, si no se cumple ninguna condición muestra el error
    except ValueError as error:
        print(error)

# Ejemplo de la función
lista_nombres = ["Daniel", "Jaime", "Silvia"]
nombre_buscado = "Silvia"
buscar_nombre(lista_nombres, nombre_buscado)

#### 33. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_trabajador_y_puesto(nombre, empleados_puestos):
    """
    Busca si un trabajador se encuentra en la lista, y devuelve su puesto.
    
    Parámetros:
    nombre (str): Empleado a buscar.
    empleados_puestos (list): Listado de empleados.
    
    Retorna:
    bool: Retorna un booleano que confirme si el empleado trabaja ahí o no (y cual es su puesto).
    """
    if nombre in empleados_puestos:
        return f"✅ {nombre} trabaja como {empleados_puestos[nombre]} en la empresa"
    else:
        return f"❌ {nombre} no trabaja aquí."

# Ejemplo de la función
empleados_puestos = {
    "Pedro Rodriguez": "Abogado",
    "Pablo Paez": "Programador",
    "Fernando Rosales": "Contable",
    "Juan Martin": "Contable"
}

nombre_buscado = "Juan Martin"
resultado = buscar_trabajador_y_puesto(nombre_buscado, empleados_puestos)
print(resultado)

#### 34. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_elementos = lambda listaA, listaB: [listaA[i] + listaB[i] for i in range(len(listaA))]
"""
    Realiza la suma de los elementos de dos listas dadas.
    
    Parámetros:
    listaA (list): Primer listado.
    listaB (list): Segundo listado.
    
    Retorna:
    list: Una lista con la suma de las dos listas dadas.
"""
# Ejemplo de la función
listaA = [0, 1, 2, 3]
listaB = [1, 1, 4, 5]

resultado = sumar_elementos(listaA, listaB)
print(resultado)

#### 35. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#### Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de
# ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el
# número de ramas y las longitudes de las mismas.

#### Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.
# Creamos la clase arbol y definimos las funciones
class Arbol:
# Inicializamos que el arbol tiene un tronco y no tiene ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []
# Esta función aumenta el tronco +1
    def crecer_tronco(self):
        self.tronco += 1
# Esta función aumenta la rama con una longitud de 1
    def nueva_rama(self):
        self.ramas.append(1)
# Aumenta la longitud de todas las ramas en 1
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]
# Elimina la rama en la posición especificada
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("❌ Esta posición no existe, no se puede quitar la rama.")
# Información actual del arbol con las modificaciones
    def info_arbol(self):
        info = {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
        return info

# Ejemplo de uso
# Paso 1
arbol = Arbol()
# Paso 2
arbol.crecer_tronco()
# Paso 3
arbol.nueva_rama()
# Paso 4
arbol.crecer_ramas()
# Paso 5
arbol.nueva_rama()
arbol.nueva_rama()
# Paso 6
arbol.quitar_rama(2)
# Paso 7
informacion = arbol.info_arbol()
print(informacion)

#### 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#### Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta
# corriente mediante True y False.
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

#### Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Alicia".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".
# Creamos la clase y definimos las diferentes funciones
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
        
# Definimos la función de retirar saldo
    def retirar_dinero(self, cantidad):
# En esta condición, definimos que si la cantidad a retirar es mayor que el saldo, no se puede realizar la retirada
        if cantidad > self.saldo:
            raise ValueError(f"❌ No se puede retirar {cantidad} unidades: debido al saldo insuficiente.")
        self.saldo -= cantidad
        print(f"✅ {self.nombre} ha retirado {cantidad}. El saldo actual es: {self.saldo}")

# Definimos la función de transferencia
    def transferir_dinero(self, otra_persona, cantidad):
# En esta condición, definimos que si la cantidad a transferir es mayor que el saldo en la cuenta, no es posible realizar la transferencia
        if cantidad > otra_persona.saldo:
            raise ValueError(f"❌ No se puede transferir {cantidad} desde {otra_persona.nombre}: debido al saldo insuficiente.")
        otra_persona.saldo -= cantidad
        self.saldo += cantidad
        print(f"✅ {self.nombre} ha recibido una transferencia de {cantidad} desde {otra_persona.nombre}. El saldo actual es: {self.saldo}")

# Definimos la función agregar dinero, la cual añade dinero extra a la cantidad actual. Utilizamos self para distinguir atributos entre los parámetros
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"✅ {self.nombre} ha agregado {cantidad} unidades. Saldo actual: {self.saldo}")

# Caso de uso:
# Paso 1
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
# Paso 2
alicia.agregar_dinero(20)
# Paso 3
alicia.transferir_dinero(bob, 80)
# Paso 4
alicia.retirar_dinero(50)

#### 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
#### Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#### Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
# Definimos la función contar palabras, que se encarga de contar el número de veces que aparece cada palabra
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
# Definimos la condición de que si se repite la palabra se suma a contador (nuestro diccionario vacío)
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
# Definimos esta función para reemplazar la palabra original por otra nueva
def reemplazar_palabras(texto, palabra, palabra_nueva):
    return texto.replace(palabra, palabra_nueva)
# Definimos esta función para eliminar una palabra del texto
def eliminar_palabra(texto, palabra):
    return ' '.join([palabra for palabra in texto.split() if palabra != palabra])
# Definimos la función procesar_texto que almacena las otras tres funciones dentro. En caso de elegir una función concreta, se ejecuta cumpliendo su objetivo
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
# En esta condición, definimos que mínimo debe haber 2 palabras o más para poder reemplazar una por la otra
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("❌ Es necesario tener dos palabras para reemplazar una por otra.")
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
# En esta condición, definimos que mínimo debe haber una palabra para poder eliminarla
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("❌ Debe existir mínimo una palabra para poder eliminar.")
        palabra = args[0]
        return eliminar_palabra(texto, palabra)
    else:
        raise ValueError("❌ La opción no es válida. Selecciona una entre: contar, reemplazar y eliminar")

# Ejemplo de la función
texto = "en este fragmento hay que contar las veces que se repite cada palabra en este fragmento"
print(procesar_texto(texto, "contar"))

#### 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia(hora):
    """
    Calcula si es de noche, día o tarde según la hora proporcionada.
    
    Parámetros:
    hora (int): Hora del día elegida.
    
    Retorna:
    str: Un string indicando la hora del día en la que nos encontramos.
    """
    if 7 <= hora < 14:
        return "☀️ Actualmente es de Día"
    elif 14 <= hora < 21:
        return "🌄 Actualmente es de Tarde"
    elif (21 <= hora < 24) or (0 <= hora < 7):
        return "🌚 Actualmente es de Noche"
    else:
        return "❌ No existe esa hora"

# Ejemplo de la función
hora_elegida = 8
resultado = momento_del_dia(hora_elegida)
print(resultado)

#### 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
def calificacion_final(calificacion):
    """
    Calcula en texto la calificación de un alumno, en función de su calificación numérica.
    
    Parámetros:
    calificación (int): Calificación del alumno en número.
    
    Retorna:
    str: Calificación del alumno en texto.
    """
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <= calificacion <= 89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "❌ No existe esa calificación"

# Ejemplo de la función
calificacion_alumno = 66
resultado = calificacion_final(calificacion_alumno)
print(f"El alumno ha obtenido {calificacion_alumno} puntos, que equivale a un {resultado}")

#### 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area_figura(figura, datos):
    """
    Calcula el área de la función elegida.
    
    Parámetros:
    figura (str): Listado de las figuras disponibles.
    datos (int): Valores numéricos.
    
    Retorna:
    str: Cadena de texto con el área de la figura calculada.
    """
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura == "circulo":
        radio, = datos
        pi = 3.14
        return pi * radio ** 2
    else:
        return "❌ La figura seleccionada no puede ser calculada"

# Ejemplo de la función
figura_seleccionada = "rectangulo"
resultado = calcular_area_figura("rectangulo", (10,20))
print(f"Has elegido {figura_seleccionada} y su area es {resultado}")

#### 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o
# no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón
# de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el
# valor del cupón sea válido (es decir, mayor a cero). Por ejemplo,
# descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento
# aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else
# para llevar a cabo estas acciones en tu programa de Python.
# Definimos la función y pedimos al usuario que ingrese el precio original
def calcular_precio():
    precio_original = float(input("Ingresa el precio original del artículo: €"))
# Definimos si el usuario tiene o no cupón de descuento. Con strip eliminamos espacios en blanco y lower todo a minúsculas
    cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
# Inicializar el valor del descuento
    valor_descuento = 0
# Condición si el usuario tiene cupón
    if cupon == "sí":
        valor_cupon = float(input("Ingresa el valor del cupón de descuento (€): "))
# El cupón es válido si es mayor de 0
        if valor_cupon > 0:
            valor_descuento = valor_cupon
        elif valor_cupon <= 0:
            print("❌ Este cupón no es válido")
# En caso de que no haya cupón
    elif cupon == "no":
        print("❌ No hay cupón, el precio original se mantiene sin descuentos")
    else:
        print("❌ Respuesta no válida. Por favor, ingresa 'sí' o 'no'.")
# Precio final descontando el descuento del cupón
    precio_final = precio_original - valor_descuento
    
# Ejemplo de la función
    print(f"El precio final de la compra es: €{precio_final}")
calcular_precio()