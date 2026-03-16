def quick_sort(arr):
    """
    Quick sort implementation.

    Parameters
    ---
    arr : list
        List of comparable elements.

    Returns
    ---
    list
        Sorted copy of the input list.
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)