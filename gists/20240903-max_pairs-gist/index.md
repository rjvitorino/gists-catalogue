# 20240903-max_pairs-gist

**Gist file**: [https://gist.github.com/rjvitorino/0918db0cd3a3e19ba964f35a0157b339](https://gist.github.com/rjvitorino/0918db0cd3a3e19ba964f35a0157b339)

**Description**: Cassidy's interview question of the week: a function to calculate the maximum number of matching shoe pairs in an array of strings

## max_pairs.py

```Python
from collections import defaultdict
from typing import List


def max_pairs(shoes: List[str]) -> int:
    """
    Calculate the maximum number of matching pairs of shoes that can be formed.

    :param shoes: A list of strings where each string represents a shoe with
                  its type ('L' for left or 'R' for right) and its size.
    :return: The maximum number of matching pairs of shoes.
    """

    # Dictionary to count the number of left and right shoes for each size
    shoe_count = defaultdict(lambda: {"L": 0, "R": 0})

    # Iterate the list of shoes (side+size) and increment the corresponding count
    for side, size in (shoe.split("-") for shoe in shoes):
        shoe_count[size][side] += 1

    # Sum the minimum of left and right shoe counts for each size, as the maximum
    # number of pairs for each size is determined by the lesser of the two counts.
    pairs = sum(min(sides["L"], sides["R"]) for sides in shoe_count.values())

    return pairs


# Example 1: Three pairs can be formed: 2 from size 10, 1 from size 11
assert max_pairs(["L-10", "R-10", "L-11", "R-10", "L-10", "R-11"]) == 3

# Example 2: No pairs can be formed as there are only left shoes
assert max_pairs(["L-10", "L-11", "L-12", "L-13"]) == 0

# Example 3: Only one pair can be formed from size 8
assert max_pairs(["L-8", "L-8", "L-8", "R-8"]) == 1

# Example 4: All shoes have matching pairs
assert max_pairs(["L-9", "R-9", "L-10", "R-10"]) == 2

# Example 5: Shoes of multiple sizes with different counts
assert max_pairs(["L-7", "R-7", "L-7", "R-7", "L-8", "R-8", "L-8"]) == 3

# Example 6: All shoes are right, so no pairs can be formed
assert max_pairs(["R-9", "R-9", "R-10", "R-10"]) == 0

# Example 7: Multiple pairs for a single size
assert max_pairs(["L-11", "R-11", "L-11", "R-11", "L-11", "R-11"]) == 3

print("All tests passed!")

```