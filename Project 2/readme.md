# Project: Fibonacci Heap Implementation

## Description
This project involves implementing a Fibonacci Heap data structure in Python. The Fibonacci Heap is a collection of trees that are organized to allow efficient operations such as insert, delete_min, decrease_priority, and find_min. The project also includes an implementation of the Fibonacci Heap with lazy deletion and find operations, as described in the original paper by Fredman and Tarjan.

## Files

1. `fib.py`: This file contains the implementation of the standard Fibonacci Heap with the following methods:
  - `__init__()`: Initializes an empty Fibonacci Heap.
  - `get_roots()`: Returns a list of all the root nodes in the heap.
  - `insert(val)`: Inserts a new node with the specified value into the heap and returns the new node.
  - `delete_min()`: Removes the node with the minimum value from the heap.
  - `find_min()`: Returns the node with the minimum value in the heap.
  - `decrease_priority(node, new_val)`: Decreases the value of the specified node to the new value and updates the heap structure accordingly.

2. `fib_lazy.py`: This file contains the implementation of the Fibonacci Heap with lazy deletion and find operations, as described in the original paper. It includes the following methods:
  - `__init__()`: Initializes an empty Fibonacci Heap.
  - `get_roots()`: Returns a list of all the root nodes in the heap.
  - `insert(val)`: Inserts a new node with the specified value into the heap and returns the new node.
  - `delete_min_lazy()`: Removes the node with the minimum value from the heap using the lazy deletion approach.
  - `find_min_lazy()`: Returns the node with the minimum value in the heap using the lazy find approach.
  - `decrease_priority(node, new_val)`: Decreases the value of the specified node to the new value and updates the heap structure accordingly.

3. `requirements.py`: This file provides the problem statement and instructions for the project.

4. `project2_tests.py`: This file contains some basic test cases to help verify the correctness of the implementation.

## How to Run

1. Make sure you have Python 3.6 or later installed on your system.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the test cases by executing the following command:

4. This will run the provided test cases and print the results to the console.

## Note

- The implementations in `fib.py` and `fib_lazy.py` are expected to conform to the specifications outlined in `requirements.py`.
- The test cases in `project2_tests.py` are not exhaustive and are provided as a starting point. It is recommended to create additional test cases to thoroughly test the implementations.
- The project may have additional requirements or constraints specified in the `requirements.py` file or other provided materials.

Feel free to modify this README file as per your project's specific requirements and add any additional sections or instructions as needed.
