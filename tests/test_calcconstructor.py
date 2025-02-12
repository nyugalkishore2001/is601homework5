from decimal import Decimal
import pytest

from calculator.CalcConstructor import CalcConstructor
from calculator.CalcOperations import add,subtract,multiply,divide


@pytest.mark.parameterize("a,b,operation,expected",[
    (Decimal('3'), Decimal('4'), add, Decimal('7')),
    (Decimal('3'), Decimal('4'), subtract, Decimal('-1')),
    (Decimal('3'), Decimal('4'), multiply, Decimal('12')),
    (Decimal('2'), Decimal('4'), divide, Decimal('0.5')),
    (Decimal('3.5'), Decimal('4.5'), add, Decimal('8')),
    (Decimal('3.5'), Decimal('4.5'), subtract, Decimal('-1.5')),
    (Decimal('3.5'), Decimal('4.5'), multiply, Decimal('15.75')),
    (Decimal('3.5'), Decimal('10'), divide, Decimal('0.35')),
])

def test_calculation_operations(a, b, operation, expected):
    calc = CalcConstructor(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    calc = CalcConstructor(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr

def test_divide_by_zero():
    calc = CalcConstructor(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
