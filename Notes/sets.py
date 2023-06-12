'''In Python, a set is an unordered collection of unique elements. It is defined using curly braces `{}` or the `set()` function. Sets are mutable, which means you can add, remove, or modify elements after creation. Here are some key characteristics and operations related to Python sets:

1. Creating a Set:
   - Using curly braces: You can create a set by enclosing comma-separated values within curly braces.
   
     Example:'''
fruits = {'apple', 'banana', 'orange'}
'''
   - Using the `set()` function: You can create a set by passing an iterable (such as a list or tuple) to the `set()` function.
   
     Example:'''
colors = set(['red', 'green', 'blue'])

'''2. Set Operations:
   - Adding Elements: You can add elements to a set using the `add()` method.
   
     Example:'''
fruits.add('grape')
'''
   - Removing Elements: You can remove elements from a set using the `remove()` or `discard()` methods. The `remove()` method raises a `KeyError` if the element doesn't exist, while `discard()` silently ignores the operation.
   
     Example:'''
fruits.remove('apple')
'''
   - Checking Membership: You can check if an element is present in a set using the `in` keyword.
   
     Example:'''
if 'banana' in fruits:
    print("Banana is present in the set.")

'''   - Set Operations: Sets support various operations such as union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`), and subset/superset checking.
   
     Example:'''
set1 = {1, 2, 3}
set2 = {2, 3, 4}

union = set1 | set2  # {1, 2, 3, 4}
intersection = set1 & set2  # {2, 3}
difference = set1 - set2  # {1}
symmetric_difference = set1 ^ set2  # {1, 4}
is_subset = set1 <= set2  # False
is_superset = set1 >= set2  # False

'''3. Set Properties:
   - Uniqueness: Sets only contain unique elements. If you try to add a duplicate element, it will be ignored.
   
     Example:'''
fruits = {'apple', 'banana', 'orange', 'apple'}
print(fruits)  # Output: {'apple', 'banana', 'orange'}
'''
   - Unordered: Sets are unordered, meaning the elements are not stored in any specific order. When iterating over a set, the order of retrieval may vary.
   
     Example:'''
for fruit in fruits:
    print(fruit)
# Output (order may vary):
# 'banana'
# 'apple'
# 'orange'
'''
Sets are useful when you want to store a collection of unique elements and perform operations such as set operations, membership checks, or removing duplicates from a list of values.'''