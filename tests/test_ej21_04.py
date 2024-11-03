import pytest
from src.condicionales.ej21_04 import num_par_o_impar, pedir_num, comprobar_num

def test_num_par_o_impar():
    assert num_par_o_impar(4) == 'par'
    assert num_par_o_impar(3) == 'impar'
    assert num_par_o_impar(0) == 'par'
    assert num_par_o_impar(-2) == 'par'

def test_comprobar_num():
    assert comprobar_num('10') is True
    assert comprobar_num('0') is True
    assert comprobar_num('-5') is True
    assert comprobar_num(' ') is False
    assert comprobar_num('!@#') is False

def test_pedir_num_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    assert pedir_num() == 10

def test_pedir_num_invalido(monkeypatch):
    inputs = iter(['adfg', '10'])  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_num() == 10
