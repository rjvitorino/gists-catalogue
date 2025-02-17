# 20250217-find_shield_break-gist

**Gist file**: [https://gist.github.com/rjvitorino/7ed18298913c4bd9617ec3a86b7f87d3](https://gist.github.com/rjvitorino/7ed18298913c4bd9617ec3a86b7f87d3)

**Description**: Cassidy's interview question of the week: a function that, given an array of attack damages and a shield capacity for a spaceship, returns the index when cumulative damage exceeds the shield 

## find_shield_break.py

```Python
from typing import List
from itertools import accumulate


def find_shield_break(shield_attacks: List[int], shield_capacity: int) -> int:
    """Finds the index where cumulative damage exceeds shield capacity.

    Uses itertools.accumulate for efficient cumulative sum calculation.
    Short-circuits when shield break is detected.

    Args:
        shield_attacks: List of integer damage values for each attack
        shield_capacity: Maximum damage the shield can absorb

    Returns:
        int: Index where shield breaks, or -1 if shield survives all attacks
    """
    # Use generator expression with accumulate for memory efficiency
    for index, total_damage in enumerate(accumulate(shield_attacks)):
        if total_damage > shield_capacity:
            return index
    return -1


def run_tests() -> None:
    """Runs test cases to verify shield break functionality."""
    # Basic scenarios
    assert find_shield_break([10, 20, 30, 40], 50) == 2, "Basic case failed"
    assert find_shield_break([1, 2, 3, 4], 20) == -1, "Shield survival failed"
    assert find_shield_break([50], 30) == 0, "Single attack failed"

    # Edge cases
    assert find_shield_break([], 10) == -1, "Empty list failed"
    assert find_shield_break([0, 0, 0], 1) == -1, "Zero damage failed"

    # Boundary conditions
    assert find_shield_break([5, 5, 5], 15) == -1, "Exact capacity failed"
    assert find_shield_break([5, 5, 5], 14) == 2, "Break at last attack failed"
    assert find_shield_break([100, 200, 300], 0) == 0, "Zero capacity failed"

    # Special scenarios
    assert find_shield_break([1, 1, 1000, 1], 900) == 2, "Spike damage failed"
    assert find_shield_break([2, 3, 4, 5], 1) == 0, "First attack break failed"

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()

```