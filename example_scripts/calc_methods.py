import calculator as c
import random

"""
This python script shows the functionality of the Calculator module, using its class methods.
"""

# First, let's define the list of numeric values that can be used with Calculator():

digits = [0, 1 / 4, 2.0, 9, 3 / 8, 12]

# Checking the values – printing the values one by one:

for i in digits:
    print(i)

# Now, let's create the calculator object. While it has interactive mode, we'll now focus on checking separate methods

calc = c.Calculator()

# First, controlled trials:

# Addition:
print("Sum: ", c.Calculator.sum(digits[2], digits[1]))

# Subtraction:
print("Subtraction: ", c.Calculator.sub(digits[3], digits[2]))

# Multiplication:
print("Multiplication: ", c.Calculator.mult(digits[5], digits[4]))

# Division:
print("Division: ", c.Calculator.div(digits[4], digits[1]))

# Exponentiation
print("Exponentiation: ", c.Calculator.pow(digits[3], digits[2]))

# Root:
print("Root by: ", c.Calculator.root(digits[3], digits[2]))


# Dividing by zero will raise ZeroDivisionError
try:
    print(c.Calculator.div(digits[3], 0))
except ZeroDivisionError:
    print("9/0: Dividing by zero impossible")


# Now, let's randomize the digits from list:

length = len(digits)

print("Addition")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Sum: ", c.Calculator.sum(a, b))
    except ZeroDivisionError:
        continue

print("Subtraction")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Sub: ", c.Calculator.sub(a, b))
    except ZeroDivisionError:
        continue

print("Multiplication")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Multiplication: ", c.Calculator.mult(a, b))
    except ZeroDivisionError:
        continue

print("Division")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Division: ", c.Calculator.div(a, b))
    except ZeroDivisionError:
        continue

print("Exponentiation")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Exponentiation: ", c.Calculator.pow(a, b))
    except ZeroDivisionError:
        continue

print("Root")
for i in range(length):
    try:
        a = random.choice(digits)
        b = random.choice(digits)
        print("a: ", a, "b: ", b, "Root: ", c.Calculator.root(a, b))
    except ZeroDivisionError:
        continue


# Finally, each Calculator() object has an in-built memory and three associated class methods
# Calculator() memory initially is = 0
x = calc.memory
print(x)

# Adding 10 to memory:
calc.add(10)
x = calc.memory
print(x)

# Erasing the calculator memory
calc.erase()
x = calc.memory
print(x)
