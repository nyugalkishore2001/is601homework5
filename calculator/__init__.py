from calculator.CalcOperations import *
from calculator.CalcConstructor import *

class Calculator:
    @staticmethod
    def add(a,b):
        calcConstructor = CalcConstructor(a,b,add)
        return calcConstructor.get_result()
    @staticmethod
    def subtract(a,b):
        calcConstructor = CalcConstructor(a,b,subtract)
        return calcConstructor.get_result()
    @staticmethod
    def multiply(a,b):
        calcConstructor = CalcConstructor(a,b,multiply)
        return calcConstructor.get_result()
    @staticmethod
    def divide(a,b):
        calcConstructor = CalcConstructor(a,b,divide)
        return calcConstructor.get_result()
    