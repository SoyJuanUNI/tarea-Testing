"""
Ejercicio 2: Manipulación de Texto

Este módulo implementa clases para manipular y analizar cadenas de texto
usando Programación Orientada a Objetos.
Incluye operaciones como contar palabras, invertir texto y verificar palíndromos.
"""

import re
from typing import Dict, List, Set


class ManipuladorTexto:
    """
    Clase principal para manipular y transformar texto.
    
    Esta clase encapsula todas las operaciones de manipulación de texto
    como inversión, capitalización y limpieza de espacios.
    """
    
    def __init__(self, texto: str = ""):
        """
        Inicializa el manipulador de texto.
        
        Args:
            texto (str): El texto inicial a manipular
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(texto)
        self._texto = texto
    
    @property
    def texto(self) -> str:
        """Obtiene el texto actual."""
        return self._texto
    
    @texto.setter
    def texto(self, nuevo_texto: str):
        """
        Establece un nuevo texto.
        
        Args:
            nuevo_texto (str): El nuevo texto a establecer
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(nuevo_texto)
        self._texto = nuevo_texto
    
    def _validar_texto(self, texto):
        """
        Valida que el parámetro sea una cadena de texto.
        
        Args:
            texto: El texto a validar
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        if not isinstance(texto, str):
            raise TypeError("El parámetro debe ser una cadena de texto")
    
    def invertir(self) -> str:
        """
        Invierte el orden de los caracteres en el texto.
        
        Returns:
            str: El texto invertido
        """
        return self._texto[::-1]
    
    def capitalizar_palabras(self) -> str:
        """
        Capitaliza la primera letra de cada palabra en el texto.
        
        Returns:
            str: El texto con cada palabra capitalizada
        """
        return self._texto.title()
    
    def eliminar_espacios_extra(self) -> str:
        """
        Elimina espacios extra del texto, dejando solo un espacio entre palabras.
        
        Returns:
            str: El texto sin espacios extra
        """
        return ' '.join(self._texto.split())
    
    def convertir_a_minusculas(self) -> str:
        """
        Convierte todo el texto a minúsculas.
        
        Returns:
            str: El texto en minúsculas
        """
        return self._texto.lower()
    
    def convertir_a_mayusculas(self) -> str:
        """
        Convierte todo el texto a mayúsculas.
        
        Returns:
            str: El texto en mayúsculas
        """
        return self._texto.upper()
    
    def reemplazar_palabra(self, palabra_antigua: str, palabra_nueva: str) -> str:
        """
        Reemplaza todas las ocurrencias de una palabra por otra.
        
        Args:
            palabra_antigua (str): La palabra a reemplazar
            palabra_nueva (str): La nueva palabra
        
        Returns:
            str: El texto con las palabras reemplazadas
        """
        return self._texto.replace(palabra_antigua, palabra_nueva)
    
    def __str__(self) -> str:
        """Representación en cadena del manipulador."""
        return f"ManipuladorTexto(texto='{self._texto[:50]}{'...' if len(self._texto) > 50 else ''}')"


class AnalizadorTexto:
    """
    Clase para analizar y obtener estadísticas de texto.
    
    Esta clase se enfoca en operaciones de análisis como contar palabras,
    vocales, caracteres únicos y verificar palíndromos.
    """
    
    def __init__(self, texto: str = ""):
        """
        Inicializa el analizador de texto.
        
        Args:
            texto (str): El texto inicial a analizar
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(texto)
        self._texto = texto
        self._vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    
    @property
    def texto(self) -> str:
        """Obtiene el texto actual."""
        return self._texto
    
    @texto.setter
    def texto(self, nuevo_texto: str):
        """
        Establece un nuevo texto.
        
        Args:
            nuevo_texto (str): El nuevo texto a establecer
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(nuevo_texto)
        self._texto = nuevo_texto
    
    def _validar_texto(self, texto):
        """
        Valida que el parámetro sea una cadena de texto.
        
        Args:
            texto: El texto a validar
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        if not isinstance(texto, str):
            raise TypeError("El parámetro debe ser una cadena de texto")
    
    def contar_palabras(self) -> int:
        """
        Cuenta el número de palabras en el texto.
        
        Returns:
            int: El número de palabras en el texto
        """
        if not self._texto.strip():
            return 0
        return len(self._texto.split())
    
    def contar_vocales(self) -> int:
        """
        Cuenta el número de vocales en el texto.
        
        Returns:
            int: El número de vocales en el texto
        """
        return sum(1 for c in self._texto if c in self._vocales)
    
    def contar_consonantes(self) -> int:
        """
        Cuenta el número de consonantes en el texto.
        
        Returns:
            int: El número de consonantes en el texto
        """
        return sum(1 for c in self._texto if c.isalpha() and c not in self._vocales)
    
    def contar_caracteres_unicos(self) -> int:
        """
        Cuenta el número de caracteres únicos en el texto (case-sensitive),
        contando cada espacio como carácter independiente.
        
        Returns:
            int: La cuenta combinada de caracteres únicos (excluyendo espacios) más
                 el número de espacios individuales presentes en el texto
        """
        caracteres_sin_espacio = {c for c in self._texto if c != ' '}
        num_espacios = self._texto.count(' ')
        return len(caracteres_sin_espacio) + num_espacios
    
    def es_palindromo(self) -> bool:
        """
        Verifica si el texto es un palíndromo (se lee igual al derecho y al revés).
        Ignora espacios, mayúsculas y signos de puntuación.
        
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        # Limpiar el texto: solo letras y números, en minúsculas
        texto_limpio = ''.join(c.lower() for c in self._texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def obtener_estadisticas(self) -> Dict[str, int]:
        """
        Obtiene un resumen completo de estadísticas del texto.
        
        Returns:
            Dict[str, int]: Diccionario con las estadísticas del texto
        """
        return {
            'total_caracteres': len(self._texto),
            'total_palabras': self.contar_palabras(),
            'total_vocales': self.contar_vocales(),
            'total_consonantes': self.contar_consonantes(),
            'caracteres_unicos': self.contar_caracteres_unicos(),
            'es_palindromo': 1 if self.es_palindromo() else 0
        }
    
    def obtener_palabras_unicas(self) -> Set[str]:
        """
        Obtiene un conjunto de palabras únicas en el texto.
        
        Returns:
            Set[str]: Conjunto de palabras únicas
        """
        palabras = self._texto.lower().split()
        return set(palabras)
    
    def contar_ocurrencias_palabra(self, palabra: str) -> int:
        """
        Cuenta las ocurrencias de una palabra específica en el texto.
        
        Args:
            palabra (str): La palabra a buscar
        
        Returns:
            int: Número de ocurrencias de la palabra
        """
        if not isinstance(palabra, str):
            raise TypeError("La palabra debe ser una cadena de texto")
        
        palabras = self._texto.lower().split()
        return palabras.count(palabra.lower())
    
    def __str__(self) -> str:
        """Representación en cadena del analizador."""
        return f"AnalizadorTexto(texto='{self._texto[:50]}{'...' if len(self._texto) > 50 else ''}')"


class ProcesadorTextoCompleto:
    """
    Clase que combina manipulación y análisis de texto.
    
    Esta clase hereda funcionalidades de ambas clases anteriores
    para proporcionar un procesamiento completo de texto.
    """
    
    def __init__(self, texto: str = ""):
        """
        Inicializa el procesador completo de texto.
        
        Args:
            texto (str): El texto inicial a procesar
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(texto)
        self._texto = texto
        self._manipulador = ManipuladorTexto(texto)
        self._analizador = AnalizadorTexto(texto)
    
    @property
    def texto(self) -> str:
        """Obtiene el texto actual."""
        return self._texto
    
    @texto.setter
    def texto(self, nuevo_texto: str):
        """
        Establece un nuevo texto y actualiza los componentes internos.
        
        Args:
            nuevo_texto (str): El nuevo texto a establecer
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        self._validar_texto(nuevo_texto)
        self._texto = nuevo_texto
        self._manipulador.texto = nuevo_texto
        self._analizador.texto = nuevo_texto
    
    def _validar_texto(self, texto):
        """
        Valida que el parámetro sea una cadena de texto.
        
        Args:
            texto: El texto a validar
        
        Raises:
            TypeError: Si el texto no es una cadena
        """
        if not isinstance(texto, str):
            raise TypeError("El parámetro debe ser una cadena de texto")
    
    # Métodos de manipulación
    def invertir(self) -> str:
        """Invierte el texto."""
        return self._manipulador.invertir()
    
    def capitalizar_palabras(self) -> str:
        """Capitaliza las palabras del texto."""
        return self._manipulador.capitalizar_palabras()
    
    def eliminar_espacios_extra(self) -> str:
        """Elimina espacios extra del texto."""
        return self._manipulador.eliminar_espacios_extra()
    
    def convertir_a_minusculas(self) -> str:
        """Convierte el texto a minúsculas."""
        return self._manipulador.convertir_a_minusculas()
    
    def convertir_a_mayusculas(self) -> str:
        """Convierte el texto a mayúsculas."""
        return self._manipulador.convertir_a_mayusculas()
    
    def reemplazar_palabra(self, palabra_antigua: str, palabra_nueva: str) -> str:
        """Reemplaza palabras en el texto."""
        return self._manipulador.reemplazar_palabra(palabra_antigua, palabra_nueva)
    
    # Métodos de análisis
    def contar_palabras(self) -> int:
        """Cuenta las palabras en el texto."""
        return self._analizador.contar_palabras()
    
    def contar_vocales(self) -> int:
        """Cuenta las vocales en el texto."""
        return self._analizador.contar_vocales()
    
    def contar_consonantes(self) -> int:
        """Cuenta las consonantes en el texto."""
        return self._analizador.contar_consonantes()
    
    def contar_caracteres_unicos(self) -> int:
        """Cuenta los caracteres únicos en el texto."""
        return self._analizador.contar_caracteres_unicos()
    
    def es_palindromo(self) -> bool:
        """Verifica si el texto es un palíndromo."""
        return self._analizador.es_palindromo()
    
    def obtener_estadisticas(self) -> Dict[str, int]:
        """Obtiene estadísticas completas del texto."""
        return self._analizador.obtener_estadisticas()
    
    def obtener_palabras_unicas(self) -> Set[str]:
        """Obtiene palabras únicas del texto."""
        return self._analizador.obtener_palabras_unicas()
    
    def contar_ocurrencias_palabra(self, palabra: str) -> int:
        """Cuenta ocurrencias de una palabra específica."""
        return self._analizador.contar_ocurrencias_palabra(palabra)
    
    def generar_reporte_completo(self) -> str:
        """
        Genera un reporte completo del texto.
        
        Returns:
            str: Reporte formateado con toda la información del texto
        """
        stats = self.obtener_estadisticas()
        palabras_unicas = self.obtener_palabras_unicas()
        
        reporte = f"""
