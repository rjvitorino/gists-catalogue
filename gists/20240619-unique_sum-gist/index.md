# 20240619-unique_sum-gist

**Description**: Cassidoo's interview question of the week (20240401 - April fools!): Given an array of numbers, add all of the values together but only if the number does not repeat a digit.

## unique_sum.py

```Python
def has_unique_digits(number: int) -> bool:
    """
    Check if the given number has all unique digits.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if all digits are unique, False otherwise.
    """
    digits = str(number)
    return len(set(digits)) == len(digits)

def unique_sum(numbers: list) -> int:
    """
    Calculate the sum of numbers in the list that have unique digits.

    Args:
    numbers (list): List of integers.

    Returns:
    int: The sum of numbers with unique digits.
    """
    return sum(number for number in numbers if has_unique_digits(number))

# Testing the function with the provided examples.
test_cases = [
    ([1, 2, 3], 6),
    ([11, 22, 33], 0),
    ([101, 2, 3], 5),
    ([123, 456, 789, 122, 133], 1368)  # Additional test case
]

# Running tests and printing results
for numbers, expected in test_cases:
    result = unique_sum(numbers)
    assert result == expected, f"Test failed for input {numbers}: expected {expected}, got {result}"
    print(f"Test passed for input {numbers}: got {result}")

```