"""
Ejercicio 1: Calculadora de Figuras Geométricas

Este módulo implementa clases para calcular áreas y perímetros
de diferentes figuras geométricas básicas usando Programación Orientada a Objetos.
"""

import math
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """
    Clase abstracta base para todas las figuras geométricas.
    
    Define la interfaz común que deben implementar todas las figuras.
    """
    
    @abstractmethod
    def calcular_area(self):
        """
        Calcula el área de la figura geométrica.
        
        Returns:
            float: El área de la figura
        """
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """
        Calcula el perímetro de la figura geométrica.
        
        Returns:
            float: El perímetro de la figura
        """
        pass
    
    def _validar_numero(self, valor, nombre_parametro):
        """
        Valida que un valor sea un número positivo.
        
        Args:
            valor: El valor a validar
            nombre_parametro (str): Nombre del parámetro para mensajes de error
        
        Raises:
            TypeError: Si el valor no es un número
            ValueError: Si el valor es negativo
        """
        if not isinstance(valor, (int, float)):
            raise TypeError(f"{nombre_parametro} debe ser un número")
        
        if valor < 0:
            raise ValueError(f"{nombre_parametro} no puede ser negativo")


class Rectangulo(FiguraGeometrica):
    """
    Clase que representa un rectángulo.
    
    Attributes:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    """
    
    def __init__(self, base, altura):
        """
        Inicializa un rectángulo con base y altura.
        
        Args:
            base (float): La base del rectángulo
            altura (float): La altura del rectángulo
        
        Raises:
            TypeError: Si los parámetros no son números
            ValueError: Si los parámetros son negativos
        """
        self._validar_numero(base, "La base")
        self._validar_numero(altura, "La altura")
        
        self._base = base
        self._altura = altura
    
    @property
    def base(self):
        """Obtiene la base del rectángulo."""
        return self._base
    
    @property
    def altura(self):
        """Obtiene la altura del rectángulo."""
        return self._altura
    
    def calcular_area(self):
        """
        Calcula el área del rectángulo.
        
        Returns:
            float: El área del rectángulo
        """
        return self._base * self._altura
    
    def calcular_perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        
        Returns:
            float: El perímetro del rectángulo
        """
        return 2 * (self._base + self._altura)
    
    def __str__(self):
        """Representación en cadena del rectángulo."""
        return f"Rectángulo(base={self._base}, altura={self._altura})"


class Circulo(FiguraGeometrica):
    """
    Clase que representa un círculo.
    
    Attributes:
        radio (float): El radio del círculo
    """
    
    def __init__(self, radio):
        """
        Inicializa un círculo con radio.
        
        Args:
            radio (float): El radio del círculo
        
        Raises:
            TypeError: Si el radio no es un número
            ValueError: Si el radio es negativo
        """
        self._validar_numero(radio, "El radio")
        self._radio = radio
    
    @property
    def radio(self):
        """Obtiene el radio del círculo."""
        return self._radio
    
    def calcular_area(self):
        """
        Calcula el área del círculo.
        
        Returns:
            float: El área del círculo
        """
        return math.pi * self._radio ** 2
    
    def calcular_perimetro(self):
        """
        Calcula el perímetro (circunferencia) del círculo.
        
        Returns:
            float: El perímetro del círculo
        """
        return 2 * math.pi * self._radio
    
    def __str__(self):
        """Representación en cadena del círculo."""
        return f"Círculo(radio={self._radio})"


class Triangulo(FiguraGeometrica):
    """
    Clase que representa un triángulo.
    
    Attributes:
        base (float): La base del triángulo
        altura (float): La altura del triángulo
    """
    
    def __init__(self, base, altura):
        """
        Inicializa un triángulo con base y altura.
        
        Args:
            base (float): La base del triángulo
            altura (float): La altura del triángulo
        
        Raises:
            TypeError: Si los parámetros no son números
            ValueError: Si los parámetros son negativos
        """
        self._validar_numero(base, "La base")
        self._validar_numero(altura, "La altura")
        
        self._base = base
        self._altura = altura
    
    @property
    def base(self):
        """Obtiene la base del triángulo."""
        return self._base
    
    @property
    def altura(self):
        """Obtiene la altura del triángulo."""
        return self._altura
    
    def calcular_area(self):
        """
        Calcula el área del triángulo.
        
        Returns:
            float: El área del triángulo
        """
        return (self._base * self._altura) / 2
    
    def calcular_perimetro(self):
        """
        Calcula el perímetro del triángulo.
        Nota: Para un triángulo genérico, necesitaríamos los tres lados.
        Este método lanza NotImplementedError para indicar que se necesita más información.
        
        Raises:
            NotImplementedError: Se necesita más información para calcular el perímetro
        """
        raise NotImplementedError(
            "Para calcular el perímetro de un triángulo se necesitan los tres lados. "
            "Use TrianguloCompleto en su lugar."
        )
    
    def __str__(self):
        """Representación en cadena del triángulo."""
        return f"Triángulo(base={self._base}, altura={self._altura})"


class TrianguloCompleto(Triangulo):
    """
    Clase que representa un triángulo con información completa para calcular perímetro.
    
    Attributes:
        base (float): La base del triángulo
        altura (float): La altura del triángulo
        lado1 (float): Primer lado del triángulo
        lado2 (float): Segundo lado del triángulo
    """
    
    def __init__(self, base, altura, lado1, lado2):
        """
        Inicializa un triángulo completo con base, altura y lados.
        
        Args:
            base (float): La base del triángulo
            altura (float): La altura del triángulo
            lado1 (float): Primer lado del triángulo
            lado2 (float): Segundo lado del triángulo
        
        Raises:
            TypeError: Si los parámetros no son números
            ValueError: Si los parámetros son negativos
        """
        super().__init__(base, altura)
        self._validar_numero(lado1, "El lado1")
        self._validar_numero(lado2, "El lado2")
        
        self._lado1 = lado1
        self._lado2 = lado2
    
    @property
    def lado1(self):
        """Obtiene el primer lado del triángulo."""
        return self._lado1
    
    @property
    def lado2(self):
        """Obtiene el segundo lado del triángulo."""
        return self._lado2
    
    def calcular_perimetro(self):
        """
        Calcula el perímetro del triángulo.
        
        Returns:
            float: El perímetro del triángulo
        """
        return self._base + self._lado1 + self._lado2
    
    def __str__(self):
        """Representación en cadena del triángulo completo."""
        return f"TriánguloCompleto(base={self._base}, altura={self._altura}, lado1={self._lado1}, lado2={self._lado2})"


# Funciones de compatibilidad para mantener la interfaz anterior
def area_rectangulo(base, altura):
    """
    Función de compatibilidad para calcular el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    """
    rectangulo = Rectangulo(base, altura)
    return rectangulo.calcular_area()


def area_circulo(radio):
    """
    Función de compatibilidad para calcular el área de un círculo.
    
    Args:
        radio (float): El radio del círculo
    
    Returns:
        float: El área del círculo
    """
    circulo = Circulo(radio)
    return circulo.calcular_area()


def area_triangulo(base, altura):
    """
    Función de compatibilidad para calcular el área de un triángulo.
    
    Args:
        base (float): La base del triángulo
        altura (float): La altura del triángulo
    
    Returns:
        float: El área del triángulo
    """
    triangulo = Triangulo(base, altura)
    return triangulo.calcular_area()


def perimetro_rectangulo(base, altura):
    """
    Función de compatibilidad para calcular el perímetro de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El perímetro del rectángulo
    """
    rectangulo = Rectangulo(base, altura)
    return rectangulo.calcular_perimetro()


def perimetro_circulo(radio):
    """
    Función de compatibilidad para calcular el perímetro de un círculo.
    
    Args:
        radio (float): El radio del círculo
    
    Returns:
        float: El perímetro del círculo
    """
    circulo = Circulo(radio)
    return circulo.calcular_perimetro()
