import pytest
from calculator.history import History
from calculator.calculation import Calculation

def test_add():
    #Tests to see if addition works
    calc = Calculation()
    assert calc.add(1, 2) == 3

def test_subtract():
    #Tests to see if subtraction works
    calc = Calculation()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    #Tests to see if multiplication works
    calc = Calculation()
    assert calc.multiply(2, 4) == 8

def test_divide():
    #Tests to see if division works
    calc = Calculation()
    assert calc.divide(8, 2) == 4

def test_divide_by_zero():
    #Tests to see if dividing by zero runs or fails
    with pytest.raises(ZeroDivisionError):
        Calculation.divide(1, 0)

def test_history():
    #Tests retrieving hprevious calculations
    History.clear_history()
    Calculation.add(10, 20)
    assert "Added 10 to 20 got 30" in History.get_history()