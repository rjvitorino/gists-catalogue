# 20240909-min_rows-gist

**Gist file**: [https://gist.github.com/rjvitorino/a595e69656a4069ae07eeacfd35f9fc6](https://gist.github.com/rjvitorino/a595e69656a4069ae07eeacfd35f9fc6)

**Description**: Cassidy's interview question of the week: a function to calculate the minimum number of rows required to seat everyone such that no group is split

## min_rows.py

```Python
from typing import List


def min_rows(groups: List[int], row_size: int) -> int:
    """
    Calculate the minimum number of rows required to seat all groups
    without splitting them across rows.

    :param groups: List of integers where each integer represents a group size.
    :param row_size: Integer representing the maximum number of people that can sit in a row.
    :return: Minimum number of rows required to seat all the groups.
    """

    # Sort the groups in descending order to prioritise larger groups first
    groups.sort(reverse=True)

    rows = 0

    # Loop until all groups are seated
    while groups:
        remaining_space = row_size
        groups_to_remove = []

        # Try to place as many groups as possible in the current row
        for group_index, group_size in enumerate(groups):
            if group_size <= remaining_space:
                remaining_space -= group_size
                groups_to_remove.append(group_index)

        # Remove the groups that have been placed in the current row
        for index in reversed(groups_to_remove):
            groups.pop(index)

        # Move to the next row
        rows += 1

    return rows


def main() -> None:
    """
    Run test cases to verify if min_rows function works.
    """

    test_cases = [
        ([4, 8, 3, 5, 6], 10, 3),  # Expected: 3
        ([4, 5, 4, 3, 3], 10, 2),  # Expected: 2
        ([7, 7, 8, 9, 6], 10, 5),  # Expected: 5
        # Additional test cases
        ([2, 2, 2, 2, 2, 2, 2, 2], 4, 4),  # Expected: 4
        ([10, 10, 10, 10], 10, 4),  # Expected: 4
        ([1, 9, 2, 8, 3, 7, 4, 6], 10, 4),  # Expected: 4
        ([6, 6, 6, 6, 6, 6], 12, 3),  # Expected: 3
        ([2, 8, 5, 5, 5, 5], 10, 3),  # Expected: 3
        ([3, 2, 2, 2, 2, 2, 2, 2], 4, 5),  # Expected: 5
        # Problematic cases for a greedy approach
        ([9, 2, 2, 2, 2, 2], 10, 2),  # Expected: 3 (Greedy might use 4 rows)
        ([6, 6, 5, 5, 4], 10, 3),  # Expected: 3 (Greedy might use 4 rows)
        ([5, 5, 5, 5, 5, 5], 10, 3),  # Expected: 3 (Greedy might use 4 rows)
        ([9, 9, 9, 1, 1, 1], 10, 3),  # Expected: 3 (Greedy might use 4 rows)
    ]

    for groups, row_size, expected in test_cases:
        result = min_rows(groups[:], row_size)
        assert (
            result == expected
        ), f"Test failed for groups: {groups} and row_size: {row_size}. Expected {expected}, got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    main()

```