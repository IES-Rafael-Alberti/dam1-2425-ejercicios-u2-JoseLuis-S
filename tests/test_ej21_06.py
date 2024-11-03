import pytest
from src.condicionales.ej21_06 import determinar_grupo, pedir_genero, pedir_nombre, GRUPOS, LETRA_HOMBRE, LETRA_MUJER

def test_determinar_grupo():
    assert determinar_grupo('masculino', 'Carlos', GRUPOS, LETRA_HOMBRE, LETRA_MUJER) == 'B'
    assert determinar_grupo('masculino', 'Oscar', GRUPOS, LETRA_HOMBRE, LETRA_MUJER) == 'A'
    assert determinar_grupo('femenino', 'Maria', GRUPOS, LETRA_HOMBRE, LETRA_MUJER) == 'B'
    assert determinar_grupo('femenino', 'Ana', GRUPOS, LETRA_HOMBRE, LETRA_MUJER) == 'A'

def test_pedir_genero_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'masculino')
    assert pedir_genero() == 'masculino'
    monkeypatch.setattr('builtins.input', lambda _: 'femenino')
    assert pedir_genero() == 'femenino'

def test_pedir_genero_invalido(monkeypatch):
    inputs = iter(['otro', 'femenino'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_genero() == 'femenino'

def test_pedir_nombre_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Carlos')
    assert pedir_nombre() == 'Carlos'
    monkeypatch.setattr('builtins.input', lambda _: 'maria')
    assert pedir_nombre() == 'Maria'

def test_pedir_nombre_invalido(monkeypatch):
    inputs = iter(['Carlos123', 'Ana'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pedir_nombre() == 'Ana'
