from typing import List
from typing import Tuple


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Calculates, for each day, the number of days expected until a warmer temperature.
    If there is no future day for which a temperature is warmer, a 0 is returned.

    :param temperatures: List of daily temperatures.
    :return: List where each element is the number of days to wait for a warmer temperature.
    """
    # Ensure all elements in the list are integers to prevent type errors during computation
    if not all(isinstance(temperature, int) for temperature in temperatures):
        raise ValueError("All elements in the temperatures list must be integers")

    num_days: int = len(temperatures)
    days_until_warmer: List[int] = [
        0
    ] * num_days  # Initialize the result list with zeros
    stack: List[
        int
    ] = []  # Stores indices of temperatures that are waiting for a warmer day

    for current_day in range(num_days):
        # Compare the current day's temperature with the temperatures of the days stored (stack)
        # The stack keeps track of indices of days with unresolved warmer temperatures
        while stack and temperatures[current_day] > temperatures[stack[-1]]:
            previous_day: int = stack.pop()  # Pop the index from the stack
            # Calculate the number of days until a warmer temperature
            days_until_warmer[previous_day] = current_day - previous_day
        # Push the current day's index onto the stack to wait for a future warmer temperature
        stack.append(current_day)

    return days_until_warmer


def test_daily_temperatures() -> None:
    """
    Tests the daily_temperatures function with various test cases.

    :param None: No parameters
    :return: None
    """
    test_cases: List[Tuple[List[int], List[int]]] = [
        # All temperatures are the same
        ([50, 50, 50, 50], [0, 0, 0, 0]),
        # Strictly decreasing temperatures
        ([80, 70, 60, 50], [0, 0, 0, 0]),
        # Strictly increasing temperatures
        ([50, 60, 70, 80], [1, 1, 1, 0]),
        # Mixed temperatures with some fluctuations
        ([70, 72, 68, 76, 73, 71, 75, 74], [1, 2, 1, 0, 2, 1, 0, 0]),
        # Single temperature
        ([60], [0]),
        # Two temperatures, with increasing and decreasing scenarios
        ([60, 70], [1, 0]),
        ([70, 60], [0, 0]),
        # Large input to test performance
        ([i for i in range(100, 0, -1)], [0] * 100),
        # Randomised temperatures
        ([55, 50, 60, 58, 62, 53, 64, 49], [2, 1, 2, 1, 2, 1, 0, 0]),
        # Alternating temperatures
        ([60, 70, 60, 70, 60, 70], [1, 0, 1, 0, 1, 0]),
        # Temperatures with a plateau
        ([65, 65, 65, 70], [3, 2, 1, 0]),
        # Empty list
        ([], []),
    ]

    for index, (input, expected) in enumerate(test_cases):
        result: List[int] = daily_temperatures(input)
        assert (
            result == expected
        ), f"Test case {index + 1} failed: expected {expected}, got {result}"
        print(f"Test case {index + 1} passed!")


if __name__ == "__main__":
    # Input from Cassidy
    print(daily_temperatures([70, 70, 70, 75]))  # [3, 2, 1, 0]
    print(daily_temperatures([90, 80, 70, 60]))  # [0, 0, 0, 0]
    print(
        daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    )  # [1, 1, 4, 2, 1, 1, 0, 0]
    # Test other scenarios
    test_daily_temperatures()
