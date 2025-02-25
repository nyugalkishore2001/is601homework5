import pytest
from decimal import Decimal
from calculator import Calculator

def test_addition():
    assert Calculator.add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtraction():
    assert Calculator.subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiplication():
    assert Calculator.multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_division():
    assert Calculator.divide(Decimal('6'), Decimal('3')) == Decimal('2')

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('6'), Decimal('0'))