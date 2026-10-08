# DSA 1 (30%)

* Sorting

  * Bubble Sort
  * Selection Sort
  * Insertion Sort

* Searching

  * Linear Search
  * Binary Search

* Complexity Analysis

  * 15–20 Programs

* Array

* Stack

* Queue

* Linked List

* Tree (InSort)

* Graphs (InSort)

* Hashing (InSort)

---

# SORTING

## 1. Bubble Sort

### Example

```text
10, 6, 12, 8, 3, 1
```

**Order:** Ascending

---

### Pass-1

**i)** Compare `10` and `6`

```text
6, 10, 12, 8, 3, 1
```

**ii)** Compare `10` and `12`

```text
6, 10, 12, 8, 3, 1
```

**iii)** Compare `12` and `8`

```text
6, 10, 8, 12, 3, 1
```

**iv)** Compare `12` and `3`

```text
6, 10, 8, 3, 12, 1
```

**v)** Compare `12` and `1`

```text
6, 10, 8, 3, 1, 12
```

**Array after Pass-1:**

```text
6, 10, 8, 3, 1, 12
```

**Iterations:** `5`

---

### Pass-2

**i)** Compare `6` and `10`

```text
6, 10, 8, 3, 1, 12
```

**ii)** Compare `10` and `8`

```text
6, 8, 10, 3, 1, 12
```

**iii)** Compare `10` and `3`

```text
6, 8, 3, 10, 1, 12
```

**iv)** Compare `10` and `1`

```text
6, 8, 3, 1, 10, 12
```

**Array after Pass-2:**

```text
6, 8, 3, 1, 10, 12
```

**Iterations:** `4`

---

### Pass-3

**i)** Compare `6` and `8`

```text
6, 8, 3, 1, 10, 12
```

**ii)** Compare `8` and `3`

```text
6, 3, 8, 1, 10, 12
```

**iii)** Compare `8` and `1`

```text
6, 3, 1, 8, 10, 12
```

**Array after Pass-3:**

```text
6, 3, 1, 8, 10, 12
```

**Iterations:** `3`

---

### Pass-4

**i)** Compare `6` and `3`

```text
3, 6, 1, 8, 10, 12
```

**ii)** Compare `6` and `1`

```text
3, 1, 6, 8, 10, 12
```

**Array after Pass-4:**

```text
3, 1, 6, 8, 10, 12
```

**Iterations:** `2`

---

### Pass-5

**i)** Compare `3` and `1`

```text
1, 3, 6, 8, 10, 12
```

**Array after Pass-5:**

```text
1, 3, 6, 8, 10, 12
```

**Iterations:** `1`

---

# Analysis

### Q.1 If `n` elements are there, how many maximum passes in Bubble Sort?

**Answer:**

```text
n - 1
```

---

### Q.2 How many comparisons are required in the first pass if `n` elements are there?

**Answer:**

```text
n - 1
```

---

### Q.3 How many comparisons are required in the second pass if `n` elements are there?

**Answer:**

```text
n - 2
```

---

### Q.4 How many comparisons are required in the last pass if `n` elements are there?

**Answer:**

```text
1
```

---

### Q.5 Time Complexity of Bubble Sort

```text
O(n²)
```

---

### Q.6 Space Complexity of Bubble Sort

```text
O(1)
```

---

### Q.7 How many total comparisons will be required?

**Answer:**

```text
(n - 1) + (n - 2) + ... + 1
```

We know:

```text
1 + 2 + 3 + ... + n
= n(n + 1) / 2
```

Therefore:

```text
1 + 2 + 3 + ... + (n - 1)

= (n - 1)((n - 1) + 1) / 2

= n(n - 1) / 2
```

Therefore:

```text
Total Comparisons = n(n - 1) / 2
```

So the order is:

```text
O(n²)
```

---

# Complexity Analysis on Bubble Sort

## Best Case

```text
1, 2, 3, 4, 5, 6
```

### Pass-1

**i)** Compare `1` and `2` — No swapping

```text
1, 2, 3, 4, 5, 6
```

**ii)** Compare `2` and `3` — No swapping

```text
1, 2, 3, 4, 5, 6
```

**iii)** Compare `3` and `4` — No swapping

