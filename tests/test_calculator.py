"This is the test file"
from calculator import add

def test_addition():
    "Returns he sum of two numbers"
    assert add(2,2) == 4
