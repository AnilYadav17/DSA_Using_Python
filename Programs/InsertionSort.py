"""
Insertion Sort Algorithm Implementation in Python
-------------------------------------------------
Author: Anil Yadav
Repository: DSA_Using_Python

Time Complexity:
    - Best Case:    O(n)     (When array is already sorted)
    - Average Case: O(n^2)   (When array elements are in random order)
    - Worst Case:   O(n^2)   (When array is reverse sorted)

Space Complexity:
    - Auxiliary Space: O(1)  (In-place sorting)

Properties:
    - Stable: Yes (does not change relative order of identical elements)
    - Adaptive: Yes (executes in O(n) for nearly sorted or sorted inputs)
    - Online: Yes (can sort a list as it receives elements)
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Iterates through elements from index 1 to n - 1, inserting each key
    into its correct position within the sorted prefix.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print(" " * 14 + "INSERTION SORT DEMO")
    print("=" * 50)

    try:
        user_input = input(
            "Enter numbers separated by space (or press Enter for default demo): "
        ).strip()
        if user_input:
            numbers = list(map(int, user_input.split()))
        else:
            numbers = [12, 11, 13, 5, 6]
            print(f"Using default sample array: {numbers}")

        print(f"Original Array : {numbers}")
        sorted_numbers = insertion_sort(numbers)
        print(f"Sorted Array   : {sorted_numbers}")
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")
