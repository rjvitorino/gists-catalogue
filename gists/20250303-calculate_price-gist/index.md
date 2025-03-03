# 20250303-calculate_price-gist

**Gist file**: [https://gist.github.com/rjvitorino/4691fe6660df9a90053c619a95ad4ab5](https://gist.github.com/rjvitorino/4691fe6660df9a90053c619a95ad4ab5)

**Description**: Cassidy's interview question of the week: a function that, given a store's closing date, a visit date, and the original price of a product, calculates the discounted price based on a 10% weekly reduction until the store closes. If the visit date is after the closing date, the price remains unchanged.

## calculate_price.py

```Python
"""
A store is going out of business and will reduce the price of all products by 10% every week leading up to the closing date.
Given the closing_date, visit_date, and the original_price of a product, this function returns the price of the product on the visit_date.
The function assumes that original_price is a positive number.

Examples:
    >>> calculate_price('2025-04-01', '2025-03-03', 100)  # 4 weeks of discounts
    65.61
    >>> calculate_price('2025-04-01', '2025-03-15', 50)   # 2 weeks of discounts
    40.5
    >>> calculate_price('2025-04-01', '2025-04-15', 75)   # No discount (visit after closing)
    75.0
"""

from datetime import datetime


def calculate_price(closing_date: str, visit_date: str, original_price: int) -> int:
    """
    Calculate the price of a product on a given visit date, considering a 10% discount every week leading up to the closing date.

    Args:
        closing_date (str): The date of the store's closing in YYYY-MM-DD format
        visit_date (str): The date of the visit in YYYY-MM-DD format
        original_price (int): The original price of the product

    Returns:
        int: The price of the product on the visit date
    """
    # Parse the dates
    closing_date, visit_date = (
        datetime.strptime(date, "%Y-%m-%d") for date in (closing_date, visit_date)
    )

    # Calculate the number of weeks between the closing date and the visit date
    weeks_between = max(0, (closing_date - visit_date).days // 7)

    # Apply compound discounting: multiply price by 0.9 (90%) for each week
    # Example: For $100, after 2 weeks: 100 * 0.9^2 = $81.00
    # Round to 2 decimal places for cents
    price = original_price * (1 - 0.1) ** weeks_between
    rounded_price = round(price, 2)
    return int(rounded_price) if rounded_price.is_integer() else rounded_price


if __name__ == "__main__":
    # Test cases from examples
    assert calculate_price("2025-04-01", "2025-03-03", 100) == 65.61
    assert calculate_price("2025-04-01", "2025-03-15", 50) == 40.5
    assert calculate_price("2025-04-01", "2025-04-15", 75) == 75

    # Test cases for edge cases
    assert (
        calculate_price("2025-04-01", "2025-04-01", 100) == 100
    )  # Visit on closing day
    assert calculate_price("2025-04-01", "2025-03-25", 100) == 90  # One week discount
    assert calculate_price("2025-04-01", "2025-02-01", 100) == 43.05  # 8 weeks discount

    # Test cases with different price points
    assert calculate_price("2025-04-01", "2025-03-18", 25) == 20.25  # Small amount
    assert calculate_price("2025-04-01", "2025-03-18", 999) == 809.19  # Large amount

    print("All tests passed!")

```