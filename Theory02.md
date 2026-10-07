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
