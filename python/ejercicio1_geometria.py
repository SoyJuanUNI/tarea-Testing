"""
Ejercicio 1: Calculadora de Figuras Geométricas

Este módulo implementa funciones para calcular áreas y perímetros
de diferentes figuras geométricas básicas.
"""

import math


def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    
    Raises:
        TypeError: Si los parámetros no son números
        ValueError: Si los parámetros son negativos
    """
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Los parámetros deben ser números")
    
    if base < 0 or altura < 0:
        raise ValueError("Las dimensiones no pueden ser negativas")
    
    return base * altura


def area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): El radio del círculo
    
    Returns:
        float: El área del círculo
    
    Raises:
        TypeError: Si el parámetro no es un número
        ValueError: Si el radio es negativo
    """
    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número")
    
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    
    return math.pi * radio ** 2


def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    
    Args:
        base (float): La base del triángulo
        altura (float): La altura del triángulo
    
    Returns:
        float: El área del triángulo
    
    Raises:
        TypeError: Si los parámetros no son números
        ValueError: Si los parámetros son negativos
    """
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Los parámetros deben ser números")
    
    if base < 0 or altura < 0:
        raise ValueError("Las dimensiones no pueden ser negativas")
    
    return (base * altura) / 2


def perimetro_rectangulo(base, altura):
    """
    Calcula el perímetro de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El perímetro del rectángulo
    
    Raises:
        TypeError: Si los parámetros no son números
        ValueError: Si los parámetros son negativos
    """
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Los parámetros deben ser números")
    
    if base < 0 or altura < 0:
        raise ValueError("Las dimensiones no pueden ser negativas")
    
    return 2 * (base + altura)


def perimetro_circulo(radio):
    """
    Calcula el perímetro (circunferencia) de un círculo.
    
    Args:
        radio (float): El radio del círculo
    
    Returns:
        float: El perímetro del círculo
    
    Raises:
        TypeError: Si el parámetro no es un número
        ValueError: Si el radio es negativo
    """
    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número")
    
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    
    return 2 * math.pi * radio
