/**
 * Ejercicio 1: Calculadora Básica
 * 
 * Este módulo implementa una calculadora con operaciones básicas.
 * Incluye validación de entrada y manejo de casos especiales.
 */

/**
 * Suma dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} La suma de a y b
 * @throws {TypeError} Si los parámetros no son números
 */
function sumar(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Ambos parámetros deben ser números');
  }
  return a + b;
}

/**
 * Resta dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} La resta de a menos b
 * @throws {TypeError} Si los parámetros no son números
 */
function restar(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Ambos parámetros deben ser números');
  }
  return a - b;
}

/**
 * Multiplica dos números
 * @param {number} a - Primer número
 * @param {number} b - Segundo número
 * @returns {number} El producto de a y b
 * @throws {TypeError} Si los parámetros no son números
 */
function multiplicar(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Ambos parámetros deben ser números');
  }
  return a * b;
}

/**
 * Divide dos números
 * @param {number} a - Dividendo
 * @param {number} b - Divisor
 * @returns {number} El cociente de a dividido por b
 * @throws {TypeError} Si los parámetros no son números
 * @throws {Error} Si el divisor es cero
 */
function dividir(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Ambos parámetros deben ser números');
  }
  if (b === 0) {
    throw new Error('No se puede dividir por cero');
  }
  return a / b;
}

module.exports = {
  sumar,
  restar,
  multiplicar,
  dividir
};
