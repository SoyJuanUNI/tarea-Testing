"""
Ejercicio 3: Operaciones con Listas

Este módulo implementa clases para manipular y analizar listas
usando Programación Orientada a Objetos.
Incluye operaciones de búsqueda, ordenamiento y transformación.
"""

from typing import List, Any, Dict, Union, Optional
import statistics


class ManipuladorListas:
    """
    Clase para manipular y transformar listas.
    
    Esta clase encapsula operaciones de manipulación como ordenamiento,
    filtrado, aplanado y división de listas.
    """
    
    def __init__(self, lista: List[Any] = None):
        """
        Inicializa el manipulador de listas.
        
        Args:
            lista (List[Any]): La lista inicial a manipular
        """
        if lista is None:
            lista = []
        self._validar_lista(lista)
        self._lista = lista.copy()  # Crear una copia para no modificar la original
    
    @property
    def lista(self) -> List[Any]:
        """Obtiene la lista actual."""
        return self._lista.copy()  # Retornar copia para evitar modificaciones externas
    
    @lista.setter
    def lista(self, nueva_lista: List[Any]):
        """
        Establece una nueva lista.
        
        Args:
            nueva_lista (List[Any]): La nueva lista a establecer
        """
        self._validar_lista(nueva_lista)
        self._lista = nueva_lista.copy()
    
    def _validar_lista(self, lista):
        """
        Valida que el parámetro sea una lista.
        
        Args:
            lista: La lista a validar
        
        Raises:
            TypeError: Si no es una lista
        """
        if not isinstance(lista, list):
            raise TypeError("El parámetro debe ser una lista")
    
    def _validar_numeros(self, lista: List[Any] = None):
        """
        Valida que todos los elementos de la lista sean números.
        
        Args:
            lista (List[Any]): Lista a validar, si es None usa la lista interna
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        if lista is None:
            lista = self._lista
        
        if not all(isinstance(x, (int, float)) for x in lista):
            raise TypeError("Todos los elementos deben ser números")
    
    def ordenar_descendente(self) -> List[Union[int, float]]:
        """
        Ordena la lista de números en orden descendente.
        
        Returns:
            List[Union[int, float]]: Nueva lista ordenada en orden descendente
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        self._validar_numeros()
        return sorted(self._lista, reverse=True)
    
    def ordenar_ascendente(self) -> List[Union[int, float]]:
        """
        Ordena la lista de números en orden ascendente.
        
        Returns:
            List[Union[int, float]]: Nueva lista ordenada en orden ascendente
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        self._validar_numeros()
        return sorted(self._lista)
    
    def filtrar_impares(self) -> List[Union[int, float]]:
        """
        Filtra los números impares de la lista.
        
        Returns:
            List[Union[int, float]]: Nueva lista con solo los números impares
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        self._validar_numeros()
        return [x for x in self._lista if x % 2 != 0]
    
    def filtrar_pares(self) -> List[Union[int, float]]:
        """
        Filtra los números pares de la lista.
        
        Returns:
            List[Union[int, float]]: Nueva lista con solo los números pares
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        self._validar_numeros()
        return [x for x in self._lista if x % 2 == 0]
    
    def filtrar_por_condicion(self, condicion) -> List[Any]:
        """
        Filtra elementos que cumplan una condición específica.
        
        Args:
            condicion: Función que define la condición de filtrado
        
        Returns:
            List[Any]: Nueva lista con elementos que cumplen la condición
        """
        return [x for x in self._lista if condicion(x)]
    
    def aplanar(self) -> List[Any]:
        """
        Aplana la lista de listas en una sola lista.
        
        Returns:
            List[Any]: Lista aplanada
        """
        resultado = []
        for elemento in self._lista:
            if isinstance(elemento, list):
                resultado.extend(elemento)
            else:
                resultado.append(elemento)
        return resultado
    
    def dividir(self, tamaño: int) -> List[List[Any]]:
        """
        Divide la lista en sublistas de un tamaño específico.
        
        Args:
            tamaño (int): Tamaño de cada sublista
        
        Returns:
            List[List[Any]]: Lista de sublistas
        
        Raises:
            TypeError: Si el tamaño no es un entero
            ValueError: Si el tamaño es menor o igual a 0
        """
        if not isinstance(tamaño, int):
            raise TypeError("El tamaño debe ser un entero")
        
        if tamaño <= 0:
            raise ValueError("El tamaño debe ser mayor que 0")
        
        return [self._lista[i:i + tamaño] for i in range(0, len(self._lista), tamaño)]
    
    def obtener_unicos_ordenados(self) -> List[Any]:
        """
        Obtiene los elementos únicos de la lista y los retorna ordenados.
        
        Returns:
            List[Any]: Lista con elementos únicos ordenados
        
        Raises:
            TypeError: Si los elementos no son comparables
        """
        try:
            return sorted(set(self._lista))
        except TypeError:
            raise TypeError("Los elementos deben ser comparables")
    
    def __str__(self) -> str:
        """Representación en cadena del manipulador."""
        return f"ManipuladorListas(lista={self._lista})"


class AnalizadorListas:
    """
    Clase para analizar y obtener estadísticas de listas.
    
    Esta clase se enfoca en operaciones de análisis como encontrar mínimos,
    máximos, sumas, búsquedas y estadísticas.
    """
    
    def __init__(self, lista: List[Any] = None):
        """
        Inicializa el analizador de listas.
        
        Args:
            lista (List[Any]): La lista inicial a analizar
        """
        if lista is None:
            lista = []
        self._validar_lista(lista)
        self._lista = lista.copy()
    
    @property
    def lista(self) -> List[Any]:
        """Obtiene la lista actual."""
        return self._lista.copy()
    
    @lista.setter
    def lista(self, nueva_lista: List[Any]):
        """
        Establece una nueva lista.
        
        Args:
            nueva_lista (List[Any]): La nueva lista a establecer
        """
        self._validar_lista(nueva_lista)
        self._lista = nueva_lista.copy()
    
    def _validar_lista(self, lista):
        """
        Valida que el parámetro sea una lista.
        
        Args:
            lista: La lista a validar
        
        Raises:
            TypeError: Si no es una lista
        """
        if not isinstance(lista, list):
            raise TypeError("El parámetro debe ser una lista")
    
    def _validar_numeros(self, lista: List[Any] = None):
        """
        Valida que todos los elementos de la lista sean números.
        
        Args:
            lista (List[Any]): Lista a validar, si es None usa la lista interna
        
        Raises:
            TypeError: Si contiene elementos no numéricos
        """
        if lista is None:
            lista = self._lista
        
        if not all(isinstance(x, (int, float)) for x in lista):
            raise TypeError("Todos los elementos deben ser números")
    
    def _validar_lista_no_vacia(self, lista: List[Any] = None):
        """
        Valida que la lista no esté vacía.
        
        Args:
            lista (List[Any]): Lista a validar, si es None usa la lista interna
        
        Raises:
            ValueError: Si la lista está vacía
        """
        if lista is None:
            lista = self._lista
        
        if len(lista) == 0:
            raise ValueError("La lista no puede estar vacía")
    
    def encontrar_minimo(self) -> Union[int, float]:
        """
        Encuentra el valor mínimo en la lista de números.
        
        Returns:
            Union[int, float]: El valor mínimo de la lista
        
        Raises:
            TypeError: Si contiene elementos no numéricos
            ValueError: Si la lista está vacía
        """
        self._validar_lista_no_vacia()
        self._validar_numeros()
        return min(self._lista)
    
    def encontrar_maximo(self) -> Union[int, float]:
        """
        Encuentra el valor máximo en la lista de números.
        
        Returns:
            Union[int, float]: El valor máximo de la lista
        
        Raises:
            TypeError: Si contiene elementos no numéricos
            ValueError: Si la lista está vacía
        """
        self._validar_lista_no_vacia()
        self._validar_numeros()
        return max(self._lista)
    
    def sumar_elementos(self) -> Union[int, float]:
        """
        Suma todos los elementos de la lista de números.
        
        Returns:
            Union[int, float]: La suma de todos los elementos
        
        Raises:
            TypeError: Si contiene elementos no numéricos
            ValueError: Si la lista está vacía
        """
        self._validar_lista_no_vacia()
        self._validar_numeros()
        return sum(self._lista)
    
    def buscar_elemento(self, elemento: Any) -> int:
        """
        Busca un elemento en la lista y retorna su índice.
        
        Args:
            elemento (Any): Elemento a buscar
        
        Returns:
            int: El índice del elemento, o -1 si no se encuentra
        """
        try:
            return self._lista.index(elemento)
        except ValueError:
            return -1
    
    def contar_ocurrencias(self, elemento: Any) -> int:
        """
        Cuenta las ocurrencias de un elemento en la lista.
        
        Args:
            elemento (Any): Elemento a contar
        
        Returns:
            int: Número de ocurrencias del elemento
        """
        return self._lista.count(elemento)
    
    def obtener_estadisticas_numericas(self) -> Dict[str, Union[int, float]]:
        """
        Obtiene estadísticas numéricas completas de la lista.
        
        Returns:
            Dict[str, Union[int, float]]: Diccionario con estadísticas
        
        Raises:
            TypeError: Si contiene elementos no numéricos
            ValueError: Si la lista está vacía
        """
        self._validar_lista_no_vacia()
        self._validar_numeros()
        
        return {
            'minimo': min(self._lista),
            'maximo': max(self._lista),
            'suma': sum(self._lista),
            'promedio': statistics.mean(self._lista),
            'mediana': statistics.median(self._lista),
            'moda': statistics.mode(self._lista) if len(set(self._lista)) < len(self._lista) else None,
            'desviacion_estandar': statistics.stdev(self._lista) if len(self._lista) > 1 else 0,
            'varianza': statistics.variance(self._lista) if len(self._lista) > 1 else 0,
            'total_elementos': len(self._lista),
            'elementos_unicos': len(set(self._lista))
        }
    
    def obtener_informacion_general(self) -> Dict[str, Any]:
        """
        Obtiene información general sobre la lista.
        
        Returns:
            Dict[str, Any]: Diccionario con información general
        """
        return {
            'total_elementos': len(self._lista),
            'elementos_unicos': len(set(self._lista)),
            'esta_vacia': len(self._lista) == 0,
            'tiene_duplicados': len(self._lista) != len(set(self._lista)),
            'tipos_elementos': list(set(type(x).__name__ for x in self._lista)),
            'es_numerica': all(isinstance(x, (int, float)) for x in self._lista)
        }
    
    def __str__(self) -> str:
        """Representación en cadena del analizador."""
        return f"AnalizadorListas(lista={self._lista})"


class ProcesadorListasCompleto:
    """
    Clase que combina manipulación y análisis de listas.
    
    Esta clase integra funcionalidades de ManipuladorListas y AnalizadorListas
    para proporcionar un procesamiento completo de listas.
    """
    
    def __init__(self, lista: List[Any] = None):
        """
        Inicializa el procesador completo de listas.
        
        Args:
            lista (List[Any]): La lista inicial a procesar
        """
        if lista is None:
            lista = []
        self._validar_lista(lista)
        self._lista = lista.copy()
        self._manipulador = ManipuladorListas(lista)
        self._analizador = AnalizadorListas(lista)
    
    @property
    def lista(self) -> List[Any]:
        """Obtiene la lista actual."""
        return self._lista.copy()
    
    @lista.setter
    def lista(self, nueva_lista: List[Any]):
        """
        Establece una nueva lista y actualiza los componentes internos.
        
        Args:
            nueva_lista (List[Any]): La nueva lista a establecer
        """
        self._validar_lista(nueva_lista)
        self._lista = nueva_lista.copy()
        self._manipulador.lista = nueva_lista
        self._analizador.lista = nueva_lista
    
    def _validar_lista(self, lista):
        """
        Valida que el parámetro sea una lista.
        
        Args:
            lista: La lista a validar
        
        Raises:
            TypeError: Si no es una lista
        """
        if not isinstance(lista, list):
            raise TypeError("El parámetro debe ser una lista")
    
    # Métodos de manipulación
    def ordenar_descendente(self) -> List[Union[int, float]]:
        """Ordena la lista en orden descendente."""
        return self._manipulador.ordenar_descendente()
    
    def ordenar_ascendente(self) -> List[Union[int, float]]:
        """Ordena la lista en orden ascendente."""
        return self._manipulador.ordenar_ascendente()
    
    def filtrar_impares(self) -> List[Union[int, float]]:
        """Filtra los números impares."""
        return self._manipulador.filtrar_impares()
    
    def filtrar_pares(self) -> List[Union[int, float]]:
        """Filtra los números pares."""
        return self._manipulador.filtrar_pares()
    
    def filtrar_por_condicion(self, condicion) -> List[Any]:
        """Filtra elementos por condición."""
        return self._manipulador.filtrar_por_condicion(condicion)
    
    def aplanar(self) -> List[Any]:
        """Aplana la lista."""
        return self._manipulador.aplanar()
    
    def dividir(self, tamaño: int) -> List[List[Any]]:
        """Divide la lista en sublistas."""
        return self._manipulador.dividir(tamaño)
    
    def obtener_unicos_ordenados(self) -> List[Any]:
        """Obtiene elementos únicos ordenados."""
        return self._manipulador.obtener_unicos_ordenados()
    
    # Métodos de análisis
    def encontrar_minimo(self) -> Union[int, float]:
        """Encuentra el valor mínimo."""
        return self._analizador.encontrar_minimo()
    
    def encontrar_maximo(self) -> Union[int, float]:
        """Encuentra el valor máximo."""
        return self._analizador.encontrar_maximo()
    
    def sumar_elementos(self) -> Union[int, float]:
        """Suma todos los elementos."""
        return self._analizador.sumar_elementos()
    
    def buscar_elemento(self, elemento: Any) -> int:
        """Busca un elemento en la lista."""
        return self._analizador.buscar_elemento(elemento)
    
    def contar_ocurrencias(self, elemento: Any) -> int:
        """Cuenta ocurrencias de un elemento."""
        return self._analizador.contar_ocurrencias(elemento)
    
    def obtener_estadisticas_numericas(self) -> Dict[str, Union[int, float]]:
        """Obtiene estadísticas numéricas completas."""
        return self._analizador.obtener_estadisticas_numericas()
    
    def obtener_informacion_general(self) -> Dict[str, Any]:
        """Obtiene información general sobre la lista."""
        return self._analizador.obtener_informacion_general()
    
    def generar_reporte_completo(self) -> str:
        """
        Genera un reporte completo de la lista.
        
        Returns:
            str: Reporte formateado con toda la información de la lista
        """
        info_general = self.obtener_informacion_general()
        
        reporte = f"""
