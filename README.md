# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 6: Learn Algorithm Design by Building a Shortest Path Algorithm
Algorithms are step-by-step procedures that developers use to perform calculations and solve computational problems.

## Shortest Path Algorithm
This function is going to explore all the nodes connected to the starting node. It will calculate the shortest paths for all of them. Then, it will remove the starting node from the unvisited nodes.

Next, the closest neighbor node will be visited and the process will be repeated until all the nodes are visited.

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
{key: val_1 if condition else val_2 for key in dict}
```

# Extras
Pass `key=distances.get` as the second argument to your `min()` call. In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.

```python
while unvisited:
        current = min(unvisited, key=distances.get)
```

# Ternary syntax
```python
val_1 if condition else val_2
```
