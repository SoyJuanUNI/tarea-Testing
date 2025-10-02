"""
Pruebas unitarias para el módulo de Manipulación de Texto

Estas pruebas verifican el correcto funcionamiento de las funciones
para manipular y analizar cadenas de texto.
"""

import pytest
from ejercicio2_texto import (
    contar_palabras,
    invertir_texto,
    es_palindromo,
    contar_vocales,
    capitalizar_palabras,
    eliminar_espacios_extra,
    contar_caracteres_unicos
)


class TestContarPalabras:
    """Pruebas para la función contar_palabras"""
    
    def test_contar_palabras_simple(self):
        """Debe contar palabras correctamente"""
        assert contar_palabras("Hola mundo") == 2
        assert contar_palabras("Una dos tres cuatro") == 4
    
    def test_contar_palabras_espacios_extra(self):
        """Debe contar palabras ignorando espacios extra"""
        assert contar_palabras("Hola    mundo") == 2
        assert contar_palabras("  Texto  con  espacios  ") == 3
    
    def test_contar_palabras_vacio(self):
        """Debe retornar 0 con texto vacío"""
        assert contar_palabras("") == 0
        assert contar_palabras("   ") == 0
    
    def test_contar_palabras_una_palabra(self):
        """Debe contar correctamente una sola palabra"""
        assert contar_palabras("Hola") == 1
    
    def test_contar_palabras_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            contar_palabras(123)
        with pytest.raises(TypeError):
            contar_palabras(None)


class TestInvertirTexto:
    """Pruebas para la función invertir_texto"""
    
    def test_invertir_texto_simple(self):
        """Debe invertir el texto correctamente"""
        assert invertir_texto("Hola") == "aloH"
        assert invertir_texto("Python") == "nohtyP"
    
    def test_invertir_texto_con_espacios(self):
        """Debe invertir texto con espacios"""
        assert invertir_texto("Hola mundo") == "odnum aloH"
    
    def test_invertir_texto_vacio(self):
        """Debe retornar cadena vacía con entrada vacía"""
        assert invertir_texto("") == ""
    
    def test_invertir_texto_palindromo(self):
        """Debe invertir correctamente un palíndromo"""
        assert invertir_texto("oso") == "oso"
    
    def test_invertir_texto_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            invertir_texto(123)


class TestEsPalindromo:
    """Pruebas para la función es_palindromo"""
    
    def test_es_palindromo_simple(self):
        """Debe identificar palíndromos simples"""
        assert es_palindromo("oso") == True
        assert es_palindromo("ana") == True
        assert es_palindromo("radar") == True
    
    def test_es_palindromo_con_mayusculas(self):
        """Debe ignorar mayúsculas"""
        assert es_palindromo("Oso") == True
        assert es_palindromo("Ana") == True
    
    def test_es_palindromo_con_espacios(self):
        """Debe ignorar espacios"""
        assert es_palindromo("anita lava la tina") == True
        assert es_palindromo("A man a plan a canal Panama") == True
    
    def test_no_es_palindromo(self):
        """Debe identificar cuando no es palíndromo"""
        assert es_palindromo("hola") == False
        assert es_palindromo("python") == False
    
    def test_es_palindromo_vacio(self):
        """Debe considerar cadena vacía como palíndromo"""
        assert es_palindromo("") == True
    
    def test_es_palindromo_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            es_palindromo(123)


class TestContarVocales:
    """Pruebas para la función contar_vocales"""
    
    def test_contar_vocales_simple(self):
        """Debe contar vocales correctamente"""
        assert contar_vocales("Hola") == 2
        assert contar_vocales("murcielago") == 5
    
    def test_contar_vocales_mayusculas(self):
        """Debe contar vocales mayúsculas"""
        assert contar_vocales("AEIOU") == 5
    
    def test_contar_vocales_mixtas(self):
        """Debe contar vocales mixtas"""
        assert contar_vocales("Educación") == 5
    
    def test_contar_vocales_sin_vocales(self):
        """Debe retornar 0 sin vocales"""
        assert contar_vocales("xyz") == 0
    
    def test_contar_vocales_vacio(self):
        """Debe retornar 0 con cadena vacía"""
        assert contar_vocales("") == 0
    
    def test_contar_vocales_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            contar_vocales(123)


class TestCapitalizarPalabras:
    """Pruebas para la función capitalizar_palabras"""
    
    def test_capitalizar_palabras_simple(self):
        """Debe capitalizar palabras correctamente"""
        assert capitalizar_palabras("hola mundo") == "Hola Mundo"
    
    def test_capitalizar_palabras_ya_capitalizado(self):
        """Debe mantener capitalización correcta"""
        assert capitalizar_palabras("Hola Mundo") == "Hola Mundo"
    
    def test_capitalizar_palabras_minusculas(self):
        """Debe capitalizar texto en minúsculas"""
        assert capitalizar_palabras("python es genial") == "Python Es Genial"
    
    def test_capitalizar_palabras_vacio(self):
        """Debe retornar cadena vacía con entrada vacía"""
        assert capitalizar_palabras("") == ""
    
    def test_capitalizar_palabras_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            capitalizar_palabras(123)


class TestEliminarEspaciosExtra:
    """Pruebas para la función eliminar_espacios_extra"""
    
    def test_eliminar_espacios_extra_multiples(self):
        """Debe eliminar espacios extra"""
        assert eliminar_espacios_extra("Hola    mundo") == "Hola mundo"
    
    def test_eliminar_espacios_extra_inicio_fin(self):
        """Debe eliminar espacios al inicio y fin"""
        assert eliminar_espacios_extra("  Hola mundo  ") == "Hola mundo"
    
    def test_eliminar_espacios_extra_normal(self):
        """Debe mantener texto sin espacios extra"""
        assert eliminar_espacios_extra("Hola mundo") == "Hola mundo"
    
    def test_eliminar_espacios_extra_vacio(self):
        """Debe retornar cadena vacía con solo espacios"""
        assert eliminar_espacios_extra("     ") == ""
    
    def test_eliminar_espacios_extra_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            eliminar_espacios_extra(123)


class TestContarCaracteresUnicos:
    """Pruebas para la función contar_caracteres_unicos"""
    
    def test_contar_caracteres_unicos_simple(self):
        """Debe contar caracteres únicos correctamente"""
        assert contar_caracteres_unicos("hola") == 4
        assert contar_caracteres_unicos("aaa") == 1
    
    def test_contar_caracteres_unicos_repetidos(self):
        """Debe contar solo caracteres únicos"""
        assert contar_caracteres_unicos("hello") == 4  # h, e, l, o
    
    def test_contar_caracteres_unicos_case_sensitive(self):
        """Debe distinguir mayúsculas y minúsculas"""
        assert contar_caracteres_unicos("Aa") == 2
    
    def test_contar_caracteres_unicos_con_espacios(self):
        """Debe contar espacios como caracteres"""
        assert contar_caracteres_unicos("a b c") == 5  # a, espacio, b, espacio, c
    
    def test_contar_caracteres_unicos_vacio(self):
        """Debe retornar 0 con cadena vacía"""
        assert contar_caracteres_unicos("") == 0
    
    def test_contar_caracteres_unicos_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            contar_caracteres_unicos(123)
