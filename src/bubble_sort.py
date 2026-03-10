def bubble_sort(arr: list) -> list:
    """
    Bubble Sort implementation.

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
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr