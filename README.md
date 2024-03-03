# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 5: Learn Regular Expressions by Building a Password Generator
A Python module is a file that contains a set of statements and definitions that you can use in your code.

In this project, you'll learn how to import modules from the Python standard library. You'll also learn how to use Regular Expressions by building your own password generator program.

# What's new to me

# `random` built-in library
## `random.choice()`
The `choice()` function from the `random` module takes a sequence and returns a random item of the sequence.

# `secrets` built-in library
## `secrets.choice()`
Although the effect might seem equal to `random.choice()`, `secrets` ensure you the most secure source of randomness that your operating system can provide.

# `_`
A standalone single underscore is used to represent a value you don't care or that won't be used in your code. Your iteration variable is not actually used.

``` python
# instead of this
# for i in range(10):
#     x += 1
# We can use
for _ in range(10):
     x += 1
```

# Tuple
A tuple is another built-in data structure in Python. Tuples are very much like lists, but they are defined with parentheses `()`, instead of square brackets. Also, tuples are immutable, unlike lists.
```python
my_tuple = ('larch', 1, Ture)
```

# `re` built-in library
The `re` module allows you to use regular expressions in your code.

A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to `if`/`else` conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.
## `re.compile()`
The `compile()` function from the `re` module compiles the string passed as the argument into a regular expression object that can be used by other `re` methods.
```python
pattern = re.compile('i')
```

## `re.search()`
The `search()` function from the `re` module analyzes the string passed as the argument looking for the first place where the regex pattern matches the string.

```python
pattern = re.compile('i')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))
# // None
```
The value `None` is returned since `i` is not found inside the parsed string.
```python
pattern = re.compile('l')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))
# // <re.Match object; span=(5, 6), match='l'>
```
now the regex matches the first `l` inside the string.

In your pattern, you can add a quantifier after a character to specify how many times that character should be repeated. For example, the `+` quantifier means it should repeat one or more times.
```python
pattern = re.compile('l+')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))
# // <re.Match object; span=(5, 7), match='ll'>
```

You can also obtain the same result without using the `compile()` function:
```python
pattern = 'l+'
quote = 'Not all those who wander are lost.'
print(re.search(pattern, quote))
# // <re.Match object; span=(5, 7), match='ll'>
```

## `re.findall()`
`re.findall()` is similar to `search` but it returns a **list** with all the occurrences of the matched pattern.
```python
pattern = 'l+'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))
# // ['ll', 'l']
```

# working with character
- A character class is indicated by square brackets and matches one character among those specified between the brackets. For example, `ma[dnt]` matches either `mad`, `man`, or `mat`.
```python
pattern = 'w[ha]'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))
# // ['wh', 'wa']
```

- Character classes also allow you to indicate a range of characters to match. You need to specify the starting and the ending characters separated by an hyphen, `-`. Characters follow the Unicode order.
```python
# instead of '[abcdefghijklmnopqrstuvwxyz]t' , we can just type
pattern = '[a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

# // ['ot', 'st']
```
This matches any letter `t` **preceded** by a lowercase letter in the quote variable with the range of characters from `a` to `z`.
