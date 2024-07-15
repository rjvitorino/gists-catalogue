from typing import List


def increasing_subsequence(nums: List[int], allow_non_consecutive: bool = True) -> int:
    """
    Given an integer array nums, return the length of the longest increasing subsequence.

    Args:
    nums (List[int]): The input list of integers.
    allow_non_consecutive (bool): If True, allows non-consecutive subsequences;
                                  if False, only considers consecutive subsequences.

    Returns:
    int: The length of the longest increasing subsequence.
    """
    # Assert that all elements in nums are integers
    assert all(
        isinstance(num, int) for num in nums
    ), "All elements in nums must be integers"

    # If the list is empty, the longest increasing subsequence is 0
    if not nums:
        return 0

    if allow_non_consecutive is True:
        # Initialise an array `lengths` where each index represents the length of the
        # longest increasing subsequence ending at that index
        lengths = [1] * len(nums)

        # Loop through the list and update the lengths array
        for current_index, current_value in enumerate(nums):
            for previous_index in range(current_index):
                previous_value = nums[previous_index]
                if current_value > previous_value:
                    lengths[current_index] = max(
                        lengths[current_index], lengths[previous_index] + 1
                    )

        # The length of the longest increasing subsequence is the maximum value in lengths
        return max(lengths)
    else:
        # Find the longest increasing subsequence where elements are consecutive
        max_length = 1
        current_length = 1
        previous_value = nums[0]

        for current_value in nums[1:]:
            if current_value > previous_value:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1
            previous_value = current_value

        return max_length


# Non-consecutive examples
assert increasing_subsequence([10, 9, 2, 3, 7, 101, 18]) == 4
assert increasing_subsequence([4, 4, 4, 4, 3]) == 1
assert increasing_subsequence([1, 2, 3, 4, 5]) == 5
assert increasing_subsequence([5, 4, 3, 2, 1]) == 1
assert increasing_subsequence([2, 2, 2, 2, 2]) == 1
assert increasing_subsequence([10, 20, 10, 30, 20, 50]) == 4
assert increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6  # fmt: off

# Consecutive only examples
assert increasing_subsequence([10, 9, 2, 3, 7, 101, 18], allow_non_consecutive=False) == 4  # fmt: off
assert increasing_subsequence([4, 4, 4, 4, 3], allow_non_consecutive=False) == 1
assert increasing_subsequence([1, 2, 3, 4, 5], allow_non_consecutive=False) == 5
assert increasing_subsequence([5, 4, 3, 2, 1], allow_non_consecutive=False) == 1
assert increasing_subsequence([2, 2, 2, 2, 2], allow_non_consecutive=False) == 1
assert increasing_subsequence([10, 20, 10, 30, 20, 50], allow_non_consecutive=False) == 2  # fmt: off
assert increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], allow_non_consecutive=False) == 2  # fmt: off
