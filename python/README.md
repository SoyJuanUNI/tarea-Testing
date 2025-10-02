# 🐍 Ejercicios Python - Pruebas Unitarias

Documentación completa de los ejercicios de Python con pytest.

## 📁 Estructura

```
python/
├── __init__.py                         # Módulo Python
├── ejercicio1_geometria.py             # Calculadora geométrica
├── test_ejercicio1_geometria.py        # Pruebas de geometría
├── ejercicio2_texto.py                 # Manipulación de texto
├── test_ejercicio2_texto.py            # Pruebas de texto
├── ejercicio3_listas.py                # Operaciones con listas
├── test_ejercicio3_listas.py           # Pruebas de listas
└── README.md                           # Este archivo
```

## 🚀 Instalación

### Requisitos Previos
- **Python** (versión 3.8 o superior)
- **pip** (incluido con Python)

### Instalar Dependencias

Desde la raíz del proyecto:
```bash
pip install -r requirements.txt
```

## 🧪 Ejecutar las Pruebas

### Todas las pruebas de Python:
```bash
pytest python/
```

### Pruebas con salida detallada:
```bash
pytest python/ -v
```

### Pruebas con reporte de cobertura:
```bash
pytest python/ --cov=python --cov-report=html
```

### Ejecutar un archivo de pruebas específico:
```bash
# Ejercicio 1
pytest python/test_ejercicio1_geometria.py -v

# Ejercicio 2
pytest python/test_ejercicio2_texto.py -v

# Ejercicio 3
pytest python/test_ejercicio3_listas.py -v
```

### Ejecutar una clase de pruebas específica:
```bash
pytest python/test_ejercicio1_geometria.py::TestAreaRectangulo -v
```

## 📚 Ejercicios

### Ejercicio 1: Calculadora de Figuras Geométricas

**Archivo**: `ejercicio1_geometria.py`

#### Funciones Implementadas

##### `area_rectangulo(base, altura)`
Calcula el área de un rectángulo.
- **Parámetros**: `base` (float), `altura` (float)
- **Retorna**: `float` - El área del rectángulo
- **Excepciones**: 
  - `TypeError` si los parámetros no son números
  - `ValueError` si los parámetros son negativos

##### `area_circulo(radio)`
Calcula el área de un círculo.
- **Parámetros**: `radio` (float)
- **Retorna**: `float` - El área del círculo (π × radio²)
- **Excepciones**: 
  - `TypeError` si el parámetro no es un número
  - `ValueError` si el radio es negativo

##### `area_triangulo(base, altura)`
Calcula el área de un triángulo.
- **Parámetros**: `base` (float), `altura` (float)
- **Retorna**: `float` - El área del triángulo ((base × altura) / 2)
- **Excepciones**: 
  - `TypeError` si los parámetros no son números
  - `ValueError` si los parámetros son negativos

##### `perimetro_rectangulo(base, altura)`
Calcula el perímetro de un rectángulo.
- **Parámetros**: `base` (float), `altura` (float)
- **Retorna**: `float` - El perímetro del rectángulo
- **Excepciones**: 
  - `TypeError` si los parámetros no son números
  - `ValueError` si los parámetros son negativos

##### `perimetro_circulo(radio)`
Calcula el perímetro (circunferencia) de un círculo.
- **Parámetros**: `radio` (float)
- **Retorna**: `float` - El perímetro del círculo (2 × π × radio)
- **Excepciones**: 
  - `TypeError` si el parámetro no es un número
  - `ValueError` si el radio es negativo

#### Ejemplos de Uso

```python
from python.ejercicio1_geometria import (
    area_rectangulo,
    area_circulo,
    area_triangulo,
    perimetro_rectangulo,
    perimetro_circulo
)

# Área de rectángulo
print(area_rectangulo(5, 3))          # 15

# Área de círculo
print(area_circulo(5))                # 78.53981633974483

# Área de triángulo
print(area_triangulo(6, 4))           # 12.0

# Perímetro de rectángulo
print(perimetro_rectangulo(5, 3))     # 16

# Perímetro de círculo
print(perimetro_circulo(5))           # 31.41592653589793
```

#### Pruebas (25 tests)
- ✅ Cálculo de áreas con números positivos y decimales
- ✅ Cálculo de perímetros con diferentes dimensiones
- ✅ Manejo de valores cero
- ✅ Validación de tipos de datos
- ✅ Validación de valores negativos

---

### Ejercicio 2: Manipulación de Texto

**Archivo**: `ejercicio2_texto.py`

#### Funciones Implementadas

##### `contar_palabras(texto)`
Cuenta el número de palabras en un texto.
- **Parámetros**: `texto` (str)
- **Retorna**: `int` - El número de palabras
- **Excepciones**: `TypeError` si no es una cadena

