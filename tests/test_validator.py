import pytest
from calculator.calculator import Calculator

def test_validator_default() -> None:
    calc = Calculator()
    assert calc.validator("2 + 1") == True
    assert calc.validator("1/2 - 3") == True
    assert calc.validator("2.3 * 2") == True
    assert calc.validator("9 / 1/3") == True
    assert calc.validator("9 ** 2") == True
    assert calc.validator("81 ** 1/2") == True


def test_validator_no_of_arguments() -> None:
    calc = Calculator()
    assert calc.validator("2 + 1 - 3") == IndexError
    assert calc.validator("1/2") == IndexError
    assert calc.validator("") == IndexError
    assert calc.validator("2 **") == IndexError
    assert calc.validator("2+1") == IndexError


def test_validator_alpha_args() -> None:
    calc = Calculator()
    assert calc.validator("2 + cat") == False
    assert calc.validator("cat") == IndexError
    assert calc.validator("cat plus dog") == False
    assert calc.validator("dog + 4") == False
    assert calc.validator("dog +") == IndexError
    assert calc.validator("dog + cat") == False