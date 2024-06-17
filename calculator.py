import re


class Calculator:
    """Creates calculator instance

    A Calculator is used to create calculator object,
    which can be either perform mathematical actions in the
    interactive mode, or can provide addition, subtraction,
    multiplication, division, exponentiation and root actions
    as class methods to be used in code separately.

    Attributes:
        memory: a calculator memory, initially = 0
    """

    def __init__(self):
        """Initializes the calculator instance"""
        self._memory = 0

    def interactive(self):
        """Instantiates the calculator in the interactive mode

        The interactive mode accepts user input as a mathematical
        expression and returns the solution. The user is reprompted again.

        Args:
            s: a string in a format 'n + m', where n,m are digits or
            fractions (1/1); accepted operators ['+', '-', '*', '/', '**'];
            only a single expression with 3 elements are accepted

            s == 'quit': breaks the loop, quits the interactive mode
            s == 'add': prompts for n: float to add to memory
            s == 'm': displays current calculator memory
            s == 'erase': erases the calculator memory

        Returns:
            A solution to the provided mathematical expression as float,
            for example:
            s == '3 ** 3'
            > 81.0
        """
        while True:
            try:
                self.s = input("Enter the expression: ")
                if self.s == "quit":
                    break
                elif self.s == "add":
                    m = float(input("Add to memory: "))
                    self.add(m)
                    continue
                elif self.s == "erase":
                    self.erase()
                elif self.s == "m":
                    print(self.memory)
                else:
                    solution = self.solve(self.s)
                    print(solution)
            except TypeError:
                print("Exptected numeric arguments in format 'n + m'")
                continue
            except ValueError:
                continue
            except IndexError:
                print("Exptected three arguments in format 'n + m'")
                continue
            except ZeroDivisionError:
                print("Division by zero impossible")
                continue

    def validator(self, s: str) -> bool:
        """Validates the user input in the interactive mode

        The function checks the correct length of the input string as list,
        making sure it's a single expression. Matches the pattern to validate
        the format ('n + m')

        Args:
            s: an input string, expected 'n + m', where n,m are digits or
            fractions (1/1); accepted operators ['+', '-', '*', '/', '**'];
            only a single expression with 3 elements are accepted

        Returns:
            A bool if the input string matches the pattern, example:
            s == '4 / 1/2'
            > True

            If the input length is not 3, returns IndexError
        """
        as_l = s.strip().split()
        if len(as_l) != 3:
            return IndexError
        else:
            pattern = re.compile(
                r"^-?(\d+(\.\d+)?(/\d+(\.\d+)?)?)\s[\+\-\*/]\s-?(\d+(\.\d+)?(/\d+(\.\d+)?)?)$|"
                r"^-?(\d+(\.\d+)?(/\d+(\.\d+)?)?)\s\*\*\s-?(\d+(\.\d+)?(/\d+(\.\d+)?)?)$"
            )
            return bool(pattern.match(s))

    def fraction(self, num: str) -> float:
        """Converts fraction str to float

        The function converts string fractions (1/1) in the expression
        to numerical value (float)

        Args:
            num: a str in the format '1/1'

        Returns:
            A division expression as float (a/b), for example:
            num == '1/4'
            > 0.25
        """
        pos = num.index("/")
        a = float(num[:pos])
        b = float(num[pos + 1 :])
        return a / b

    def solve(self, s: str) -> float:
        """Solves the expression in the interactive mode

        Takes input (math expression) and returns the answer, leveraging
        validator(s) and fraction(num) funcs to validate the input. Uses
        class methods sum(a, b), sub(a, b), mult(a, b), div(a, b),
        pow(a, b) for mathematical operations

        Args:
            s: an input string, expected 'n + m', where n,m are digits or
            fractions (1/1); accepted operators ['+', '-', '*', '/', '**'];
            only a single expression with 3 elements are accepted

        Returns:
            A solution to a mathematical expression as float, for example:
            s == '25 / 5'
            > 5.0

        Raises:
            IndexError: if the expression is shorter or longer than 3
            ZeroDivisionError: if b in div(a, b) = 0
            TypeError: if alpha characters are used as parts of expression
        """
        if self.validator(s) == IndexError:
            raise IndexError
        if self.validator(s):
            as_l = s.strip().split()

            if "/" in as_l[0]:
                a = self.fraction(as_l[0])
            else:
                a = float(as_l[0])

            if "/" in as_l[2]:
                b = self.fraction(as_l[2])
            else:
                b = float(as_l[2])

            if as_l[1] == "+":
                return self.sum(a, b)
            if as_l[1] == "-":
                return self.sub(a, b)
            if as_l[1] == "*":
                return self.mult(a, b)
            if as_l[1] == "/":
                if b == 0:
                    raise ZeroDivisionError
                return self.div(a, b)
            if as_l[1] == "**":
                return self.pow(a, b)
        else:
            raise TypeError

    @classmethod
    def sum(cls, a: float, b: float) -> float:
        """Calculates the sum (addition)

        Takes two numeric arguments, returns their sum.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.sum(2, 2))
            > 4.0
        """
        return float(a + b)

    @classmethod
    def sub(cls, a: float, b: float) -> float:
        """Calculates the difference (subtraction)

        Takes two numeric arguments, returns their difference.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.sub(6, -3))
            > 9.0
        """
        return float(a - b)

    @classmethod
    def mult(cls, a: float, b: float) -> float:
        """Calculates the multiplication

        Takes two numeric arguments, returns their multiplication.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.mult(0, 2))
            > 0.0
        """
        return float(a * b)

    @classmethod
    def div(cls, a: float, b: float) -> float:
        """Calculates the division

        Takes two numeric arguments, returns their division.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.div(9, 3))
            > 3.0

        Raises:
            ZeroDivisioError: if b = 0
        """
        return round((a / b), 5)

    @classmethod
    def pow(cls, a: float, b: float) -> float:
        """Calculates the exponentiation

        Takes two numeric arguments, returns a by power of b.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.pow(3, 3))
            > 27.0
        """
        return float(a**b)

    @classmethod
    def root(cls, a: float, b: float) -> float:
        """Calculates the root of degree b

        Takes two numeric arguments, returns the root.

        Args:
            a: a number or a fraction
            b: a number or a fraction

        Returns:
            A result of the expression as float, for example:
            print(c.Calculator.root(81, 4))
            > 3.0

        Raises:
            ZeroDivisionError: if b = 0
        """
        return round((a ** (1 / b)), 5)

    @property
    def memory(self) -> int:
        """
        The initial calculator memory, = 0
        """
        return self._memory

    def add(self, n: float) -> float:
        """Adds to memory

        Takes one argument, adds it to calculator memory

        Args:
            a: a number or a fraction
        """
        self._memory += n

    def erase(self) -> int:
        """Erases the memory

        Resets calculator memory to 0, does not return anything
        """
        self._memory = 0
