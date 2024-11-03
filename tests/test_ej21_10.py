import pytest
from src.condicionales.ej21_10 import elegir_tipo_pizza, elegir_ingrediente, INGREDIENTES_PARA_PERSONAS, INGREDIENTES_VEGANOS

def test_elegir_tipo_pizza_si(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'si')
    tipo = elegir_tipo_pizza()
    assert tipo == 'vegetariana'

def test_elegir_tipo_pizza_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    tipo = elegir_tipo_pizza()
    assert tipo == 'normal'

def test_elegir_tipo_pizza_invalido(monkeypatch):
    inputs = iter(['talvez', 'si'])  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tipo = elegir_tipo_pizza()
    assert tipo == 'vegetariana'  

def test_elegir_ingrediente_normal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'peperoni')
    ingrediente = elegir_ingrediente('normal', INGREDIENTES_PARA_PERSONAS, INGREDIENTES_VEGANOS)
    assert ingrediente == 'peperoni'

def test_elegir_ingrediente_vegano(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'tofu')
    ingrediente = elegir_ingrediente('vegetariana', INGREDIENTES_PARA_PERSONAS, INGREDIENTES_VEGANOS)
    assert ingrediente == 'tofu'

def test_elegir_ingrediente_invalido(monkeypatch):
    inputs = iter(['queso', 'pimiento']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ingrediente = elegir_ingrediente('vegetariana', INGREDIENTES_PARA_PERSONAS, INGREDIENTES_VEGANOS)
    assert ingrediente == 'pimiento' 