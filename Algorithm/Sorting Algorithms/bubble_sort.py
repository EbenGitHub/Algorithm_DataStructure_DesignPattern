# Worst-case time complexity: O(n^2)
# Best-case time complexity: O(n)
# Average time complexity: O(n^2)
# Space complexity: O(1)

def bubble_sort(numbers):
    """
    Sort a list of numbers in ascending order using the bubble sort algorithm.

    Parameters:
    numbers (list): A list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, num in enumerate(numbers[:-1]):
            if num > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
    return numbers

output = bubble_sort([3, 5, 2, 4, 33, 2, 1, 4, 10, 9, 5, 7, 6, 4, 3, 4])
print(output)