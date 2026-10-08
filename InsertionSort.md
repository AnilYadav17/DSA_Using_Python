# Insertion Sort

## Example

```text
10 8 5 7 6 9 12
```

### Pass 1

Compare `10` and `8`.

```text
8 10 5 7 6 9 12
```

### Pass 2

Insert `5` into the sorted portion.

```text
5 8 10 7 6 9 12
```

### Pass 3

Insert `7` into the sorted portion.

```text
5 7 8 10 6 9 12
```

### Pass 4

Insert `6` into the sorted portion.

```text
5 6 7 8 10 9 12
```

### Pass 5

Insert `9` into the sorted portion.

```text
5 6 7 8 9 10 12
```

### Pass 6

Insert `12` into the sorted portion.

```text
5 6 7 8 9 10 12
```

---

# Worst Case

```text
5 4 3 2 1
```

### Pass 1

```text
4 5 3 2 1
```

**1 comparison**

### Pass 2

```text
3 4 5 2 1
```

**2 comparisons**

### Pass 3

```text
2 3 4 5 1
```

**3 comparisons**

### Pass 4

```text
1 2 3 4 5
```

**4 comparisons**

### Worst Case Analysis

If there are `n` elements, the maximum number of passes required is:

```text
n - 1
```

The maximum number of comparisons is:

```text
1 + 2 + 3 + ... + (n - 1)
```

Therefore:

```text
n(n - 1) / 2
```

So the **worst-case time complexity** is:

```text
O(n²)
```

---

# Best Case

```text
1 2 3 4 5
```

### Pass 1

```text
1 2 3 4 5
```

**1 comparison**

### Pass 2

```text
1 2 3 4 5
```

**1 comparison**

### Pass 3

```text
1 2 3 4 5
```

**1 comparison**

### Pass 4

```text
1 2 3 4 5
```

**1 comparison**

### Best Case Analysis

There is one comparison in every pass.

```text
1 + 1 + 1 + ... + 1
```

There are `n - 1` passes.

Therefore:

```text
Total comparisons = n - 1
```

So the **best-case time complexity** is:

```text
O(n)
```

### Minimum Passes

If there are `n` elements in Insertion Sort, the minimum number of passes required is:

```text
n - 1
```

---

# Insertion Sort Complexity

| Case         |    Comparisons | Time Complexity |
| ------------ | -------------: | --------------: |
| Best Case    |        `n - 1` |          `O(n)` |
| Average Case |              — |         `O(n²)` |
| Worst Case   | `n(n - 1) / 2` |         `O(n²)` |

---

# Bubble Sort vs Selection Sort vs Insertion Sort

| Algorithm      | Best Case | Average Case | Worst Case |
| -------------- | --------- | ------------ | ---------- |
| Bubble Sort    | `O(n)`*   | `O(n²)`      | `O(n²)`    |
| Selection Sort | `O(n²)`   | `O(n²)`      | `O(n²)`    |
| Insertion Sort | `O(n)`    | `O(n²)`      | `O(n²)`    |

> **Note:** Bubble Sort's `O(n)` best case applies to the **optimized version with the swap flag**.

---

# Insertion Sort Program

```python
numbers = [12, 11, 13, 5, 6]

n = len(numbers)

for i in range(1, n):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print(numbers)
```
