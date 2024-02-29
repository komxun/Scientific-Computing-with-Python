# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 1: Learn String Manipulation by Building a Cipher (Encryption/ Decryption) 
# What's new to me

## Set the default value of function
```python
def someFunction(x, y, z=20):
  #<code>
```

## `pass` 
In case the function argument is not given. This is to prevent
```python
def someFunction(x, y, z):
  pass
```
## Finding the index
- `.find()` method gives the index of the argument. It throws `-1` if it couldn't find the match
- `.index()` method is identical to the `.find()` method, but it throws a `ValueError` exception if it is unable to find


## `.isalpha`
The `.isalpha()` method returns `True` if all the character of the string on which it is called are letters. For example, the code below returns `True`:
``` python
'freeCodeCamp`.isalpha()
# True
```

## 2 Ways of concatenating string
``` python
text = 'Hello'
print('Message: ' + 'text')
print(f'Message: {text}')
```
