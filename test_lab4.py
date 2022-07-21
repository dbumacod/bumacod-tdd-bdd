import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b


@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_lab4_subtract(base_calculator):
    assert base_calculator.subtract(15,10) == 5
    assert base_calculator.subtract(17,-5) == 22
    assert base_calculator.subtract(2,10) == -8
    #assert base_calculator.subtract(2,10) == 8
    
def test_lab4_multiply(base_calculator):
    assert base_calculator.multiply(14,2) == 28
    assert base_calculator.multiply(5,-5) == -25
    assert base_calculator.multiply(-3,-4) == 12
    #assert base_calculator.multiply(-3,-4) == -12