##### `invertir_texto(texto)`
Invierte el orden de los caracteres en un texto.
- **Parámetros**: `texto` (str)
- **Retorna**: `str` - El texto invertido
- **Excepciones**: `TypeError` si no es una cadena

##### `es_palindromo(texto)`
Verifica si un texto es un palíndromo (se lee igual al derecho y al revés).
Ignora espacios, mayúsculas y signos de puntuación.
- **Parámetros**: `texto` (str)
- **Retorna**: `bool` - True si es palíndromo, False en caso contrario
- **Excepciones**: `TypeError` si no es una cadena

##### `contar_vocales(texto)`
Cuenta el número de vocales en un texto.
- **Parámetros**: `texto` (str)
- **Retorna**: `int` - El número de vocales
- **Excepciones**: `TypeError` si no es una cadena

##### `capitalizar_palabras(texto)`
Capitaliza la primera letra de cada palabra en un texto.
- **Parámetros**: `texto` (str)
- **Retorna**: `str` - El texto con cada palabra capitalizada
- **Excepciones**: `TypeError` si no es una cadena

##### `eliminar_espacios_extra(texto)`
Elimina espacios extra del texto, dejando solo un espacio entre palabras.
- **Parámetros**: `texto` (str)
- **Retorna**: `str` - El texto sin espacios extra
- **Excepciones**: `TypeError` si no es una cadena

##### `contar_caracteres_unicos(texto)`
Cuenta el número de caracteres únicos en un texto (case-sensitive).
- **Parámetros**: `texto` (str)
- **Retorna**: `int` - El número de caracteres únicos
- **Excepciones**: `TypeError` si no es una cadena

#### Ejemplos de Uso

```python
from python.ejercicio2_texto import (
    contar_palabras,
    invertir_texto,
    es_palindromo,
    contar_vocales,
    capitalizar_palabras,
    eliminar_espacios_extra,
    contar_caracteres_unicos
)

# Contar palabras
print(contar_palabras("Hola mundo"))                    # 2

# Invertir texto
print(invertir_texto("Python"))                         # "nohtyP"

# Verificar palíndromo
print(es_palindromo("anita lava la tina"))              # True
print(es_palindromo("hola"))                            # False

# Contar vocales
print(contar_vocales("Educación"))                      # 5

# Capitalizar palabras
print(capitalizar_palabras("hola mundo"))               # "Hola Mundo"

# Eliminar espacios extra
print(eliminar_espacios_extra("Hola    mundo"))         # "Hola mundo"

# Contar caracteres únicos
print(contar_caracteres_unicos("hello"))                # 4 (h, e, l, o)
```

#### Pruebas (35 tests)
- ✅ Conteo de palabras con espacios extra
- ✅ Inversión de texto con espacios y caracteres especiales
- ✅ Detección de palíndromos ignorando mayúsculas y espacios
- ✅ Conteo de vocales incluyendo acentos
- ✅ Capitalización de palabras
- ✅ Eliminación de espacios múltiples
- ✅ Conteo de caracteres únicos (case-sensitive)

---

### Ejercicio 3: Operaciones con Listas

**Archivo**: `ejercicio3_listas.py`

#### Funciones Implementadas

##### `encontrar_minimo(lista)`
Encuentra el valor mínimo en una lista de números.
- **Parámetros**: `lista` (list)
- **Retorna**: `float/int` - El valor mínimo
- **Excepciones**: 
  - `TypeError` si no es una lista o contiene elementos no numéricos
  - `ValueError` si la lista está vacía

##### `ordenar_descendente(lista)`
Ordena una lista de números en orden descendente.
- **Parámetros**: `lista` (list)
- **Retorna**: `list` - Nueva lista ordenada en orden descendente
- **Excepciones**: `TypeError` si no es una lista o contiene elementos no numéricos

##### `filtrar_impares(lista)`
Filtra los números impares de una lista.
- **Parámetros**: `lista` (list)
- **Retorna**: `list` - Nueva lista con solo números impares
- **Excepciones**: `TypeError` si no es una lista o contiene elementos no numéricos

##### `sumar_elementos(lista)`
Suma todos los elementos de una lista de números.
- **Parámetros**: `lista` (list)
- **Retorna**: `float/int` - La suma de todos los elementos
- **Excepciones**: 
  - `TypeError` si no es una lista o contiene elementos no numéricos
  - `ValueError` si la lista está vacía

##### `buscar_elemento(lista, elemento)`
Busca un elemento en una lista y retorna su índice.
- **Parámetros**: `lista` (list), `elemento` (any)
- **Retorna**: `int` - El índice del elemento, o -1 si no se encuentra
- **Excepciones**: `TypeError` si no es una lista

