"""
Pruebas unitarias para el módulo de Manipulación de Texto

Estas pruebas verifican el correcto funcionamiento de las clases POO
y funciones de compatibilidad para manipular y analizar cadenas de texto.
"""

import pytest
from ejercicio2_texto import (
    # Funciones de compatibilidad
    contar_palabras,
    invertir_texto,
    es_palindromo,
    contar_vocales,
    capitalizar_palabras,
    eliminar_espacios_extra,
    contar_caracteres_unicos,
    # Clases POO
    ManipuladorTexto,
    AnalizadorTexto,
    ProcesadorTextoCompleto
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


# ============================================================================
# PRUEBAS PARA CLASES POO
# ============================================================================

class TestManipuladorTexto:
    """Pruebas para la clase ManipuladorTexto"""
    
    def test_manipulador_creacion(self):
        """Debe crear un manipulador correctamente"""
        manip = ManipuladorTexto("Hola mundo")
        assert manip.texto == "Hola mundo"
    
    def test_manipulador_cambiar_texto(self):
        """Debe cambiar el texto correctamente"""
        manip = ManipuladorTexto("Hola")
        manip.texto = "Adiós"
        assert manip.texto == "Adiós"
    
    def test_manipulador_invertir(self):
        """Debe invertir el texto correctamente"""
        manip = ManipuladorTexto("Hola")
        assert manip.invertir() == "aloH"
    
    def test_manipulador_capitalizar_palabras(self):
        """Debe capitalizar palabras correctamente"""
        manip = ManipuladorTexto("hola mundo")
        assert manip.capitalizar_palabras() == "Hola Mundo"
    
    def test_manipulador_eliminar_espacios_extra(self):
        """Debe eliminar espacios extra correctamente"""
        manip = ManipuladorTexto("Hola    mundo")
        assert manip.eliminar_espacios_extra() == "Hola mundo"
    
    def test_manipulador_convertir_a_minusculas(self):
        """Debe convertir a minúsculas correctamente"""
        manip = ManipuladorTexto("HOLA MUNDO")
        assert manip.convertir_a_minusculas() == "hola mundo"
    
    def test_manipulador_convertir_a_mayusculas(self):
        """Debe convertir a mayúsculas correctamente"""
        manip = ManipuladorTexto("hola mundo")
        assert manip.convertir_a_mayusculas() == "HOLA MUNDO"
    
    def test_manipulador_reemplazar_palabra(self):
        """Debe reemplazar palabras correctamente"""
        manip = ManipuladorTexto("Hola mundo")
        assert manip.reemplazar_palabra("mundo", "Python") == "Hola Python"
    
    def test_manipulador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            ManipuladorTexto(123)
        with pytest.raises(TypeError):
            ManipuladorTexto("Hola").texto = 123
    
    def test_manipulador_str(self):
        """Debe tener representación en cadena correcta"""
        manip = ManipuladorTexto("Hola mundo")
        assert "ManipuladorTexto" in str(manip)


class TestAnalizadorTexto:
    """Pruebas para la clase AnalizadorTexto"""
    
    def test_analizador_creacion(self):
        """Debe crear un analizador correctamente"""
        analizador = AnalizadorTexto("Hola mundo")
        assert analizador.texto == "Hola mundo"
    
    def test_analizador_cambiar_texto(self):
        """Debe cambiar el texto correctamente"""
        analizador = AnalizadorTexto("Hola")
        analizador.texto = "Adiós"
        assert analizador.texto == "Adiós"
    
    def test_analizador_contar_palabras(self):
        """Debe contar palabras correctamente"""
        analizador = AnalizadorTexto("Hola mundo Python")
        assert analizador.contar_palabras() == 3
    
    def test_analizador_contar_vocales(self):
        """Debe contar vocales correctamente"""
        analizador = AnalizadorTexto("Hola mundo")
        assert analizador.contar_vocales() == 4  # o, a, u, o
    
    def test_analizador_contar_consonantes(self):
        """Debe contar consonantes correctamente"""
        analizador = AnalizadorTexto("Hola")
        assert analizador.contar_consonantes() == 2  # H, l
    
    def test_analizador_contar_caracteres_unicos(self):
        """Debe contar caracteres únicos correctamente"""
        analizador = AnalizadorTexto("a b c")
        assert analizador.contar_caracteres_unicos() == 5
    
    def test_analizador_es_palindromo(self):
        """Debe verificar palíndromos correctamente"""
        analizador = AnalizadorTexto("Anita lava la tina")
        assert analizador.es_palindromo() == True
        analizador.texto = "Hola mundo"
        assert analizador.es_palindromo() == False
    
    def test_analizador_obtener_estadisticas(self):
        """Debe obtener estadísticas correctamente"""
        analizador = AnalizadorTexto("Hola mundo")
        stats = analizador.obtener_estadisticas()
        assert stats['total_caracteres'] == 10  # "Hola mundo" tiene 10 caracteres
        assert stats['total_palabras'] == 2
        assert stats['total_vocales'] == 4
        assert 'total_consonantes' in stats
        assert 'caracteres_unicos' in stats
        assert 'es_palindromo' in stats
    
    def test_analizador_obtener_palabras_unicas(self):
        """Debe obtener palabras únicas correctamente"""
        analizador = AnalizadorTexto("Hola mundo hola")
        palabras_unicas = analizador.obtener_palabras_unicas()
        assert len(palabras_unicas) == 2
        assert "hola" in palabras_unicas
        assert "mundo" in palabras_unicas
    
    def test_analizador_contar_ocurrencias_palabra(self):
        """Debe contar ocurrencias de palabras correctamente"""
        analizador = AnalizadorTexto("Hola mundo hola")
        assert analizador.contar_ocurrencias_palabra("hola") == 2
        assert analizador.contar_ocurrencias_palabra("mundo") == 1
        assert analizador.contar_ocurrencias_palabra("python") == 0
    
    def test_analizador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            AnalizadorTexto(123)
        with pytest.raises(TypeError):
            AnalizadorTexto("Hola").texto = 123
        with pytest.raises(TypeError):
            AnalizadorTexto("Hola").contar_ocurrencias_palabra(123)
    
    def test_analizador_str(self):
        """Debe tener representación en cadena correcta"""
        analizador = AnalizadorTexto("Hola mundo")
        assert "AnalizadorTexto" in str(analizador)


class TestProcesadorTextoCompleto:
    """Pruebas para la clase ProcesadorTextoCompleto"""
    
    def test_procesador_creacion(self):
        """Debe crear un procesador correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        assert procesador.texto == "Hola mundo"
    
    def test_procesador_cambiar_texto(self):
        """Debe cambiar el texto correctamente"""
        procesador = ProcesadorTextoCompleto("Hola")
        procesador.texto = "Adiós"
        assert procesador.texto == "Adiós"
    
    def test_procesador_metodos_manipulacion(self):
        """Debe ejecutar métodos de manipulación correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        assert procesador.invertir() == "odnum aloH"
        assert procesador.capitalizar_palabras() == "Hola Mundo"
        assert procesador.eliminar_espacios_extra() == "Hola mundo"
        assert procesador.convertir_a_minusculas() == "hola mundo"
        assert procesador.convertir_a_mayusculas() == "HOLA MUNDO"
        assert procesador.reemplazar_palabra("mundo", "Python") == "Hola Python"
    
    def test_procesador_metodos_analisis(self):
        """Debe ejecutar métodos de análisis correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        assert procesador.contar_palabras() == 2
        assert procesador.contar_vocales() == 4
        assert procesador.contar_consonantes() == 5
        assert procesador.contar_caracteres_unicos() == 9
        assert procesador.es_palindromo() == False
    
    def test_procesador_obtener_estadisticas(self):
        """Debe obtener estadísticas correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        stats = procesador.obtener_estadisticas()
        assert isinstance(stats, dict)
        assert 'total_caracteres' in stats
        assert 'total_palabras' in stats
        assert 'total_vocales' in stats
        assert 'total_consonantes' in stats
        assert 'caracteres_unicos' in stats
        assert 'es_palindromo' in stats
    
    def test_procesador_obtener_palabras_unicas(self):
        """Debe obtener palabras únicas correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo hola")
        palabras_unicas = procesador.obtener_palabras_unicas()
        assert len(palabras_unicas) == 2
        assert "hola" in palabras_unicas
        assert "mundo" in palabras_unicas
    
    def test_procesador_contar_ocurrencias_palabra(self):
        """Debe contar ocurrencias de palabras correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo hola")
        assert procesador.contar_ocurrencias_palabra("hola") == 2
        assert procesador.contar_ocurrencias_palabra("mundo") == 1
    
    def test_procesador_generar_reporte_completo(self):
        """Debe generar reporte completo correctamente"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        reporte = procesador.generar_reporte_completo()
        assert isinstance(reporte, str)
        assert "REPORTE COMPLETO DEL TEXTO" in reporte
        assert "ESTADÍSTICAS" in reporte
        assert "TRANSFORMACIONES" in reporte
        assert "PALABRAS ÚNICAS" in reporte
        assert "Hola mundo" in reporte
    
    def test_procesador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            ProcesadorTextoCompleto(123)
        with pytest.raises(TypeError):
            ProcesadorTextoCompleto("Hola").texto = 123
    
    def test_procesador_str(self):
        """Debe tener representación en cadena correcta"""
        procesador = ProcesadorTextoCompleto("Hola mundo")
        assert "ProcesadorTextoCompleto" in str(procesador)


class TestIntegracionPOO:
    """Pruebas de integración entre las clases POO"""
    
    def test_manipulador_y_analizador_independientes(self):
        """Debe funcionar manipulador y analizador independientemente"""
        texto = "Hola mundo"
        manip = ManipuladorTexto(texto)
        analizador = AnalizadorTexto(texto)
        
        # Manipulador no afecta al analizador
        manip.invertir()
        assert analizador.contar_palabras() == 2
        
        # Analizador no afecta al manipulador
        analizador.es_palindromo()
        assert manip.texto == texto
    
    def test_procesador_completo_integra_funcionalidades(self):
        """Debe integrar todas las funcionalidades correctamente"""
        procesador = ProcesadorTextoCompleto("Anita lava la tina")
        
        # Verificar que tiene todas las funcionalidades
        assert procesador.contar_palabras() == 4
        assert procesador.es_palindromo() == True
        assert procesador.invertir() == "anit al aval atinA"
        assert procesador.capitalizar_palabras() == "Anita Lava La Tina"
        
        # Verificar que el reporte incluye todo
        reporte = procesador.generar_reporte_completo()
        assert "Anita lava la tina" in reporte
        assert "4" in reporte  # número de palabras
        assert "Sí" in reporte  # es palíndromo
    
    def test_cambio_de_texto_sincroniza_componentes(self):
        """Debe sincronizar cambios de texto en todos los componentes"""
        procesador = ProcesadorTextoCompleto("Texto inicial")
        assert procesador.contar_palabras() == 2
        
        procesador.texto = "Nuevo texto con más palabras"
        assert procesador.contar_palabras() == 5
        assert procesador.invertir() == "sarbalap sám noc otxet oveuN"  # Corregido: "más" con acento
