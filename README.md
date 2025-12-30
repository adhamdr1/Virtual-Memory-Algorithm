# Virtual Memory Algorithm Simulator

A Python implementation of various page replacement algorithms used in operating systems for virtual memory management.

## Overview

This project simulates and compares different page replacement algorithms that operating systems use to manage memory pages. When physical memory is full and a new page needs to be loaded, these algorithms determine which existing page should be replaced.

## Implemented Algorithms

### 1. **FIFO (First-In-First-Out)**
- Replaces the oldest page in memory
- Simple to implement but may not always be optimal
- Uses a queue-like structure

### 2. **LRU (Least Recently Used)**
- Replaces the page that hasn't been used for the longest time
- Based on the principle of temporal locality
- Generally performs better than FIFO

### 3. **LFU (Least Frequently Used)**
- Replaces the page with the lowest access frequency
- Tracks how many times each page is accessed
- Good for workloads with repeated access patterns

### 4. **MFU (Most Frequently Used)**
- Replaces the page with the highest access frequency
- Based on the assumption that frequently used pages won't be needed soon
- Less common in practice

### 5. **Clock Algorithm**
- Approximation of LRU using a circular buffer
- Uses reference bits to track page usage
- More efficient than true LRU implementation

## Features

- Clean and simple implementation of each algorithm
- Easy to compare performance across different algorithms
- Customizable page reference string and memory capacity
- Returns page fault count for each algorithm

## Usage

```python
# Define your page reference string
pages = [7, 0, 1, 2, 0, 3, 0, 4, 0, 3, 2, 1, 0, 4, 5]

# Set memory capacity (number of frames)
capacity = 3

# Run the algorithms
print("FIFO:", fifo(pages, capacity))
print("LRU:", lru(pages, capacity))
print("LFU:", lfu(pages, capacity))
print("MFU:", mfu(pages, capacity))
print("Clock:", clock(pages, capacity))
```

## Sample Output

```
FIFO: 12
LRU: 9
LFU: 10
MFU: 13
Clock: 11
```

Lower numbers indicate fewer page faults, meaning better performance.

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/adhamdr1/Virtual-Memory-Algorithm.git
```

2. Navigate to the directory:
```bash
cd Virtual-Memory-Algorithm
```

3. Run the script:
```bash
python Virtual_Memory.py
```

## How It Works

**Page Fault**:  Occurs when a requested page is not currently in memory and must be loaded from disk.

Each algorithm minimizes page faults differently:
- **FIFO**:  Maintains insertion order
- **LRU**:  Tracks last access time
- **LFU**:  Counts access frequency
- **MFU**:  Assumes most-used pages can be replaced
- **Clock**: Uses second-chance approach with reference bits

## Customization

You can modify the `pages` list and `capacity` variable to test different scenarios:

```python
# Example: Larger memory capacity
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 4
```

## Educational Purpose

This project is ideal for: 
- Operating Systems students learning about memory management
- Understanding the trade-offs between different page replacement strategies
- Comparing algorithm performance on different workloads

## Contributing

Feel free to open issues or submit pull requests with improvements or additional algorithms (e.g., Optimal Page Replacement, Second Chance, etc.).

## License

This project is open source and available for educational purposes. 

## Author

[@adhamdr1](https://github.com/adhamdr1)

---

**Note**: These are simplified implementations for educational purposes. Real operating systems use more complex optimizations. 
