"""
Pruebas unitarias para el módulo de Geometría

Estas pruebas verifican el correcto funcionamiento de las clases POO
y funciones de compatibilidad para calcular áreas y perímetros de figuras geométricas.
"""

import pytest
import math
from ejercicio1_geometria import (
    # Funciones de compatibilidad
    area_rectangulo,
    area_circulo,
    area_triangulo,
    perimetro_rectangulo,
    perimetro_circulo,
    # Clases POO
    FiguraGeometrica,
    Rectangulo,
    Circulo,
    Triangulo,
    TrianguloCompleto
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


# ============================================================================
# PRUEBAS PARA CLASES POO
# ============================================================================

class TestFiguraGeometrica:
    """Pruebas para la clase abstracta FiguraGeometrica"""
    
    def test_figura_geometrica_no_instanciable(self):
        """No se debe poder instanciar FiguraGeometrica directamente"""
        with pytest.raises(TypeError):
            FiguraGeometrica()


class TestRectanguloPOO:
    """Pruebas para la clase Rectangulo"""
    
    def test_rectangulo_creacion(self):
        """Debe crear un rectángulo correctamente"""
        rect = Rectangulo(5, 3)
        assert rect.base == 5
        assert rect.altura == 3
    
    def test_rectangulo_area(self):
        """Debe calcular el área correctamente"""
        rect = Rectangulo(5, 3)
        assert rect.calcular_area() == 15
    
    def test_rectangulo_perimetro(self):
        """Debe calcular el perímetro correctamente"""
        rect = Rectangulo(5, 3)
        assert rect.calcular_perimetro() == 16
    
    def test_rectangulo_str(self):
        """Debe tener representación en cadena correcta"""
        rect = Rectangulo(5, 3)
        assert str(rect) == "Rectángulo(base=5, altura=3)"
    
    def test_rectangulo_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            Rectangulo("5", 3)
        with pytest.raises(TypeError):
            Rectangulo(5, "3")
    
    def test_rectangulo_validacion_negativo(self):
        """Debe validar valores negativos"""
        with pytest.raises(ValueError):
            Rectangulo(-5, 3)
        with pytest.raises(ValueError):
            Rectangulo(5, -3)


class TestCirculoPOO:
    """Pruebas para la clase Circulo"""
    
    def test_circulo_creacion(self):
        """Debe crear un círculo correctamente"""
        circ = Circulo(5)
        assert circ.radio == 5
    
    def test_circulo_area(self):
        """Debe calcular el área correctamente"""
        circ = Circulo(5)
        esperado = math.pi * 25
        assert abs(circ.calcular_area() - esperado) < 0.0001
    
    def test_circulo_perimetro(self):
        """Debe calcular el perímetro correctamente"""
        circ = Circulo(5)
        esperado = 2 * math.pi * 5
        assert abs(circ.calcular_perimetro() - esperado) < 0.0001
    
    def test_circulo_str(self):
        """Debe tener representación en cadena correcta"""
        circ = Circulo(5)
        assert str(circ) == "Círculo(radio=5)"
    
    def test_circulo_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            Circulo("5")
    
    def test_circulo_validacion_negativo(self):
        """Debe validar valores negativos"""
        with pytest.raises(ValueError):
            Circulo(-5)


class TestTrianguloPOO:
    """Pruebas para la clase Triangulo"""
    
    def test_triangulo_creacion(self):
        """Debe crear un triángulo correctamente"""
        tri = Triangulo(6, 4)
        assert tri.base == 6
        assert tri.altura == 4
    
    def test_triangulo_area(self):
        """Debe calcular el área correctamente"""
        tri = Triangulo(6, 4)
        assert tri.calcular_area() == 12
    
    def test_triangulo_perimetro_no_implementado(self):
        """Debe lanzar NotImplementedError para perímetro"""
        tri = Triangulo(6, 4)
        with pytest.raises(NotImplementedError):
            tri.calcular_perimetro()
    
    def test_triangulo_str(self):
        """Debe tener representación en cadena correcta"""
        tri = Triangulo(6, 4)
        assert str(tri) == "Triángulo(base=6, altura=4)"
    
    def test_triangulo_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            Triangulo("6", 4)
        with pytest.raises(TypeError):
            Triangulo(6, "4")
    
    def test_triangulo_validacion_negativo(self):
        """Debe validar valores negativos"""
        with pytest.raises(ValueError):
            Triangulo(-6, 4)
        with pytest.raises(ValueError):
            Triangulo(6, -4)


class TestTrianguloCompletoPOO:
    """Pruebas para la clase TrianguloCompleto"""
    
    def test_triangulo_completo_creacion(self):
        """Debe crear un triángulo completo correctamente"""
        tri = TrianguloCompleto(6, 4, 5, 7)
        assert tri.base == 6
        assert tri.altura == 4
        assert tri.lado1 == 5
        assert tri.lado2 == 7
    
    def test_triangulo_completo_area(self):
        """Debe calcular el área correctamente"""
        tri = TrianguloCompleto(6, 4, 5, 7)
        assert tri.calcular_area() == 12
    
    def test_triangulo_completo_perimetro(self):
        """Debe calcular el perímetro correctamente"""
        tri = TrianguloCompleto(6, 4, 5, 7)
        assert tri.calcular_perimetro() == 18  # 6 + 5 + 7
    
    def test_triangulo_completo_str(self):
        """Debe tener representación en cadena correcta"""
        tri = TrianguloCompleto(6, 4, 5, 7)
        assert str(tri) == "TriánguloCompleto(base=6, altura=4, lado1=5, lado2=7)"
    
    def test_triangulo_completo_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            TrianguloCompleto("6", 4, 5, 7)
        with pytest.raises(TypeError):
            TrianguloCompleto(6, 4, "5", 7)
    
    def test_triangulo_completo_validacion_negativo(self):
        """Debe validar valores negativos"""
        with pytest.raises(ValueError):
            TrianguloCompleto(-6, 4, 5, 7)
        with pytest.raises(ValueError):
            TrianguloCompleto(6, 4, -5, 7)


class TestPolimorfismo:
    """Pruebas para demostrar polimorfismo con las clases"""
    
    def test_polimorfismo_calcular_area(self):
        """Debe poder calcular área de diferentes figuras polimórficamente"""
        figuras = [
            Rectangulo(5, 3),
            Circulo(2),
            Triangulo(6, 4)
        ]
        
        areas = [fig.calcular_area() for fig in figuras]
        
        assert areas[0] == 15  # Rectángulo
        assert abs(areas[1] - math.pi * 4) < 0.0001  # Círculo
        assert areas[2] == 12  # Triángulo
    
    def test_polimorfismo_calcular_perimetro(self):
        """Debe poder calcular perímetro de figuras que lo soporten"""
        figuras = [
            Rectangulo(5, 3),
            Circulo(2),
            TrianguloCompleto(6, 4, 5, 7)
        ]
        
        perimetros = [fig.calcular_perimetro() for fig in figuras]
        
        assert perimetros[0] == 16  # Rectángulo
        assert abs(perimetros[1] - 2 * math.pi * 2) < 0.0001  # Círculo
        assert perimetros[2] == 18  # TriánguloCompleto
