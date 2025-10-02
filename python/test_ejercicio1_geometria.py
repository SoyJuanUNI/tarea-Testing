"""
Pruebas unitarias para el módulo de Geometría

Estas pruebas verifican el correcto funcionamiento de las funciones
para calcular áreas y perímetros de figuras geométricas.
"""

import pytest
import math
from ejercicio1_geometria import (
    area_rectangulo,
    area_circulo,
    area_triangulo,
    perimetro_rectangulo,
    perimetro_circulo
)


class TestAreaRectangulo:
    """Pruebas para la función area_rectangulo"""
    
    def test_area_rectangulo_positivos(self):
        """Debe calcular el área con números positivos"""
        assert area_rectangulo(5, 3) == 15
        assert area_rectangulo(10, 2) == 20
    
    def test_area_rectangulo_decimales(self):
        """Debe calcular el área con números decimales"""
        assert area_rectangulo(5.5, 2.0) == 11.0
    
    def test_area_rectangulo_cero(self):
        """Debe calcular el área cuando una dimensión es cero"""
        assert area_rectangulo(5, 0) == 0
        assert area_rectangulo(0, 3) == 0
    
    def test_area_rectangulo_tipo_invalido(self):
        """Debe lanzar TypeError con tipos inválidos"""
        with pytest.raises(TypeError):
            area_rectangulo("5", 3)
        with pytest.raises(TypeError):
            area_rectangulo(5, None)
    
    def test_area_rectangulo_negativo(self):
        """Debe lanzar ValueError con dimensiones negativas"""
        with pytest.raises(ValueError):
            area_rectangulo(-5, 3)
        with pytest.raises(ValueError):
            area_rectangulo(5, -3)


class TestAreaCirculo:
    """Pruebas para la función area_circulo"""
    
    def test_area_circulo_positivo(self):
        """Debe calcular el área correctamente"""
        resultado = area_circulo(5)
        esperado = math.pi * 25
        assert abs(resultado - esperado) < 0.0001
    
    def test_area_circulo_radio_uno(self):
        """Debe calcular el área con radio 1"""
        assert abs(area_circulo(1) - math.pi) < 0.0001
    
    def test_area_circulo_cero(self):
        """Debe retornar 0 con radio 0"""
        assert area_circulo(0) == 0
    
    def test_area_circulo_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            area_circulo("5")
    
    def test_area_circulo_negativo(self):
        """Debe lanzar ValueError con radio negativo"""
        with pytest.raises(ValueError):
            area_circulo(-5)


class TestAreaTriangulo:
    """Pruebas para la función area_triangulo"""
    
    def test_area_triangulo_positivos(self):
        """Debe calcular el área correctamente"""
        assert area_triangulo(6, 4) == 12
        assert area_triangulo(10, 5) == 25
    
    def test_area_triangulo_decimales(self):
        """Debe calcular el área con decimales"""
        assert area_triangulo(5.5, 4.0) == 11.0
    
    def test_area_triangulo_cero(self):
        """Debe retornar 0 cuando una dimensión es cero"""
        assert area_triangulo(5, 0) == 0
    
    def test_area_triangulo_tipo_invalido(self):
        """Debe lanzar TypeError con tipos inválidos"""
        with pytest.raises(TypeError):
            area_triangulo("6", 4)
    
    def test_area_triangulo_negativo(self):
        """Debe lanzar ValueError con dimensiones negativas"""
        with pytest.raises(ValueError):
            area_triangulo(-6, 4)


class TestPerimetroRectangulo:
    """Pruebas para la función perimetro_rectangulo"""
    
    def test_perimetro_rectangulo_positivos(self):
        """Debe calcular el perímetro correctamente"""
        assert perimetro_rectangulo(5, 3) == 16
        assert perimetro_rectangulo(10, 2) == 24
    
    def test_perimetro_rectangulo_cuadrado(self):
        """Debe calcular el perímetro de un cuadrado"""
        assert perimetro_rectangulo(5, 5) == 20
    
    def test_perimetro_rectangulo_tipo_invalido(self):
        """Debe lanzar TypeError con tipos inválidos"""
        with pytest.raises(TypeError):
            perimetro_rectangulo("5", 3)
    
    def test_perimetro_rectangulo_negativo(self):
        """Debe lanzar ValueError con dimensiones negativas"""
        with pytest.raises(ValueError):
            perimetro_rectangulo(-5, 3)


class TestPerimetroCirculo:
    """Pruebas para la función perimetro_circulo"""
    
    def test_perimetro_circulo_positivo(self):
        """Debe calcular el perímetro correctamente"""
        resultado = perimetro_circulo(5)
        esperado = 2 * math.pi * 5
        assert abs(resultado - esperado) < 0.0001
    
    def test_perimetro_circulo_radio_uno(self):
        """Debe calcular el perímetro con radio 1"""
        resultado = perimetro_circulo(1)
        esperado = 2 * math.pi
        assert abs(resultado - esperado) < 0.0001
    
    def test_perimetro_circulo_cero(self):
        """Debe retornar 0 con radio 0"""
        assert perimetro_circulo(0) == 0
    
    def test_perimetro_circulo_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            perimetro_circulo("5")
    
    def test_perimetro_circulo_negativo(self):
        """Debe lanzar ValueError con radio negativo"""
        with pytest.raises(ValueError):
            perimetro_circulo(-5)