=== REPORTE COMPLETO DE LA LISTA ===
Lista original: {self._lista}

INFORMACIÓN GENERAL:
- Total de elementos: {info_general['total_elementos']}
- Elementos únicos: {info_general['elementos_unicos']}
- Está vacía: {'Sí' if info_general['esta_vacia'] else 'No'}
- Tiene duplicados: {'Sí' if info_general['tiene_duplicados'] else 'No'}
- Es numérica: {'Sí' if info_general['es_numerica'] else 'No'}
- Tipos de elementos: {', '.join(info_general['tipos_elementos'])}
"""
        
        if info_general['es_numerica'] and not info_general['esta_vacia']:
            try:
                stats = self.obtener_estadisticas_numericas()
                reporte += f"""
ESTADÍSTICAS NUMÉRICAS:
- Mínimo: {stats['minimo']}
- Máximo: {stats['maximo']}
- Suma: {stats['suma']}
- Promedio: {stats['promedio']:.2f}
- Mediana: {stats['mediana']}
- Moda: {stats['moda'] if stats['moda'] is not None else 'No hay moda'}
- Desviación estándar: {stats['desviacion_estandar']:.2f}
- Varianza: {stats['varianza']:.2f}
"""
            except (TypeError, ValueError):
                reporte += "\nESTADÍSTICAS NUMÉRICAS: No disponibles\n"
        
        if not info_general['esta_vacia']:
            reporte += f"""
