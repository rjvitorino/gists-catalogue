# 20250804-min_monster_distance-gist

**Gist file**: [https://gist.github.com/rjvitorino/5d39783fe52ec74fcf972a0c26188f67](https://gist.github.com/rjvitorino/5d39783fe52ec74fcf972a0c26188f67)

**Description**: Monster distance checker (Cassidy's interview question of the week): a function that takes a list of monster positions along a straight line and a minimum safe distance, returning the smallest distance between any two monsters if they're not safely spaced, or -1 if all monsters are at least the required distance apart.

## min_monster_distance.py

```Python
"""
Monster Distance Checker

This module provides a function to determine if all monsters are at least a minimum
distance apart from each other. If not, it returns the smallest distance found
between any two monsters.

Example:
    >>> min_monster_distance([3, 8, 10, 15], 6)
    2
    >>> min_monster_distance([5, 9, 14, 18], 4)
    -1
"""


def min_monster_distance(monsters: list[int], d: int) -> int:
    """
    Determine if all monsters are at least d units apart.

    If all monsters are safely spaced (at least d units apart), return -1.
    Otherwise, return the smallest distance found between any two monsters.

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the sorted list

    Args:
        monsters: List of integers representing monster positions along a straight line
        d: Minimum safe distance required between any two monsters

    Returns:
        int: The smallest distance between any two monsters if they are not safely spaced,
             or -1 if all monsters are at least d units apart

    Raises:
        ValueError: If the list has fewer than 2 monsters
    """
    if len(monsters) < 2:
        raise ValueError("At least 2 monsters are required to calculate distances")

    # Sort the monster positions and calculate distances between adjacent pairs
    sorted_monsters = sorted(monsters)

    # Use zip to pair adjacent elements and calculate distances
    distances = [
        next_pos - curr_pos
        for curr_pos, next_pos in zip(
            sorted_monsters, sorted_monsters[1:], strict=False
        )
    ]

    # Find the minimum distance
    min_distance = min(distances)

    # Return -1 if all monsters are safely spaced, otherwise return the minimum distance
    return -1 if min_distance >= d else min_distance


def run_tests() -> None:
    """Run test cases for the monster distance function."""
    test_cases = [
        # (monsters, d, expected_result)
        ([3, 8, 10, 15], 6, 2),
        ([5, 9, 14, 18], 4, -1),
        ([1, 3, 5, 7], 2, -1),
        ([1, 2, 3, 4], 2, 1),
        ([10, 20, 30, 40], 15, 10),
        ([1, 5, 9, 13], 3, -1),
        ([2, 4, 6, 8], 1, -1),
        ([1, 1, 1, 1], 1, 0),  # Edge case: monsters at same position
        ([1, 10, 100, 1000], 50, 9),
    ]

    print("Testing monster distance function:")
    for monsters, d, expected in test_cases:
        result = min_monster_distance(monsters, d)
        assert result == expected, (
            f"Expected {expected}, but got {result} "
            f"for monsters {monsters} with d={d}"
        )
        print(f"Monsters: {monsters}, d={d} -> {result}")

    # Test edge cases
    try:
        min_monster_distance([1], 5)
        raise AssertionError("Should raise ValueError for single monster")
    except ValueError:
        print("✓ Correctly raised ValueError for single monster")

    try:
        min_monster_distance([], 5)
        raise AssertionError("Should raise ValueError for empty list")
    except ValueError:
        print("✓ Correctly raised ValueError for empty list")

    print("\nAll tests passed!")


def main() -> None:
    """Main function to demonstrate usage."""
    # Example from the problem description
    monsters1 = [3, 8, 10, 15]
    d1 = 6
    result1 = min_monster_distance(monsters1, d1)
    print(f"Example 1: Monsters at positions {monsters1}, minimum distance {d1}")
    print(f"Result: {result1}")

    monsters2 = [5, 9, 14, 18]
    d2 = 4
    result2 = min_monster_distance(monsters2, d2)
    print(f"\nExample 2: Monsters at positions {monsters2}, minimum distance {d2}")
    print(f"Result: {result2}")


if __name__ == "__main__":
    # Uncomment to run demonstration examples
    # main()
    run_tests()

```