##### `aplanar_lista(lista)`
Aplana una lista de listas en una sola lista.
- **Parámetros**: `lista` (list)
- **Retorna**: `list` - Lista aplanada
- **Excepciones**: `TypeError` si no es una lista

##### `obtener_unicos_ordenados(lista)`
Obtiene los elementos únicos de una lista y los retorna ordenados.
- **Parámetros**: `lista` (list)
- **Retorna**: `list` - Lista con elementos únicos ordenados
- **Excepciones**: `TypeError` si no es una lista o contiene elementos no comparables

##### `dividir_lista(lista, tamaño)`
Divide una lista en sublistas de un tamaño específico.
- **Parámetros**: `lista` (list), `tamaño` (int)
- **Retorna**: `list` - Lista de sublistas
- **Excepciones**: 
  - `TypeError` si los parámetros no son del tipo correcto
  - `ValueError` si el tamaño es menor o igual a 0

#### Ejemplos de Uso

```python
from python.ejercicio3_listas import (
    encontrar_minimo,
    ordenar_descendente,
    filtrar_impares,
    sumar_elementos,
    buscar_elemento,
    aplanar_lista,
    obtener_unicos_ordenados,
    dividir_lista
)

# Encontrar mínimo
print(encontrar_minimo([5, 2, 8, 1, 9]))                # 1

# Ordenar descendente
print(ordenar_descendente([3, 1, 4, 1, 5]))             # [5, 4, 3, 1, 1]

# Filtrar impares
print(filtrar_impares([1, 2, 3, 4, 5, 6]))              # [1, 3, 5]

# Sumar elementos
print(sumar_elementos([1, 2, 3, 4, 5]))                 # 15

# Buscar elemento
print(buscar_elemento([1, 2, 3, 4, 5], 3))              # 2 (índice)

# Aplanar lista
print(aplanar_lista([[1, 2], [3, 4], [5]]))             # [1, 2, 3, 4, 5]

# Obtener únicos ordenados
print(obtener_unicos_ordenados([3, 1, 2, 1, 3, 2]))     # [1, 2, 3]

# Dividir lista
print(dividir_lista([1, 2, 3, 4, 5, 6], 2))             # [[1, 2], [3, 4], [5, 6]]
```

#### Pruebas (40 tests)
- ✅ Búsqueda de mínimo con números positivos, negativos y mixtos
- ✅ Ordenamiento descendente sin modificar lista original
- ✅ Filtrado de impares incluyendo negativos
- ✅ Suma de elementos con diferentes tipos de números
- ✅ Búsqueda de elementos con índices
- ✅ Aplanamiento de listas anidadas
- ✅ Obtención de únicos con ordenamiento
- ✅ División de listas en partes iguales

## 📊 Estadísticas

| Ejercicio | Funciones | Pruebas | Líneas de Código |
|-----------|-----------|---------|------------------|
| Geometría | 5 | 25 | ~130 |
| Texto | 7 | 35 | ~150 |
| Listas | 8 | 40 | ~200 |
| **TOTAL** | **20** | **100** | **~480** |

## 🎯 Cobertura de Pruebas

- **Cobertura total**: >95%
- **Casos normales**: ✅ Cubiertos
- **Casos límite**: ✅ Cubiertos
- **Validación de errores**: ✅ Cubierta
- **Validación de tipos**: ✅ Cubierta

## 🛠️ Tecnologías

- **Python**: v3.8+
- **pytest**: v7.4.3
- **pytest-cov**: v4.1.0

## 📖 Documentación

Todo el código está documentado con **Docstrings**:

```python
"""
Descripción de la función

Args:
    nombre (type): Descripción del parámetro

Returns:
    type: Descripción del retorno

Raises:
    ErrorType: Descripción del error
"""
```

## ✅ Buenas Prácticas Implementadas

1. ✅ **Validación de tipos** en todas las funciones
2. ✅ **Manejo de errores** con excepciones descriptivas
3. ✅ **Inmutabilidad** - No se modifican los parámetros originales
4. ✅ **Nombres descriptivos** - snake_case para funciones y variables
5. ✅ **Pruebas exhaustivas** - Casos normales, límite y errores
6. ✅ **Documentación completa** - Docstrings en todas las funciones
7. ✅ **Type hints** - Tipos de datos claros en la documentación

## 🔗 Ver También

- **[README principal](../README.md)** - Documentación general del proyecto
- **[Ejercicios JavaScript](../javascript/README.md)** - Ejercicios en JavaScript
- **[Ejemplos Python](./EJEMPLOS.md)** - Más ejemplos de uso

---

**¡Feliz Testing con Python! 🧪✨**
