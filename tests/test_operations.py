from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply():
    assert multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide():
    assert divide(Decimal('6'), Decimal('3')) == Decimal('2')

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(Decimal('6'), Decimal('0'))