=== REPORTE COMPLETO DEL TEXTO ===
Texto original: "{self._texto[:100]}{'...' if len(self._texto) > 100 else ''}"

ESTADÍSTICAS:
- Total de caracteres: {stats['total_caracteres']}
- Total de palabras: {stats['total_palabras']}
- Total de vocales: {stats['total_vocales']}
- Total de consonantes: {stats['total_consonantes']}
- Caracteres únicos: {stats['caracteres_unicos']}
- Es palíndromo: {'Sí' if stats['es_palindromo'] else 'No'}

TRANSFORMACIONES:
- Texto invertido: "{self.invertir()[:50]}{'...' if len(self.invertir()) > 50 else ''}"
- Texto capitalizado: "{self.capitalizar_palabras()[:50]}{'...' if len(self.capitalizar_palabras()) > 50 else ''}"
- Sin espacios extra: "{self.eliminar_espacios_extra()[:50]}{'...' if len(self.eliminar_espacios_extra()) > 50 else ''}"

PALABRAS ÚNICAS ({len(palabras_unicas)}): {', '.join(sorted(palabras_unicas)[:10])}{'...' if len(palabras_unicas) > 10 else ''}
"""
        return reporte.strip()
    
    def __str__(self) -> str:
        """Representación en cadena del procesador."""
        return f"ProcesadorTextoCompleto(texto='{self._texto[:50]}{'...' if len(self._texto) > 50 else ''}')"


# Funciones de compatibilidad para mantener la interfaz anterior
def contar_palabras(texto):
    """
    Función de compatibilidad para contar palabras.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: El número de palabras en el texto
    """
    analizador = AnalizadorTexto(texto)
    return analizador.contar_palabras()


def invertir_texto(texto):
    """
    Función de compatibilidad para invertir texto.
    
    Args:
        texto (str): El texto a invertir
    
    Returns:
        str: El texto invertido
    """
    manipulador = ManipuladorTexto(texto)
    return manipulador.invertir()


def es_palindromo(texto):
    """
    Función de compatibilidad para verificar palíndromos.
    
    Args:
        texto (str): El texto a verificar
    
    Returns:
        bool: True si es palíndromo, False en caso contrario
    """
    analizador = AnalizadorTexto(texto)
    return analizador.es_palindromo()


def contar_vocales(texto):
    """
    Función de compatibilidad para contar vocales.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: El número de vocales en el texto
    """
    analizador = AnalizadorTexto(texto)
    return analizador.contar_vocales()


def capitalizar_palabras(texto):
    """
    Función de compatibilidad para capitalizar palabras.
    
    Args:
        texto (str): El texto a capitalizar
    
    Returns:
        str: El texto con cada palabra capitalizada
    """
    manipulador = ManipuladorTexto(texto)
    return manipulador.capitalizar_palabras()


def eliminar_espacios_extra(texto):
    """
    Función de compatibilidad para eliminar espacios extra.
    
    Args:
        texto (str): El texto a limpiar
    
    Returns:
        str: El texto sin espacios extra
    """
    manipulador = ManipuladorTexto(texto)
    return manipulador.eliminar_espacios_extra()


def contar_caracteres_unicos(texto):
    """
    Función de compatibilidad para contar caracteres únicos.
    
    Args:
        texto (str): El texto a analizar
    
    Returns:
        int: La cuenta de caracteres únicos
    """
    analizador = AnalizadorTexto(texto)
    return analizador.contar_caracteres_unicos()
