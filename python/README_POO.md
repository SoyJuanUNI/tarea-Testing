# Programación Orientada a Objetos (POO) - Ejercicios de Python

## ¿Qué es la Programación Orientada a Objetos (POO)?

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que organiza el código en torno a **objetos** y **clases**. Los objetos son instancias de clases que encapsulan datos (atributos) y comportamientos (métodos) relacionados.

### Principios Fundamentales de POO:

1. **Encapsulación**: Ocultar los detalles internos de una clase y controlar el acceso a sus datos
2. **Abstracción**: Simplificar la complejidad mostrando solo las características esenciales
3. **Herencia**: Crear nuevas clases basadas en clases existentes, reutilizando código
4. **Polimorfismo**: Permitir que diferentes clases respondan al mismo mensaje de manera específica

### Ventajas de POO:

- **Reutilización de código**: Las clases pueden ser reutilizadas en diferentes contextos
- **Mantenibilidad**: El código es más fácil de mantener y modificar
- **Escalabilidad**: Fácil agregar nuevas funcionalidades sin afectar el código existente
- **Organización**: Mejor estructura y organización del código
- **Modularidad**: Cada clase tiene una responsabilidad específica

---

## Ejercicio 1: Calculadora de Figuras Geométricas

### Implementación POO:

#### Clases Creadas:

1. **`FiguraGeometrica`** (Clase Abstracta Base)
   - Define la interfaz común para todas las figuras
   - Métodos abstractos: `calcular_area()` y `calcular_perimetro()`
   - Método protegido: `_validar_numero()` para validación común

2. **`Rectangulo`** (Hereda de FiguraGeometrica)
   - Atributos: `_base`, `_altura` (privados)
   - Propiedades: `base`, `altura` (públicas)
   - Métodos: `calcular_area()`, `calcular_perimetro()`

3. **`Circulo`** (Hereda de FiguraGeometrica)
   - Atributos: `_radio` (privado)
   - Propiedades: `radio` (pública)
   - Métodos: `calcular_area()`, `calcular_perimetro()`

4. **`Triangulo`** (Hereda de FiguraGeometrica)
   - Atributos: `_base`, `_altura` (privados)
   - Propiedades: `base`, `altura` (públicas)
   - Métodos: `calcular_area()`, `calcular_perimetro()` (lanza NotImplementedError)

5. **`TrianguloCompleto`** (Hereda de Triangulo)
   - Atributos adicionales: `_lado1`, `_lado2` (privados)
   - Propiedades: `lado1`, `lado2` (públicas)
   - Implementa `calcular_perimetro()` correctamente

#### Características POO Utilizadas:

- **Herencia**: Todas las figuras heredan de `FiguraGeometrica`
- **Polimorfismo**: Todas las figuras implementan los mismos métodos con comportamientos específicos
- **Encapsulación**: Atributos privados con acceso controlado mediante propiedades
- **Abstracción**: Clase abstracta que define la interfaz común

### Pruebas Implementadas:

#### Pruebas de Funciones de Compatibilidad (25 pruebas):
- `TestAreaRectangulo`: Pruebas para área de rectángulos
- `TestAreaCirculo`: Pruebas para área de círculos
- `TestAreaTriangulo`: Pruebas para área de triángulos
- `TestPerimetroRectangulo`: Pruebas para perímetro de rectángulos
- `TestPerimetroCirculo`: Pruebas para perímetro de círculos

#### Pruebas de Clases POO (26 pruebas):
- `TestFiguraGeometrica`: Verifica que la clase abstracta no sea instanciable
- `TestRectanguloPOO`: Pruebas completas de la clase Rectangulo
- `TestCirculoPOO`: Pruebas completas de la clase Circulo
- `TestTrianguloPOO`: Pruebas completas de la clase Triangulo
- `TestTrianguloCompletoPOO`: Pruebas completas de la clase TrianguloCompleto
- `TestPolimorfismo`: Demuestra el polimorfismo entre diferentes figuras

**Total: 51 pruebas**

---

