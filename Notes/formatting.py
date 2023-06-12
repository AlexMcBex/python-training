'''Python provides several ways to format strings, allowing you to dynamically insert values into text or control the appearance of the output. Here are some common techniques for string formatting in Python:

1. String Concatenation: You can concatenate strings together using the addition operator (+). This allows you to combine strings and variables into a single string.

Example:'''
name = "John"
age = 25

message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)  # Output: My name is John and I am 25 years old.

'''2. Using the `%` Operator (Old-style Formatting): Python supports the `%` operator for string formatting, often referred to as "old-style formatting." It uses placeholders (%s, %d, %f) to represent values and replaces them with the corresponding variables.

Example:'''
name = "John"
age = 25

message = "My name is %s and I am %d years old." % (name, age)
print(message)  # Output: My name is John and I am 25 years old.

'''3. Using the `format()` Method: The `format()` method is a more flexible and preferred way of string formatting in Python. It uses curly braces ({}) as placeholders and allows you to specify the order of variables or use named placeholders.

Example:'''
name = "John"
age = 25

message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is John and I am 25 years old.

'''4. f-Strings (Formatted String Literals): Introduced in Python 3.6, f-strings provide a concise and readable way to format strings. They use the prefix 'f' before the string and allow you to directly embed variables or expressions within curly braces.

Example:'''
name = "John"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is John and I am 25 years old.

'''5. Template Strings: Python's `string.Template` class allows you to create templates with placeholders and substitute them with values using the `substitute()` method. Template strings are useful for string formatting when working with user-generated content.

Example:'''
from string import Template

name = "John"
age = 25

template = Template("My name is $name and I am $age years old.")
message = template.substitute(name=name, age=age)
print(message)  # Output: My name is John and I am 25 years old.
'''
These are the main techniques for string formatting in Python. Each method has its advantages, so choose the one that best fits your needs and coding style.'''