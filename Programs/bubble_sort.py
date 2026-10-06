"""
Bubble Sort Algorithm Implementation in Python
----------------------------------------------
Author: Anil Yadav
Repository: DSA_Using_Python

Time Complexity:
    - Best Case:    O(n)     (When array is already sorted)
    - Average Case: O(n^2)
    - Worst Case:   O(n^2)   (When array is reverse sorted)

Space Complexity:
    - Auxiliary Space: O(1)  (In-place sorting)

Properties:
    - Stable: Yes (does not change the relative order of duplicate elements)
    - Adaptive: Yes (with early termination check `swapped`)
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the optimized Bubble Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        # Last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, array is sorted
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print(" " * 15 + "BUBBLE SORT DEMO")
    print("=" * 50)

    try:
        user_input = input("Enter numbers separated by space (or press Enter for default demo): ").strip()
        if user_input:
            numbers = list(map(int, user_input.split()))
        else:
            numbers = [10, 6, 12, 8, 3, 1]
            print(f"Using default sample array: {numbers}")

        print(f"Original Array : {numbers}")
        sorted_numbers = bubble_sort(numbers)
        print(f"Sorted Array   : {sorted_numbers}")
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")