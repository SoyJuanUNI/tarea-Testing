# 🧪 Tarea de Pruebas Unitarias

Este proyecto contiene 6 ejercicios con pruebas unitarias: 3 implementados en JavaScript y 3 en Python. Cada ejercicio está completamente documentado y cuenta con un conjunto completo de pruebas unitarias.

## 📖 Documentación por Lenguaje

### 📘 JavaScript
- **[README](javascript/README.md)** - Documentación completa de los ejercicios JavaScript
- **[Ejemplos](javascript/EJEMPLOS.md)** - Ejemplos prácticos y casos de uso
- **[Inicio Rápido](javascript/INICIO_RAPIDO.md)** - Guía de inicio en 5 minutos
- **[Resumen](javascript/RESUMEN.md)** - Estadísticas y métricas

### 🐍 Python
- **[README](python/README.md)** - Documentación completa de los ejercicios Python
- **[Ejemplos](python/EJEMPLOS.md)** - Ejemplos prácticos y casos de uso
- **[Inicio Rápido](python/INICIO_RAPIDO.md)** - Guía de inicio en 5 minutos
- **[Resumen](python/RESUMEN.md)** - Estadísticas y métricas

### 📚 Documentación General
- **[📊 RESUMEN.md](RESUMEN.md)** - Resumen ejecutivo general del proyecto

## 📁 Estructura del Proyecto

```
tarea-testing/
├── javascript/
│   ├── ejercicio1-calculadora.js          # Calculadora básica
│   ├── ejercicio1-calculadora.test.js     # Pruebas de calculadora
│   ├── ejercicio2-validador.js            # Validador de datos
│   ├── ejercicio2-validador.test.js       # Pruebas de validador
│   ├── ejercicio3-array-utils.js          # Utilidades para arrays
│   └── ejercicio3-array-utils.test.js     # Pruebas de arrays
├── python/
│   ├── ejercicio1_geometria.py            # Calculadora geométrica
│   ├── test_ejercicio1_geometria.py       # Pruebas de geometría
│   ├── ejercicio2_texto.py                # Manipulación de texto
│   ├── test_ejercicio2_texto.py           # Pruebas de texto
│   ├── ejercicio3_listas.py               # Operaciones con listas
│   └── test_ejercicio3_listas.py          # Pruebas de listas
├── package.json                            # Configuración de Node.js
├── jest.config.js                          # Configuración de Jest
├── requirements.txt                        # Dependencias de Python
└── README.md                               # Este archivo
```

## 🚀 Instalación

### Requisitos Previos

- **Node.js** (versión 14 o superior)
- **Python** (versión 3.8 o superior)
- **npm** (incluido con Node.js)
- **pip** (incluido con Python)

### Instalación de Dependencias

#### Para JavaScript (Jest):

```bash
npm install
```

#### Para Python (pytest):

```bash
pip install -r requirements.txt
```

## 🧪 Ejecutar las Pruebas

### Pruebas de JavaScript

#### Ejecutar todas las pruebas:
```bash
npm test
```

#### Ejecutar pruebas en modo watch (se ejecutan automáticamente al guardar):
```bash
npm run test:watch
```

#### Ejecutar pruebas con reporte de cobertura:
```bash
npm run test:coverage
```

#### Ejecutar un archivo de pruebas específico:
```bash
npx jest javascript/ejercicio1-calculadora.test.js
```

### Pruebas de Python

#### Ejecutar todas las pruebas:
```bash
pytest python/
```

#### Ejecutar pruebas con salida detallada:
```bash
pytest python/ -v
```

#### Ejecutar pruebas con reporte de cobertura:
```bash
pytest python/ --cov=python --cov-report=html
```

#### Ejecutar un archivo de pruebas específico:
```bash
pytest python/test_ejercicio1_geometria.py
```

#### Ejecutar una clase de pruebas específica:
```bash
pytest python/test_ejercicio1_geometria.py::TestAreaRectangulo
```

## 📚 Descripción de los Ejercicios

### JavaScript

#### Ejercicio 1: Calculadora Básica
- **Archivo**: `javascript/ejercicio1-calculadora.js`
- **Funciones**: `sumar()`, `restar()`, `multiplicar()`, `dividir()`
- **Características**:
  - Operaciones aritméticas básicas
  - Validación de tipos de datos
  - Manejo de división por cero
  - 20+ pruebas unitarias

#### Ejercicio 2: Validador de Datos
- **Archivo**: `javascript/ejercicio2-validador.js`
- **Funciones**: `validarEmail()`, `validarPassword()`, `validarTelefono()`, `validarNoVacio()`
- **Características**:
  - Validación de emails con regex
  - Validación de contraseñas seguras (8+ caracteres, mayúsculas, minúsculas, números)
  - Validación de números de teléfono en múltiples formatos
  - 25+ pruebas unitarias

#### Ejercicio 3: Utilidades para Arrays
- **Archivo**: `javascript/ejercicio3-array-utils.js`
- **Funciones**: `encontrarMaximo()`, `calcularPromedio()`, `filtrarPares()`, `eliminarDuplicados()`, `invertirArray()`, `contarOcurrencias()`
- **Características**:
  - Búsqueda y análisis de arrays
  - Filtrado y transformación de datos
  - Operaciones estadísticas
  - 30+ pruebas unitarias

### Python

