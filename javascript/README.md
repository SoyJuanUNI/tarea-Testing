# 📘 Ejercicios JavaScript - Pruebas Unitarias

Documentación completa de los ejercicios de JavaScript con Jest.

## 📁 Estructura

```
javascript/
├── ejercicio1-calculadora.js          # Calculadora básica
├── ejercicio1-calculadora.test.js     # Pruebas de calculadora
├── ejercicio2-validador.js            # Validador de datos
├── ejercicio2-validador.test.js       # Pruebas de validador
├── ejercicio3-array-utils.js          # Utilidades para arrays
├── ejercicio3-array-utils.test.js     # Pruebas de arrays
└── README.md                           # Este archivo
```

## 🚀 Instalación

### Requisitos Previos
- **Node.js** (versión 14 o superior)
- **npm** (incluido con Node.js)

### Instalar Dependencias

Desde la raíz del proyecto:
```bash
npm install
```

## 🧪 Ejecutar las Pruebas

### Todas las pruebas de JavaScript:
```bash
npm test
```

### Pruebas en modo watch (se ejecutan automáticamente al guardar):
```bash
npm run test:watch
```

### Pruebas con reporte de cobertura:
```bash
npm run test:coverage
```

### Ejecutar un archivo de pruebas específico:
```bash
# Ejercicio 1
npx jest javascript/ejercicio1-calculadora.test.js

# Ejercicio 2
npx jest javascript/ejercicio2-validador.test.js

# Ejercicio 3
npx jest javascript/ejercicio3-array-utils.test.js
```

## 📚 Ejercicios

### Ejercicio 1: Calculadora Básica

**Archivo**: `ejercicio1-calculadora.js`

#### Funciones Implementadas

##### `sumar(a, b)`
Suma dos números.
- **Parámetros**: `a` (number), `b` (number)
- **Retorna**: `number` - La suma de a y b
- **Excepciones**: `TypeError` si los parámetros no son números

##### `restar(a, b)`
Resta dos números.
- **Parámetros**: `a` (number), `b` (number)
- **Retorna**: `number` - La resta de a menos b
- **Excepciones**: `TypeError` si los parámetros no son números

##### `multiplicar(a, b)`
Multiplica dos números.
- **Parámetros**: `a` (number), `b` (number)
- **Retorna**: `number` - El producto de a y b
- **Excepciones**: `TypeError` si los parámetros no son números

##### `dividir(a, b)`
Divide dos números.
- **Parámetros**: `a` (number), `b` (number)
- **Retorna**: `number` - El cociente de a dividido por b
- **Excepciones**: 
  - `TypeError` si los parámetros no son números
  - `Error` si el divisor es cero

#### Ejemplos de Uso

```javascript
const { sumar, restar, multiplicar, dividir } = require('./ejercicio1-calculadora');

// Suma
console.log(sumar(5, 3));        // 8
console.log(sumar(-5, 3));       // -2

// Resta
console.log(restar(10, 3));      // 7

// Multiplicación
console.log(multiplicar(4, 5));  // 20

// División
console.log(dividir(10, 2));     // 5

// Manejo de errores
try {
    dividir(10, 0);
} catch (error) {
    console.log(error.message);  // "No se puede dividir por cero"
}
```

#### Pruebas (20 tests)
- ✅ Suma de números positivos y negativos
- ✅ Resta con resultados positivos y negativos
- ✅ Multiplicación con cero y números negativos
- ✅ División con decimales
- ✅ Validación de división por cero
- ✅ Validación de tipos de datos

---

### Ejercicio 2: Validador de Datos

**Archivo**: `ejercicio2-validador.js`

#### Funciones Implementadas

##### `validarEmail(email)`
Valida si un email tiene un formato correcto.
- **Parámetros**: `email` (string)
- **Retorna**: `boolean` - true si es válido, false en caso contrario
- **Formato aceptado**: `usuario@dominio.com`

##### `validarPassword(password)`
Valida si una contraseña cumple con los requisitos de seguridad.
- **Parámetros**: `password` (string)
- **Retorna**: `boolean` - true si es válida, false en caso contrario
- **Requisitos**:
  - Mínimo 8 caracteres
  - Al menos una letra mayúscula
  - Al menos una letra minúscula
  - Al menos un número

##### `validarTelefono(telefono)`
Valida si un número de teléfono tiene un formato correcto.
- **Parámetros**: `telefono` (string)
- **Retorna**: `boolean` - true si es válido, false en caso contrario
- **Formatos aceptados**: 
  - `1234567890`
  - `123-456-7890`
  - `(123) 456-7890`

##### `validarNoVacio(texto)`
Valida si una cadena no está vacía (después de eliminar espacios).
- **Parámetros**: `texto` (string)
- **Retorna**: `boolean` - true si no está vacío, false en caso contrario

#### Ejemplos de Uso

```javascript
const { 
    validarEmail, 
    validarPassword, 
    validarTelefono, 
    validarNoVacio 
} = require('./ejercicio2-validador');

// Validar emails
console.log(validarEmail('usuario@ejemplo.com'));     // true
console.log(validarEmail('correo-invalido'));         // false

// Validar contraseñas
console.log(validarPassword('Password123'));          // true
console.log(validarPassword('corta'));                // false

// Validar teléfonos
console.log(validarTelefono('1234567890'));           // true
console.log(validarTelefono('(123) 456-7890'));       // true

// Validar no vacío
console.log(validarNoVacio('Hola'));                  // true
console.log(validarNoVacio('   '));                   // false
```

