# 💡 Ejemplos de Uso - Python

Ejemplos prácticos y casos de uso reales para las funciones de Python.

## 🐍 Ejercicio 1: Calculadora de Figuras Geométricas

### Uso Básico

```python
from python.ejercicio1_geometria import (
    area_rectangulo,
    area_circulo,
    area_triangulo,
    perimetro_rectangulo,
    perimetro_circulo
)

# Áreas
print(area_rectangulo(5, 3))          # 15
print(area_circulo(5))                # 78.53981633974483
print(area_triangulo(6, 4))           # 12.0

# Perímetros
print(perimetro_rectangulo(5, 3))     # 16
print(perimetro_circulo(5))           # 31.41592653589793
```

### Trabajando con Decimales

```python
import math

# Cálculos precisos
radio = 2.5
area = area_circulo(radio)
perimetro = perimetro_circulo(radio)

print(f"Radio: {radio}")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
```

### Manejo de Errores

```python
# Dimensiones negativas
try:
    area = area_rectangulo(-5, 3)
except ValueError as e:
    print(f"Error: {e}")
    # "Las dimensiones no pueden ser negativas"

# Tipo de dato incorrecto
try:
    area = area_circulo("5")
except TypeError as e:
    print(f"Error: {e}")
    # "El radio debe ser un número"
```

### Caso de Uso: Calculadora de Materiales para Construcción

```python
from python.ejercicio1_geometria import (
    area_rectangulo,
    area_circulo,
    perimetro_rectangulo
)

def calcular_materiales_habitacion(largo, ancho, precio_piso_m2, precio_rodapie_m):
    """Calcula materiales necesarios para una habitación"""
    
    # Área del piso
    area_piso = area_rectangulo(largo, ancho)
    costo_piso = area_piso * precio_piso_m2
    
    # Perímetro para rodapié
    perimetro = perimetro_rectangulo(largo, ancho)
    costo_rodapie = perimetro * precio_rodapie_m
    
    return {
        'area_piso_m2': area_piso,
        'perimetro_m': perimetro,
        'costo_piso': costo_piso,
        'costo_rodapie': costo_rodapie,
        'costo_total': costo_piso + costo_rodapie
    }

# Habitación de 5m x 4m
resultado = calcular_materiales_habitacion(5, 4, 25, 5)
print(resultado)
"""
{
    'area_piso_m2': 20,
    'perimetro_m': 18,
    'costo_piso': 500,
    'costo_rodapie': 90,
    'costo_total': 590
}
"""
```

### Caso de Uso: Calculadora de Jardín Circular

```python
from python.ejercicio1_geometria import area_circulo, perimetro_circulo

def planificar_jardin_circular(radio, precio_cesped_m2, precio_cerca_m):
    """Planifica un jardín circular"""
    
    area = area_circulo(radio)
    perimetro = perimetro_circulo(radio)
    
    costo_cesped = area * precio_cesped_m2
    costo_cerca = perimetro * precio_cerca_m
    
    return {
        'radio_m': radio,
        'area_m2': round(area, 2),
        'perimetro_m': round(perimetro, 2),
        'costo_cesped': round(costo_cesped, 2),
        'costo_cerca': round(costo_cerca, 2),
        'costo_total': round(costo_cesped + costo_cerca, 2)
    }

jardin = planificar_jardin_circular(3, 15, 20)
print(jardin)
```

---

## 🐍 Ejercicio 2: Manipulación de Texto

### Análisis de Texto Básico

```python
from python.ejercicio2_texto import (
    contar_palabras,
    contar_vocales,
    contar_caracteres_unicos
)

texto = "Python es un lenguaje de programación"

print(f"Palabras: {contar_palabras(texto)}")              # 6
print(f"Vocales: {contar_vocales(texto)}")                # 13
print(f"Caracteres únicos: {contar_caracteres_unicos(texto)}")  # 20
```

### Detección de Palíndromos

```python
from python.ejercicio2_texto import es_palindromo

# Palíndromos famosos
palindromos = [
    "anita lava la tina",
    "A man a plan a canal Panama",
    "Dábale arroz a la zorra el abad",
    "reconocer",
    "oso"
]

for texto in palindromos:
    resultado = "✓" if es_palindromo(texto) else "✗"
    print(f"{resultado} {texto}")
```

### Limpieza y Formato de Texto

```python
from python.ejercicio2_texto import (
    eliminar_espacios_extra,
    capitalizar_palabras,
    invertir_texto
)

# Texto con formato inconsistente
texto_sucio = "  hola    mundo   desde   python  "

# Limpiar y formatear
texto_limpio = eliminar_espacios_extra(texto_sucio)
texto_capitalizado = capitalizar_palabras(texto_limpio)

print(f"Original: '{texto_sucio}'")
print(f"Limpio: '{texto_limpio}'")
print(f"Capitalizado: '{texto_capitalizado}'")
```

### Caso de Uso: Analizador de Comentarios

