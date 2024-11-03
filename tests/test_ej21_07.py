import pytest
from src.condicionales.ej21_07 import calcular_impuestos, determinar_tramo, pedir_renta_anual, RENTAS

def test_calcular_impuestos():
    assert calcular_impuestos(15000, 15) == 2250.0
    assert calcular_impuestos(25000, 20) == 5000.0
    assert calcular_impuestos(50000, 30) == 15000.0
    assert calcular_impuestos(75000, 45) == 33750.0
    assert calcular_impuestos(0, 5) == 0.0

def test_determinar_tramo():
    assert determinar_tramo(5000, RENTAS) == (0, 10000, 5)
    assert determinar_tramo(15000, RENTAS) == (10000, 20000, 15)
    assert determinar_tramo(25000, RENTAS) == (20000, 35000, 20)
    assert determinar_tramo(50000, RENTAS) == (35000, 60000, 30)

def test_pedir_renta_anual_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '35000')
    assert pedir_renta_anual() == 35000.0

def test_pedir_renta_anual_invalida(monkeypatch):
    inputs = iter(['no_valido', '25000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_renta_anual() == 25000.0
