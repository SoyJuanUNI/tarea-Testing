"""
Pruebas unitarias para el módulo de Operaciones con Listas

Estas pruebas verifican el correcto funcionamiento de las funciones
para manipular y analizar listas.
"""

import pytest
from ejercicio3_listas import (
    encontrar_minimo,
    ordenar_descendente,
    filtrar_impares,
    sumar_elementos,
    buscar_elemento,
    aplanar_lista,
    obtener_unicos_ordenados,
    dividir_lista
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
