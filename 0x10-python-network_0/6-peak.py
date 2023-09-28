#!/usr/bin/python3
"""
    Find a peak element in a list of integers using a binary search algorithm.
    """

def find_peak(list_of_integers):
    """
    Find a peak element in a list of integers using a binary search algorithm.

    Args:
        list_of_integers (list of int): A list of integers.

    Returns:
        int: The peak element.

    Algorithm:
    This function uses a binary search algorithm to find a peak element in
    a list of integers. A peak element is defined as an element that is
    greater than or equal to its neighbors. The algorithm starts with the
    entire list and iteratively narrows down the search range until
    a peak is found.

    1. Initialize left and right pointers to the beginning and end of the
       list, respectively.
    2. Enter a while loop that continues until the left pointer is less than
       the right pointer.
    3. Calculate the middle index (mid) as the average of left and right.
    4. Compare the element at mid with its right neighbor (mid + 1).
    5. If the element at mid is greater, update the right pointer to mid,
       indicating that the peak is in the left half.
    6. If the element at mid is not greater, update the left pointer to
       mid + 1, indicating that the peak is in the right half.
    7. Repeat steps 3-6 until the left pointer is equal to the right pointer.
    8. Return the element at the left pointer as the peak.

    Example:
    >>> find_peak([1, 2, 3, 1])
    3
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
