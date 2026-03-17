# Sorting Algorithms Analysis
Math Concepts for Developers – Final Exam Project

## Overview

This project explores several classical sorting algorithms through both **mathematical analysis** and **Python implementations**.

Sorting algorithms are a fundamental topic in computer science and provide a strong foundation for understanding:

- algorithmic complexity
- asymptotic analysis
- performance trade-offs between algorithmic approaches

The project combines theoretical explanations, mathematical formulas, and empirical experiments implemented in Python using Jupyter Notebook.

## How to run

### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Open in jupyter lab or notebook
```
jupyter lab
```
or
```
jupyter notebook
```

## Algorithms Covered

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort


## Project Components

The project includes:

- Mathematical explanation of sorting complexity
- Python implementations of several algorithms
- Empirical performance benchmarking
- Visualizations of algorithm performance

## Benchmarking

The project includes empirical benchmarking of the implemented algorithms.  
Random arrays of increasing size are generated and sorted using each algorithm while measuring execution time.

The results are visualized using **Matplotlib**, allowing comparison between:

- quadratic time algorithms $O(n^2)$
- more efficient algorithms $O(n \log n)$

This demonstrates how theoretical complexity analysis translates into real-world performance.

## Technologies

- Python 3.12+
- Jupyter Notebook
- Matplotlib

## Repository Structure

```
src/ – Python implementations of sorting algorithms
sorting_algorithms_analysis.ipynb - Main project
requirements.txt - Required libraries
```


## Purpose

This project was created as the final project for the **Math Concepts for Developers** course.  
Its goal is to demonstrate the connection between **mathematical reasoning and algorithm design** through the study of sorting algorithms.
