import pytest
from src.condicionales.ej21_03 import division, pedir_num, comprobar_num, comprobar_cero

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(-10, 2) == -5
    assert division(10, -2) == -5

def test_comprobar_num():
    assert comprobar_num('10') is True
    assert comprobar_num('3.5') is False  
    assert comprobar_num('abc') is False
    assert comprobar_num(' ') is False

def test_comprobar_cero():
    assert comprobar_cero(5) is True
    assert comprobar_cero(0) is False

def test_pedir_num_dividendo(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    assert pedir_num(0) == 10.0

def test_pedir_num_divisor(monkeypatch):
    inputs = iter(['0', '2']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_num(1) == 2.0
