from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_creation():
    calc = Calculation.create(Decimal('2'), Decimal('3'), add)
    assert calc.a == Decimal('2')
    assert calc.b == Decimal('3')
    assert calc.operation == add

def test_calculation_perform():
    calc = Calculation.create(Decimal('2'), Decimal('3'), add)
    assert calc.perform() == Decimal('5')

def test_calculation_repr():
    calc = Calculation.create(Decimal('2'), Decimal('3'), add)
    assert repr(calc) == "Calculation(2, 3, add)"