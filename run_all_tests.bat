@echo off
echo ========================================
echo  EJECUTANDO TODAS LAS PRUEBAS
echo ========================================
echo.

echo [1/4] Verificando Node.js...
node --version
if %errorlevel% neq 0 (
    echo ERROR: Node.js no esta instalado
    pause
    exit /b 1
)

echo [2/4] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado
    pause
    exit /b 1
)

echo.
echo ========================================
echo  PRUEBAS DE JAVASCRIPT (Jest)
echo ========================================
echo.

call npm test

echo.
echo ========================================
echo  PRUEBAS DE PYTHON (pytest)
echo ========================================
echo.

python -m pytest python/ -v

echo.
echo ========================================
echo  TODAS LAS PRUEBAS COMPLETADAS
echo ========================================
echo.
pause
