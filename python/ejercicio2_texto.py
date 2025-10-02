"""
Ejercicio 2: Manipulación de Texto

Este módulo implementa funciones para manipular y analizar cadenas de texto.
Incluye operaciones como contar palabras, invertir texto y verificar palíndromos.
"""


def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: El número de palabras en el texto
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    if not texto.strip():
        return 0
    
    return len(texto.split())


def invertir_texto(texto):
    """
    Invierte el orden de los caracteres en un texto.
    
    Args:
        texto (str): El texto a invertir
    
    Returns:
        str: El texto invertido
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    return texto[::-1]


def es_palindromo(texto):
    """
    Verifica si un texto es un palíndromo (se lee igual al derecho y al revés).
    Ignora espacios, mayúsculas y signos de puntuación.
    
    Args:
        texto (str): El texto a verificar
    
    Returns:
        bool: True si es palíndromo, False en caso contrario
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    # Limpiar el texto: solo letras y números, en minúsculas
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    
    return texto_limpio == texto_limpio[::-1]


def contar_vocales(texto):
    """
    Cuenta el número de vocales en un texto.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: El número de vocales en el texto
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return sum(1 for c in texto if c in vocales)


def capitalizar_palabras(texto):
    """
    Capitaliza la primera letra de cada palabra en un texto.
    
    Args:
        texto (str): El texto a capitalizar
    
    Returns:
        str: El texto con cada palabra capitalizada
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    return texto.title()


def eliminar_espacios_extra(texto):
    """
    Elimina espacios extra del texto, dejando solo un espacio entre palabras.
    
    Args:
        texto (str): El texto a limpiar
    
    Returns:
        str: El texto sin espacios extra
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    return ' '.join(texto.split())


def contar_caracteres_unicos(texto):
    """
    Cuenta el número de caracteres únicos en un texto (case-sensitive).
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: El número de caracteres únicos
    
    Raises:
        TypeError: Si el parámetro no es una cadena
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro debe ser una cadena de texto")
    
    return len(set(texto))
