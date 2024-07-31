# Island Perimeter

## Resources
- [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists within lists in Python.
- [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-multi-dimensional-arrays/): A guide to working with 2D arrays in Python effectively.
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.
- [Python 2D arrays and lists](https://www.youtube.com/watch?v=HGOBQPFzWKo): YouTube tutorial on Python 2D arrays and lists.

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You'll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.


## 0-island_primeter
Create a function `island_perimeter(grid)` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally).
- `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))
```

Output:
```
12
```

## Approach

To solve this problem, you can iterate over the grid and apply logical operations to identify the perimeter of the island. You'll need to count the edges that contribute to the island's perimeter by checking the status of adjacent cells. By breaking down the problem into smaller tasks and utilizing the provided resources, you'll be able to approach the problem methodically and solve it effectively.


## HappyCoding!
