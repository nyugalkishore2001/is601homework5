from decimal import Decimal
from typing import Callable
from calculator import CalcFunctions
from calculator.CalcOperations import *
from calculator.CalcConstructor import *

class Calculator:

    @staticmethod
    def _perform_calculation (a : Decimal, b : Decimal, operation : Callable[[Decimal,Decimal],Decimal]):
        calcConstructor = CalcConstructor.create(a, b, operation)
        CalcFunctions.add_calcoperation(calcConstructor)
        return calcConstructor.perform()
    
    @staticmethod
    def add(a : Decimal,b : Decimal) -> Decimal:
        return Calculator._perform_calculation(a,b,add)
    
    @staticmethod
    def subtract(a : Decimal,b : Decimal) -> Decimal:
        return Calculator._perform_calculation(a,b,subtract)
    
    @staticmethod
    def multiply(a : Decimal,b : Decimal) -> Decimal:
        return Calculator._perform_calculation(a,b,multiply)
    
    @staticmethod
    def divide(a : Decimal,b : Decimal) -> Decimal:
        return Calculator._perform_calculation(a,b,divide)
    
    