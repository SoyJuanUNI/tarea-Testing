/**
 * Configuración de Jest para las pruebas unitarias
 */
module.exports = {
  testEnvironment: 'node',
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'javascript/**/*.js',
    '!javascript/**/*.test.js'
  ],
  testMatch: [
    '**/javascript/**/*.test.js'
  ]
};
