# HSA13_hw22_profiling

Here’s a detailed `README.md` file in Markdown format written in English for your project. It describes the project structure, purpose, installation instructions, and usage details.

---

# Balanced Binary Search Tree Project

This project implements a **Balanced Binary Search Tree (AVL Tree)** in Python, along with scripts to profile its space and time complexity. The implementation includes basic operations such as `insert`, `delete`, and `search`, with performance analysis visualized using Matplotlib.


## Features

- **AVL Tree Implementation**: A self-balancing binary search tree with O(log n) time complexity for insert, delete, and search operations.
- **Space Profiling**: Measures memory usage to confirm O(n) space complexity.
- **Time Profiling**: Measures execution time of the `search` operation to confirm O(log n) time complexity.
- **Visualization**: Plots the profiling results using Matplotlib for easy analysis.


## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd balanced_binary_search_tree_project
   ```

2. **Install Dependencies**:
   Install the required Python libraries listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   The dependencies include:
   - `matplotlib` (for plotting)
   - `pympler` (for memory profiling)

## Usage

### Running Space Profiling
To analyze the space complexity and generate a plot:
```bash
python scripts/profile_space.py
```
- **Output**: A Matplotlib plot showing memory usage (in bytes) vs. the number of nodes (n). The graph compares actual memory usage with a theoretical O(n) line.

### Running Time Profiling
To analyze the time complexity of the `search` operation and generate a plot:
```bash
python scripts/profile_time.py
```
- **Output**: A Matplotlib plot showing average search time (in seconds) vs. the number of nodes (n, logarithmic scale). The graph compares actual time with a theoretical O(log n) curve.

### Example of Using AVL Tree
You can import and use the `AVLTree` class directly in your Python code:
```python
from balanced_binary_search_tree.avl_tree import AVLTree

# Create an AVL Tree instance
avl = AVLTree()

# Insert some keys
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    avl.insert_key(key)

# Search for a key
node = avl.search_key(30)
print(node.key if node else "Not found")  # Output: 30

# Delete a key
avl.delete_key(30)
print(avl.search_key(30))  # Output: None
```

## Complexity Analysis

- **Space Complexity**: O(n)
  - The AVL Tree stores n nodes, each with a key, left/right pointers, and height, leading to linear memory usage.
  - Confirmed by `profile_space.py`.

- **Time Complexity**: O(log n)
  - Operations (`insert`, `delete`, `search`) take logarithmic time due to the tree’s balanced height.
  - Confirmed by `profile_time.py`.

## Expected Output

- **Space Profile Plot**: A nearly linear graph, confirming O(n) space complexity.
- **Time Profile Plot**: A logarithmic curve (on a log-scale x-axis), confirming O(log n) time complexity for search operations.

