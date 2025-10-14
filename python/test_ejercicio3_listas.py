"""
Pruebas unitarias para el módulo de Operaciones con Listas

Estas pruebas verifican el correcto funcionamiento de las clases POO
y funciones de compatibilidad para manipular y analizar listas.
"""

import pytest
from ejercicio3_listas import (
    # Funciones de compatibilidad
    encontrar_minimo,
    ordenar_descendente,
    filtrar_impares,
    sumar_elementos,
    buscar_elemento,
    aplanar_lista,
    obtener_unicos_ordenados,
    dividir_lista,
    # Clases POO
    ManipuladorListas,
    AnalizadorListas,
    ProcesadorListasCompleto
)


class TestEncontrarMinimo:
    """Pruebas para la función encontrar_minimo"""
    
    def test_encontrar_minimo_positivos(self):
        """Debe encontrar el mínimo en números positivos"""
        assert encontrar_minimo([5, 2, 8, 1, 9]) == 1
    
    def test_encontrar_minimo_negativos(self):
        """Debe encontrar el mínimo con números negativos"""
        assert encontrar_minimo([-5, -2, -8, -1]) == -8
    
    def test_encontrar_minimo_mixtos(self):
        """Debe encontrar el mínimo con números mixtos"""
        assert encontrar_minimo([-5, 10, 3, -2]) == -5
    
    def test_encontrar_minimo_un_elemento(self):
        """Debe funcionar con un solo elemento"""
        assert encontrar_minimo([42]) == 42
    
    def test_encontrar_minimo_lista_vacia(self):
        """Debe lanzar ValueError con lista vacía"""
        with pytest.raises(ValueError):
            encontrar_minimo([])
    
    def test_encontrar_minimo_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            encontrar_minimo("no es lista")
        with pytest.raises(TypeError):
            encontrar_minimo([1, 2, "3"])


