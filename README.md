# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 6: Learn Algorithm Design by Building a Shortest Path Algorithm
Algorithms are step-by-step procedures that developers use to perform calculations and solve computational problems.

# What's new to me

# `list()`
The `list()` type constructor enables you to build a list from an iterable.

```python
# Instead using for loop:
def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

# You can use this:
def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {}
    
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
```

# Dictionary Comprehension
With a dictionary comprehension, you can create a dictionary starting from an existing dictionary:
```python
{key: val for key in dict}
```

