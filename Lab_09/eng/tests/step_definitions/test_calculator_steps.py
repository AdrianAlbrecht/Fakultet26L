import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.calculator import Calculator

# Load scenarios from the feature file.
scenarios('../features/calculator.feature')

# Fixture that provides an instance of Calculator.
@pytest.fixture
def calculator():
    return Calculator()

# Step definition for the Given step.
@given("I have a calculator")
def given_calculator(calculator):
    return calculator

# Step definition for adding numbers.
@when(parsers.parse("I add the numbers {a:Number} and {b:Number}", extra_types={"Number": int}))
def when_add(calculator, a, b):
    calculator.add(a, b)

# Step definition for subtracting numbers.
@when(parsers.parse("I subtract {b:Number} from {a:Number}", extra_types={"Number": int}))
def when_subtract(calculator, a, b):
    calculator.subtract(a, b)

# Step definition for multiplying numbers.
@when(parsers.parse("I multiply the numbers {a:Number} and {b:Number}", extra_types={"Number": int}))
def when_multiply(calculator, a, b):
    calculator.multiply(a, b)

# Step definition to validate the result.
@then(parsers.parse("the result should be {expected:Number}", extra_types={"Number": int}))
def then_result(calculator, expected):
    assert calculator.result == expected
