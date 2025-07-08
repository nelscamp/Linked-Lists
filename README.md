# Linked-Lists

An implementation of a doubly linked list data structure using sentinel nodes, with tests and time complexity analysis.

## Overview

This project implements a doubly linked list with sentinel header and trailer nodes, providing efficient insertion and removal operations while maintaining bidirectional traversal capabilities. The implementation includes Python iterator protocol support and a reverse operation.

## Key Features

- **Sentinel Nodes**: Header and trailer sentinels eliminate edge case handling
- **Bidirectional Links**: Each node maintains both next and previous pointers
- **Iterator Support**: Full Python iterator protocol implementation
- **Reverse Operation**: Linear-time list reversal that preserves original list
- **Comprehensive Testing**: Edge cases including empty lists, single elements, and boundary conditions

## Time Complexity Analysis

| Operation | Time Complexity | Reason |
|-----------|----------------|--------|
| `append_element()` | O(1) | Direct access via sentinel trailer |
| `insert_element_at()` | O(n) | Requires traversal to index position |
| `remove_element_at()` | O(n) | Requires traversal to index position |
| `get_element_at()` | O(n) | Requires traversal to index position |
| `rotate_left()` | O(1) | Combines three constant-time operations |
| `__len__()` | O(1) | Returns maintained size counter |
| `__str__()` | O(n) | Must visit all nodes for string building |
| `__reversed__()` | O(n) | Single traversal with constant appends |

## Usage

```python
from Linked_List import Linked_List

# Create and populate list
ll = Linked_List()
ll.append_element(1)
ll.append_element(2)
ll.append_element(3)

# Access elements
print(ll.get_element_at(0))  # Output: 1
print(ll)                    # Output: [ 1, 2, 3 ]

# Insert and remove
ll.insert_element_at(10, 1)  # Insert 10 at index 1
ll.remove_element_at(0)      # Remove first element

# Iteration
for val in ll:
    print(val)

# Reverse iteration
for val in reversed(ll):
    print(val)

# Rotation
ll.rotate_left()  # Move head to tail
```

## Implementation Details

### Sentinel Node Architecture
The list uses two sentinel nodes (header and trailer) that never contain data. This design:
- Eliminates special cases for empty lists
- Simplifies insertion/removal logic
- Enables O(1) append operations

### Memory Management
Each node stores three references:
- `val`: The data value
- `next`: Reference to next node
- `prev`: Reference to previous node

### Iterator Protocol
Implements `__iter__()` and `__next__()` for Python's for-loop compatibility, enabling seamless integration with Python's iteration mechanisms.

## Testing Strategy

The comprehensive test suite covers:
- **Empty list operations**: Verifying proper exception handling
- **Single element scenarios**: Testing edge cases with minimal data
- **Boundary conditions**: First/last element operations
- **Invalid indices**: Confirming IndexError exceptions
- **Iterator functionality**: Forward and reverse iteration testing
- **String representation**: Format verification across different list states

## Technical Insights

This implementation demonstrates the tradeoff between **index-based access** and **insertion efficiency**. While array-like structures provide O(1) indexed access, this linked list achieves O(1) insertion/removal at known positions, making it ideal for applications with frequent list modifications but infrequent random access.
