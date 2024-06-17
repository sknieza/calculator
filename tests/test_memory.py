import pytest
from calculator.calculator import Calculator


def test_memory_default() -> None:
    calc = Calculator()
    assert calc.memory == 0


def test_add_to_memory() -> None:
    calc = Calculator()
    assert calc.add(2) == None
    assert calc.add(1 / 3) == None
    assert calc.add(0) == None
    assert calc.add(4.5) == None
    with pytest.raises(TypeError):
        calc.add("dog")
    with pytest.raises(NameError):
        calc.add(dog)
    with pytest.raises(ZeroDivisionError):
        calc.solve(5 / 0)


def test_erase_memory() -> None:
    calc = Calculator()
    assert calc.memory == 0
    calc.add(5)
    assert calc.memory == 5
    calc.erase()
    assert calc.memory == 0
