import pytest
from calculator import Calculator


def test_solve_default() -> None:
    calc = Calculator()
    assert calc.solve("2 + 1") == 3.0
    assert calc.solve("-18.6 - -18.6") == 0.0
    assert calc.solve("2/3 * 3/2") == 1.0
    assert calc.solve("15.0 / 3/1") == 5.0
    assert calc.solve("2 ** 4") == 16.0
    assert calc.solve("16 ** 1/4") == 2.0


def test_solve_no_of_arguments() -> None:
    calc = Calculator()
    with pytest.raises(IndexError):
        calc.solve("1 + 2 + 4")
    with pytest.raises(IndexError):
        calc.solve("1 +")
    with pytest.raises(IndexError):
        calc.solve("1")
    with pytest.raises(IndexError):
        calc.solve("")


def test_solve_zero_division() -> None:
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.solve("1 / 0")
    with pytest.raises(ZeroDivisionError):
        calc.solve("1 ** 1/0")
    with pytest.raises(ZeroDivisionError):
        calc.solve("1/0 * 6")


def test_solve_alpha() -> None:
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.solve("cat + dog")
    with pytest.raises(TypeError):
        calc.solve("cat + 2")
    with pytest.raises(TypeError):
        calc.solve("3 + dog")
    with pytest.raises(IndexError):
        calc.solve("dog")