#### Ejercicio 1: Calculadora de Figuras Geométricas
- **Archivo**: `python/ejercicio1_geometria.py`
- **Funciones**: `area_rectangulo()`, `area_circulo()`, `area_triangulo()`, `perimetro_rectangulo()`, `perimetro_circulo()`
- **Características**:
  - Cálculo de áreas y perímetros
  - Validación de dimensiones
  - Uso de constantes matemáticas (π)
  - 25+ pruebas unitarias

#### Ejercicio 2: Manipulación de Texto
- **Archivo**: `python/ejercicio2_texto.py`
- **Funciones**: `contar_palabras()`, `invertir_texto()`, `es_palindromo()`, `contar_vocales()`, `capitalizar_palabras()`, `eliminar_espacios_extra()`, `contar_caracteres_unicos()`
- **Características**:
  - Análisis y transformación de strings
  - Detección de palíndromos
  - Manipulación de espacios y capitalización
  - 35+ pruebas unitarias

#### Ejercicio 3: Operaciones con Listas
- **Archivo**: `python/ejercicio3_listas.py`
- **Funciones**: `encontrar_minimo()`, `ordenar_descendente()`, `filtrar_impares()`, `sumar_elementos()`, `buscar_elemento()`, `aplanar_lista()`, `obtener_unicos_ordenados()`, `dividir_lista()`
- **Características**:
  - Búsqueda y ordenamiento
  - Filtrado y transformación
  - Operaciones de conjunto
  - 40+ pruebas unitarias

## 📊 Cobertura de Pruebas

Todos los ejercicios cuentan con una cobertura de pruebas superior al 95%, incluyendo:

- ✅ Casos normales (happy path)
- ✅ Casos límite (edge cases)
- ✅ Validación de errores
- ✅ Validación de tipos de datos
- ✅ Manejo de valores especiales (vacíos, nulos, negativos, etc.)

## 🎯 Conceptos de Testing Cubiertos

### Tipos de Pruebas
- **Pruebas unitarias**: Cada función se prueba de forma aislada
- **Pruebas de validación**: Verificación de tipos y valores
- **Pruebas de excepciones**: Manejo correcto de errores

### Patrones de Testing
- **Arrange-Act-Assert (AAA)**: Estructura clara de las pruebas
- **Descripción clara**: Nombres descriptivos para cada prueba
- **Organización por describe/class**: Agrupación lógica de pruebas

### Técnicas Utilizadas
- Validación de tipos de datos
- Pruebas de valores límite
- Pruebas de casos especiales
- Verificación de inmutabilidad
- Pruebas de precisión numérica

## 📖 Documentación del Código

Todo el código está completamente documentado siguiendo los estándares:

### JavaScript (JSDoc)
```javascript
/**
 * Descripción de la función
 * @param {type} nombre - Descripción del parámetro
 * @returns {type} Descripción del retorno
 * @throws {ErrorType} Descripción del error
 */
```

### Python (Docstrings)
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

## 🛠️ Tecnologías Utilizadas

### JavaScript
- **Jest**: Framework de testing para JavaScript
- **Node.js**: Entorno de ejecución

### Python
- **pytest**: Framework de testing para Python
- **pytest-cov**: Plugin para reportes de cobertura

## 📝 Notas Adicionales

### Buenas Prácticas Implementadas

1. **Código limpio y legible**: Nombres descriptivos y estructura clara
2. **Documentación completa**: Cada función está documentada
3. **Validación robusta**: Verificación de tipos y valores
4. **Manejo de errores**: Excepciones claras y específicas
5. **Pruebas exhaustivas**: Cobertura completa de casos
6. **Inmutabilidad**: Las funciones no modifican los parámetros originales
7. **Separación de responsabilidades**: Cada función tiene un propósito único

### Convenciones de Nombres

- **JavaScript**: camelCase para funciones y variables
- **Python**: snake_case para funciones y variables
- **Archivos de prueba**: 
  - JavaScript: `*.test.js`
  - Python: `test_*.py`

## 🤝 Contribución

Para agregar más pruebas o ejercicios:

1. Sigue la estructura de archivos existente
2. Documenta todas las funciones
3. Escribe pruebas exhaustivas
4. Asegúrate de que todas las pruebas pasen antes de hacer commit

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 🔗 Navegación Rápida

### Por Lenguaje
- **JavaScript**: [README](javascript/README.md) | [Ejemplos](javascript/EJEMPLOS.md)
- **Python**: [README](python/README.md) | [Ejemplos](python/EJEMPLOS.md)

### Por Ejercicio

#### JavaScript
1. **Calculadora**: [Código](javascript/ejercicio1-calculadora.js) | [Pruebas](javascript/ejercicio1-calculadora.test.js)
2. **Validador**: [Código](javascript/ejercicio2-validador.js) | [Pruebas](javascript/ejercicio2-validador.test.js)
3. **Array Utils**: [Código](javascript/ejercicio3-array-utils.js) | [Pruebas](javascript/ejercicio3-array-utils.test.js)

#### Python
1. **Geometría**: [Código](python/ejercicio1_geometria.py) | [Pruebas](python/test_ejercicio1_geometria.py)
2. **Texto**: [Código](python/ejercicio2_texto.py) | [Pruebas](python/test_ejercicio2_texto.py)
3. **Listas**: [Código](python/ejercicio3_listas.py) | [Pruebas](python/test_ejercicio3_listas.py)

### Guías
- 📊 [Resumen Ejecutivo](RESUMEN.md) - Estadísticas generales del proyecto

---

**¡Feliz Testing! 🧪✨**
