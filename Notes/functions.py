'''In Python, functions are blocks of reusable code that perform specific tasks. They are defined using the `def` keyword followed by the function name, parentheses `( )`, and a colon `:`. Functions can have parameters (inputs) and can optionally return a value.

Here's the general syntax for defining a function in Python:'''

def function_name(parameter1, parameter2):
    # Function body (code block)
    # Perform operations and computations
    # Optionally, return a value
    return result

'''Let's break down the components of a function:

- `def`: It is the keyword used to define a function.
- `function_name`: It is the name given to the function. Choose a meaningful and descriptive name to indicate the purpose of the function.
- `parameters`: These are optional placeholders for values that the function expects as inputs. Parameters are enclosed in parentheses, and multiple parameters are separated by commas. They act as variables within the function.
- `:`: It marks the end of the function definition header and indicates the start of the function body.
- Function body: It is an indented block of code that contains the statements to be executed when the function is called. The body can include any valid Python code, such as assignments, loops, conditionals, and function calls.
- `return`: It is an optional statement that specifies the value to be returned by the function. It terminates the execution of the function and passes the value back to the caller. If no return statement is used, the function returns `None` by default.'''
'''
Here's an example of a simple function that adds two numbers and returns the result:
'''
def add_numbers(a, b):
    sum = a + b
    return sum
'''
To use a function, you call it by its name and provide the required arguments (if any). The function executes its code block and may return a value.'''

result = add_numbers(3, 4)
print(result)  # Output: 7

'''Functions provide modularity and reusability in code. They allow you to encapsulate a specific set of instructions into a single entity, making the code more organized and easier to maintain. Functions can be called multiple times with different arguments, and they help avoid repetitive code by promoting code reuse.'''