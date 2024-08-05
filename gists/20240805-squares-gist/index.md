# 20240805-squares-gist

**Gist file**: [https://gist.github.com/rjvitorino/f0449b96f89b897701b12c78b5fb37fd](https://gist.github.com/rjvitorino/f0449b96f89b897701b12c78b5fb37fd)

**Description**: Cassidoo's interview question of the week: a function that should take one argument n, a positive integer, and return the sum of all squared positive integers between 1 and n, inclusive.

## squares.py

```Python
from typing import Union


def squares(n: int) -> Union[int, None]:
    """
    Calculate the sum of all squared positive integers from 1 to n, inclusive.

    Args:
        n (int): A positive integer.

    Returns:
        Union[int, None]: The sum of squares from 1 to n if n is positive; otherwise, None.
    """
    if n <= 0:
        return None
    return sum(number**2 for number in range(1, n + 1))


assert squares(5) == 55
assert squares(10) == 385
assert squares(25) == 5525
assert squares(100) == 338350
assert squares(1) == 1
assert squares(0) is None
assert squares(-5) is None
assert squares(50) == 42925
assert squares(15) == 1240

print("All assertions passed.")

```