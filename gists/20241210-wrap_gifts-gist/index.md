# 20241210-wrap_gifts-gist

**Gist file**: [https://gist.github.com/rjvitorino/ef5905749489173598c4c51462bd19e9](https://gist.github.com/rjvitorino/ef5905749489173598c4c51462bd19e9)

**Description**: Cassidy's interview question of the week: a function that finds the maximum number of gifts that can be wrapped using a single strip of wrapping paper of a given width

## wrap_gifts.py

```Python
from typing import Sequence
from array import array
from itertools import accumulate


def wrap_gifts(gift_lengths: Sequence[int], paper_width: int) -> int:
    """
    Find the maximum number of gifts that can be wrapped using a single strip of wrapping paper.

    Args:
        gift_lengths (Sequence[int]): The lengths of the gifts.
        paper_width (int): The width of the wrapping paper.

    Returns:
        int: The maximum number of gifts that can be wrapped.

    Raises:
        ValueError: If paper_width is negative or gift_lengths contains negative values.
    """
    # Fast path for common cases
    if not gift_lengths:
        return 0
    if paper_width <= 0:
        raise ValueError("Paper width cannot be negative")

    # Use array for memory efficiency
    gifts = array("i", sorted(gift_lengths))

    # Early exit if smallest gift doesn't fit
    if gifts[0] > paper_width:
        return 0

    # Use prefix sum for efficient length calculation:
    # [1, 2, 3, 4] results in [1, 3, 6, 10] meaning each
    # element represents the sum of all previous + current one
    prefix_sums = array("i", accumulate(gifts))

    # Binary search optimization
    left, right = 0, len(gifts)
    # left: starts at 0 (no gifts)
    # right: starts at total number of gifts
    # These represent the search range for the maximum number of gifts that can fit

    while left < right:
        # Continues until the search range converges to a single point
        # When left == right, we've found our answer
        mid = (left + right + 1) >> 1 
        # >> is a bit shift operator, equivalent to dividing by 2 but faster
        if prefix_sums[mid - 1] <= paper_width:
            left = mid
        else:
            right = mid - 1

    return left


def test_wrap_gifts():
    """Test cases for wrap_gifts function with performance metrics."""
    test_cases = [
        ([2, 3, 4, 5], 7, 2),  # Either [2, 5] or [3, 4]
        ([1, 1, 1, 1, 1, 1, 1], 3, 3),  # [1, 1, 1]
        ([1, 2, 3, 4, 5], 6, 3),  # [1, 2, 3]
        ([5, 5, 5, 5], 10, 2),  # [5, 5]
        ([6, 7, 8], 5, 0),  # No gift fits
        ([3, 2, 1], 6, 3),  # [1, 2, 3] after sorting
    ]

    for gifts, width, expected in test_cases:
        result = wrap_gifts(gifts, width)
        assert (
            result == expected
        ), f"Failed: gifts={gifts}, width={width}, got={result}, expected={expected}"

    print("All tests passed!")


if __name__ == "__main__":
    test_wrap_gifts()

```