# `Calculator` module

## 00 Functionality and installation

The `calculator` is a Python module that can perform basic mathematical operations, using its class methods. 

### The `calculator` instance can:

- Add two numbers together (a + b)
- Subtract one number from another (a - b)
- Multiply two numbers (a * b)
- Divide number by another (a / b)
- Raise the number by the power of another (a ** b)
- Take a number root by the degree of another num (a root^b)

Every instance also has a default memory = 0, which can be increased or erased back to 0.

To start using the module, in your script, import the module as follows:

```python
import calculator as c
```

## 01 Module methods

The `calculator` has 6 methods which represent main basic mathematical operations. Their format is `c.method(a, b)`, where:
- `c` is an instance, created from a module class
- `method` is a mathematical operation that is called
- `a` and `b` are numbers in format `1`, `1.0` or `1/1`

These methods can be called as follows:

### Addition

`c.sum(a, b)` returns the sum of two numbers.

```python
c.sum(2.0, 5)
# returns 7.0
```

### Subtraction

`c.sub(a, b)` returns the difference of two numbers.

```python
c.sub(2.0, 5)
# returns -3.0
```

### Multiplication

`c.mult(a, b)` returns the multiplication of two numbers.

```python
c.mult(2.0, 5)
# returns 10.0
```

### Division

`c.div(a, b)` returns the division of two numbers.

```python
c.div(2.0, 5)
# returns 0.4
```

### Exponentiation

`c.pow(a, b)` returns the exponentiation of a by b.

```python
c.pow(2.0, 5)
# returns 32.0
```

### Root

`c.root(a, b)` returns the the root of a by degree of b.

```python
c.pow(32, 5)
# returns 2.0
```

To see how these methods operate in code, refer to the nothebook `calc_methods.ipynb`.

## 02 `calculator` memory

The instantiated calculator object has a default memory of zero. It can be further manipulated and used in opearations, using class methods.

### Memory

The property `c.memory`, initially set to 0, returns the current memory of the calculator:

```python
x = c.memory
print(x)
# returns 0
```

### Add to memory

The `c.add(n)` method adds number `n` to the current memory:

```python
c.add(10)
x = c.memory
print(x)
# returns 10
```

### Erase memory

The `c.erase()` method resets the memory to 0:

```python
calc.erase()
x = calc.memory
print(x)
# returns 0
```

### Use memory

The value of `c.memory` can be assigned to varibles and used in code as any other number, for example:

```python
calc.add(5)
x = calc.memory
y = calc.div(50, 10)
print(calc.sum(x, y))
# returns 15.0
```

## 03 `interactive` mode

The `calculator` module also has the `c.interactive()` method, which initializes the interactive calculator. It leverages the class methods, and performs the following operations:

- Add two numbers together (a + b)
- Subtract one number from another (a - b)
- Multiply two numbers (a * b)
- Divide number by another (a / b)
- Raise the number by the power of another (a ** b)

**Notice** that interactive mode doesn't have the `root` option as there's no specific root operator in mathematical expressions. However, remember, that the root of the `n` degree is also the exponentiation by the power of `1/n`. Thus, the cubic root of 27 can be expressed as `27 ** 1/3`.

### Expected input

This interactive mode expects a string as input in the format as follows:

- Add: `"a + b"`
- Subtract: `"a - b"`
- Multiply: `"a * b"`
- Divide: `"a / b"`
- Exponentiate: `"a ** b"`

The numbers `a` and `b` are expected to be digits in the format 1, 1.0 or 1/1 – i.e., `int`, `float` or a fraction.

### Special inputs

Interactive calculator mode accepts some special inputs that steer the operations of the instance.

- `'quit'` will break the loop, effectivelly making the calculator stop and close
- `'add'` will reprompt for `n` (num) to add to calculator memory
- `'m'` displays the current calculator memory
- `'erase'` will reset calculator memory to 0

## 04 Package contents

This package contains the following files:
1. `/tests` dir with tests for various module methods;
2. `calculator.py`, the main module script, containing the `Calculator()` class and its methods;
3. `calc_methods.py` and `calc_instance.py` – demo scripts of method and interactive functionalities of the module;
4. `calc_methods.ipynb` and `calc_instance.ipynb` – demo scripts as Jupyter Notebooks.