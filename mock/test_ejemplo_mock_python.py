"""
Pruebas que demuestran el uso de mocks con pytest y unittest.mock
para funciones en `ejemplo_mock_python.py`.
"""

import json
from unittest.mock import patch, mock_open

import pytest

from .ejemplo_mock_python import (
    obtener_timestamp,
    generar_token,
    leer_config,
)


def test_obtener_timestamp_mock_time():
    # Forzar que time.time() devuelva un valor fijo
    with patch("time.time", return_value=1_700_000_000):
        assert obtener_timestamp() == 1_700_000_000


def test_generar_token_mock_random():
    # Opción 1: inyectar una función determinística
    token = generar_token("alice", rand_func=lambda: 0.123456)
    # La aserción exacta del token no es necesaria; basta con estabilidad
    assert isinstance(token, str) and len(token) == 8

    # Opción 2: mockear random.random
    with patch("random.random", return_value=0.9999):
        token2 = generar_token("alice")
        assert isinstance(token2, str) and len(token2) == 8
        assert token2 != token  # debería cambiar con otro random


def test_generar_token_errores():
    with pytest.raises(TypeError):
        generar_token(123)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        generar_token("")


def test_leer_config_mock_open():
    # Simular contenido JSON sin tocar el sistema de archivos
    contenido = {"debug": True, "retries": 3}
    data = json.dumps(contenido)

    with patch("pathlib.Path.open", mock_open(read_data=data)):
        cfg = leer_config("config.json")
        assert cfg == contenido


def test_leer_config_mock_open_invalido():
    # Simular JSON inválido para probar manejo de errores
    with patch("pathlib.Path.open", mock_open(read_data="{invalido}")):
        with pytest.raises(json.JSONDecodeError):
            leer_config("config.json")
