/**
 * Ejercicio 2: Validador de Datos
 * 
 * Este módulo implementa funciones para validar diferentes tipos de datos
 * como emails, contraseñas y números de teléfono.
 */

/**
 * Valida si un email tiene un formato correcto
 * @param {string} email - El email a validar
 * @returns {boolean} true si el email es válido, false en caso contrario
 */
function validarEmail(email) {
  if (typeof email !== 'string') {
    return false;
  }
  
  // Expresión regular para validar email
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

/**
 * Valida si una contraseña cumple con los requisitos de seguridad
 * Requisitos:
 * - Mínimo 8 caracteres
 * - Al menos una letra mayúscula
 * - Al menos una letra minúscula
 * - Al menos un número
 * 
 * @param {string} password - La contraseña a validar
 * @returns {boolean} true si la contraseña es válida, false en caso contrario
 */
function validarPassword(password) {
  if (typeof password !== 'string') {
    return false;
  }
  
  if (password.length < 8) {
    return false;
  }
  
  const tieneMayuscula = /[A-Z]/.test(password);
  const tieneMinuscula = /[a-z]/.test(password);
  const tieneNumero = /[0-9]/.test(password);
  
  return tieneMayuscula && tieneMinuscula && tieneNumero;
}

/**
 * Valida si un número de teléfono tiene un formato correcto
 * Acepta formatos: 1234567890, 123-456-7890, (123) 456-7890
 * 
 * @param {string} telefono - El número de teléfono a validar
 * @returns {boolean} true si el teléfono es válido, false en caso contrario
 */
function validarTelefono(telefono) {
  if (typeof telefono !== 'string') {
    return false;
  }
  
  // Eliminar espacios, guiones y paréntesis
  const telefonoLimpio = telefono.replace(/[\s\-\(\)]/g, '');
  
  // Verificar que tenga exactamente 10 dígitos
  return /^\d{10}$/.test(telefonoLimpio);
}

/**
 * Valida si una cadena no está vacía (después de eliminar espacios)
 * @param {string} texto - El texto a validar
 * @returns {boolean} true si el texto no está vacío, false en caso contrario
 */
function validarNoVacio(texto) {
  if (typeof texto !== 'string') {
    return false;
  }
  
  return texto.trim().length > 0;
}

module.exports = {
  validarEmail,
  validarPassword,
  validarTelefono,
  validarNoVacio
};
