# archivo: tests/test_funciones.py
from src.funciones import clasificar_por_posteo

def test_clasificar_por_posteo():
    assert clasificar_por_posteo(6) == "Activo"
    assert clasificar_por_posteo(3) == "Inactivo"
