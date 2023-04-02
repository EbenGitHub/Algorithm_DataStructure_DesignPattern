# Worst-case time complexity: O(n^2)
# Best-case time complexity: O(n)
# Average time complexity: O(n^2)
# Space complexity: O(1)

def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Parameters:
    arr (list): An unsorted list of comparable elements.

    Returns:
    list: A sorted list of the same elements.
    """
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
    return arr

output = insertion_sort([3, 5, 2, 4, 33, 2, 1, 4, 10, 9, 5, 7, 6, 4, 3, 4])
print(output)