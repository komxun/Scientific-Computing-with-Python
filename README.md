# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 2: Learn how to work with numbers and strings by implementing the Luhn Algorithm
The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers

# What's new to me

# `.maketrans` to define the translation
to create a translation table. This table can be used to replace characters in a string
```python
str.maketrans({'t': 'c', 'l': 'b'})
```
The above, when called on a string, will replace all `t` characters with `c` and all `l` characters with `b`.
Note that you must type `str.maketrans()` to define the translation (use `str`)

# `.translate` to perform the translation
```python
my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)
```

# Access elements (characters) of a string with `string[x:y:h]`
Where `x` is the starting index, `y` is the ending index, and `h` is the step (the amount of characters to skip over).

# Luhn Algorithm
The Luhn algorithm is as follows:

1. From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.

2. Take the sum of all the digits.

3. If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
Assume an example of an account number "7992739871" that will have a check digit added, making it of the form 7992739871x:

```
Account number      7   9  9  2  7  3  9   8  7  1  x
Double every other  7  18  9  4  7  6  9  16  7  2  x
Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
```
You can get each digit by using _integer division_ to get the first digit and the modulus operator `%` to get the second digit:

``` python
my_number = 12
first_digit = my_number // 10
second_digit = my_number % 10
```
