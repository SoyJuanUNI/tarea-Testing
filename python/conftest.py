import os
import sys

# Asegura que la carpeta 'python' esté en sys.path para los imports de los tests
CURRENT_DIR = os.path.dirname(__file__)
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)