```python
from python.ejercicio2_texto import (
    contar_palabras,
    contar_vocales,
    eliminar_espacios_extra,
    validar_no_vacio
)

def analizar_comentario(comentario):
    """Analiza un comentario de usuario"""
    
    # Limpiar el comentario
    comentario_limpio = eliminar_espacios_extra(comentario)
    
    # Validar que no esté vacío
    if not comentario_limpio:
        return {'valido': False, 'error': 'Comentario vacío'}
    
    # Análisis
    num_palabras = contar_palabras(comentario_limpio)
    num_vocales = contar_vocales(comentario_limpio)
    
    # Validaciones
    if num_palabras < 3:
        return {
            'valido': False,
            'error': 'El comentario debe tener al menos 3 palabras'
        }
    
    if num_palabras > 100:
        return {
            'valido': False,
            'error': 'El comentario no debe exceder 100 palabras'
        }
    
    return {
        'valido': True,
        'comentario': comentario_limpio,
        'palabras': num_palabras,
        'vocales': num_vocales,
        'caracteres': len(comentario_limpio)
    }

# Ejemplo
comentario = "Este es un excelente producto, muy recomendado"
resultado = analizar_comentario(comentario)
print(resultado)
```

### Caso de Uso: Procesador de Títulos

```python
from python.ejercicio2_texto import (
    capitalizar_palabras,
    eliminar_espacios_extra
)

def procesar_titulo(titulo):
    """Procesa y formatea un título"""
    
    # Limpiar espacios
    titulo = eliminar_espacios_extra(titulo)
    
    # Capitalizar
    titulo = capitalizar_palabras(titulo)
    
    return titulo

titulos = [
    "  introducción   a   python  ",
    "guía de PRUEBAS unitarias",
    "mejores    prácticas    de    programación"
]

for titulo in titulos:
    print(f"Original: '{titulo}'")
    print(f"Procesado: '{procesar_titulo(titulo)}'")
    print()
```

### Caso de Uso: Contador de Estadísticas de Texto

```python
from python.ejercicio2_texto import (
    contar_palabras,
    contar_vocales,
    contar_caracteres_unicos
)

def estadisticas_texto(texto):
    """Genera estadísticas completas de un texto"""
    
    palabras = contar_palabras(texto)
    vocales = contar_vocales(texto)
    caracteres_unicos = contar_caracteres_unicos(texto)
    caracteres_totales = len(texto)
    
    # Calcular porcentajes
    porcentaje_vocales = (vocales / caracteres_totales * 100) if caracteres_totales > 0 else 0
    
    return {
        'palabras': palabras,
        'caracteres_totales': caracteres_totales,
        'caracteres_unicos': caracteres_unicos,
        'vocales': vocales,
        'porcentaje_vocales': round(porcentaje_vocales, 2),
        'promedio_caracteres_por_palabra': round(caracteres_totales / palabras, 2) if palabras > 0 else 0
    }

texto = "Python es un lenguaje de programación interpretado"
stats = estadisticas_texto(texto)
print(stats)
```

---

## 🐍 Ejercicio 3: Operaciones con Listas

### Operaciones Básicas

```python
from python.ejercicio3_listas import (
    encontrar_minimo,
    ordenar_descendente,
    filtrar_impares,
    sumar_elementos
)

numeros = [5, 2, 8, 1, 9, 3, 7]

print(f"Mínimo: {encontrar_minimo(numeros)}")           # 1
print(f"Suma: {sumar_elementos(numeros)}")              # 35
print(f"Ordenado: {ordenar_descendente(numeros)}")      # [9, 8, 7, 5, 3, 2, 1]
print(f"Impares: {filtrar_impares(numeros)}")           # [5, 1, 9, 3, 7]
```

### Caso de Uso: Análisis de Calificaciones

```python
from python.ejercicio3_listas import (
    encontrar_minimo,
    sumar_elementos,
    ordenar_descendente
)

def analizar_calificaciones(calificaciones):
    """Analiza un conjunto de calificaciones de estudiantes"""
    
    if not calificaciones:
        return {'error': 'No hay calificaciones'}
    
    total_estudiantes = len(calificaciones)
    suma_total = sumar_elementos(calificaciones)
    promedio = suma_total / total_estudiantes
    
    # Encontrar máximo y mínimo
    ordenadas = ordenar_descendente(calificaciones)
    maxima = ordenadas[0]
    minima = encontrar_minimo(calificaciones)
    
    # Contar aprobados (>= 60)
    aprobados = [c for c in calificaciones if c >= 60]
    reprobados = total_estudiantes - len(aprobados)
    
    return {
        'total_estudiantes': total_estudiantes,
        'promedio': round(promedio, 2),
        'calificacion_maxima': maxima,
        'calificacion_minima': minima,
        'aprobados': len(aprobados),
        'reprobados': reprobados,
        'porcentaje_aprobacion': round(len(aprobados) / total_estudiantes * 100, 2)
    }

calificaciones = [85, 92, 78, 95, 88, 76, 90, 55, 82, 70]
resultado = analizar_calificaciones(calificaciones)
print(resultado)
```

### Caso de Uso: Procesamiento de Datos de Ventas

