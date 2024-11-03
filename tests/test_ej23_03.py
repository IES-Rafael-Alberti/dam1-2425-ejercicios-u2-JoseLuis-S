import pytest
from src.excepciones.ej23_03 import generar_cuenta_atras, pedir_num

def test_generar_cuenta_atras():
    assert generar_cuenta_atras(5) == '5, 4, 3, 2, 1 y 0'
    assert generar_cuenta_atras(0) == '0'
    assert generar_cuenta_atras(2) == '2, 1 y 0'
    assert generar_cuenta_atras(10) == '10, 9, 8, 7, 6, 5, 4, 3, 2, 1 y 0'

def test_pedir_num_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert pedir_num() == 3

def test_pedir_num_no_entero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(ValueError):
        pedir_num()

def test_pedir_num_negativo(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '-5')
    with pytest.raises(ValueError):
        pedir_num()