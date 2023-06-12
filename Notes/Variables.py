'''In Python, variables are used to store data values. They serve as containers that hold information, allowing you to manipulate and reference the data throughout your code. Here are some key points to understand about Python variables:'''

'''1. Variable Assignment: To create a variable in Python, you use the assignment operator (=). You assign a value to a variable by specifying the variable name on the left side of the equals sign and the value on the right side.

Example:'''
x = 10
name = "John"

'''2. Dynamic Typing: Python is a dynamically typed language, which means you don't need to declare the type of a variable explicitly. The type of a variable is determined by the value it holds. You can assign a different value of any type to the same variable without any issues.

Example:'''
x = 10  # x is an integer
x = "Hello"  # x is now a string

'''3. Variable Naming Rules: Python has certain rules for naming variables:
   - Variable names must start with a letter or an underscore (_).
   - They can contain letters, digits, and underscores.
   - Variable names are case-sensitive, so "myVariable" and "myvariable" are different variables.
   - Avoid using reserved keywords (e.g., "if," "for," "while") as variable names.

Example:'''
my_variable = 10
_name = "John"

'''4. Data Types: Variables can hold values of different data types, such as numbers (integers, floats, complex numbers), strings, booleans, lists, tuples, dictionaries, and more. The type of a variable is determined by the value assigned to it.

Example:'''
x = 10  # Integer
y = 3.14  # Float
name = "John"  # String
is_true = True  # Boolean
numbers = [1, 2, 3, 4, 5]  # List
point = (2, 5)  # Tuple
student = {'name': 'John', 'age': 20}  # Dictionary

'''5. Variable Usage: Once a variable is assigned a value, you can use it in various ways within your code. You can perform operations, manipulate its value, combine it with other variables, and pass it as arguments to functions.

Example:'''
x = 10
y = x + 5
name = "John"
greeting = "Hello, " + name

print(y)  # Output: 15
print(greeting)  # Output: Hello, John
'''

6. Reassigning Variables: You can change the value of a variable by assigning it a new value using the assignment operator. The variable will then hold the new value, and the old value will be overwritten.

Example:'''
x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20

'''Understanding variables is fundamental to programming in Python. They allow you to store and manipulate data, making your code more flexible and powerful.'''