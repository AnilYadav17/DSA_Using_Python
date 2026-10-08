<div align="center">

# 🚀 Data Structures & Algorithms in Python

An organized, production-quality repository dedicated to learning and mastering **Data Structures and Algorithms (DSA)** using **Python**. Featuring clean implementations, step-by-step dry-run traces, mathematical analyses, and Big-O complexity breakdowns.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/AnilYadav17/DSA_Using_Python)
[![GitHub Stars](https://img.shields.io/github/stars/AnilYadav17/DSA_Using_Python?style=for-the-badge)](https://github.com/AnilYadav17/DSA_Using_Python/stargazers)

<br/>

[Curriculum](#-curriculum--roadmap) •
[Repository Structure](#-repository-structure) •
[Complexity Cheat Sheet](#-complexity-cheat-sheet) •
[Getting Started](#-getting-started) •
[Contributing](#-contributing)

</div>

---

## 📌 Overview

This repository is designed as both a **study companion** and an **engineering reference**. Every algorithm is provided with:
- 💡 **Clean, PEP 8 Compliant Python Code** with type annotations and docstrings.
- 📝 **In-depth Theoretical Notes** breaking down intuition, edge cases, and dry-runs.
- ⏱️ **Time & Space Complexity Proofs** (Best, Average, and Worst cases).
- 🧪 **Interactive Demonstrations** ready to execute directly from the terminal.

---

## 🗺️ Curriculum & Roadmap

### 1. Sorting Algorithms
- [x] **Bubble Sort** ([Code](Programs/bubble_sort.py) | [Notes](BubbleSort.md))
- [x] **Selection Sort** ([Code](Programs/selection_sort.py) | [Notes](SelectionSort.md))
- [ ] **Insertion Sort** *(Upcoming)*
- [ ] **Merge Sort** *(Upcoming)*
- [ ] **Quick Sort** *(Upcoming)*

### 2. Searching Algorithms
- [ ] **Linear Search** *(Upcoming)*
- [ ] **Binary Search** *(Upcoming)*

### 3. Complexity Analysis
- [x] **Asymptotic Notation** ($\mathcal{O}$, $\Omega$, $\Theta$)
- [x] **Iteration & Swap Calculation Formulas** ([Notes (Bubble Sort)](BubbleSort.md) | [Notes (Selection Sort)](SelectionSort.md))

### 4. Linear Data Structures
- [ ] **Arrays & Dynamic Arrays**
- [ ] **Stack** (Array & Linked List implementations)
- [ ] **Queue** (Simple, Circular, & Deque)
- [ ] **Linked List** (Singly, Doubly, & Circular)

### 5. Non-Linear Data Structures & Advanced Topics
- [ ] **Trees & Binary Search Trees (BST)**
- [ ] **Graphs & Traversals (BFS / DFS)**
- [ ] **Hashing & Hash Maps**

---

## 📊 Complexity Cheat Sheet

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable? | In-Place? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Yes | Yes |
| **Selection Sort** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | No | Yes |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Yes | Yes |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | Yes | No |
| **Quick Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | No | Yes |

---

## 📁 Repository Structure

```plaintext
DSA_Using_Python/
│
├── .gitignore              # Ignores bytecode, caches, and environment configs
├── BubbleSort.md           # Theoretical foundation, dry-runs & Bubble Sort notes
├── LICENSE                 # MIT Open-Source License
├── README.md               # Repository documentation and navigation guide
├── SelectionSort.md        # Selection Sort theory, pass traces & complexity notes
│
└── Programs/               # Executable Python implementations
    ├── bubble_sort.py      # Bubble Sort (PEP 8 standard naming)
    ├── BubleSort.py        # Bubble Sort implementation
    ├── selection_sort.py   # Selection Sort (PEP 8 standard naming)
    └── SelectionSort.py    # Selection Sort implementation
```

---

## ⚡ Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/AnilYadav17/DSA_Using_Python.git
cd DSA_Using_Python
```

### 2. Run an Algorithm
Each program contains an interactive demo mode:

```bash
# Run Bubble Sort demo
python3 Programs/bubble_sort.py

# Run Selection Sort demo
python3 Programs/selection_sort.py
```

**Example Run (Bubble Sort):**
```text
==================================================
               BUBBLE SORT DEMO
==================================================
Enter numbers separated by space (or press Enter for default demo): 64 34 25 12 22 11 90
Original Array : [64, 34, 25, 12, 22, 11, 90]
Sorted Array   : [11, 12, 22, 25, 34, 64, 90]
```

**Example Run (Selection Sort):**
```text
==================================================
              SELECTION SORT DEMO
==================================================
Enter numbers separated by space (or press Enter for default demo): 10 5 8 2 1 3
Original Array : [10, 5, 8, 2, 1, 3]
Sorted Array   : [1, 2, 3, 5, 8, 10]
```

---

## 🛠️ Standards & Best Practices

All implementations in this repository follow strict coding principles:
- **Type Hinting:** Using Python's `typing` module for clear parameter and return types.
- **Documentation:** Google/Sphinx style docstrings describing time and space complexities.
- **Modularity:** Algorithms are encapsulated in reusable functions with `__main__` entry points.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewAlgorithm`)
3. Commit your Changes (`git commit -m 'Add Selection Sort algorithm'`)
4. Push to the Branch (`git push origin feature/NewAlgorithm`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more details.

---

<div align="center">
  <b>Author:</b> <a href="https://github.com/AnilYadav17">Anil Yadav</a> &bull; Happy Coding! 💻
</div>
