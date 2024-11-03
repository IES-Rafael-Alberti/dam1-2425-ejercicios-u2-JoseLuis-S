import pytest
from src.condicionales.ej21_02 import comprobarContraseña, preguntarContraseña, pedirContraseña

def test_comprobarContraseña_correcta():
    assert comprobarContraseña('password123', 'password123') == 'Has introducido la contraseña con exito.'

def test_comprobarContraseña_incorrecta():
    assert comprobarContraseña('password123', 'password456') == 'Has introducido la contraseña incorrecta.'

def test_pedirContraseña(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Password123')
    assert pedirContraseña() == 'password123'

def test_preguntarContraseña(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Password456')
    assert preguntarContraseña() == 'password456'
