# Lockboxes

## Description
This project aims to determine if all the boxes can be opened. It provides a method `canUnlockAll` that takes a list of lists representing the boxes and their keys as input and returns `True` if all boxes can be opened, and `False` otherwise.

## Concepts Needed
To efficiently solve this problem, you will need a solid understanding of the following concepts:

- Lists and List Manipulation: Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically. You can refer to the [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists) documentation for more information.

- Graph Theory Basics: Although not explicitly required, knowledge of graph theory, especially concepts related to traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be very helpful in solving this problem. The boxes and keys can be thought of as nodes and edges in a graph. You can learn more about graph theory from the [Khan Academy Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs) resource.

- Algorithmic Complexity: Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms. You can refer to the [Big O Notation](https://www.geeksforgeeks.org/big-o-notation/) article for a better understanding.

- Recursion: Some solutions might require a recursive approach to traverse through the boxes and keys. You can learn more about recursion in Python from the [Real Python Recursion](https://realpython.com/python-thinking-recursively/) guide.

- Queue and Stack: Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes. You can refer to the [Python Queue and Stack](https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/) resource for more information.

- Set Operations: Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process. You can refer to the [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) documentation for more information.

By reviewing these concepts and utilizing the provided resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

## Additional Resources
- [Mock Technical Interview](https://www.interviewing.io/recordings/Python-Mock-Interview-Google-1/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)


## Task
0. Lockboxes
You have ``n`` number of locked boxes in front of you. Each box is numbered sequentially from ``0`` to ``n - 1`` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: ``def canUnlockAll(boxes)``
- ``boxes`` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
    - There can be keys that do not have boxes
- The first box ``boxes[0]`` is unlocked
- Return ``True`` if all boxes can be opened, else return ``False``

```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

```
carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

## HappyCoding!