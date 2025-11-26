import pytest
from my_program import Calculator

def test_unittest1():
    calc = Calculator()  # Create an instance of Calculator
    result = calc.add(3, 4)  # Combine overall operation
    assert result == 7  # Check the final outcome

def test_unittest2():
    calc = Calculator()  
    result = calc.add(1, -1)
    assert result == 0  

def test_unittest3():
    calc = Calculator()
    result = calc.add(0, 0)
    assert result == 0     

#this is a test