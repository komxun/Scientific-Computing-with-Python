# Scientific-Computing-with-Python
Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

 > Summary from freeCodeCamp.org

# Day 7: Learn Recursion by Solving the Tower of Hanoi Puzzle
Recursion is a programming approach that allows you to solve complicated computational problems with just a little code.
![image](https://github.com/komxun/Scientific-Computing-with-Python/assets/133139057/745b70c1-212c-4d1c-9813-e81ae28de45c)

The puzzle consists of three rods and a number of disks of different diameters.

The goal of this puzzle is moving the disks from the first rod to the third rod, following specific rules that restrict placing a larger disk on top of a smaller one.

The Tower of Hanoi puzzle can be solved in 2^n - 1 moves, where n is the number of disks

# What's new to me
To solve the puzzle with recursion, the first thing to do is break the original problem down into smaller sub-problems.

The final configuration with `n` disks piled up to the third rod in decreasing order can be obtained by moving:

`n - 1` disks from the source to the auxiliary rod
the largest disk from the source to the target
and then the `n - 1` disks from the auxiliary rod to the target.
So, the first thing the move function should do is calling itself with `n - 1` as the first argument. But if you try to do so without defining a base case, you will get a `RecursionError`. This happens because the function keeps calling itself indefinitely.


# Iterative Approach
https://github.com/komxun/Scientific-Computing-with-Python/blob/cf257dd213fc43376853f8e2b598a0e22a19866c/Tower_of_Hanoi_Iterative.py#L1-L49

# Recursive Approach
- more flexible, doesn't have to deal with even/odd case
https://github.com/komxun/Scientific-Computing-with-Python/blob/cf257dd213fc43376853f8e2b598a0e22a19866c/Tower_of_Hanoi_Recursive.py#L1-L23
