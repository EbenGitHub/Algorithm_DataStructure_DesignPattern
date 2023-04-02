# Worst-case time complexity: O(n^2)
# Best-case time complexity: O(n^2)

def selection_sort(numbers):
    """
    Sort a list of numbers in ascending order using the selection sort algorithm.

    Parameters:
    numbers (list): A list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    for i, _ in enumerate(numbers):
        min_index = i
        for j, next_num in enumerate(numbers[i + 1:], start=i + 1):
            if next_num < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

output = selection_sort([3, 5, 2, 4, 33, 2, 1, 4, 10, 9, 5, 7, 6, 4, 3, 4])
print(output)