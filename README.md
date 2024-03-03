# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 3: Learn Lambda Functions by Building an Expense Tracker
Lambda functions give you a concise way to write small, throwaway functions in your code.

# What's new to me

# `lambda()` function
Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the `lambda` keyword, and they use the following syntax:

```python
lambda x: expr
```
In the example above, `x` is a parameter to be used in the expression `expr`. To call a lambda function you can use the usual function syntax with a pair of parentheses after the variable name. Example:

``` python
test = lambda x: x*2
print( test(3) )
# 6
```

# `map()` function
Lambda functions can be valuably combined with the `map()` function, which executes a specified function for each element in a collection of objects, such as a list:

``` python
map(lambda x: x * 2, [1, 2, 3])
```
The result of the example above would be `[2, 4, 6]`, where each item in the list passed to `map()` has been doubled by the action of the lambda function.

# `filter()` function
The `filter()` function allows you to select items from an iterable, such as a list, based on the output of a function:

```python
filter(my_function, my_list)
```

In this example, `filter()` returns an iterator in which the elements of `my_list` are included, for which `my_function` returns `True`. An iterator is a special object that enables you to iterate over the elements of a collection, like a list.

# `__name__`
You can use the `__name__` variable to determine if a Python script is being run as the main program or if it is being imported as a module (code written in another Python file).

If the value of `__name__` is set to `'__main__'`, it implies that the current script is the main program, and not a module.
```python
if __name__ == '__main__':
  main()
```
