# test_calculator.py
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 1) == -1

def test_multiply():
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-1, 1) == -1

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(3, 2) == 1.5
    assert calculator.divide(3, 0) == "Error: Division by zero"

def test_invalid_division_by_zero():
    assert calculator.divide(5, 0) == "Error: Division by zero"
