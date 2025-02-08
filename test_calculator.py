# test_calculator.py

import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    resultado = calc.add(2, 3)
    assert resultado == 5, "A soma de 2 e 3 deve ser 5"

def test_subtraction():
    calc = Calculator()
    resultado = calc.subtract(10, 4)
    assert resultado == 6, "A subtração de 10 por 4 deve ser 6"

def test_multiplication():
    calc = Calculator()
    resultado = calc.multiply(3, 4)
    assert resultado == 12, "A multiplicação de 3 por 4 deve ser 12"

def test_division():
    calc = Calculator()
    resultado = calc.divide(10, 2)
    assert resultado == 5, "A divisão de 10 por 2 deve ser 5"

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
