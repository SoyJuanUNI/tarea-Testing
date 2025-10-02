/**
 * Ejercicio 3: Utilidades para Arrays
 * 
 * Este módulo implementa funciones útiles para manipular y analizar arrays.
 * Incluye operaciones como búsqueda, filtrado y cálculos estadísticos.
 */

/**
 * Encuentra el valor máximo en un array de números
 * @param {number[]} array - Array de números
 * @returns {number} El valor máximo del array
 * @throws {Error} Si el array está vacío o no contiene números
 */
function encontrarMaximo(array) {
  if (!Array.isArray(array) || array.length === 0) {
    throw new Error('El array no puede estar vacío');
  }
  
  if (!array.every(item => typeof item === 'number')) {
    throw new Error('Todos los elementos deben ser números');
  }
  
  return Math.max(...array);
}

/**
 * Calcula el promedio de un array de números
 * @param {number[]} array - Array de números
 * @returns {number} El promedio de los números
 * @throws {Error} Si el array está vacío o no contiene números
 */
function calcularPromedio(array) {
  if (!Array.isArray(array) || array.length === 0) {
    throw new Error('El array no puede estar vacío');
  }
  
  if (!array.every(item => typeof item === 'number')) {
    throw new Error('Todos los elementos deben ser números');
  }
  
  const suma = array.reduce((acc, num) => acc + num, 0);
  return suma / array.length;
}

/**
 * Filtra los números pares de un array
 * @param {number[]} array - Array de números
 * @returns {number[]} Nuevo array con solo los números pares
 * @throws {Error} Si no es un array o no contiene números
 */
function filtrarPares(array) {
  if (!Array.isArray(array)) {
    throw new Error('El parámetro debe ser un array');
  }
  
  if (!array.every(item => typeof item === 'number')) {
    throw new Error('Todos los elementos deben ser números');
  }
  
  return array.filter(num => num % 2 === 0);
}

/**
 * Elimina elementos duplicados de un array
 * @param {Array} array - Array con posibles duplicados
 * @returns {Array} Nuevo array sin duplicados
 * @throws {Error} Si no es un array
 */
function eliminarDuplicados(array) {
  if (!Array.isArray(array)) {
    throw new Error('El parámetro debe ser un array');
  }
  
  return [...new Set(array)];
}

/**
 * Invierte el orden de los elementos de un array
 * @param {Array} array - Array a invertir
 * @returns {Array} Nuevo array con elementos en orden inverso
 * @throws {Error} Si no es un array
 */
function invertirArray(array) {
  if (!Array.isArray(array)) {
    throw new Error('El parámetro debe ser un array');
  }
  
  return [...array].reverse();
}

/**
 * Cuenta cuántas veces aparece un elemento en un array
 * @param {Array} array - Array donde buscar
 * @param {*} elemento - Elemento a contar
 * @returns {number} Número de veces que aparece el elemento
 * @throws {Error} Si no es un array
 */
function contarOcurrencias(array, elemento) {
  if (!Array.isArray(array)) {
    throw new Error('El primer parámetro debe ser un array');
  }
  
  return array.filter(item => item === elemento).length;
}

module.exports = {
  encontrarMaximo,
  calcularPromedio,
  filtrarPares,
  eliminarDuplicados,
  invertirArray,
  contarOcurrencias
};
