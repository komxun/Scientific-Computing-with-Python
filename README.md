# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 9: Learn Classes and Objects by Building a Sudoku Solver
Classes and objects are important programming concepts. These Object-Oriented Programming tools help developers to achieve code modularity, abstraction, and readability. And they promote reusability.

# About Sudoku
``` python
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
```
![image](https://github.com/komxun/Scientific-Computing-with-Python/assets/133139057/b9573efc-b619-4e84-85ea-6c859d8d30b1)

# What's new to me

The `__init__` method is a special method that allows you to instantiate an object to a customized state. When a class implements an `__init__` method, `__init__` is automatically called upon instantiation.

# `self`
`self` is a reference to the instance of the class. It is a convention to name this parameter self.

# `__str__`
This method is automatically called when you use the `str()` function on an instance of the class or when you use `print()` with the object.

# `enumerate()`
Enumeration is a convenient way to keep track of both the element and its position on a list. The `enumerate()` function is a built-in function in Python that takes an iterable (such as a list, tuple, or string) and returns an iterator that produces tuples containing indices and corresponding values from the iterable.

# `replace()
The `replace()` method takes two arguments, the first one is the character to be replaced and the second one is the character to be replaced with.

# `.extend()` vs `.append()`
In Python, `.append()` and `.extend()` are both methods that you can use on lists, but they work in different ways:

- `list.append(item)`: This method adds the item to the end of the list. If the item is a list itself, it will be added as a single element, so you’ll end up with a nested list.

```python
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # Output: [1, 2, 3, [4, 5]]
```
- `list.extend(iterable)`: This method adds each element from the iterable (like a list or any other iterable) to the end of the list. It essentially concatenates the list with the iterable.

```python
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # Output: [1, 2, 3, 4, 5]
```
So, the main difference is that `.append()` adds its argument as a single element to the end of the list while `.extend()` adds each element of the iterable argument to the list. 
- If you want to add a list as an individual element, use `.append()`
- If you want to merge a list with another list, use `.extend()`

  # `try`
- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `else` block lets you execute code when there is no error.
- The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

```python
try:
    col = contents.index(0)
    return row, col
except ValueError:
    pass
```
- If `0` is found, the code immediately returns a tuple (row, col) with the row index and column index of the empty cell.
- `except` block handle the ValueError exception that is thrown if `0` is not found
- If the value `0` is not present in the current row, an exception would be thrown and the `except` block would execute.

# `:=` walrus operator
- walrus operator (`:=`) formally known as the **assignment expression operator**, offers a way to assign to variables within an expression, including variables that do not exist yet. 
- the walrus operator allows us to both assign a value to a variable, and to return that value, all in the same expression.

# Result
![image](https://github.com/komxun/Scientific-Computing-with-Python/assets/133139057/0a90cef7-9d73-4d86-8a0d-f4b7b4ee8e8a)


