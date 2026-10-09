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

# Complexity Analysis Examples

## Example 1: Constant Complexity — `O(1)`

```python
for i in range(1, 101):
    print("hii")
```

### Analysis

The loop always executes 100 times, regardless of the input size.

There is no input variable `n` controlling the number of iterations.

Therefore:

```text
Time Complexity: O(1)
```

This is called **constant time complexity** because the amount of computational work does not grow with the input size.

---

## Example 2: Linear Complexity — `O(n)`

```python
for i in range(1, n + 1):
    print("hii")
```

### Analysis

The loop executes `n` times.

If `n = 5`, the loop executes 5 times.

If `n = 100`, the loop executes 100 times.

Therefore:

```text
Time Complexity: O(n)
```

This is called **linear time complexity**.

---

## Example 3: Quadratic Complexity — `O(n²)`

```python
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("hii")
```

### Analysis

The outer loop executes `n` times.

For every iteration of the outer loop, the inner loop executes `n` times.

Total operations:

```text
n × n = n²
```

Therefore:

```text
Time Complexity: O(n²)
```

This is called **quadratic time complexity**.

---

## Example 4: Square Root Complexity — `O(√n)`

Consider the following code:

```python
for i in range(1, n + 1):
    if i**2 <= n:
        print("hii")
    else:
        print("bye")
        break
```

### Analysis

The condition is:

```text
i² <= n
```

Taking the square root:

```text
i <= √n
```

The loop continues until `i` exceeds `√n`. After that, the `break` statement terminates the loop.

The number of iterations is proportional to `√n`.

Therefore:

```text
Time Complexity: O(√n)
```

**Correction:** Your original example used `range(100)`, which has a fixed limit. That exact code has `O(1)` time complexity, not `O(√n)`. The version above uses `range(1, n + 1)` to demonstrate square root complexity.

---

