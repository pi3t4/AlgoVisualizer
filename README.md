# AlgoVisualAlyzer

A Python-based tool to visualize and understand sorting algorithms!

This project showcases the functionality of popular sorting algorithms, including:
- Bubble Sort  
- Quick Sort  
- Insertion Sort  
- Selection Sort  
- Heap Sort  

![Demo](demo.gif)  
*Include a demo GIF/screenshot here!*

---

## Features

- **Intuitive Visualizations**: See how each sorting algorithm processes data step-by-step.
- **Educational Focus**: Designed to help learners grasp sorting algorithms through interactive demos.
- **Modular Design**: Each algorithm is implemented in a clean, modular format for easy understanding and reuse.
- **Customizable Speed**: Adjust the visualization speed to observe steps in detail.
- **Randomized Data**: Generates random arrays to visualize sorting dynamically.
- **Interactive Controls**: Use keyboard shortcuts to reset, start, or switch between algorithms.

---

## Sorting Algorithms Implemented

### 1. **Bubble Sort**
   - Compares adjacent elements and swaps them if they are in the wrong order.
   - **Time Complexity**:
     - Best Case: `O(n)`  
     - Worst Case: `O(n²)`
   - **Space Complexity**: `O(1)`

### 2. **Quick Sort**
   - A divide-and-conquer algorithm that partitions the array and sorts the partitions recursively.
   - **Time Complexity**:
     - Best Case: `O(n log n)`  
     - Worst Case: `O(n²)` (when the pivot selection is poor)
   - **Space Complexity**: `O(log n)` (due to recursion)

### 3. **Insertion Sort**
   - Builds the sorted array one item at a time by inserting elements in their correct positions.
   - **Time Complexity**:
     - Best Case: `O(n)`  
     - Worst Case: `O(n²)`
   - **Space Complexity**: `O(1)`

### 4. **Selection Sort**
   - Selects the smallest element from the unsorted portion and swaps it with the first unsorted element.
   - **Time Complexity**:
     - Best Case: `O(n²)`  
     - Worst Case: `O(n²)`
   - **Space Complexity**: `O(1)`

### 5. **Heap Sort**
   - Uses a binary heap data structure to sort elements by repeatedly extracting the maximum (or minimum) element.
   - **Time Complexity**:
     - Best Case: `O(n log n)`  
     - Worst Case: `O(n log n)`
   - **Space Complexity**: `O(1)` (in-place sorting)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pi3t4/AlgoVisualAlyzer.git
   cd AlgoVisualAlyzer
   pip install -r requirements.txt
   python Algovisual.py
   ```
   Usage Instructions
Controls :
R: Reset the list and generate a new random dataset.
SPACE: Start the selected sorting algorithm.
A: Switch to ascending order.
D: Switch to descending order.
I: Select Insertion Sort.
B: Select Bubble Sort.
S: Select Selection Sort.
M: Select Merge Sort.
Q: Select Quick Sort.
H: Select Heap Sort.
Visualization :
The bars represent the values in the list. As the algorithm progresses, the bars change color to indicate which elements are being compared or swapped.