## Ejercicio 2: Manipulación de Texto

### Implementación POO:

#### Clases Creadas:

1. **`ManipuladorTexto`**
   - Responsabilidad: Transformaciones y manipulaciones de texto
   - Atributos: `_texto` (privado)
   - Propiedades: `texto` (pública con getter/setter)
   - Métodos: `invertir()`, `capitalizar_palabras()`, `eliminar_espacios_extra()`, etc.

2. **`AnalizadorTexto`**
   - Responsabilidad: Análisis y estadísticas de texto
   - Atributos: `_texto`, `_vocales` (privados)
   - Propiedades: `texto` (pública con getter/setter)
   - Métodos: `contar_palabras()`, `contar_vocales()`, `es_palindromo()`, etc.

3. **`ProcesadorTextoCompleto`**
   - Responsabilidad: Integrar manipulación y análisis
   - Composición: Usa `ManipuladorTexto` y `AnalizadorTexto` internamente
   - Método especial: `generar_reporte_completo()`

#### Características POO Utilizadas:

- **Separación de Responsabilidades**: Cada clase tiene una función específica
- **Composición**: `ProcesadorTextoCompleto` combina otras clases
- **Encapsulación**: Atributos privados con acceso controlado
- **Validación**: Métodos de validación reutilizables

### Pruebas Implementadas:

#### Pruebas de Funciones de Compatibilidad (22 pruebas):
- `TestContarPalabras`: Pruebas para contar palabras
- `TestInvertirTexto`: Pruebas para invertir texto
- `TestEsPalindromo`: Pruebas para verificar palíndromos
- `TestContarVocales`: Pruebas para contar vocales
- `TestCapitalizarPalabras`: Pruebas para capitalizar palabras
- `TestEliminarEspaciosExtra`: Pruebas para eliminar espacios extra
- `TestContarCaracteresUnicos`: Pruebas para contar caracteres únicos

#### Pruebas de Clases POO (51 pruebas):
- `TestManipuladorTexto`: Pruebas completas de manipulación de texto
- `TestAnalizadorTexto`: Pruebas completas de análisis de texto
- `TestProcesadorTextoCompleto`: Pruebas de la clase integradora
- `TestIntegracionPOO`: Pruebas de integración entre clases

**Total: 73 pruebas**

---

## Ejercicio 3: Operaciones con Listas

### Implementación POO:

#### Clases Creadas:

1. **`ManipuladorListas`**
   - Responsabilidad: Transformaciones y manipulaciones de listas
   - Atributos: `_lista` (privado)
   - Propiedades: `lista` (pública con getter/setter)
   - Métodos: `ordenar_descendente()`, `filtrar_impares()`, `aplanar()`, etc.

2. **`AnalizadorListas`**
   - Responsabilidad: Análisis y estadísticas de listas
   - Atributos: `_lista` (privado)
   - Propiedades: `lista` (pública con getter/setter)
   - Métodos: `encontrar_minimo()`, `sumar_elementos()`, `obtener_estadisticas_numericas()`, etc.

3. **`ProcesadorListasCompleto`**
   - Responsabilidad: Integrar manipulación y análisis
   - Composición: Usa `ManipuladorListas` y `AnalizadorListas` internamente
   - Método especial: `generar_reporte_completo()`

#### Características POO Utilizadas:

- **Separación de Responsabilidades**: Cada clase tiene una función específica
- **Composición**: `ProcesadorListasCompleto` combina otras clases
- **Encapsulación**: Atributos privados con acceso controlado
- **Copia Defensiva**: Protección contra modificaciones externas
- **Type Hints**: Mejor documentación y validación

### Pruebas Implementadas:

#### Pruebas de Funciones de Compatibilidad (40 pruebas):
- `TestEncontrarMinimo`: Pruebas para encontrar mínimo
- `TestOrdenarDescendente`: Pruebas para ordenar descendente
- `TestFiltrarImpares`: Pruebas para filtrar impares
- `TestSumarElementos`: Pruebas para sumar elementos
- `TestBuscarElemento`: Pruebas para buscar elementos
- `TestAplanarLista`: Pruebas para aplanar listas
- `TestObtenerUnicosOrdenados`: Pruebas para obtener únicos ordenados
- `TestDividirLista`: Pruebas para dividir listas

