import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2
    assert calculate(-1, 1, '+') == 0
    assert calculate(0.5, 0.5, '+') == 1.0

def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2
    assert calculate(3, 5, '-') == -2
    assert calculate(0, 0, '-') == 0
    assert calculate(-1, -1, '-') == 0

def test_calculate_multiplication():
    assert calculate(2, 3, '*') == 6
    assert calculate(-2, 3, '*') == -6
    assert calculate(0, 5, '*') == 0
    assert calculate(1.5, 2, '*') == 3.0

def test_calculate_division():
    assert calculate(8, 2, '/') == 4
    assert calculate(9, 2, '/') == 4.5
    assert calculate(-6, 3, '/') == -2
    assert calculate(5, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."
    assert calculate(5, 5, '') == "Неизвестная операция."
    assert calculate(5, 5, None) == "Неизвестная операция."
