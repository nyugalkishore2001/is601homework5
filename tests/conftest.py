import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

faker = Faker()

def create_test_cases(record_count):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(record_count):
        num1 = Decimal(faker.random_number(digits=2))
        num2 = Decimal(faker.random_number(digits=2)) if _ % 4 != 3 else Decimal(faker.random_number(digits=1))
        operation_key = faker.random_element(elements=list(operations.keys()))
        operation_func = operations[operation_key]

        if operation_func == divide:
            num2 = Decimal('1') if num2 == Decimal('0') else num2

        try:
            if operation_func == divide and num2 == Decimal('0'):
                result = "ZeroDivisionError"
            else:
                result = operation_func(num1, num2)
        except ZeroDivisionError:
            result = "ZeroDivisionError"

        yield num1, num2, operation_key, operation_func, result

def pytest_addoption(parser):
    parser.addoption("--test_cases", action="store", default=5, type=int, help="Number of test cases to generate")

def pytest_generate_tests(metafunc):
    if {"num1", "num2", "expected_result"}.intersection(set(metafunc.fixturenames)):
        test_count = metafunc.config.getoption("test_cases")
        test_data = list(create_test_cases(test_count))

        formatted_data = [
            (num1, num2, op_key if 'operation_key' in metafunc.fixturenames else op_func, result)
            for num1, num2, op_key, op_func, result in test_data
        ]
        
        metafunc.parametrize("num1,num2,operation,expected_result", formatted_data)
