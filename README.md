# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 4: Learn Python List Comprehension by Building a Case Converter Program
List Comprehension is a way to construct a new Python list from an iterable types: lists, tuples, and strings. All **without** using a for loop or the `.append()` list method.

- Apart from being briefer, list comprehensions often run faster.

# What's new to me
- Pascal cased string: 'ThisIsSomeString'
- Snake cased string: 'this_is_some_string'

# Converting Uppercase to Lowercase
1. Use `.isupper()` to find the uppercase character
2. Use `.lower()` to convert uppercase characters to lowercase characters

# `.join()`
Use the `.join()` string method to convert the list of characters into a string.

For example:
```python
''.join(char_list)
```
This joins the characters from the `char_list` to the empty string on which you called the `.join()` method

# `.strip()`
Use the `.strip()` to remove unwanted character from the string
```python
some_string.strip('_')
# This strip off any dangling underscores from some_string
```

# Without List Comprehension
```python
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string
```
# List Comprehension
```python
def convert_to_snake_case(pascal_or_camel_cased_string):
   snake_cased_char_list  = [
     '_' + char.lower() if char.isupper()
      else char
      for char in pascal_or_camel_cased_string
   ]

   return ''.join(snake_cased_char_list).strip('_')
```
Python will interpret this expression as "append `'_' + char.lower()` to the list if `char` is in uppercase, append `char` as is otherwise" and this will convert the case for the capital letters in the input string.

- These three lines of code do the same task as the `for` loop you worked on previously while being cleaner and somewhat faster.
