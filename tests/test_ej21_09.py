import pytest
from src.condicionales.ej21_09 import determinar_precio, pedir_edad, RANGOS_EDADES, PRECIOS

def test_determinar_precio_bebes():
    assert determinar_precio(3, RANGOS_EDADES, PRECIOS) == 'Tienes 3 años y tienes que pagar 0 euros.'

def test_determinar_precio_ninos():
    assert determinar_precio(10, RANGOS_EDADES, PRECIOS) == 'Tienes 10 años y tienes que pagar 5 euros.'

def test_determinar_precio_adultos():
    assert determinar_precio(25, RANGOS_EDADES, PRECIOS) == 'Tienes 25 años y tienes que pagar 10 euros.'

def test_determinar_precio_menor_de_0():
    with pytest.raises(IndexError):
        determinar_precio(-1, RANGOS_EDADES, PRECIOS)

def test_determinar_precio_mayor_de_120():
    with pytest.raises(IndexError):
        determinar_precio(121, RANGOS_EDADES, PRECIOS)

def test_pedir_edad_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '25')
    assert pedir_edad() == 25

def test_pedir_edad_invalida(monkeypatch):
    inputs = iter(['no_valido', '25'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_edad() == 25

def test_pedir_edad_negativa(monkeypatch):
    inputs = iter(['-1', '25'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_edad() == 25

def test_pedir_edad_mayor_120(monkeypatch):
    inputs = iter(['125', '25'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_edad() == 25
