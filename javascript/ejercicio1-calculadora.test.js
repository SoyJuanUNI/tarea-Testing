/**
 * Pruebas unitarias para el módulo de Calculadora
 * 
 * Estas pruebas verifican el correcto funcionamiento de las operaciones
 * básicas de la calculadora, incluyendo casos normales y casos límite.
 */

const { sumar, restar, multiplicar, dividir } = require('./ejercicio1-calculadora');

describe('Calculadora - Operaciones Básicas', () => {
  
  describe('sumar()', () => {
    test('debe sumar dos números positivos correctamente', () => {
      expect(sumar(5, 3)).toBe(8);
    });

    test('debe sumar números negativos correctamente', () => {
      expect(sumar(-5, -3)).toBe(-8);
    });

    test('debe sumar un número positivo y uno negativo', () => {
      expect(sumar(10, -3)).toBe(7);
    });

    test('debe sumar con cero', () => {
      expect(sumar(5, 0)).toBe(5);
    });

    test('debe lanzar error si los parámetros no son números', () => {
      expect(() => sumar('5', 3)).toThrow(TypeError);
      expect(() => sumar(5, '3')).toThrow(TypeError);
    });
  });

  describe('restar()', () => {
    test('debe restar dos números positivos correctamente', () => {
      expect(restar(10, 3)).toBe(7);
    });

    test('debe restar números negativos correctamente', () => {
      expect(restar(-5, -3)).toBe(-2);
    });

    test('debe restar con resultado negativo', () => {
      expect(restar(3, 10)).toBe(-7);
    });

    test('debe lanzar error si los parámetros no son números', () => {
      expect(() => restar('10', 3)).toThrow(TypeError);
    });
  });

  describe('multiplicar()', () => {
    test('debe multiplicar dos números positivos correctamente', () => {
      expect(multiplicar(5, 3)).toBe(15);
    });

    test('debe multiplicar por cero', () => {
      expect(multiplicar(5, 0)).toBe(0);
    });

    test('debe multiplicar números negativos', () => {
      expect(multiplicar(-5, -3)).toBe(15);
      expect(multiplicar(-5, 3)).toBe(-15);
    });

    test('debe lanzar error si los parámetros no son números', () => {
      expect(() => multiplicar(5, null)).toThrow(TypeError);
    });
  });

  describe('dividir()', () => {
    test('debe dividir dos números correctamente', () => {
      expect(dividir(10, 2)).toBe(5);
    });

    test('debe dividir con resultado decimal', () => {
      expect(dividir(10, 3)).toBeCloseTo(3.333, 3);
    });

    test('debe dividir números negativos', () => {
      expect(dividir(-10, 2)).toBe(-5);
      expect(dividir(10, -2)).toBe(-5);
    });

    test('debe lanzar error al dividir por cero', () => {
      expect(() => dividir(10, 0)).toThrow('No se puede dividir por cero');
    });

    test('debe lanzar error si los parámetros no son números', () => {
      expect(() => dividir('10', 2)).toThrow(TypeError);
    });
  });
});
