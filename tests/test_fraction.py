import pytest
from calculator.calculator import Calculator


def test_fraction_default() -> None:
    calc = Calculator()
    assert calc.fraction("1/2") == 1 / 2
    assert calc.fraction("5/3") == 5 / 3
    assert calc.fraction("0/2") == 0


def test_fraction_zero_division() -> None:
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.fraction("1/0")


def test_fraction_no_of_arguments() -> None:
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.fraction("1")
    with pytest.raises(ValueError):
        calc.fraction("1/4 1")
    with pytest.raises(ValueError):
        calc.fraction("1 2/3")
    with pytest.raises(ValueError):
        calc.fraction("2 3")
    with pytest.raises(ValueError):
        calc.fraction("1-4")