#### Pruebas (25 tests)
- ✅ Validación de emails correctos e incorrectos
- ✅ Validación de contraseñas seguras e inseguras
- ✅ Validación de teléfonos en múltiples formatos
- ✅ Validación de campos vacíos y con espacios
- ✅ Validación de tipos de datos

---

### Ejercicio 3: Utilidades para Arrays

**Archivo**: `ejercicio3-array-utils.js`

#### Funciones Implementadas

##### `encontrarMaximo(array)`
Encuentra el valor máximo en un array de números.
- **Parámetros**: `array` (number[])
- **Retorna**: `number` - El valor máximo
- **Excepciones**: 
  - `Error` si el array está vacío
  - `Error` si no todos los elementos son números

##### `calcularPromedio(array)`
Calcula el promedio de un array de números.
- **Parámetros**: `array` (number[])
- **Retorna**: `number` - El promedio
- **Excepciones**: 
  - `Error` si el array está vacío
  - `Error` si no todos los elementos son números

##### `filtrarPares(array)`
Filtra los números pares de un array.
- **Parámetros**: `array` (number[])
- **Retorna**: `number[]` - Array con solo números pares
- **Excepciones**: `Error` si no es un array o no contiene números

##### `eliminarDuplicados(array)`
Elimina elementos duplicados de un array.
- **Parámetros**: `array` (Array)
- **Retorna**: `Array` - Array sin duplicados
- **Excepciones**: `Error` si no es un array

##### `invertirArray(array)`
Invierte el orden de los elementos de un array.
- **Parámetros**: `array` (Array)
- **Retorna**: `Array` - Nuevo array invertido
- **Excepciones**: `Error` si no es un array

##### `contarOcurrencias(array, elemento)`
Cuenta cuántas veces aparece un elemento en un array.
- **Parámetros**: `array` (Array), `elemento` (any)
- **Retorna**: `number` - Número de ocurrencias
- **Excepciones**: `Error` si no es un array

#### Ejemplos de Uso

```javascript
const {
    encontrarMaximo,
    calcularPromedio,
    filtrarPares,
    eliminarDuplicados,
    invertirArray,
    contarOcurrencias
} = require('./ejercicio3-array-utils');

// Encontrar máximo
console.log(encontrarMaximo([1, 5, 3, 9, 2]));       // 9

// Calcular promedio
console.log(calcularPromedio([2, 4, 6, 8]));         // 5

// Filtrar pares
console.log(filtrarPares([1, 2, 3, 4, 5, 6]));       // [2, 4, 6]

// Eliminar duplicados
console.log(eliminarDuplicados([1, 2, 2, 3, 3, 3])); // [1, 2, 3]

// Invertir array
console.log(invertirArray([1, 2, 3, 4, 5]));         // [5, 4, 3, 2, 1]

// Contar ocurrencias
console.log(contarOcurrencias([1, 2, 3, 2, 2], 2));  // 3
```

#### Pruebas (30 tests)
- ✅ Búsqueda de máximo con números positivos, negativos y mixtos
- ✅ Cálculo de promedio con diferentes conjuntos de datos
- ✅ Filtrado de pares incluyendo cero y negativos
- ✅ Eliminación de duplicados en números y strings
- ✅ Inversión de arrays sin modificar el original
- ✅ Conteo de ocurrencias distinguiendo tipos

## 📊 Estadísticas

| Ejercicio | Funciones | Pruebas | Líneas de Código |
|-----------|-----------|---------|------------------|
| Calculadora | 4 | 20 | ~70 |
| Validador | 4 | 25 | ~90 |
| Array Utils | 6 | 30 | ~120 |
| **TOTAL** | **14** | **75** | **~280** |

## 🎯 Cobertura de Pruebas

- **Cobertura total**: >95%
- **Casos normales**: ✅ Cubiertos
- **Casos límite**: ✅ Cubiertos
- **Validación de errores**: ✅ Cubierta
- **Validación de tipos**: ✅ Cubierta

## 🛠️ Tecnologías

- **Node.js**: v14+
- **Jest**: v29.7.0
- **JavaScript**: ES6+

## 📖 Documentación

Todo el código está documentado con **JSDoc**:

```javascript
/**
 * Descripción de la función
 * @param {type} nombre - Descripción del parámetro
 * @returns {type} Descripción del retorno
 * @throws {ErrorType} Descripción del error
 */
```

## ✅ Buenas Prácticas Implementadas

1. ✅ **Validación de tipos** en todas las funciones
2. ✅ **Manejo de errores** con excepciones descriptivas
3. ✅ **Inmutabilidad** - No se modifican los parámetros originales
4. ✅ **Nombres descriptivos** - camelCase para funciones y variables
5. ✅ **Pruebas exhaustivas** - Casos normales, límite y errores
6. ✅ **Documentación completa** - JSDoc en todas las funciones

## 🔗 Ver También

- **[README principal](../README.md)** - Documentación general del proyecto
- **[Ejercicios Python](../python/README.md)** - Ejercicios en Python
- **[Ejemplos JavaScript](./EJEMPLOS.md)** - Más ejemplos de uso

---

**¡Feliz Testing con JavaScript! 🧪✨**