#### Pruebas de Clases POO (42 pruebas):
- `TestManipuladorListas`: Pruebas completas de manipulación de listas
- `TestAnalizadorListas`: Pruebas completas de análisis de listas
- `TestProcesadorListasCompleto`: Pruebas de la clase integradora
- `TestIntegracionPOO`: Pruebas de integración entre clases

**Total: 82 pruebas**

---

## Cómo Funcionan las Pruebas

### Estructura de las Pruebas:

Cada ejercicio tiene dos tipos de pruebas:

1. **Pruebas de Funciones de Compatibilidad**: Verifican que las funciones originales sigan funcionando
2. **Pruebas de Clases POO**: Verifican el funcionamiento de las nuevas clases

### Tipos de Pruebas Implementadas:

#### 1. Pruebas de Creación y Configuración:
```python
def test_creacion(self):
    """Verifica que se pueda crear la clase correctamente"""
    objeto = MiClase(datos)
    assert objeto.atributo == datos
```

#### 2. Pruebas de Funcionalidad:
```python
def test_funcionalidad(self):
    """Verifica que los métodos funcionen correctamente"""
    objeto = MiClase(datos)
    resultado = objeto.metodo()
    assert resultado == esperado
```

#### 3. Pruebas de Validación:
```python
def test_validacion(self):
    """Verifica que se validen correctamente los parámetros"""
    with pytest.raises(TypeError):
        MiClase(datos_invalidos)
```

#### 4. Pruebas de Integración:
```python
def test_integracion(self):
    """Verifica que las clases trabajen juntas correctamente"""
    # Pruebas que involucran múltiples clases
```

### Ejecución de Pruebas:

Para ejecutar todas las pruebas:
```bash
python -m pytest test_ejercicio1_geometria.py -v
python -m pytest test_ejercicio2_texto.py -v
python -m pytest test_ejercicio3_listas.py -v
```

Para ejecutar todas las pruebas de una vez:
```bash
python -m pytest -v
```

### Cobertura de Pruebas:

- **Ejercicio 1**: 51 pruebas (25 funcionales + 26 POO)
- **Ejercicio 2**: 73 pruebas (22 funcionales + 51 POO)
- **Ejercicio 3**: 82 pruebas (40 funcionales + 42 POO)
- **Total**: 206 pruebas

---

## Beneficios de la Conversión a POO

### Antes (Programación Funcional):
- Funciones independientes sin relación
- Código duplicado para validaciones
- Difícil de extender y mantener
- Sin reutilización de código

### Después (Programación Orientada a Objetos):
- Clases organizadas con responsabilidades claras
- Reutilización de código a través de herencia y composición
- Encapsulación de datos y comportamientos
- Fácil extensión y mantenimiento
- Mejor organización y estructura del código

### Funcionalidades Adicionales Agregadas:

1. **Ejercicio 1**: Clase `TrianguloCompleto` para triángulos con perímetro
2. **Ejercicio 2**: Estadísticas avanzadas, reportes completos, filtrado por condición
3. **Ejercicio 3**: Estadísticas numéricas completas, información general, reportes

### Compatibilidad Mantenida:

Todos los ejercicios mantienen **100% de compatibilidad** con el código original a través de funciones de compatibilidad que internamente usan las nuevas clases POO.

---

## Conclusión

La conversión a POO ha mejorado significativamente la calidad del código, proporcionando:

- **Mejor organización** y estructura
- **Reutilización de código** efectiva
- **Facilidad de mantenimiento** y extensión
- **Funcionalidades adicionales** sin romper compatibilidad
- **Pruebas exhaustivas** que garantizan la calidad

El código ahora es más profesional, mantenible y escalable, siguiendo las mejores prácticas de desarrollo de software.
