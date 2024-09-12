# Python - Sets and Dictionaries

## Introduction
In Python, **Sets** and **Dictionaries** are built-in data structures that help in storing and manipulating collections of items. Both are widely used due to their efficiency and unique properties.

### 1. Sets
A **Set** is an unordered collection of unique items. Sets do not allow duplicate elements, and their elements are not indexed, meaning you cannot access elements by position like in a list or tuple.

#### Key Features:
- **Unordered**: Elements do not have a specific order.
- **Unique elements**: No duplicates allowed.
- **Mutable**: You can add or remove elements after the set has been created.
- **Supports Set operations**: Like union, intersection, difference, etc.

#### Example:
```python
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element
fruits.add("orange")

# Removing an element
fruits.remove("banana")

# Checking membership
print("apple" in fruits)  # Output: True

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))         # Output: {1, 2, 3, 4, 5}
print(A.intersection(B))   # Output: {3}

## 2. Dictionaries

A **Dictionary** is an unordered collection of key-value pairs. Each key is unique, and the values can be of any data type. Dictionaries are often used to store related data where each item has a label (key).

### Key Features:
- **Key-value pairs**: Each key is mapped to a value.
- **Keys are unique**: No duplicate keys.
- **Mutable**: You can add, modify, or remove items.
- **Unordered**: Before Python 3.7, dictionaries were unordered. From Python 3.7+, they maintain insertion order.