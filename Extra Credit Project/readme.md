# Trie and Suffix Tree Implementation

## Description
This project involves implementing a Trie and a Suffix Tree data structure in Python. A Trie, also known as a prefix tree, is a tree-based data structure used for efficient information retrieval operations, such as searching for words or strings. On the other hand, a Suffix Tree is a compressed Trie that stores suffixes of a given set of strings, enabling efficient pattern matching and string operations.

The project includes the implementation of both compressed and uncompressed versions of Tries and Suffix Trees, allowing for a comparison of space and time efficiency between the two approaches.

## Data Structures

### Trie

A Trie is a tree-like data structure where each node represents a character in a string. Each path from the root node to a leaf node represents a word or a prefix. The key advantages of using a Trie include:

- Efficient prefix search: Searching for words or prefixes can be done in O(k) time, where k is the length of the word or prefix.
- Space-efficient: In the case of compressed Tries, common prefixes are stored only once, reducing the overall memory usage.

### Suffix Tree

A Suffix Tree is a compressed Trie that stores all suffixes of a given set of strings. Unlike a regular Trie, where each node represents a single character, nodes in a Suffix Tree can represent entire substrings. This compression technique makes Suffix Trees more space-efficient than Tries, especially for large datasets.

Suffix Trees are particularly useful for various string processing operations, including:

- Pattern matching: Finding all occurrences of a pattern in a string can be done in linear time.
- Longest common substring: Finding the longest common substring among a set of strings can be efficiently performed using a Suffix Tree.
- Data compression: Suffix Trees can be used for data compression algorithms like the Burrows-Wheeler Transform.

## Files

1. `trie.py`: This file contains the implementation of the Trie and Suffix Tree classes, with the following methods:
  - `__init__(is_compressed)`: Initializes a Trie or Suffix Tree instance, where `is_compressed` determines whether the data structure should be compressed or uncompressed.
  - `construct_trie_from_text(text)`: Constructs a Trie from the given list of strings.
  - `construct_suffix_tree_from_text(keys)`: Constructs a Suffix Tree from the given list of strings.
  - `search_and_get_depth(key)`: Searches for the given key in the Trie or Suffix Tree and returns its depth. If the key is not found, it returns -1.
  - `compress_trie(node)`: Helper method for compressing a Trie recursively.
  - `compress_suffix(node)`: Helper method for compressing a Suffix Tree recursively.
  - `insert_suffix_tree(suffix)`: Helper method for inserting a suffix into the Suffix Tree.

2. `requirements.py`: This file provides the problem statement and instructions for the project.

3. `project_ec_tests.py`: This file contains some basic test cases to help verify the correctness of the implementation.

## Implementation Details

The `Trie` and `Suffix Tree` classes are implemented using a recursive approach. The `TrieNode` class represents a single node in the data structure, with the following properties:

- `children`: A dictionary that maps characters to their respective child nodes.
- `is_end_word`: A boolean flag indicating whether the current node represents the end of a word or suffix.
- `label`: A string representing the character or substring associated with the current node (for compressed Tries and Suffix Trees).

The `Trie` class provides methods for constructing and searching Tries and Suffix Trees, as well as helper methods for compressing the data structures.

The `construct_trie_from_text` and `construct_suffix_tree_from_text` methods build the respective data structures by iterating over the input strings and inserting them into the Trie or Suffix Tree.

The `search_and_get_depth` method searches for a given key in the Trie or Suffix Tree and returns its depth. If the key is not found, it returns -1.

The `compress_trie` and `compress_suffix` methods are helper functions that recursively compress the Trie and Suffix Tree, respectively, by collapsing consecutive nodes with a single child into a single node with a longer label.

## How to Run

1. Make sure you have Python 3.6 or later installed on your system.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the test cases by executing the following command:
