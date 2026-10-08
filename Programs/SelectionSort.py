"""
Selection Sort Algorithm Implementation in Python
--------------------------------------------------
Author: Anil Yadav
Repository: DSA_Using_Python

Time Complexity:
    - Best Case:    O(n^2)   (Requires n(n - 1)/2 comparisons even if sorted)
    - Average Case: O(n^2)
    - Worst Case:   O(n^2)   (When array is reverse sorted)

Space Complexity:
    - Auxiliary Space: O(1)  (In-place sorting)

Properties:
    - Stable: No (swapping distant elements can change relative order of equal keys)
    - In-Place: Yes
    - Swaps: O(n) (At most n - 1 swaps, making it useful when write memory is expensive)
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    In each pass, finds the minimum element from the unsorted subarray
    and places it at the beginning of that subarray.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)

    for i in range(n - 1):
        # Assume the current element is the minimum
        min_idx = i

        # Scan the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap only if a smaller element was found (avoids redundant self-swaps)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    print("=" * 50)
    print(" " * 14 + "SELECTION SORT DEMO")
    print("=" * 50)

    try:
        user_input = input(
            "Enter numbers separated by space (or press Enter for default demo): "
        ).strip()
        if user_input:
            numbers = list(map(int, user_input.split()))
        else:
            numbers = [10, 5, 8, 2, 1, 3]
            print(f"Using default sample array: {numbers}")

        print(f"Original Array : {numbers}")
        sorted_numbers = selection_sort(numbers)
        print(f"Sorted Array   : {sorted_numbers}")
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")
