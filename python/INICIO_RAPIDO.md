# 🚀 Inicio Rápido - Python

Guía rápida para empezar con los ejercicios de Python en menos de 5 minutos.

## ⚡ Instalación Rápida

### Paso 1: Verificar Python
```bash
python --version
# o
python3 --version
```
Si no tienes Python instalado, descárgalo de [python.org](https://www.python.org/)

### Paso 2: Instalar Dependencias
Desde la raíz del proyecto:
```bash
pip install -r requirements.txt
```

## 🧪 Ejecutar Pruebas

### Opción 1: Todas las Pruebas de Python
```bash
pytest python/
```

### Opción 2: Pruebas con Salida Detallada
```bash
pytest python/ -v
```

### Opción 3: Pruebas Específicas
```bash
# Ejercicio 1 - Geometría
pytest python/test_ejercicio1_geometria.py -v

# Ejercicio 2 - Texto
pytest python/test_ejercicio2_texto.py -v

# Ejercicio 3 - Listas
pytest python/test_ejercicio3_listas.py -v
```

### Opción 4: Con Cobertura
```bash
pytest python/ --cov=python --cov-report=html
```

### Opción 5: Ejecutar una Clase de Pruebas Específica
```bash
pytest python/test_ejercicio1_geometria.py::TestAreaRectangulo -v
```

## 📊 Ver Resultados

Después de ejecutar las pruebas, verás algo como:

```
test_ejercicio1_geometria.py ✓✓✓✓✓ (25 passed)
test_ejercicio2_texto.py ✓✓✓✓✓✓✓ (35 passed)
test_ejercicio3_listas.py ✓✓✓✓✓✓✓✓ (40 passed)

======================== 100 passed in 0.5s ========================
```

## 📚 Explorar el Código

### Ejercicio 1: Geometría
```bash
# Ver el código
code python/ejercicio1_geometria.py

# Ver las pruebas
code python/test_ejercicio1_geometria.py
```

**Funciones disponibles:**
- `area_rectangulo(base, altura)` - Calcula área de rectángulo
- `area_circulo(radio)` - Calcula área de círculo
- `area_triangulo(base, altura)` - Calcula área de triángulo
- `perimetro_rectangulo(base, altura)` - Calcula perímetro de rectángulo
- `perimetro_circulo(radio)` - Calcula perímetro de círculo

### Ejercicio 2: Texto
```bash
# Ver el código
code python/ejercicio2_texto.py
```

**Funciones disponibles:**
- `contar_palabras(texto)` - Cuenta palabras
- `invertir_texto(texto)` - Invierte el texto
- `es_palindromo(texto)` - Verifica si es palíndromo
- `contar_vocales(texto)` - Cuenta vocales
- `capitalizar_palabras(texto)` - Capitaliza palabras
- `eliminar_espacios_extra(texto)` - Elimina espacios extra
- `contar_caracteres_unicos(texto)` - Cuenta caracteres únicos

### Ejercicio 3: Listas
```bash
# Ver el código
code python/ejercicio3_listas.py
```

**Funciones disponibles:**
- `encontrar_minimo(lista)` - Encuentra el mínimo
- `ordenar_descendente(lista)` - Ordena descendente
- `filtrar_impares(lista)` - Filtra impares
- `sumar_elementos(lista)` - Suma elementos
- `buscar_elemento(lista, elemento)` - Busca elemento
- `aplanar_lista(lista)` - Aplana lista de listas
- `obtener_unicos_ordenados(lista)` - Obtiene únicos ordenados
- `dividir_lista(lista, tamaño)` - Divide lista

## 💡 Ejemplo Rápido

Crea un archivo `test.py` en la raíz:

```python
from python.ejercicio1_geometria import area_rectangulo, area_circulo
from python.ejercicio2_texto import contar_palabras, es_palindromo
from python.ejercicio3_listas import encontrar_minimo

# Geometría
print('Área rectángulo 5x3:', area_rectangulo(5, 3))      # 15
print('Área círculo radio 5:', area_circulo(5))           # 78.54...

# Texto
print('Palabras:', contar_palabras("Hola mundo"))         # 2
print('Es palíndromo?', es_palindromo("oso"))             # True

# Listas
print('Mínimo:', encontrar_minimo([5, 2, 8, 1, 9]))       # 1
```

Ejecuta:
```bash
python test.py
```

## 📖 Documentación Completa

- **[README Python](README.md)** - Documentación completa
- **[Ejemplos Python](EJEMPLOS.md)** - Casos de uso prácticos

## ✅ Verificación Rápida

Para verificar que todo funciona:

```bash
# Ejecutar una prueba específica
pytest python/test_ejercicio1_geometria.py -v
```

Si ves `✓ PASSED`, ¡todo está funcionando correctamente! ✨

## 🎯 Próximos Pasos

1. ✅ Instalar dependencias con `pip install -r requirements.txt`
2. ✅ Ejecutar pruebas con `pytest python/`
3. 📖 Leer [README.md](README.md) para documentación completa
4. 💡 Ver [EJEMPLOS.md](EJEMPLOS.md) para casos de uso
5. 🔧 Modificar el código y ver cómo fallan las pruebas
6. 🧪 Agregar tus propias pruebas

## 💡 Consejos

- **Usa `-v`** para ver detalles de cada prueba
- **Usa `--cov`** para ver la cobertura de código
- **Revisa los docstrings** en el código para entender cada función
- **Experimenta modificando** las funciones para ver cómo fallan las pruebas
- **Consulta EJEMPLOS.md** para ver casos de uso reales

## 🆘 Problemas Comunes

### Error: "No module named 'pytest'"
```bash
pip install -r requirements.txt
```

### Error: "python: command not found"
Usa `python3` en lugar de `python`:
```bash
python3 --version
pip3 install -r requirements.txt
pytest python/
```

### Error: "ModuleNotFoundError: No module named 'python'"
Asegúrate de ejecutar pytest desde la raíz del proyecto:
```bash
# Verifica que estás en la raíz
pwd  # o cd en Windows

# Ejecuta desde la raíz
pytest python/
```

### Las pruebas no se ejecutan
```bash
# Reinstala dependencias
pip uninstall pytest pytest-cov
pip install -r requirements.txt
```

---

**¡Listo para empezar con Python! 🎉**
