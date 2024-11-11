# 20241111-see_buildings_left-gist

**Gist file**: [https://gist.github.com/rjvitorino/5591a15f936b524e560cf9e049e21a4d](https://gist.github.com/rjvitorino/5591a15f936b524e560cf9e049e21a4d)

**Description**: Cassidoo's interview question of the week: a function that given a list of integers representing the heights of buildings, returns the maximum number of buildings that can be seen when looking from the left.

## see_buildings_left.py

```Python
from typing import List


def see_buildings_left(buildings: List[int]) -> int:
    """
    Calculate the number of buildings visible from the left.

    A building is visible if it is taller than all the buildings to its left.

    Args:
        buildings (List[int]): List of building heights.

    Returns:
        int: Count of visible buildings.
    """
    # Track the maximum height seen and the count of visible buildings
    max_height = float("-inf")
    visible_count = 0

    for height in buildings:
        # A building is visible if it exceeds the max height seen so far
        if height > max_height:
            visible_count += 1
            max_height = height  # Update the maximum height

    return visible_count


def test_see_buildings_left() -> None:
    """
    Test the `see_buildings_left` function with various examples to ensure correctness.
    """
    # Provided examples
    assert see_buildings_left([1, 2, 3, 4, 5]) == 5
    assert see_buildings_left([5, 4, 3, 2, 1]) == 1
    assert see_buildings_left([3, 7, 8, 3, 6, 1]) == 3

    # Additional edge cases and odd scenarios
    assert see_buildings_left([3, 1, 6, 3, 7, 8]) == 4
    assert see_buildings_left([10, 10, 10, 10, 10]) == 1
    assert see_buildings_left([0, 0, 0, 0, 0]) == 1
    assert see_buildings_left([9, 8, 10, 11, 7, 15, 3]) == 4
    assert see_buildings_left([1, 100, 50, 200, 150, 300, 400]) == 5
    assert see_buildings_left([50, 40, 30, 20, 10, 60, 70]) == 3
    assert see_buildings_left([1, 3, 2, 5, 4, 6, 2, 7]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_see_buildings_left()

```