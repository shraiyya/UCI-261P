
# Cuckoo Hashing Implementations

This repository contains Python implementations of Cuckoo Hashing and a 2,4-cuckoo hash table. The classes `CuckooHash` and `CuckooHash24` handle efficient key insertion, lookup, deletion, and rehashing to avoid collisions in hash tables.

## CuckooHash Class

The `CuckooHash` class provides a basic Cuckoo Hashing algorithm with the following functionalities:

- **Initialization (`__init__`):** Initializes the Cuckoo Hash with specified sizes and cycle detection threshold.
- **Insertion (`insert`):** Inserts a key into the hash tables using double hashing, handling collisions.
- **Lookup (`lookup`):** Checks if a key exists in the hash tables using double hashing.
- **Deletion (`delete`):** Removes a key from the hash tables using double hashing.
- **Rehashing (`rehash`):** Increases the size of the hash tables and redistributes existing keys to avoid collisions.

### Usage Example

```python
from cuckoo_hash import CuckooHash

# Initialize CuckooHash with a table size of 10
c = CuckooHash(10)

# Insert keys
c.insert(5)
c.insert(8)

# Lookup key
result = c.lookup(5)
print(result)  # Output: True

# Delete key
c.delete(5)
```

## CuckooHash24 Class

The `CuckooHash24` class extends the Cuckoo Hashing concept to a 2,4-cuckoo hash table. It includes the same functionalities as the `CuckooHash` class with additional methods:

- **Random Index from Bucket (`get_rand_idx_from_bucket`):** Returns a random index from a given bucket for displacing keys during insertion.

### Usage Example

```python
from cuckoo_hash_24 import CuckooHash24

# Initialize CuckooHash24 with a table size of 10
c = CuckooHash24(10)

# Insert keys
c.insert(5)
c.insert(8)

# Lookup key
result = c.lookup(5)
print(result)  # Output: True

# Delete key
c.delete(5)
```

## Testing

The repository includes comprehensive tests to ensure the correctness and reliability of both implementations. Test cases cover basic operations, edge cases, and specific scenarios for each implementation.

### Running Tests

Use the provided test scripts to execute the tests:

- For `CuckooHash`: Run `python project1_tests.py`.
- For `CuckooHash24`: Run `python project1_tests_24.py`.

## Future Considerations

Future improvements may include optimizing hashing functions, introducing advanced cycle detection mechanisms, and exploring additional features for specific use cases.

Feel free to contribute, report issues, or suggest enhancements!
