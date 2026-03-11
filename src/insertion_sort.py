def insertion_sort(arr):
    """
    Insertion sort implementation.

    Parameters
    ---
    arr : list
        List of comparable elements.

    Returns
    ---
    list
        Sorted copy of the input list.
    """
    
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr