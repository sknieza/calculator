import calculator as c

"""
This python script shows the interactive functionality of the Calculator module.
:input s: An expression in the format 'n + m', where n,m are digits or fractions (1/1)
:type s: str
:raise TypeError: If n,m are not digits or fractions
:raise IndexError: If less or more than one expression entered
:return: Solution of the expresion 'n + m'
:rtype: float
"""

calc = c.Calculator()

calc.interactive()
