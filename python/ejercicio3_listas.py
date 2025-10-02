"""
Ejercicio 3: Operaciones con Listas

Este módulo implementa funciones para manipular y analizar listas.
Incluye operaciones de búsqueda, ordenamiento y transformación.
"""


def encontrar_minimo(lista):
    """
    Encuentra el valor mínimo en una lista de números.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float/int: El valor mínimo de la lista
    
    Raises:
        TypeError: Si no es una lista o contiene elementos no numéricos
        ValueError: Si la lista está vacía
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía")
    
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos los elementos deben ser números")
    
    return min(lista)


def ordenar_descendente(lista):
    """
    Ordena una lista de números en orden descendente.
    
    Args:
        lista (list): Lista de números a ordenar
    
    Returns:
        list: Nueva lista ordenada en orden descendente
    
    Raises:
        TypeError: Si no es una lista o contiene elementos no numéricos
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos los elementos deben ser números")
    
    return sorted(lista, reverse=True)


def filtrar_impares(lista):
    """
    Filtra los números impares de una lista.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        list: Nueva lista con solo los números impares
    
    Raises:
        TypeError: Si no es una lista o contiene elementos no numéricos
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos los elementos deben ser números")
    
    return [x for x in lista if x % 2 != 0]


def sumar_elementos(lista):
    """
    Suma todos los elementos de una lista de números.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float/int: La suma de todos los elementos
    
    Raises:
        TypeError: Si no es una lista o contiene elementos no numéricos
        ValueError: Si la lista está vacía
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía")
    
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos los elementos deben ser números")
    
    return sum(lista)


def buscar_elemento(lista, elemento):
    """
    Busca un elemento en una lista y retorna su índice.
    
    Args:
        lista (list): Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        int: El índice del elemento, o -1 si no se encuentra
    
    Raises:
        TypeError: Si no es una lista
    """
    if not isinstance(lista, list):
        raise TypeError("El primer parámetro debe ser una lista")
    
    try:
        return lista.index(elemento)
    except ValueError:
        return -1


def aplanar_lista(lista):
    """
    Aplana una lista de listas en una sola lista.
    
    Args:
        lista (list): Lista de listas
    
    Returns:
        list: Lista aplanada
    
    Raises:
        TypeError: Si no es una lista
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(elemento)
        else:
            resultado.append(elemento)
    
    return resultado


def obtener_unicos_ordenados(lista):
    """
    Obtiene los elementos únicos de una lista y los retorna ordenados.
    
    Args:
        lista (list): Lista con posibles duplicados
    
    Returns:
        list: Lista con elementos únicos ordenados
    
    Raises:
        TypeError: Si no es una lista o contiene elementos no comparables
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro debe ser una lista")
    
    try:
        return sorted(set(lista))
    except TypeError:
        raise TypeError("Los elementos deben ser comparables")


def dividir_lista(lista, tamaño):
    """
    Divide una lista en sublistas de un tamaño específico.
    
    Args:
        lista (list): Lista a dividir
        tamaño (int): Tamaño de cada sublista
    
    Returns:
        list: Lista de sublistas
    
    Raises:
        TypeError: Si los parámetros no son del tipo correcto
        ValueError: Si el tamaño es menor o igual a 0
    """
    if not isinstance(lista, list):
        raise TypeError("El primer parámetro debe ser una lista")
    
    if not isinstance(tamaño, int):
        raise TypeError("El tamaño debe ser un entero")
    
    if tamaño <= 0:
        raise ValueError("El tamaño debe ser mayor que 0")
    
    return [lista[i:i + tamaño] for i in range(0, len(lista), tamaño)]
