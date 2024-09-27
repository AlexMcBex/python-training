def basic_operations(a,b):
    print("Addition: ", a+b)
    print("Subtraction: ", a-b)
    print("Multiplication: ", a*b)
    try:
        print("Division: ", a/b)
        print("Modulus: ", a%b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

basic_operations(10, 2)