# Selection Sort

Selection Sort is a simple sorting algorithm that builds the final sorted array one item at a time.

It is less efficient for large lists than advanced sorting algorithms such as Quicksort, Heapsort, and Merge Sort.

### Example

```text
10, 5, 8, 2, 1, 3
```

**Order:** Ascending

---

## Pass-1

`10` as minimum

```text
5 < min → min = 5
8 > min → min = 5
2 < min → min = 2
1 < min → min = 1
3 > min → min = 1
```

So, swap `10` and `1`.

```text
1, 5, 8, 2, 10, 3
```

---

## Pass-2

`5` as minimum

```text
8 > min → min = 5
2 < min → min = 2
10 > min → min = 2
3 > min → min = 2
```

So, swap `5` and `2`.

```text
1, 2, 8, 5, 10, 3
```

---

## Pass-3

`8` as minimum

```text
5 < min → min = 5
10 > min → min = 5
3 < min → min = 3
```

So, swap `8` and `3`.

```text
1, 2, 3, 5, 10, 8
```

---

## Pass-4

`5` as minimum

```text
10 > min → min = 5
8 > min → min = 5
```

No swap is required because `5` is already in the correct position.

```text
1, 2, 3, 5, 10, 8
```

---

## Pass-5

`10` as minimum

```text
8 < min → min = 8
```

So, swap `10` and `8`.

```text
1, 2, 3, 5, 8, 10
```

---

# Theoretical Analysis & Formulas

### Q.1 In Selection Sort, if `n` elements are present, how many maximum passes are required?

**Answer:**

```text
n - 1
```

---

### Q.2 In Selection Sort, how many comparisons are required in the first pass?

**Answer:**

```text
n - 1
```

---

### Q.3 How many total comparisons are required in Selection Sort?

**Answer:**

```text
(n - 1) + (n - 2) + (n - 3) + ... + 1
= n * (n - 1) / 2
```

Therefore, the time complexity is:

```text
O(n²)
```

---

# Best Case Analysis (Already Sorted Array)

Given array:

```text
1, 2, 3, 4, 5
```

### Pass-1: `min = 1`

```text
2 > 1 → min = 1
3 > 1 → min = 1
4 > 1 → min = 1
5 > 1 → min = 1
```

No swap is required.

---

### Pass-2: `min = 2`

```text
3 > 2 → min = 2
4 > 2 → min = 2
5 > 2 → min = 2
```

No swap is required.

---

### Pass-3: `min = 3`

```text
4 > 3 → min = 3
5 > 3 → min = 3
```

No swap is required.

---

### Pass-4: `min = 4`

```text
5 > 4 → min = 4
```

No swap is required.

---

### Key Questions on Passes and Swaps

### Q.4 In Selection Sort, how many minimum passes are required for an already sorted array?

**Answer:**

```text
n - 1
```

> **Note:** Unlike Bubble Sort (which can terminate early in 1 pass if no swaps occur), standard Selection Sort always executes `n - 1` passes to identify the minimum element in each subarray.

---

### Q.5 In Selection Sort, what is the maximum number of swaps required?

**Answer:**

```text
n - 1
```

---

### Q.6 In Selection Sort, what is the minimum number of swaps required?

**Answer:**

```text
0
```

