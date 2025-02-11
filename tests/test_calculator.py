'''My Calculator Test'''
from calculator import add, multiply, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(2,2) == 4

def test_division():
    '''Test that division function works '''    
    assert divide(2,2) == 1

def test_division_by_zero():
    '''Test that division function works '''    
    assert divide(2,0) == "Error : Division by zero"
