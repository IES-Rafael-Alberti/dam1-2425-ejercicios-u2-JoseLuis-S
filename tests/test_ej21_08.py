import pytest
from src.condicionales.ej21_08 import calcular_salario, pedir_puntuacion, SALARIO_BASE

def test_calcular_salario():
    assert calcular_salario(0.0, SALARIO_BASE) == 0.0
    assert calcular_salario(0.4, SALARIO_BASE) == 960.0
    assert calcular_salario(0.6, SALARIO_BASE) == 1440.0
    assert calcular_salario(1.0, SALARIO_BASE) == 2400.0
    assert calcular_salario(1.5, SALARIO_BASE) == 3600.0

def test_pedir_puntuacion_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '0.6')
    assert pedir_puntuacion() == 0.6

def test_pedir_puntuacion_invalida_y_valida(monkeypatch):
    inputs = iter(['no_valido', '0.4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_puntuacion() == 0.4

def test_pedir_puntuacion_superior(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1.2')
    assert pedir_puntuacion() == 1.2
