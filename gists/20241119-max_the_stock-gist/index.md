# 20241119-max_the_stock-gist

**Gist file**: [https://gist.github.com/rjvitorino/d2f5f2ac53b3e86ab4883cbf8b2bec3e](https://gist.github.com/rjvitorino/d2f5f2ac53b3e86ab4883cbf8b2bec3e)

**Description**: Cassidy's interview question of the week: a function that determines the maximum profit one can achieve by buying and selling stock once, given an array of integers representing the stock prices of a company in chronological order

## max_the_stock.py

```Python
from typing import List


def max_the_stock(prices: List[int]) -> int:
    """
    Determine the maximum profit achievable by buying and selling a stock once.

    Args:
        prices (List[int]): A list of integers representing stock prices in chronological order.

    Returns:
        int: The maximum profit that can be achieved, or 0 if no profit is possible.
    """
    if not prices:
        # Edge case for empty lists
        return 0

    # Initialise min price to infinity and max profit to 0
    min_price = float("inf")
    max_profit = 0

    # Update the minimum price if the current price is lower and update the maximum profit
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == "__main__":
    # Example test cases
    assert max_the_stock([7, 1, 5, 3, 6, 4]) == 5  # Buy at 1, sell at 6
    assert max_the_stock([7, 6, 4, 3, 1]) == 0  # No profit possible

    # Additional cases
    assert max_the_stock([]) == 0  # Empty list
    assert max_the_stock([5]) == 0  # Single price, no transactions possible
    assert max_the_stock([5, 5, 5, 5]) == 0  # No price change, no profit possible
    assert max_the_stock([3, 2, 6, 1, 4]) == 4  # Buy at 2, sell at 6
    assert max_the_stock([1, 2, 3, 4, 5]) == 4  # Buy at 1, sell at 5
    assert max_the_stock([9, 11, 8, 5, 7, 10]) == 5  # Buy at 5, sell at 10

    print("All test cases passed!")

```