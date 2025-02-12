from typing import List
from calculator.CalcConstructor import CalcConstructor

class ClacFunctions:
    calcHistory : List[CalcConstructor]=[] 

    @classmethod
    def add_calcoperation(cls, calcConstructor : CalcConstructor):
        cls.calcHistory.append(calcConstructor) 

    @classmethod
    def get_history(cls) -> List[CalcConstructor]:
        return cls.calcHistory

    @classmethod
    def clear_history(cls):
        cls.calcHistory.clear

    @classmethod
    def get_latest(cls):
        if cls.calcHistory:
            return cls.calcHistory[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str ) -> List[CalcConstructor]:
        return [calc for calc in cls.calcHistory if calc.operation.__name__ == operation_name]  
        