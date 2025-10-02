/**
 * Pruebas unitarias para el módulo Validador de Datos
 * 
 * Estas pruebas verifican el correcto funcionamiento de las funciones
 * de validación para diferentes tipos de datos.
 */

const { 
  validarEmail, 
  validarPassword, 
  validarTelefono, 
  validarNoVacio 
} = require('./ejercicio2-validador');

describe('Validador de Datos', () => {
  
  describe('validarEmail()', () => {
    test('debe validar emails correctos', () => {
      expect(validarEmail('usuario@ejemplo.com')).toBe(true);
      expect(validarEmail('test.user@dominio.co')).toBe(true);
      expect(validarEmail('nombre123@empresa.org')).toBe(true);
    });

    test('debe rechazar emails incorrectos', () => {
      expect(validarEmail('usuario@')).toBe(false);
      expect(validarEmail('@ejemplo.com')).toBe(false);
      expect(validarEmail('usuario.ejemplo.com')).toBe(false);
      expect(validarEmail('usuario @ejemplo.com')).toBe(false);
    });

    test('debe rechazar valores no string', () => {
      expect(validarEmail(123)).toBe(false);
      expect(validarEmail(null)).toBe(false);
      expect(validarEmail(undefined)).toBe(false);
    });

    test('debe rechazar string vacío', () => {
      expect(validarEmail('')).toBe(false);
    });
  });

  describe('validarPassword()', () => {
    test('debe validar contraseñas seguras', () => {
      expect(validarPassword('Password123')).toBe(true);
      expect(validarPassword('MiClave2024')).toBe(true);
      expect(validarPassword('Segura1234')).toBe(true);
    });

    test('debe rechazar contraseñas cortas', () => {
      expect(validarPassword('Pass1')).toBe(false);
      expect(validarPassword('Abc123')).toBe(false);
    });

    test('debe rechazar contraseñas sin mayúsculas', () => {
      expect(validarPassword('password123')).toBe(false);
    });

    test('debe rechazar contraseñas sin minúsculas', () => {
      expect(validarPassword('PASSWORD123')).toBe(false);
    });

    test('debe rechazar contraseñas sin números', () => {
      expect(validarPassword('PasswordSegura')).toBe(false);
    });

    test('debe rechazar valores no string', () => {
      expect(validarPassword(12345678)).toBe(false);
      expect(validarPassword(null)).toBe(false);
    });
  });

  describe('validarTelefono()', () => {
    test('debe validar teléfonos en formato simple', () => {
      expect(validarTelefono('1234567890')).toBe(true);
    });

    test('debe validar teléfonos con guiones', () => {
      expect(validarTelefono('123-456-7890')).toBe(true);
    });

    test('debe validar teléfonos con paréntesis', () => {
      expect(validarTelefono('(123) 456-7890')).toBe(true);
    });

    test('debe rechazar teléfonos con menos de 10 dígitos', () => {
      expect(validarTelefono('123456789')).toBe(false);
    });

    test('debe rechazar teléfonos con más de 10 dígitos', () => {
      expect(validarTelefono('12345678901')).toBe(false);
    });

    test('debe rechazar teléfonos con letras', () => {
      expect(validarTelefono('123abc7890')).toBe(false);
    });

    test('debe rechazar valores no string', () => {
      expect(validarTelefono(1234567890)).toBe(false);
    });
  });

  describe('validarNoVacio()', () => {
    test('debe validar strings con contenido', () => {
      expect(validarNoVacio('Hola')).toBe(true);
      expect(validarNoVacio('Texto con espacios')).toBe(true);
    });

    test('debe rechazar strings vacíos', () => {
      expect(validarNoVacio('')).toBe(false);
    });

    test('debe rechazar strings con solo espacios', () => {
      expect(validarNoVacio('   ')).toBe(false);
      expect(validarNoVacio('\t\n')).toBe(false);
    });

    test('debe rechazar valores no string', () => {
      expect(validarNoVacio(null)).toBe(false);
      expect(validarNoVacio(undefined)).toBe(false);
      expect(validarNoVacio(123)).toBe(false);
    });
  });
});