```text
1, 2, 3, 4, 5, 6
```

**iv)** Compare `4` and `5` — No swapping

```text
1, 2, 3, 4, 5, 6
```

**v)** Compare `5` and `6` — No swapping

```text
1, 2, 3, 4, 5, 6
```

Since there is **no swap in Pass-1**, we can stop.

### Q.1 In Bubble Sort, how many minimum passes will be required?

**Answer:**

```text
1
```

> In **Bubble Sort**, if there is no swap in the first pass, then the array is sorted and we can stop.

---

### Q.2 In Bubble Sort, if `n` elements are there, then how many minimum comparisons will be required?

**Answer:**

```text
n - 1
```

**Order:**

```text
O(n)
```

---

### Q.3 In Bubble Sort, if `n` elements are there, then how many maximum comparisons will be required?

**Answer:**

```text
n(n - 1) / 2
```

**Order:**

```text
O(n²)
```

---

# Worst Case

```text
6, 5, 4, 3, 2, 1
```

### Pass-1

```text
5, 6, 4, 3, 2, 1

5, 4, 6, 3, 2, 1

5, 4, 3, 6, 2, 1

5, 4, 3, 2, 6, 1

5, 4, 3, 2, 1, 6
```

### Pass-2

```text
4, 5, 3, 2, 1, 6

4, 3, 5, 2, 1, 6

4, 3, 2, 5, 1, 6

4, 3, 2, 1, 5, 6
```

### Pass-3

```text
3, 4, 2, 1, 5, 6

3, 2, 4, 1, 5, 6

3, 2, 1, 4, 5, 6
```

### Pass-4

```text
2, 3, 1, 4, 5, 6

2, 1, 3, 4, 5, 6
```

### Pass-5

```text
1, 2, 3, 4, 5, 6
```

---

# Example

```text
1, 2, 3, 4, 7, 6, 5
```

### Pass-1

```text
1, 2, 3, 4, 7, 6, 5

1, 2, 3, 4, 7, 6, 5

1, 2, 3, 4, 7, 6, 5

1, 2, 3, 4, 6, 7, 5

1, 2, 3, 4, 6, 5, 7
```

### Pass-2

```text
1, 2, 3, 4, 6, 5, 7
```

In Pass-2, only one swap is required:

```text
6, 5 → 5, 6
```

After this:

```text
1, 2, 3, 4, 5, 6, 7
```

Since the array is sorted, the algorithm can stop in the next check.

---

# Maximum Swaps

### Q.4 In Bubble Sort, how many maximum swaps will be required?

**Answer:**

```text
n(n - 1) / 2
```

In the worst case, every comparison results in a swap.

---

# Minimum Swaps

For a sorted array:

```text
1, 2, 3, 4, 5
```

No swapping is required.

### Q.5 How many minimum swaps are required?

**Answer:**

```text
0
```

---

# Points to Remember

> **Passes**
>
> Minimum = `1`
>
> Maximum = `n - 1`

> **Comparisons**
>
> Minimum = `n - 1`
>
> Maximum = `n(n - 1) / 2`

> **Swaps**
>
> Minimum = `0`
>
> Maximum = `n(n - 1) / 2`

---

# Complete Example

```text
4, 1, 7, 10, 3, 6
```

## Pass-1

```text
1, 4, 7, 10, 3, 6

1, 4, 7, 10, 3, 6

1, 4, 7, 3, 10, 6

1, 4, 3, 7, 6, 10

1, 4, 3, 6, 7, 10
```

## Pass-2

```text
1, 3, 4, 6, 7, 10

1, 3, 4, 6, 7, 10

1, 3, 4, 6, 7, 10

1, 3, 4, 6, 7, 10
```

In Pass-2, no further swap is required.

Therefore:

```text
Total Swaps = 4

Total Passes = 2

Total Comparisons = 5 + 4 = 9
```

---

# Bubble Sort Program

```python
numbers = [1, 2, 3, 4, 5]

n = len(numbers)

for i in range(n - 1):

    swap = False

    for j in range(n - i - 1):

        if numbers[j] > numbers[j + 1]:

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            swap = True

    if swap == False:
        break

print(numbers)
```