```python
from python.ejercicio3_listas import (
    obtener_unicos_ordenados,
    sumar_elementos,
    dividir_lista
)

def procesar_ventas_mensuales(ventas):
    """Procesa datos de ventas mensuales"""
    
    # Eliminar duplicados y ordenar
    ventas_unicas = obtener_unicos_ordenados(ventas)
    
    # Calcular totales
    total = sumar_elementos(ventas)
    promedio = total / len(ventas)
    
    # Dividir en semanas (grupos de 7)
    ventas_por_semana = dividir_lista(ventas, 7)
    
    # Calcular promedio por semana
    promedios_semanales = []
    for semana in ventas_por_semana:
        if semana:
            prom = sumar_elementos(semana) / len(semana)
            promedios_semanales.append(round(prom, 2))
    
    return {
        'total_ventas': total,
        'promedio_diario': round(promedio, 2),
        'ventas_unicas': ventas_unicas,
        'numero_semanas': len(ventas_por_semana),
        'promedios_semanales': promedios_semanales
    }

# Ventas diarias del mes (30 días)
ventas = [100, 150, 200, 150, 300, 100, 250, 200, 180, 220,
          190, 210, 230, 200, 180, 160, 170, 190, 200, 210,
          220, 230, 240, 250, 260, 270, 280, 290, 300, 310]

resultado = procesar_ventas_mensuales(ventas)
print(resultado)
```

### Caso de Uso: Gestión de Inventario

```python
from python.ejercicio3_listas import (
    buscar_elemento,
    aplanar_lista,
    obtener_unicos_ordenados
)

def gestionar_inventario(productos_por_categoria):
    """Gestiona inventario de productos por categoría"""
    
    # Aplanar todas las categorías
    todos_productos = aplanar_lista(productos_por_categoria)
    
    # Obtener productos únicos
    productos_unicos = obtener_unicos_ordenados(todos_productos)
    
    # Contar cada producto
    inventario = {}
    for producto in productos_unicos:
        cantidad = todos_productos.count(producto)
        inventario[producto] = cantidad
    
    return {
        'total_items': len(todos_productos),
        'productos_unicos': len(productos_unicos),
        'inventario': inventario
    }

# Productos por categoría
productos = [
    ['manzana', 'pera', 'manzana'],      # Frutas
    ['zanahoria', 'lechuga'],             # Verduras
    ['manzana', 'pera', 'naranja']        # Más frutas
]

resultado = gestionar_inventario(productos)
print(resultado)
```

### Caso de Uso: Análisis de Encuestas

```python
from python.ejercicio3_listas import (
    obtener_unicos_ordenados,
    buscar_elemento
)

def analizar_encuesta(respuestas):
    """Analiza respuestas de una encuesta"""
    
    # Obtener respuestas únicas
    opciones = obtener_unicos_ordenados(respuestas)
    
    # Contar cada respuesta
    resultados = {}
    total = len(respuestas)
    
    for opcion in opciones:
        cantidad = respuestas.count(opcion)
        porcentaje = (cantidad / total) * 100
        resultados[opcion] = {
            'cantidad': cantidad,
            'porcentaje': round(porcentaje, 2)
        }
    
    return {
        'total_respuestas': total,
        'opciones': opciones,
        'resultados': resultados
    }

# Respuestas de satisfacción (1-5)
respuestas = [5, 4, 5, 3, 5, 4, 5, 4, 3, 5, 4, 5, 5, 4, 3]
resultado = analizar_encuesta(respuestas)
print(resultado)
```

### Composición de Funciones

```python
from python.ejercicio3_listas import (
    filtrar_impares,
    ordenar_descendente,
    sumar_elementos
)

# Combinar múltiples funciones
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar impares, ordenar y sumar
impares = filtrar_impares(numeros)
impares_ordenados = ordenar_descendente(impares)
suma_impares = sumar_elementos(impares)

print(f"Números originales: {numeros}")
print(f"Impares: {impares}")
print(f"Impares ordenados: {impares_ordenados}")
print(f"Suma de impares: {suma_impares}")
```

### Inmutabilidad

```python
from python.ejercicio3_listas import ordenar_descendente

# Las funciones no modifican la lista original
original = [3, 1, 4, 1, 5, 9, 2, 6]
ordenada = ordenar_descendente(original)

print(f"Original: {original}")    # [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Ordenada: {ordenada}")    # [9, 6, 5, 4, 3, 2, 1, 1]

# La lista original permanece sin cambios
```

## 🎯 Consejos de Uso

### 1. Siempre Valida las Entradas

```python
def procesar_datos(datos):
    """Procesa datos con validación"""
    
    if not isinstance(datos, list):
        raise TypeError("Se esperaba una lista")
    
    if not datos:
        raise ValueError("La lista no puede estar vacía")
    
    # Procesar datos...
    return sumar_elementos(datos)
```

### 2. Maneja los Errores Apropiadamente

```python
try:
    resultado = encontrar_minimo([])
except ValueError as e:
    print(f"Error: {e}")
    # Tomar acción apropiada
```

### 3. Aprovecha la Composición

```python
# Combina funciones para operaciones complejas
resultado = sumar_elementos(
    filtrar_impares(
        obtener_unicos_ordenados(datos)
    )
)
```

---

**¡Explora y experimenta con las funciones! 🚀**