class TestOrdenarDescendente:
    """Pruebas para la función ordenar_descendente"""
    
    def test_ordenar_descendente_desordenado(self):
        """Debe ordenar lista desordenada"""
        assert ordenar_descendente([3, 1, 4, 1, 5]) == [5, 4, 3, 1, 1]
    
    def test_ordenar_descendente_ya_ordenado(self):
        """Debe mantener orden descendente"""
        assert ordenar_descendente([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    
    def test_ordenar_descendente_negativos(self):
        """Debe ordenar números negativos"""
        assert ordenar_descendente([-1, -5, -3]) == [-1, -3, -5]
    
    def test_ordenar_descendente_vacio(self):
        """Debe retornar lista vacía con entrada vacía"""
        assert ordenar_descendente([]) == []
    
    def test_ordenar_descendente_no_modifica_original(self):
        """No debe modificar la lista original"""
        original = [3, 1, 4]
        resultado = ordenar_descendente(original)
        assert original == [3, 1, 4]
        assert resultado == [4, 3, 1]
    
    def test_ordenar_descendente_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            ordenar_descendente([1, 2, "3"])


class TestFiltrarImpares:
    """Pruebas para la función filtrar_impares"""
    
    def test_filtrar_impares_mixtos(self):
        """Debe filtrar solo impares"""
        assert filtrar_impares([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    
    def test_filtrar_impares_solo_pares(self):
        """Debe retornar lista vacía si solo hay pares"""
        assert filtrar_impares([2, 4, 6, 8]) == []
    
    def test_filtrar_impares_solo_impares(self):
        """Debe retornar todos si solo hay impares"""
        assert filtrar_impares([1, 3, 5, 7]) == [1, 3, 5, 7]
    
    def test_filtrar_impares_negativos(self):
        """Debe filtrar impares negativos"""
        assert filtrar_impares([-3, -2, -1, 0, 1]) == [-3, -1, 1]
    
    def test_filtrar_impares_vacio(self):
        """Debe retornar lista vacía con entrada vacía"""
        assert filtrar_impares([]) == []
    
    def test_filtrar_impares_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            filtrar_impares([1, 2, "3"])


class TestSumarElementos:
    """Pruebas para la función sumar_elementos"""
    
    def test_sumar_elementos_positivos(self):
        """Debe sumar elementos positivos"""
        assert sumar_elementos([1, 2, 3, 4, 5]) == 15
    
    def test_sumar_elementos_negativos(self):
        """Debe sumar elementos negativos"""
        assert sumar_elementos([-1, -2, -3]) == -6
    
    def test_sumar_elementos_mixtos(self):
        """Debe sumar elementos mixtos"""
        assert sumar_elementos([10, -5, 3, -2]) == 6
    
    def test_sumar_elementos_un_elemento(self):
        """Debe funcionar con un solo elemento"""
        assert sumar_elementos([42]) == 42
    
    def test_sumar_elementos_lista_vacia(self):
        """Debe lanzar ValueError con lista vacía"""
        with pytest.raises(ValueError):
            sumar_elementos([])
    
    def test_sumar_elementos_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            sumar_elementos([1, 2, "3"])


class TestBuscarElemento:
    """Pruebas para la función buscar_elemento"""
    
    def test_buscar_elemento_encontrado(self):
        """Debe encontrar el índice del elemento"""
        assert buscar_elemento([1, 2, 3, 4, 5], 3) == 2
    
    def test_buscar_elemento_no_encontrado(self):
        """Debe retornar -1 si no encuentra el elemento"""
        assert buscar_elemento([1, 2, 3], 5) == -1
    
    def test_buscar_elemento_primer_indice(self):
        """Debe retornar el primer índice si hay duplicados"""
        assert buscar_elemento([1, 2, 3, 2, 4], 2) == 1
    
    def test_buscar_elemento_strings(self):
        """Debe funcionar con strings"""
        assert buscar_elemento(['a', 'b', 'c'], 'b') == 1
    
    def test_buscar_elemento_lista_vacia(self):
        """Debe retornar -1 con lista vacía"""
        assert buscar_elemento([], 1) == -1
    
    def test_buscar_elemento_tipo_invalido(self):
        """Debe lanzar TypeError si no es lista"""
        with pytest.raises(TypeError):
            buscar_elemento("no es lista", 1)


class TestAplanarLista:
    """Pruebas para la función aplanar_lista"""
    
    def test_aplanar_lista_simple(self):
        """Debe aplanar lista de listas"""
        assert aplanar_lista([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    
    def test_aplanar_lista_mixta(self):
        """Debe aplanar lista mixta"""
        assert aplanar_lista([1, [2, 3], 4, [5]]) == [1, 2, 3, 4, 5]
    
    def test_aplanar_lista_vacia(self):
        """Debe retornar lista vacía con entrada vacía"""
        assert aplanar_lista([]) == []
    
    def test_aplanar_lista_sin_sublistas(self):
        """Debe retornar igual si no hay sublistas"""
        assert aplanar_lista([1, 2, 3]) == [1, 2, 3]
    
    def test_aplanar_lista_sublistas_vacias(self):
        """Debe manejar sublistas vacías"""
        assert aplanar_lista([1, [], 2, [], 3]) == [1, 2, 3]
    
    def test_aplanar_lista_tipo_invalido(self):
        """Debe lanzar TypeError si no es lista"""
        with pytest.raises(TypeError):
            aplanar_lista("no es lista")


class TestObtenerUnicosOrdenados:
    """Pruebas para la función obtener_unicos_ordenados"""
    
    def test_obtener_unicos_ordenados_con_duplicados(self):
        """Debe eliminar duplicados y ordenar"""
        assert obtener_unicos_ordenados([3, 1, 2, 1, 3, 2]) == [1, 2, 3]
    
    def test_obtener_unicos_ordenados_sin_duplicados(self):
        """Debe ordenar si no hay duplicados"""
        assert obtener_unicos_ordenados([3, 1, 4, 2]) == [1, 2, 3, 4]
    
    def test_obtener_unicos_ordenados_strings(self):
        """Debe funcionar con strings"""
        assert obtener_unicos_ordenados(['c', 'a', 'b', 'a']) == ['a', 'b', 'c']
    
    def test_obtener_unicos_ordenados_vacio(self):
        """Debe retornar lista vacía con entrada vacía"""
        assert obtener_unicos_ordenados([]) == []
    
    def test_obtener_unicos_ordenados_tipo_invalido(self):
        """Debe lanzar TypeError si no es lista"""
        with pytest.raises(TypeError):
            obtener_unicos_ordenados("no es lista")


class TestDividirLista:
    """Pruebas para la función dividir_lista"""
    
    def test_dividir_lista_exacto(self):
        """Debe dividir lista en partes exactas"""
        assert dividir_lista([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]
    
    def test_dividir_lista_inexacto(self):
        """Debe dividir lista con última parte más pequeña"""
        assert dividir_lista([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    
    def test_dividir_lista_tamano_mayor(self):
        """Debe retornar lista completa si tamaño es mayor"""
        assert dividir_lista([1, 2, 3], 5) == [[1, 2, 3]]
    
    def test_dividir_lista_vacia(self):
        """Debe retornar lista vacía con entrada vacía"""
        assert dividir_lista([], 2) == []
    
    def test_dividir_lista_tamano_invalido(self):
        """Debe lanzar ValueError con tamaño inválido"""
        with pytest.raises(ValueError):
            dividir_lista([1, 2, 3], 0)
        with pytest.raises(ValueError):
            dividir_lista([1, 2, 3], -1)
    
    def test_dividir_lista_tipo_invalido(self):
        """Debe lanzar TypeError con tipo inválido"""
        with pytest.raises(TypeError):
            dividir_lista("no es lista", 2)
        with pytest.raises(TypeError):
            dividir_lista([1, 2, 3], "2")


# ============================================================================
# PRUEBAS PARA CLASES POO
# ============================================================================

class TestManipuladorListas:
    """Pruebas para la clase ManipuladorListas"""
    
    def test_manipulador_creacion(self):
        """Debe crear un manipulador correctamente"""
        manip = ManipuladorListas([1, 2, 3])
        assert manip.lista == [1, 2, 3]
    
    def test_manipulador_cambiar_lista(self):
        """Debe cambiar la lista correctamente"""
        manip = ManipuladorListas([1, 2, 3])
        manip.lista = [4, 5, 6]
        assert manip.lista == [4, 5, 6]
    
    def test_manipulador_ordenar_descendente(self):
        """Debe ordenar descendente correctamente"""
        manip = ManipuladorListas([3, 1, 4, 2])
        assert manip.ordenar_descendente() == [4, 3, 2, 1]
    
    def test_manipulador_ordenar_ascendente(self):
        """Debe ordenar ascendente correctamente"""
        manip = ManipuladorListas([3, 1, 4, 2])
        assert manip.ordenar_ascendente() == [1, 2, 3, 4]
    
    def test_manipulador_filtrar_impares(self):
        """Debe filtrar impares correctamente"""
        manip = ManipuladorListas([1, 2, 3, 4, 5])
        assert manip.filtrar_impares() == [1, 3, 5]
    
    def test_manipulador_filtrar_pares(self):
        """Debe filtrar pares correctamente"""
        manip = ManipuladorListas([1, 2, 3, 4, 5])
        assert manip.filtrar_pares() == [2, 4]
    
    def test_manipulador_filtrar_por_condicion(self):
        """Debe filtrar por condición correctamente"""
        manip = ManipuladorListas([1, 2, 3, 4, 5])
        assert manip.filtrar_por_condicion(lambda x: x > 3) == [4, 5]
    
    def test_manipulador_aplanar(self):
        """Debe aplanar correctamente"""
        manip = ManipuladorListas([[1, 2], [3, 4], 5])
        assert manip.aplanar() == [1, 2, 3, 4, 5]
    
    def test_manipulador_dividir(self):
        """Debe dividir correctamente"""
        manip = ManipuladorListas([1, 2, 3, 4, 5, 6])
        assert manip.dividir(2) == [[1, 2], [3, 4], [5, 6]]
    
    def test_manipulador_obtener_unicos_ordenados(self):
        """Debe obtener únicos ordenados correctamente"""
        manip = ManipuladorListas([3, 1, 3, 2, 1])
        assert manip.obtener_unicos_ordenados() == [1, 2, 3]
    
    def test_manipulador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            ManipuladorListas("no es lista")
        with pytest.raises(TypeError):
            ManipuladorListas([1, 2, 3]).lista = "no es lista"
    
    def test_manipulador_str(self):
        """Debe tener representación en cadena correcta"""
        manip = ManipuladorListas([1, 2, 3])
        assert "ManipuladorListas" in str(manip)


class TestAnalizadorListas:
    """Pruebas para la clase AnalizadorListas"""
    
    def test_analizador_creacion(self):
        """Debe crear un analizador correctamente"""
        analizador = AnalizadorListas([1, 2, 3])
        assert analizador.lista == [1, 2, 3]
    
    def test_analizador_cambiar_lista(self):
        """Debe cambiar la lista correctamente"""
        analizador = AnalizadorListas([1, 2, 3])
        analizador.lista = [4, 5, 6]
        assert analizador.lista == [4, 5, 6]
    
    def test_analizador_encontrar_minimo(self):
        """Debe encontrar el mínimo correctamente"""
        analizador = AnalizadorListas([5, 2, 8, 1, 9])
        assert analizador.encontrar_minimo() == 1
    
    def test_analizador_encontrar_maximo(self):
        """Debe encontrar el máximo correctamente"""
        analizador = AnalizadorListas([5, 2, 8, 1, 9])
        assert analizador.encontrar_maximo() == 9
    
    def test_analizador_sumar_elementos(self):
        """Debe sumar elementos correctamente"""
        analizador = AnalizadorListas([1, 2, 3, 4])
        assert analizador.sumar_elementos() == 10
    
    def test_analizador_buscar_elemento(self):
        """Debe buscar elemento correctamente"""
        analizador = AnalizadorListas([1, 2, 3, 4, 5])
        assert analizador.buscar_elemento(3) == 2
        assert analizador.buscar_elemento(6) == -1
    
    def test_analizador_contar_ocurrencias(self):
        """Debe contar ocurrencias correctamente"""
        analizador = AnalizadorListas([1, 2, 2, 3, 2])
        assert analizador.contar_ocurrencias(2) == 3
        assert analizador.contar_ocurrencias(5) == 0
    
    def test_analizador_obtener_estadisticas_numericas(self):
        """Debe obtener estadísticas numéricas correctamente"""
        analizador = AnalizadorListas([1, 2, 3, 4, 5])
        stats = analizador.obtener_estadisticas_numericas()
        assert stats['minimo'] == 1
        assert stats['maximo'] == 5
        assert stats['suma'] == 15
        assert stats['promedio'] == 3.0
        assert stats['mediana'] == 3
        assert 'desviacion_estandar' in stats
        assert 'varianza' in stats
        assert stats['total_elementos'] == 5
        assert stats['elementos_unicos'] == 5
    
    def test_analizador_obtener_informacion_general(self):
        """Debe obtener información general correctamente"""
        analizador = AnalizadorListas([1, 2, 2, 3])
        info = analizador.obtener_informacion_general()
        assert info['total_elementos'] == 4
        assert info['elementos_unicos'] == 3
        assert info['esta_vacia'] == False
        assert info['tiene_duplicados'] == True
        assert info['es_numerica'] == True
        assert 'int' in info['tipos_elementos']
    
    def test_analizador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            AnalizadorListas("no es lista")
        with pytest.raises(TypeError):
            AnalizadorListas([1, 2, 3]).lista = "no es lista"
    
    def test_analizador_str(self):
        """Debe tener representación en cadena correcta"""
        analizador = AnalizadorListas([1, 2, 3])
        assert "AnalizadorListas" in str(analizador)


class TestProcesadorListasCompleto:
    """Pruebas para la clase ProcesadorListasCompleto"""
    
    def test_procesador_creacion(self):
        """Debe crear un procesador correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 3])
        assert procesador.lista == [1, 2, 3]
    
    def test_procesador_cambiar_lista(self):
        """Debe cambiar la lista correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 3])
        procesador.lista = [4, 5, 6]
        assert procesador.lista == [4, 5, 6]
    
    def test_procesador_metodos_manipulacion(self):
        """Debe ejecutar métodos de manipulación correctamente"""
        procesador = ProcesadorListasCompleto([3, 1, 4, 2])
        assert procesador.ordenar_descendente() == [4, 3, 2, 1]
        assert procesador.ordenar_ascendente() == [1, 2, 3, 4]
        assert procesador.filtrar_impares() == [3, 1]
        assert procesador.filtrar_pares() == [4, 2]
        assert procesador.obtener_unicos_ordenados() == [1, 2, 3, 4]
    
    def test_procesador_metodos_analisis(self):
        """Debe ejecutar métodos de análisis correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 3, 4, 5])
        assert procesador.encontrar_minimo() == 1
        assert procesador.encontrar_maximo() == 5
        assert procesador.sumar_elementos() == 15
        assert procesador.buscar_elemento(3) == 2
        assert procesador.contar_ocurrencias(2) == 1
    
    def test_procesador_obtener_estadisticas_numericas(self):
        """Debe obtener estadísticas numéricas correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 3, 4, 5])
        stats = procesador.obtener_estadisticas_numericas()
        assert isinstance(stats, dict)
        assert 'minimo' in stats
        assert 'maximo' in stats
        assert 'suma' in stats
        assert 'promedio' in stats
        assert 'mediana' in stats
    
    def test_procesador_obtener_informacion_general(self):
        """Debe obtener información general correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 2, 3])
        info = procesador.obtener_informacion_general()
        assert isinstance(info, dict)
        assert 'total_elementos' in info
        assert 'elementos_unicos' in info
        assert 'esta_vacia' in info
        assert 'tiene_duplicados' in info
        assert 'es_numerica' in info
        assert 'tipos_elementos' in info
    
    def test_procesador_generar_reporte_completo(self):
        """Debe generar reporte completo correctamente"""
        procesador = ProcesadorListasCompleto([1, 2, 3, 4, 5])
        reporte = procesador.generar_reporte_completo()
        assert isinstance(reporte, str)
        assert "REPORTE COMPLETO DE LA LISTA" in reporte
        assert "INFORMACIÓN GENERAL" in reporte
        assert "ESTADÍSTICAS NUMÉRICAS" in reporte
        assert "TRANSFORMACIONES DISPONIBLES" in reporte
        assert "[1, 2, 3, 4, 5]" in reporte
    
    def test_procesador_validacion_tipo(self):
        """Debe validar tipos de parámetros"""
        with pytest.raises(TypeError):
            ProcesadorListasCompleto("no es lista")
        with pytest.raises(TypeError):
            ProcesadorListasCompleto([1, 2, 3]).lista = "no es lista"
    
    def test_procesador_str(self):
        """Debe tener representación en cadena correcta"""
        procesador = ProcesadorListasCompleto([1, 2, 3])
        assert "ProcesadorListasCompleto" in str(procesador)


class TestIntegracionPOO:
    """Pruebas de integración entre las clases POO"""
    
    def test_manipulador_y_analizador_independientes(self):
        """Debe funcionar manipulador y analizador independientemente"""
        lista = [1, 2, 3, 4, 5]
        manip = ManipuladorListas(lista)
        analizador = AnalizadorListas(lista)
        
        # Manipulador no afecta al analizador
        manip.ordenar_descendente()
        assert analizador.encontrar_minimo() == 1
        
        # Analizador no afecta al manipulador
        analizador.sumar_elementos()
        assert manip.lista == lista
    
    def test_procesador_completo_integra_funcionalidades(self):
        """Debe integrar todas las funcionalidades correctamente"""
        procesador = ProcesadorListasCompleto([5, 2, 8, 1, 9, 2])
        
        # Verificar que tiene todas las funcionalidades
        assert procesador.encontrar_minimo() == 1
        assert procesador.encontrar_maximo() == 9
        assert procesador.sumar_elementos() == 27
        assert procesador.ordenar_descendente() == [9, 8, 5, 2, 2, 1]
        assert procesador.filtrar_impares() == [5, 1, 9]
        assert procesador.contar_ocurrencias(2) == 2
        
        # Verificar que el reporte incluye todo
        reporte = procesador.generar_reporte_completo()
        assert "[5, 2, 8, 1, 9, 2]" in reporte
        assert "6" in reporte  # total de elementos
        assert "5" in reporte  # elementos únicos
    
    def test_cambio_de_lista_sincroniza_componentes(self):
        """Debe sincronizar cambios de lista en todos los componentes"""
        procesador = ProcesadorListasCompleto([1, 2, 3])
        assert procesador.encontrar_minimo() == 1
        
        procesador.lista = [10, 20, 30, 40]
        assert procesador.encontrar_minimo() == 10
        assert procesador.sumar_elementos() == 100
        assert procesador.ordenar_descendente() == [40, 30, 20, 10]
