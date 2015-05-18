from nose.tools import *
from calculator import Calculator

def test_evaluate():
    myCalculator = Calculator()
    assert_equal(myCalculator.evaluate("2 + -1 + 1 * 0 % 3 + 2 * 2 - 1"), 4.0)

def test_evaluate2():
    myCalculator = Calculator()
    assert_equal(myCalculator.evaluate("2 - -23423432"), 23423434.0)

def test_evaluate3():
    myCalculator = Calculator()
    assert_equal(myCalculator.evaluate("2 * -23423432"), -46846864.0)
    
def test_process_operations():
    myCalculator = Calculator()
    assert_equal(myCalculator.process_operations(['3', '+', '2', '*', '5', '-', '6', '/', '3'], ['*', '/']), ['3', '+', '10.0', '-', '2.0'])

def test_multiply():
    myCalculator = Calculator()
    assert_equal(myCalculator.multiply(3, 4), 12)

def test_divide():
    myCalculator = Calculator()
    assert_equal(myCalculator.divide(8, 4), 2)

def test_add():
    myCalculator = Calculator()
    assert_equal(myCalculator.add(3, 4), 7)

def test_subtract():
    myCalculator = Calculator()
    assert_equal(myCalculator.subtract(3, 4), -1)

def test_modulo():
    myCalculator = Calculator()
    assert_equal(myCalculator.modulo(3, 4), 3)


