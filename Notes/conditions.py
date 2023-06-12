'''In Python, conditions are used to make decisions and execute different blocks of code based on whether a certain condition is true or false. Conditions are typically used with control flow statements like if-else statements and loops. Here are the key components of working with conditions in Python:

1. Comparison Operators: Python provides several comparison operators to compare values and create conditions. These operators include:
   - Equal to: `==`
   - Not equal to: `!=`
   - Greater than: `>`
   - Less than: `<`
   - Greater than or equal to: `>=`
   - Less than or equal to: `<=`

Example:'''
x = 10
y = 5

# Equal to
if x == y:
    print("x is equal to y")

# Greater than
if x > y:
    print("x is greater than y")

# Less than or equal to
if x <= y:
    print("x is less than or equal to y")

'''2. Logical Operators: Python also provides logical operators to combine or modify conditions. The commonly used logical operators are:
   - Logical AND: `and`
   - Logical OR: `or`
   - Logical NOT: `not`

Example:'''
x = 10
y = 5
z = 7

# Using logical AND
if x > y and x > z:
    print("x is the largest number")

# Using logical OR
if x == y or x == z:
    print("x is equal to either y or z")

# Using logical NOT
if not x == y:
    print("x is not equal to y")

'''3. if-else Statements: The if-else statement is used to execute different blocks of code based on a condition. If the condition is true, the code inside the if block is executed. Otherwise, if the condition is false, the code inside the else block is executed.

Example:'''
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

'''4. Nested if Statements: You can also have nested if statements, where an if statement is present inside another if or else block. This allows you to create more complex conditions and decision-making structures.

Example:'''
x = 10

if x > 5:
    if x > 7:
        print("x is greater than 7")
    else:
        print("x is greater than 5 but not greater than 7")
else:
    print("x is not greater than 5")

'''Conditions are fundamental to controlling the flow of your program. They allow you to execute specific blocks of code based on the state of variables or other conditions.'''