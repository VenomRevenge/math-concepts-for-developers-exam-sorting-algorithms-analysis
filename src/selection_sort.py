def selection_sort(arr):
    """
    Selection sort implementation.

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
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr