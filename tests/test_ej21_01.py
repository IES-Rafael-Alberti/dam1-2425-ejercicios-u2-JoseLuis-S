import pytest
from src.condicionales.ej21_01 import comprobarMayoriaEdad, pedirEdad, comprobarEdad


def test_comprobarMayoriaEdad_mayor():
    assert comprobarMayoriaEdad(18) == 'Felicidades!! Puedes tomarte una cerveza e ir a la carcel.'
    assert comprobarMayoriaEdad(30) == 'Felicidades!! Puedes tomarte una cerveza e ir a la carcel.'

def test_comprobarMayoriaEdad_menor():
    assert comprobarMayoriaEdad(17) == 'Felicidades!! Aun puedes no tener responsabilidades.'
    assert comprobarMayoriaEdad(0) == 'Felicidades!! Aun puedes no tener responsabilidades.'

def test_comprobarEdad_valida():
    assert comprobarEdad("18") is True
    assert comprobarEdad("30") is True
    assert comprobarEdad("0") is True
    assert comprobarEdad("120") is True

def test_comprobarEdad_invalida():
    assert comprobarEdad("abc") is False     
    assert comprobarEdad("18.5") is False    
    assert comprobarEdad("-5") is False      
    assert comprobarEdad("121") is False     
  
def test_pedirEdad_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "25")
    assert pedirEdad() == 25

def test_pedirEdad_invalida(monkeypatch):
    inputs = iter(["abc", "18"])  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedirEdad() == 18

