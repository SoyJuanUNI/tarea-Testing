#!/bin/bash

echo "========================================"
echo " EJECUTANDO TODAS LAS PRUEBAS"
echo "========================================"
echo ""

echo "[1/4] Verificando Node.js..."
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js no está instalado"
    exit 1
fi
node --version

echo "[2/4] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python no está instalado"
    exit 1
fi
python3 --version

echo ""
echo "========================================"
echo " PRUEBAS DE JAVASCRIPT (Jest)"
echo "========================================"
echo ""

npm test

echo ""
echo "========================================"
echo " PRUEBAS DE PYTHON (pytest)"
echo "========================================"
echo ""

python3 -m pytest python/ -v

echo ""
echo "========================================"
echo " TODAS LAS PRUEBAS COMPLETADAS"
echo "========================================"
echo ""
