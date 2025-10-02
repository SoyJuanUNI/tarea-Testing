# 💡 Ejemplos de Uso - JavaScript

Ejemplos prácticos y casos de uso reales para las funciones de JavaScript.

## 📘 Ejercicio 1: Calculadora Básica

### Uso Básico

```javascript
const { sumar, restar, multiplicar, dividir } = require('./ejercicio1-calculadora');

// Operaciones simples
console.log(sumar(5, 3));        // 8
console.log(restar(10, 3));      // 7
console.log(multiplicar(4, 5));  // 20
console.log(dividir(10, 2));     // 5
```

### Trabajando con Números Negativos

```javascript
console.log(sumar(-5, -3));      // -8
console.log(restar(-5, -3));     // -2
console.log(multiplicar(-5, 3)); // -15
console.log(dividir(-10, 2));    // -5
```

### Manejo de Errores

```javascript
// División por cero
try {
    const resultado = dividir(10, 0);
} catch (error) {
    console.error('Error:', error.message);
    // "No se puede dividir por cero"
}

// Tipo de dato incorrecto
try {
    const resultado = sumar('5', 3);
} catch (error) {
    console.error('Error:', error.message);
    // "Ambos parámetros deben ser números"
}
```

### Caso de Uso: Calculadora de Propinas

```javascript
function calcularPropina(total, porcentaje) {
    const propina = multiplicar(total, dividir(porcentaje, 100));
    const totalConPropina = sumar(total, propina);
    
    return {
        subtotal: total,
        propina: propina,
        total: totalConPropina
    };
}

const cuenta = calcularPropina(50, 15);
console.log(cuenta);
// { subtotal: 50, propina: 7.5, total: 57.5 }
```

---

## 📘 Ejercicio 2: Validador de Datos

### Validación de Emails

```javascript
const { validarEmail } = require('./ejercicio2-validador');

// Emails válidos
console.log(validarEmail('usuario@ejemplo.com'));     // true
console.log(validarEmail('test.user@dominio.co'));    // true
console.log(validarEmail('nombre123@empresa.org'));   // true

// Emails inválidos
console.log(validarEmail('usuario@'));                // false
console.log(validarEmail('@ejemplo.com'));            // false
console.log(validarEmail('usuario.ejemplo.com'));     // false
console.log(validarEmail('usuario @ejemplo.com'));    // false
```

### Validación de Contraseñas

```javascript
const { validarPassword } = require('./ejercicio2-validador');

// Contraseñas válidas
console.log(validarPassword('Password123'));          // true
console.log(validarPassword('MiClave2024'));          // true
console.log(validarPassword('Segura1234'));           // true

// Contraseñas inválidas
console.log(validarPassword('corta'));                // false (muy corta)
console.log(validarPassword('password123'));          // false (sin mayúsculas)
console.log(validarPassword('PASSWORD123'));          // false (sin minúsculas)
console.log(validarPassword('PasswordSegura'));       // false (sin números)
```

### Validación de Teléfonos

```javascript
const { validarTelefono } = require('./ejercicio2-validador');

// Formatos válidos
console.log(validarTelefono('1234567890'));           // true
console.log(validarTelefono('123-456-7890'));         // true
console.log(validarTelefono('(123) 456-7890'));       // true

// Formatos inválidos
console.log(validarTelefono('123456789'));            // false (muy corto)
console.log(validarTelefono('12345678901'));          // false (muy largo)
console.log(validarTelefono('123abc7890'));           // false (contiene letras)
```

### Caso de Uso: Validación de Formulario de Registro

```javascript
const { 
    validarEmail, 
    validarPassword, 
    validarTelefono, 
    validarNoVacio 
} = require('./ejercicio2-validador');

function validarFormularioRegistro(datos) {
    const errores = [];
    
    // Validar nombre
    if (!validarNoVacio(datos.nombre)) {
        errores.push('El nombre es requerido');
    }
    
    // Validar email
    if (!validarEmail(datos.email)) {
        errores.push('Email inválido');
    }
    
    // Validar contraseña
    if (!validarPassword(datos.password)) {
        errores.push('La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número');
    }
    
    // Validar teléfono
    if (!validarTelefono(datos.telefono)) {
        errores.push('Teléfono inválido (debe tener 10 dígitos)');
    }
    
    return {
        valido: errores.length === 0,
        errores: errores
    };
}

// Ejemplo de uso
const datosUsuario = {
    nombre: 'Juan Pérez',
    email: 'juan@ejemplo.com',
    password: 'Password123',
    telefono: '1234567890'
};

const resultado = validarFormularioRegistro(datosUsuario);
console.log(resultado);
// { valido: true, errores: [] }

// Con datos inválidos
const datosInvalidos = {
    nombre: '',
    email: 'correo-invalido',
    password: 'corta',
    telefono: '123'
};

const resultadoInvalido = validarFormularioRegistro(datosInvalidos);
console.log(resultadoInvalido);
// { valido: false, errores: [...] }
```

---

## 📘 Ejercicio 3: Utilidades para Arrays

### Operaciones Básicas

