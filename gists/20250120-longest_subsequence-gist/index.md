# 20250120-longest_subsequence-gist

**Gist file**: [https://gist.github.com/rjvitorino/88cb1c0f71f70165cf809d5103ddde0b](https://gist.github.com/rjvitorino/88cb1c0f71f70165cf809d5103ddde0b)

**Description**: Cassidy's interview question of the week: a function that finds the longest subsequence where the difference between consecutive elements is either 1 or -1

## longest_subsequence.py

```Python
from typing import List


def longest_subsequence(numbers: List[int]) -> int:
    """
    Find the length of the longest subsequence of consecutive integers in a list.
    The difference between consecutive elements is either 1 or -1.

    Args:
        numbers (List[int]): A list of integers.
    Returns:
        int: The length of the longest subsequence of consecutive integers.

    """
    if not numbers:
        return 0

    longest = 1
    current_length = 1

    for i in range(1, len(numbers)):
        # If the difference between the current and previous number is 1, increment the current length
        if abs(numbers[i] - numbers[i - 1]) == 1:
            current_length += 1
            longest = max(longest, current_length)
        # Otherwise, reset the current length
        else:
            current_length = 1

    return longest


if __name__ == "__main__":
    assert longest_subsequence([1, 2, 3, 4, 5]) == 5
    assert longest_subsequence([5, 4, 3, 2, 1]) == 5
    assert longest_subsequence([4, 2, 3, 1, 5]) == 2
    assert longest_subsequence([10, 11, 7, 8, 9, 12]) == 3
    assert longest_subsequence([]) == 0
    assert longest_subsequence([1]) == 1
    assert longest_subsequence([1, 3, 5, 7]) == 1
    print("All checks passed!")

```