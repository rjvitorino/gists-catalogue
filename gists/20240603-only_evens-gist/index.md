# 20240603-only_evens-gist

**Gist file**: [https://gist.github.com/rjvitorino/b479dc2c27d3854b210955ff032d3413](https://gist.github.com/rjvitorino/b479dc2c27d3854b210955ff032d3413)

**Description**: Cassidoo's interview question of the week: a function that takes an array of integers and returns a new array containing only the even numbers, and sorted.

## only_evens.py

```Python
from typing import List


def only_evens(numbers: List[int]) -> List[int]:
    """
    Returns a sorted list of even numbers from the input list.
    Args:
    numbers (list of int): List of integers.
    Returns:
    list of int: Sorted list of even integers.
    """
    # Validate input
    if not all(isinstance(number, int) for number in numbers):
        raise ValueError("All elements in the input list must be integers")

    def is_even(number: int) -> bool:
        return number % 2 == 0

    # Use filter to select even numbers from the input list
    even_numbers = filter(is_even, numbers)
    return sorted(even_numbers)


if __name__ == "__main__":
    # Test cases with assertions
    assert only_evens([1, 2, 3, 4, 5, 2]) == [2, 2, 4]
    assert only_evens([7, 8, 1, 0, 2, 5]) == [0, 2, 8]
    assert only_evens([11, 13, 15]) == []
    assert only_evens([]) == []
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]

    # Test case to handle ValueError
    try:
        only_evens([1, "two", 3])
    except ValueError:
        print("Caught expected ValueError for non-integer input")

    print("All tests passed!")

```