```javascript
const {
    encontrarMaximo,
    calcularPromedio,
    filtrarPares,
    eliminarDuplicados,
    invertirArray,
    contarOcurrencias
} = require('./ejercicio3-array-utils');

const numeros = [1, 5, 3, 9, 2, 7, 4];

console.log(encontrarMaximo(numeros));       // 9
console.log(calcularPromedio(numeros));      // 4.428...
console.log(filtrarPares(numeros));          // [2, 4]
console.log(eliminarDuplicados([1, 2, 2, 3])); // [1, 2, 3]
console.log(invertirArray(numeros));         // [4, 7, 2, 9, 3, 5, 1]
console.log(contarOcurrencias([1, 2, 2, 3], 2)); // 2
```

### Caso de Uso: Análisis de Calificaciones

```javascript
const {
    encontrarMaximo,
    calcularPromedio,
    filtrarPares
} = require('./ejercicio3-array-utils');

function analizarCalificaciones(calificaciones) {
    const promedio = calcularPromedio(calificaciones);
    const maxima = encontrarMaximo(calificaciones);
    const aprobados = calificaciones.filter(c => c >= 60);
    
    return {
        promedio: promedio.toFixed(2),
        calificacionMaxima: maxima,
        totalEstudiantes: calificaciones.length,
        aprobados: aprobados.length,
        reprobados: calificaciones.length - aprobados.length,
        porcentajeAprobacion: ((aprobados.length / calificaciones.length) * 100).toFixed(2) + '%'
    };
}

const calificaciones = [85, 92, 78, 95, 88, 76, 90, 55, 82, 70];
const analisis = analizarCalificaciones(calificaciones);
console.log(analisis);
/*
{
  promedio: '81.10',
  calificacionMaxima: 95,
  totalEstudiantes: 10,
  aprobados: 9,
  reprobados: 1,
  porcentajeAprobacion: '90.00%'
}
*/
```

### Caso de Uso: Procesamiento de Datos

```javascript
const {
    eliminarDuplicados,
    filtrarPares,
    calcularPromedio
} = require('./ejercicio3-array-utils');

function procesarDatosVentas(ventas) {
    // Eliminar ventas duplicadas
    const ventasUnicas = eliminarDuplicados(ventas);
    
    // Filtrar solo ventas pares (para algún análisis específico)
    const ventasPares = filtrarPares(ventasUnicas);
    
    // Calcular promedio
    const promedioTotal = calcularPromedio(ventasUnicas);
    const promedioPares = ventasPares.length > 0 ? calcularPromedio(ventasPares) : 0;
    
    return {
        totalVentas: ventasUnicas.length,
        promedioGeneral: promedioTotal.toFixed(2),
        ventasPares: ventasPares.length,
        promedioPares: promedioPares.toFixed(2)
    };
}

const ventas = [100, 150, 200, 150, 300, 100, 250, 200];
const resultado = procesarDatosVentas(ventas);
console.log(resultado);
/*
{
  totalVentas: 5,
  promedioGeneral: '180.00',
  ventasPares: 3,
  promedioPares: '183.33'
}
*/
```

### Caso de Uso: Gestión de Inventario

```javascript
const {
    contarOcurrencias,
    eliminarDuplicados
} = require('./ejercicio3-array-utils');

function analizarInventario(productos) {
    const productosUnicos = eliminarDuplicados(productos);
    
    const inventario = productosUnicos.map(producto => ({
        nombre: producto,
        cantidad: contarOcurrencias(productos, producto)
    }));
    
    return inventario;
}

const productos = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'manzana', 'pera'];
const inventario = analizarInventario(productos);
console.log(inventario);
/*
[
  { nombre: 'manzana', cantidad: 3 },
  { nombre: 'naranja', cantidad: 2 },
  { nombre: 'pera', cantidad: 2 }
]
*/
```

### Composición de Funciones

```javascript
const {
    filtrarPares,
    calcularPromedio,
    encontrarMaximo
} = require('./ejercicio3-array-utils');

// Combinar múltiples funciones
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Encontrar el promedio de los números pares
const pares = filtrarPares(numeros);
const promedioPares = calcularPromedio(pares);
console.log(`Promedio de pares: ${promedioPares}`);  // 6

// Encontrar el máximo de los números pares
const maximoPar = encontrarMaximo(pares);
console.log(`Máximo par: ${maximoPar}`);  // 10
```

### Inmutabilidad

```javascript
const { invertirArray } = require('./ejercicio3-array-utils');

// Las funciones no modifican el array original
const original = [1, 2, 3, 4, 5];
const invertido = invertirArray(original);

console.log('Original:', original);    // [1, 2, 3, 4, 5]
console.log('Invertido:', invertido);  // [5, 4, 3, 2, 1]

// El array original permanece sin cambios
```

## 🎯 Consejos de Uso

### 1. Siempre Valida las Entradas

```javascript
function procesarDatos(datos) {
    // Validar antes de procesar
    if (!validarNoVacio(datos.nombre)) {
        throw new Error('Nombre requerido');
    }
    
    if (!validarEmail(datos.email)) {
        throw new Error('Email inválido');
    }
    
    // Procesar datos...
}
```

### 2. Maneja los Errores Apropiadamente

```javascript
try {
    const resultado = dividir(10, 0);
} catch (error) {
    console.error('Error en la operación:', error.message);
    // Tomar acción apropiada
}
```

### 3. Aprovecha la Composición

```javascript
// Combina funciones para operaciones complejas
const resultado = calcularPromedio(
    filtrarPares(
        eliminarDuplicados(datos)
    )
);
```

---

**¡Explora y experimenta con las funciones! 🚀**
