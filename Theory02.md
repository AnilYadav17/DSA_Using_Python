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

---

# Practice Problem (Step-by-Step Dry Run)

### Given Array

```text
1, 2, 3, 8, 7, 6, 5, 4
```

**Number of elements (`n`):** 8

---

## Pass-1

**Minimum = 1** (at index 0)

```text
2 > min → min = 1
3 > min → min = 1
8 > min → min = 1
7 > min → min = 1
6 > min → min = 1
5 > min → min = 1
4 > min → min = 1
```

No swap is required.

```text
1, 2, 3, 8, 7, 6, 5, 4
```

---

## Pass-2

**Minimum = 2** (at index 1)

```text
3 > min → min = 2
8 > min → min = 2
7 > min → min = 2
6 > min → min = 2
5 > min → min = 2
4 > min → min = 2
```

No swap is required.

```text
1, 2, 3, 8, 7, 6, 5, 4
```

---

## Pass-3

**Minimum = 3** (at index 2)

```text
8 > min → min = 3
7 > min → min = 3
6 > min → min = 3
5 > min → min = 3
4 > min → min = 3
```

No swap is required.

```text
1, 2, 3, 8, 7, 6, 5, 4
```

---

## Pass-4

**Minimum = 8** (at index 3)

```text
7 < 8 → min = 7
6 < 7 → min = 6
5 < 6 → min = 5
4 < 5 → min = 4
```

Swap `8` and `4`.

```text
1, 2, 3, 4, 7, 6, 5, 8
```

---

## Pass-5

**Minimum = 7** (at index 4)

```text
6 < 7 → min = 6
5 < 6 → min = 5
8 > 5 → min = 5
```

Swap `7` and `5`.

```text
1, 2, 3, 4, 5, 6, 7, 8
```

---

## Pass-6

**Minimum = 6** (at index 5)

```text
7 > min → min = 6
8 > min → min = 6
```

No swap is required.

```text
1, 2, 3, 4, 5, 6, 7, 8
```

---

## Pass-7

**Minimum = 7** (at index 6)

```text
8 > min → min = 7
```

No swap is required.

```text
1, 2, 3, 4, 5, 6, 7, 8
```

---

# Comprehensive Analysis & Summary

### Total Passes

```text
n - 1 = 8 - 1 = 7 passes
```

### Comparisons Per Pass

```text
Pass 1 → 7 comparisons
Pass 2 → 6 comparisons
Pass 3 → 5 comparisons
Pass 4 → 4 comparisons
Pass 5 → 3 comparisons
Pass 6 → 2 comparisons
Pass 7 → 1 comparison
```

Therefore:

```text
Total Comparisons
= 7 + 6 + 5 + 4 + 3 + 2 + 1
= 28
```

### Swaps

```text
Pass 4 → 1 swap (8 ↔ 4)
Pass 5 → 1 swap (7 ↔ 5)
```

Therefore:

```text
Total Swaps = 2
```

### Final Summary

```text
Initial Array      : 1, 2, 3, 8, 7, 6, 5, 4
Final Sorted Array : 1, 2, 3, 4, 5, 6, 7, 8

Total Passes       : 7
Total Comparisons  : 28
Total Swaps        : 2
```

---

# Points to Remember

> **Passes**
>
> Minimum = `n - 1`
>
> Maximum = `n - 1`

> **Comparisons**
>
> Minimum = `n(n - 1) / 2`
>
> Maximum = `n(n - 1) / 2`

> **Swaps**
>
> Minimum = `0`
>
> Maximum = `n - 1`


