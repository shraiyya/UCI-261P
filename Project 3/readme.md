# Zip Tree and Skip List Implementation

## Description

This project provides an implementation of the Zip Tree and Skip List data structures in Python. The Zip Tree is a self-balancing binary search tree that maintains a rank for each node, allowing for efficient insertions, deletions, and range searches. The Skip List is a probabilistic data structure that provides expected logarithmic-time search, insertion, and deletion operations.

## Data Structures

### Zip Tree

The Zip Tree is a variation of the Randomized Search Tree, which combines the properties of a binary search tree and a skip list. Each node in the Zip Tree has a rank associated with it, drawn from a geometric distribution with mean 1. The ranks determine the probability of a node being promoted or demoted during insertions and deletions, ensuring that the tree remains balanced.

Key features of the Zip Tree implementation:

- **Insertion**: New nodes are inserted based on their rank and key value, maintaining the binary search tree property.
- **Deletion**: Nodes are removed by zipping up their children, ensuring that the tree remains balanced.
- **Range Queries**: The ranks of nodes allow for efficient range queries and order statistics operations.
- **Self-Balancing**: The tree remains balanced due to the random ranks assigned to nodes during insertion.

### Skip List

The Skip List is a hierarchical data structure that provides logarithmic-time search, insertion, and deletion operations with high probability. It consists of multiple sorted linked lists, where each higher-level list acts as an express lane for the lower-level lists, allowing for faster traversal.

Key features of the Skip List implementation:

- **Insertion**: New elements are added to the appropriate levels of the Skip List based on a random level assignment.
- **Deletion**: Elements are removed from all levels of the Skip List where they are present.
- **Search**: Elements can be efficiently searched by traversing the higher-level lists and descending to lower levels when necessary.
- **Construction from Zip Tree**: The Skip List can be constructed from a given Zip Tree, maintaining the order and rank information of the nodes.

## Files

1. `zip_tree.py`: This file contains the implementation of the Zip Tree data structure, including the `Node` and `ZipTree` classes.
2. `skip_list.py`: This file contains the implementation of the Skip List data structure, including the `SkipList` class.
3. `requirements.py`: This file provides the problem statement and instructions for the project.
4. `project3_tests.py`: This file contains test cases for both the Zip Tree and Skip List implementations.

## Implementation Details

### Zip Tree

The `ZipTree` class is implemented using the following methods:

- `__init__()`: Initializes an empty Zip Tree.
- `get_random_rank()`: Returns a random rank drawn from a geometric distribution with mean 1.
- `insert(key, val, rank)`: Inserts a new node with the given key, value, and rank into the Zip Tree.
- `remove(key)`: Removes the node with the given key from the Zip Tree.
- `find(key)`: Returns the value associated with the given key in the Zip Tree.
- `get_size()`: Returns the number of nodes in the Zip Tree.
- `get_height()`: Returns the height of the Zip Tree.
- `get_depth(key)`: Returns the depth of the node with the given key in the Zip Tree.
- `get_nodes_with_rank(level)`: Returns a list of nodes with the given rank level.

### Skip List

The `SkipList` class is implemented using the following methods:

- `__init__()`: Initializes an empty Skip List.
- `get_random_level(key)`: Determines the level at which the given key should be placed in the Skip List.
- `insert(key, val, rank)`: Inserts a new node with the given key, value, and rank into the Skip List.
- `remove(key)`: Removes the node with the given key from the Skip List.
- `find(key)`: Returns the value associated with the given key in the Skip List.
- `get_list_size_at_level(level)`: Returns the number of nodes at the given level in the Skip List.
- `from_zip_tree(zip_tree)`: Constructs a Skip List from the given Zip Tree, maintaining the order and rank information of the nodes.

## How to Run

1. Make sure you have Python 3.6 or later installed on your system.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the test cases by executing the following command:
