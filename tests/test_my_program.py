import pytest
from my_program import Calculator

@pytest.mark.unit
def test_unittest1():
    calc = Calculator()  # Create an instance of Calculator
    result = calc.add(3, 4)  # Combine overall operation
    assert result == 7  # Check the final outcome

@pytest.mark.unit
def test_unittest2():
    calc = Calculator()  
    result = calc.add(1, -1)
    assert result == 0  

@pytest.mark.unit
def test_unittest3():
    calc = Calculator()
    result = calc.add(0, 0)
    assert result == 0     

@pytest.mark.unit
def test_unittest4():
    calc = Calculator()
    result = calc.multiply(3, 4)
    assert result == 12 

@pytest.mark.unit
def test_unittest5():
    calc = Calculator()
    result = calc.multiply(0, 0)
    assert result == 0  

@pytest.mark.unit
def test_unittest6():
    calc = Calculator()
    result = calc.multiply(-1, 1)
    assert result == -1   

@pytest.mark.integration
def test_sum_of_squares1():
    calc = Calculator()
    result = calc.add(calc.multiply(1, 1), calc.multiply(1, 1))
    assert result == 2

@pytest.mark.integration
def test_sum_of_squares2():
    calc = Calculator()
    result = calc.add(calc.multiply(0, 0), calc.multiply(0, 0))
    assert result == 0

@pytest.mark.integration
def test_sum_of_squares3():
    calc = Calculator()
    result = calc.add(calc.multiply(-1, -1), calc.multiply(-1, -1))
    assert result == 2