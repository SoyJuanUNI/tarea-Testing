/**
 * Pruebas unitarias para el módulo de Utilidades para Arrays
 * 
 * Estas pruebas verifican el correcto funcionamiento de las funciones
 * de manipulación y análisis de arrays.
 */

const {
  encontrarMaximo,
  calcularPromedio,
  filtrarPares,
  eliminarDuplicados,
  invertirArray,
  contarOcurrencias
} = require('./ejercicio3-array-utils');

describe('Utilidades para Arrays', () => {
  
  describe('encontrarMaximo()', () => {
    test('debe encontrar el máximo en un array de números positivos', () => {
      expect(encontrarMaximo([1, 5, 3, 9, 2])).toBe(9);
    });

    test('debe encontrar el máximo con números negativos', () => {
      expect(encontrarMaximo([-5, -1, -10, -3])).toBe(-1);
    });

    test('debe encontrar el máximo con números mixtos', () => {
      expect(encontrarMaximo([-5, 10, 3, -2])).toBe(10);
    });

    test('debe funcionar con un solo elemento', () => {
      expect(encontrarMaximo([42])).toBe(42);
    });

    test('debe lanzar error con array vacío', () => {
      expect(() => encontrarMaximo([])).toThrow('El array no puede estar vacío');
    });

    test('debe lanzar error si no todos son números', () => {
      expect(() => encontrarMaximo([1, 2, '3'])).toThrow('Todos los elementos deben ser números');
    });
  });

  describe('calcularPromedio()', () => {
    test('debe calcular el promedio correctamente', () => {
      expect(calcularPromedio([2, 4, 6, 8])).toBe(5);
    });

    test('debe calcular el promedio con números decimales', () => {
      expect(calcularPromedio([1, 2, 3])).toBeCloseTo(2, 5);
    });

    test('debe calcular el promedio con números negativos', () => {
      expect(calcularPromedio([-2, -4, -6])).toBe(-4);
    });

    test('debe funcionar con un solo elemento', () => {
      expect(calcularPromedio([10])).toBe(10);
    });

    test('debe lanzar error con array vacío', () => {
      expect(() => calcularPromedio([])).toThrow('El array no puede estar vacío');
    });
  });

  describe('filtrarPares()', () => {
    test('debe filtrar solo los números pares', () => {
      expect(filtrarPares([1, 2, 3, 4, 5, 6])).toEqual([2, 4, 6]);
    });

    test('debe retornar array vacío si no hay pares', () => {
      expect(filtrarPares([1, 3, 5, 7])).toEqual([]);
    });

    test('debe incluir el cero como par', () => {
      expect(filtrarPares([0, 1, 2])).toEqual([0, 2]);
    });

    test('debe funcionar con números negativos', () => {
      expect(filtrarPares([-4, -3, -2, -1])).toEqual([-4, -2]);
    });

    test('debe lanzar error si no es un array', () => {
      expect(() => filtrarPares('no es array')).toThrow('El parámetro debe ser un array');
    });
  });

  describe('eliminarDuplicados()', () => {
    test('debe eliminar duplicados de números', () => {
      expect(eliminarDuplicados([1, 2, 2, 3, 3, 3, 4])).toEqual([1, 2, 3, 4]);
    });

    test('debe eliminar duplicados de strings', () => {
      expect(eliminarDuplicados(['a', 'b', 'a', 'c', 'b'])).toEqual(['a', 'b', 'c']);
    });

    test('debe retornar array sin cambios si no hay duplicados', () => {
      expect(eliminarDuplicados([1, 2, 3, 4])).toEqual([1, 2, 3, 4]);
    });

    test('debe funcionar con array vacío', () => {
      expect(eliminarDuplicados([])).toEqual([]);
    });

    test('debe lanzar error si no es un array', () => {
      expect(() => eliminarDuplicados('texto')).toThrow('El parámetro debe ser un array');
    });
  });

  describe('invertirArray()', () => {
    test('debe invertir el orden de los elementos', () => {
      expect(invertirArray([1, 2, 3, 4, 5])).toEqual([5, 4, 3, 2, 1]);
    });

    test('debe funcionar con strings', () => {
      expect(invertirArray(['a', 'b', 'c'])).toEqual(['c', 'b', 'a']);
    });

    test('debe funcionar con un solo elemento', () => {
      expect(invertirArray([1])).toEqual([1]);
    });

    test('debe funcionar con array vacío', () => {
      expect(invertirArray([])).toEqual([]);
    });

    test('no debe modificar el array original', () => {
      const original = [1, 2, 3];
      const invertido = invertirArray(original);
      expect(original).toEqual([1, 2, 3]);
      expect(invertido).toEqual([3, 2, 1]);
    });

    test('debe lanzar error si no es un array', () => {
      expect(() => invertirArray(123)).toThrow('El parámetro debe ser un array');
    });
  });

  describe('contarOcurrencias()', () => {
    test('debe contar ocurrencias de un número', () => {
      expect(contarOcurrencias([1, 2, 3, 2, 2, 4], 2)).toBe(3);
    });

    test('debe contar ocurrencias de un string', () => {
      expect(contarOcurrencias(['a', 'b', 'a', 'c', 'a'], 'a')).toBe(3);
    });

    test('debe retornar 0 si el elemento no existe', () => {
      expect(contarOcurrencias([1, 2, 3], 5)).toBe(0);
    });

    test('debe funcionar con array vacío', () => {
      expect(contarOcurrencias([], 1)).toBe(0);
    });

    test('debe distinguir entre tipos diferentes', () => {
      expect(contarOcurrencias([1, '1', 1, '1'], 1)).toBe(2);
    });

    test('debe lanzar error si no es un array', () => {
      expect(() => contarOcurrencias('texto', 'a')).toThrow('El primer parámetro debe ser un array');
    });
  });
});
