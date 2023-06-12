'''In Python, decorators are a way to modify the behavior of functions or classes by wrapping them with other functions. Decorators provide a concise and reusable way to add functionality to existing functions without modifying their source code. They make use of the concept of higher-order functions, where functions can accept other functions as arguments and return functions as values. Here's how decorators work:

1. Decorator Function: A decorator function is a function that takes another function as input, adds some functionality or modifications to it, and returns a new function that incorporates the changes. The decorator function is typically defined using the `@` symbol followed by the decorator name, which is placed above the function to be decorated.

Example of a decorator function:'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add additional functionality before the original function is called
        print("Before function execution")
        result = original_function(*args, **kwargs)  # Call the original function
        # Add additional functionality after the original function is called
        print("After function execution")
        return result
    return wrapper_function 

'''2. Applying Decorators: To apply a decorator to a function, you simply place the decorator name above the function definition using the `@` symbol. This syntactic sugar makes it easier to apply decorators to multiple functions.

Example of applying a decorator:'''
@decorator_function
def greet():
    print("Hello, world!")

'''In the above example, the `decorator_function` is applied to the `greet` function using the `@` syntax. Now, whenever the `greet` function is called, it will be wrapped with the additional functionality defined in the decorator.
'''
'''3. Decorator Class: Decorators can also be implemented using classes. In this case, the decorator class defines `__init__` and `__call__` methods, where `__call__` is responsible for modifying the behavior of the wrapped function.

Example of a decorator class:'''
class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        # Add additional functionality before the original function is called
        print("Before function execution")
        result = self.original_function(*args, **kwargs)  # Call the original function
        # Add additional functionality after the original function is called
        print("After function execution")
        return result
    
'''
To apply the decorator class, you create an instance of the class and use it to decorate the target function.

Example of applying a decorator class:'''
@DecoratorClass
def greet():
    print("Hello, world!")
'''
Decorators are commonly used for tasks such as logging, input validation, timing functions, or applying authentication and authorization checks to functions. They provide a clean and reusable way to modify the behavior of functions without altering their original code.'''