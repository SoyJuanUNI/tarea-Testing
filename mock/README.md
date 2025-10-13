# 🧪 Mocks en Pruebas

Los "mocks" (dobles de prueba) son objetos simulados que imitan el comportamiento de dependencias reales durante una prueba. Se usan para aislar el código bajo prueba, controlar escenarios y observar interacciones sin depender de recursos externos (red, base de datos, reloj del sistema, archivos, etc.).

## ¿Para qué sirven?
- Aislar la unidad bajo prueba de sus dependencias.
- Forzar rutas de código difíciles de reproducir (errores, timeouts, valores extremos).
- Hacer las pruebas más rápidas y determinísticas.
- Verificar interacciones: cuántas veces se llamó, con qué argumentos, en qué orden.

## Tipos de dobles de prueba
- **Dummy**: Parámetros requeridos que no se usan.
- **Stub**: Devuelven datos predefinidos sin lógica.
- **Spy**: Registran llamadas y argumentos.
- **Mock**: Como "spy" pero con expectativas/aseveraciones de interacción.
- **Fake**: Implementación simplificada que funciona (p. ej., base en memoria).

## Cuándo usar mocks
- Dependencias lentas o no determinísticas (APIs externas, I/O, reloj, aleatoriedad).
- Efectos secundarios que no quieres ejecutar (enviar emails, escribir archivos).
- Para simular errores/remotos y cubrir ramas de manejo de excepciones.

## Buenas prácticas
- Mockea solo lo que controlas y lo estrictamente necesario.
- Mantén contratos realistas (mismos nombres y firmas).
- Resetea/restaura los mocks entre pruebas.
- Evita sobre-mockear: si puedes probar con datos reales en memoria, prefiérelo.

## Ejemplos rápidos

### Python (pytest + unittest.mock)
```python
from unittest.mock import patch, MagicMock

# Mockear función de tiempo
with patch("mimodulo.time.time", return_value=1234567890):
    assert obtener_timestamp() == 1234567890

# Mockear cliente HTTP
cliente = MagicMock()
cliente.get.return_value.status_code = 200
cliente.get.return_value.json.return_value = {"ok": True}
use_api(cliente)
cliente.get.assert_called_once_with("/status")
```

### JavaScript (Jest)
```javascript
// Mock automático de módulo
jest.mock("axios");
const axios = require("axios");
axios.get.mockResolvedValue({ data: { ok: true } });

await fetchStatus();
expect(axios.get).toHaveBeenCalledWith("/status");

// Mock de temporizadores
jest.useFakeTimers();
startTimer();
jest.advanceTimersByTime(1000);
expect(callback).toHaveBeenCalled();
```

## Ventajas
- Pruebas rápidas, confiables y aisladas.
- Menos flaky tests al evitar dependencias externas.

## Riesgos
- Falsos positivos si el mock no refleja la realidad.
- Acoplamiento a la implementación en lugar del comportamiento público.

---

Para profundizar, considera integrar ejemplos de mocks en los ejercicios o crear una carpeta `examples/` con escenarios de red, tiempo y archivo mockeados. 