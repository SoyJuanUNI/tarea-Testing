# 🚀 Inicio Rápido - JavaScript

Guía rápida para empezar con los ejercicios de JavaScript en menos de 5 minutos.

## ⚡ Instalación Rápida

### Paso 1: Verificar Node.js
```bash
node --version
```
Si no tienes Node.js instalado, descárgalo de [nodejs.org](https://nodejs.org/)

### Paso 2: Instalar Dependencias
Desde la raíz del proyecto:
```bash
npm install
```

## 🧪 Ejecutar Pruebas

### Opción 1: Todas las Pruebas de JavaScript
```bash
npm test
```

### Opción 2: Pruebas Específicas
```bash
# Ejercicio 1 - Calculadora
npx jest javascript/ejercicio1-calculadora.test.js

# Ejercicio 2 - Validador
npx jest javascript/ejercicio2-validador.test.js

# Ejercicio 3 - Array Utils
npx jest javascript/ejercicio3-array-utils.test.js
```

### Opción 3: Modo Watch (Recomendado para desarrollo)
```bash
npm run test:watch
```
Las pruebas se ejecutarán automáticamente cada vez que guardes un archivo.

### Opción 4: Con Cobertura
```bash
npm run test:coverage
```

## 📊 Ver Resultados

Después de ejecutar las pruebas, verás algo como:

```
PASS  javascript/ejercicio1-calculadora.test.js
  ✓ Calculadora - Operaciones Básicas (20 tests)

PASS  javascript/ejercicio2-validador.test.js
  ✓ Validador de Datos (25 tests)

PASS  javascript/ejercicio3-array-utils.test.js
  ✓ Utilidades para Arrays (30 tests)

Test Suites: 3 passed, 3 total
Tests:       75 passed, 75 total
```

## 📚 Explorar el Código

### Ejercicio 1: Calculadora
```bash
# Ver el código
code javascript/ejercicio1-calculadora.js

# Ver las pruebas
code javascript/ejercicio1-calculadora.test.js
```

**Funciones disponibles:**
- `sumar(a, b)` - Suma dos números
- `restar(a, b)` - Resta dos números
- `multiplicar(a, b)` - Multiplica dos números
- `dividir(a, b)` - Divide dos números

### Ejercicio 2: Validador
```bash
# Ver el código
code javascript/ejercicio2-validador.js
```

**Funciones disponibles:**
- `validarEmail(email)` - Valida formato de email
- `validarPassword(password)` - Valida contraseña segura
- `validarTelefono(telefono)` - Valida número de teléfono
- `validarNoVacio(texto)` - Valida que no esté vacío

### Ejercicio 3: Array Utils
```bash
# Ver el código
code javascript/ejercicio3-array-utils.js
```

**Funciones disponibles:**
- `encontrarMaximo(array)` - Encuentra el valor máximo
- `calcularPromedio(array)` - Calcula el promedio
- `filtrarPares(array)` - Filtra números pares
- `eliminarDuplicados(array)` - Elimina duplicados
- `invertirArray(array)` - Invierte el array
- `contarOcurrencias(array, elemento)` - Cuenta ocurrencias

## 💡 Ejemplo Rápido

Crea un archivo `test.js` en la raíz:

```javascript
const { sumar, multiplicar } = require('./javascript/ejercicio1-calculadora');
const { validarEmail } = require('./javascript/ejercicio2-validador');
const { encontrarMaximo } = require('./javascript/ejercicio3-array-utils');

// Calculadora
console.log('5 + 3 =', sumar(5, 3));              // 8
console.log('4 × 5 =', multiplicar(4, 5));        // 20

// Validador
console.log('Email válido?', validarEmail('test@ejemplo.com'));  // true

// Arrays
console.log('Máximo:', encontrarMaximo([1, 5, 3, 9, 2]));  // 9
```

Ejecuta:
```bash
node test.js
```

## 📖 Documentación Completa

- **[README JavaScript](README.md)** - Documentación completa
- **[Ejemplos JavaScript](EJEMPLOS.md)** - Casos de uso prácticos

## ✅ Verificación Rápida

Para verificar que todo funciona:

```bash
# Ejecutar una prueba específica
npx jest javascript/ejercicio1-calculadora.test.js
```

Si ves `✓ PASS`, ¡todo está funcionando correctamente! ✨

## 🎯 Próximos Pasos

1. ✅ Instalar dependencias con `npm install`
2. ✅ Ejecutar pruebas con `npm test`
3. 📖 Leer [README.md](README.md) para documentación completa
4. 💡 Ver [EJEMPLOS.md](EJEMPLOS.md) para casos de uso
5. 🔧 Modificar el código y ver cómo fallan las pruebas
6. 🧪 Agregar tus propias pruebas

## 💡 Consejos

- **Usa `npm run test:watch`** para desarrollo activo
- **Revisa los comentarios** en el código para entender cada función
- **Experimenta modificando** las funciones para ver cómo fallan las pruebas
- **Consulta EJEMPLOS.md** para ver casos de uso reales

## 🆘 Problemas Comunes

### Error: "Cannot find module 'jest'"
```bash
npm install
```

### Error: "node: command not found"
Instala Node.js desde [nodejs.org](https://nodejs.org/)

### Las pruebas no se ejecutan
```bash
# Verifica que estás en la raíz del proyecto
pwd  # o cd en Windows

# Reinstala dependencias
rm -rf node_modules
npm install
```

---

**¡Listo para empezar con JavaScript! 🎉**
