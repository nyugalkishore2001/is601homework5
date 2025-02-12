from decimal import Decimal
from typing import Callable


class CalcConstructor:

    def __init__(self,a : Decimal,b : Decimal,operation : Callable[[Decimal,Decimal],Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    def create(a : Decimal, b : Decimal, operation : Callable[[Decimal,Decimal],Decimal]):
        return CalcConstructor(a,b,operation)
    
    def perform(self) -> Decimal:
        return self.operation(self.a,self.b)
    
    def __repr__(self):
        return "Operation({self.a},{self.b},{self.operation.__name__})"
