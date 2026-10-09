# Complexity Analysis

Complexity analysis is the study of the resources required by an algorithm to solve a problem as the input size increases.

The two major resources are:

1. **Time Complexity**
2. **Space Complexity**

---

## 1. Time Complexity

Time complexity describes how the number of computational operations performed by an algorithm grows as a function of the input size `n`.

It does not measure the exact execution time in seconds. Instead, it describes how the computational work grows as the input size increases.

## 2. Space Complexity

Space complexity describes how the memory requirements of an algorithm grow as a function of the input size `n`.

It includes memory used for variables, data structures, and other operations. Depending on the convention, we may analyze total space or auxiliary space.

* **Total space:** All memory used by the algorithm, including the input.
* **Auxiliary space:** Extra memory used by the algorithm, excluding the input storage.

---

# Asymptotic Notations

Asymptotic notations are mathematical notations used to describe the growth rate of an algorithm as the input size `n` becomes very large.

There are three major asymptotic notations:

1. Big-Omega `Ω`
2. Big-Theta `Θ`
3. Big-O `O`

## 1. Big-O — `O`

Big-O describes an asymptotic **upper bound** on the growth of an algorithm's resource usage.

It is commonly used when discussing worst-case time complexity.

## 2. Big-Omega — `Ω`

Big-Omega describes an asymptotic **lower bound** on the growth of an algorithm's resource usage.

It is commonly used when discussing best-case time complexity.

## 3. Big-Theta — `Θ`

Big-Theta describes a **tight asymptotic bound** on the growth of an algorithm's resource usage.

It means the growth is bounded both above and below by the same asymptotic order.

### Summary

| Notation  | Meaning     | Common Association            |
| --------- | ----------- | ----------------------------- |
| `O(g(n))` | Upper bound | Worst-case analysis           |
| `Ω(g(n))` | Lower bound | Best-case analysis            |
| `Θ(g(n))` | Tight bound | Exact asymptotic growth order |

**Important:** These notations describe mathematical bounds. Big-O does not inherently mean worst case, Big-Omega does not inherently mean best case, and Big-Theta does not inherently mean average case. The actual case depends on the algorithm and the analysis being performed.

---

