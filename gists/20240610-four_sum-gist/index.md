# 20240610-four_sum-gist

**Gist file**: [https://gist.github.com/rjvitorino/4ecfa7d0c4d6ee037811958deb462e19](https://gist.github.com/rjvitorino/4ecfa7d0c4d6ee037811958deb462e19)

**Description**: Cassidoo's interview question of the week: a function that takes an array of integers and a target sum, and returns all unique quadruplets [a, b, c, d] in the array such that a + b + c + d = target

## four_sum.py

```Python
from itertools import combinations
from typing import List

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Finds all unique quadruplets in the list that sum up to the target value.

    Args:
    nums (List[int]): The list of integers.
    target (int): The target sum for the quadruplets.

    Returns:
    List[List[int]]: A list of all unique quadruplets that sum up to the target.
    """
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements of the input list must be integers.")
    
    nums.sort()
    quadruplets = set()  # Store the unique quadruplets

    # Generates all unique quadruplets and filters the ones that sum to target
    for quad in combinations(nums, 4):
        if sum(quad) == target:
            quadruplets.add(quad)
    
    # Converts set of tuples back to list of lists
    return [list(quad) for quad in quadruplets]

if __name__ == "__main__":
    assert set(map(tuple, four_sum([1, 0, -1, 0, -2, 2], 0))) == {(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)}
    print(four_sum([1, 0, -1, 0, -2, 2], 0))            # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert set(map(tuple, four_sum([], 0))) == set()
    print(four_sum([], 0))                              # []
    assert set(map(tuple, four_sum([1, -2, -5, -4, -3, 3, 3, 5], -11))) == {(-5, -4, -3, 1)}
    print(four_sum([1, -2, -5, -4, -3, 3, 3, 5], -11))  # [[-5, -4, -3, 1]]
    
    try:
        four_sum([1, 0, 'a', 0, -2, 2], 0)
    except ValueError as error:
        print(error)

    try:
        four_sum([1, 2, 3.5, 4], 10)
    except ValueError as error:
        print(error)

    print("All tests passed.")

```