"""
Ejemplo simple para demostrar mocks en Python con pytest y unittest.mock.

Funciones a probar:
- obtener_timestamp: depende del reloj del sistema (time.time)
- generar_token: depende de la aleatoriedad (random.random)
- leer_config: depende del sistema de archivos (abrir un JSON)
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import random
import time
from typing import Callable, Any


def obtener_timestamp() -> int:
    """Retorna un timestamp entero del tiempo actual.

    Esta función depende de `time.time()` (variable externa y no determinística),
    ideal para ser mockeada en pruebas.
    """
    return int(time.time())


def generar_token(usuario: str, rand_func: Callable[[], float] | None = None) -> str:
    """Genera un token corto (8 hex) a partir del usuario y un número aleatorio.

    Args:
        usuario: nombre de usuario no vacío
        rand_func: función que retorna float en [0,1), inyectable para tests

    Returns:
        str: token hexadecimal de 8 caracteres
    """
    if not isinstance(usuario, str) or not usuario:
        raise TypeError("usuario debe ser un string no vacío")

    rng = rand_func or random.random
    valor = rng()
    base = f"{usuario}:{valor}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:8]


def leer_config(ruta: str | pathlib.Path) -> Any:
    """Lee un archivo JSON y retorna su contenido.

    Esta función realiza I/O real; en pruebas se recomienda mockear la lectura
    para evitar depender del sistema de archivos.
    """
    path = pathlib.Path(ruta)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
