# 20241224-factorial_trailing_zeros-gist

**Gist file**: [https://gist.github.com/rjvitorino/e9fef45c6cd126d3f72191af9d94bdcc](https://gist.github.com/rjvitorino/e9fef45c6cd126d3f72191af9d94bdcc)

**Description**: Cassidy's interview question of the week: a function to determine how many trailing zeros are in n!.

## factorial_trailing_zeros.py

```Python
def count_trailing_zeros_in_factorial(n: int) -> int:
    """
    Calculate the number of trailing zeros in n! to determine how many perfectly round cookies are made.

    Args:
        n (int): The input number for which to calculate n! and count trailing zeros.

    Returns:
        int: The count of trailing zeros in n!.

    Logic:
        - Trailing zeros in n! are caused by factors of 10, which are the result of multiplying 2 and 5.
        - Since there are always more factors of 2 than factors of 5 in a factorial, the count of trailing zeros is determined by the number of factors of 5.
        - To count factors of 5 in n!, repeatedly divide n by increasing powers of 5 and sum the results until the division result is zero.
    """
    count = 0
    power_of_five = 5
    while n >= power_of_five:
        count += n // power_of_five
        power_of_five *= 5
    return count


assert count_trailing_zeros_in_factorial(5) == 1
# 5! = 120, which has 1 trailing zero
assert (
    count_trailing_zeros_in_factorial(10) == 2
)  # 10! = 3628800, which has 2 trailing zeros
assert (
    count_trailing_zeros_in_factorial(20) == 4
)  # 20! = 2432902008176640000, which has 4 trailing zeros
assert count_trailing_zeros_in_factorial(50) == 12
# 50! has 12 trailing zeros
assert count_trailing_zeros_in_factorial(100) == 24
# 100! has 24 trailing zeros
print("All tests passed!")

```