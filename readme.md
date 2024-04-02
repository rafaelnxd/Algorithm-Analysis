# Algorithm Analysis Project

This project focuses on the practical study of sorting and searching algorithms applied to real-world scenarios. It includes the implementation of custom Python libraries for sorting and searching, following object-oriented programming (OOP) best practices.

## Project Structure

The project is organized into the following directories and files:

- `algorithms/`: Contains custom Python modules for sorting and searching algorithms.
  - `sorting.py`: Module containing a class `Sorting` with static methods for various sorting algorithms.
  - `search.py`: Module containing a class `Search` with static methods for various searching algorithms.
- `tests/`: Contains test scripts to validate the functionality of the custom library.
  - `test_sorting.py`: Script to test the sorting algorithms.
  - `test_search.py`: Script to test the searching algorithms.
- `main.py`: Main script to perform performance analysis of sorting and searching algorithms.

## Usage

### Sorting Algorithms

The `Sorting` class in `algorithms/sorting.py` provides static methods for the following sorting algorithms:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

To test the sorting algorithms, run the `test_sorting.py` script located in the `tests/` directory.

### Searching Algorithms

The `Search` class in `algorithms/search.py` provides static methods for the following searching algorithms:

- Sequential Search
- Binary Search

To test the searching algorithms, run the `test_search.py` script located in the `tests/` directory.

### Performance Analysis

The `main.py` script performs a performance analysis of the sorting and searching algorithms. It measures the execution time of each algorithm for different list sizes and generates comparative graphs.

To execute the performance analysis, run the `main.py` script.

## Requirements

- Python 3.x
- Matplotlib library for generating graphs (install using `pip install matplotlib`)