TRANSFORMACIONES DISPONIBLES:
- Lista ordenada ascendente: {self.ordenar_ascendente() if info_general['es_numerica'] else 'No disponible para listas no numéricas'}
- Lista ordenada descendente: {self.ordenar_descendente() if info_general['es_numerica'] else 'No disponible para listas no numéricas'}
- Elementos únicos ordenados: {self.obtener_unicos_ordenados()}
"""
        
        return reporte.strip()
    
    def __str__(self) -> str:
        """Representación en cadena del procesador."""
        return f"ProcesadorListasCompleto(lista={self._lista})"


# Funciones de compatibilidad para mantener la interfaz anterior
def encontrar_minimo(lista):
    """
    Función de compatibilidad para encontrar el mínimo.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float/int: El valor mínimo de la lista
    """
    analizador = AnalizadorListas(lista)
    return analizador.encontrar_minimo()


def ordenar_descendente(lista):
    """
    Función de compatibilidad para ordenar descendente.
    
    Args:
        lista (list): Lista de números a ordenar
    
    Returns:
        list: Nueva lista ordenada en orden descendente
    """
    manipulador = ManipuladorListas(lista)
    return manipulador.ordenar_descendente()


def filtrar_impares(lista):
    """
    Función de compatibilidad para filtrar impares.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        list: Nueva lista con solo los números impares
    """
    manipulador = ManipuladorListas(lista)
    return manipulador.filtrar_impares()


def sumar_elementos(lista):
    """
    Función de compatibilidad para sumar elementos.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float/int: La suma de todos los elementos
    """
    analizador = AnalizadorListas(lista)
    return analizador.sumar_elementos()


def buscar_elemento(lista, elemento):
    """
    Función de compatibilidad para buscar elemento.
    
    Args:
        lista (list): Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        int: El índice del elemento, o -1 si no se encuentra
    """
    analizador = AnalizadorListas(lista)
    return analizador.buscar_elemento(elemento)


def aplanar_lista(lista):
    """
    Función de compatibilidad para aplanar lista.
    
    Args:
        lista (list): Lista de listas
    
    Returns:
        list: Lista aplanada
    """
    manipulador = ManipuladorListas(lista)
    return manipulador.aplanar()


def obtener_unicos_ordenados(lista):
    """
    Función de compatibilidad para obtener únicos ordenados.
    
    Args:
        lista (list): Lista con posibles duplicados
    
    Returns:
        list: Lista con elementos únicos ordenados
    """
    manipulador = ManipuladorListas(lista)
    return manipulador.obtener_unicos_ordenados()


def dividir_lista(lista, tamaño):
    """
    Función de compatibilidad para dividir lista.
    
    Args:
        lista (list): Lista a dividir
        tamaño (int): Tamaño de cada sublista
    
    Returns:
        list: Lista de sublistas
    """
    manipulador = ManipuladorListas(lista)
    return manipulador.dividir(tamaño)
