'''In Python, operators are symbols or special characters that perform various operations on operands (values or variables). Python provides a wide range of operators for different purposes, including arithmetic operations, comparison operations, logical operations, assignment operations, and more. Here are the commonly used operators in Python:

1. Arithmetic Operators:
   - Addition: `+`
   - Subtraction: `-`
   - Multiplication: `*`
   - Division: `/`
   - Modulus (remainder): `%`
   - Exponentiation: `**`
   - Floor Division: `//`

Example:'''
x = 10
y = 3
operators = {
    'addition' : x + y,  # 13
    'subtraction' : x - y,  # 7
    'multiplication' : x * y,  # 30
    'division' : x / y , # 3.3333333333333335
    'modulus' : x % y , # 1
    'exponentiation' : x ** y  ,# 1000
    'floor_division' : x // y  # 3
}
print(operators)

'''2. Comparison Operators:
   - Equal to: `==`
   - Not equal to: `!=`
   - Greater than: `>`
   - Less than: `<`
   - Greater than or equal to: `>=`
   - Less than or equal to: `<=`

Example:'''
x = 10
y = 5

is_equal = x == y  # False
is_not_equal = x != y  # True
is_greater_than = x > y  # True
is_less_than = x < y  # False
is_greater_than_equal = x >= y  # True
is_less_than_equal = x <= y  # False

'''3. Logical Operators:
   - Logical AND: `and`
   - Logical OR: `or`
   - Logical NOT: `not`

Example:'''
x = 10
y = 5
z = 7

logical_and = x > y and x > z  # False
logical_or = x == y or x == z  # False
logical_not = not x == y  # True

'''4. Assignment Operators:
   - Assign: `=`
   - Add and assign: `+=`
   - Subtract and assign: `-=`
   - Multiply and assign: `*=`
   - Divide and assign: `/=`
   - Modulus and assign: `%=`
   - Exponentiate and assign: `**=`
   - Floor divide and assign: `//=`

Example:'''
x = 10

x += 5  # x = x + 5 (15)
x -= 3  # x = x - 3 (12)
x *= 2  # x = x * 2 (24)
x /= 4  # x = x / 4 (6.0)
x %= 2  # x = x % 2 (0.0)
x **= 3  # x = x ** 3 (0.0)
x //= 1.5  # x = x // 1.5 (0.0)

'''5. Membership Operators:
   - `in`: Checks if a value exists in a sequence (list, tuple, string, etc.).
   - `not in`: Checks if a value does not exist in a sequence.

Example:'''
fruits = ['apple', 'banana', 'orange']

is_apple_present = 'apple' in fruits  # True
is_mango_missing = 'mango' not in fruits  # True
'''
These are just some of the commonly used operators in Python. Python'''