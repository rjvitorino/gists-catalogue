# 20250127-find_anagrams-gist

**Gist file**: [https://gist.github.com/rjvitorino/c955b15cd54b474f9737605746deccdd](https://gist.github.com/rjvitorino/c955b15cd54b474f9737605746deccdd)

**Description**: Cassidoo's interview question of the week: given two strings, s and p, return an array of all the start indices of p's anagrams in s.

## find_anagrams.py

```Python
"""
String Anagrams Finder

This module provides two different implementations for finding anagrams of a pattern
string within a larger text string. It includes both a sliding window approach (efficient)
and a permutation-based approach (for educational purposes).

Example:
    >>> find_anagrams_sliding_window("cbaebabacd", "abc")
    [0, 6]
"""

from typing import List
from collections import Counter
from itertools import permutations


def find_anagrams_permutation(s: str, p: str) -> List[int]:
    """
    Find anagrams using permutation approach, a brute force approach
    which is not efficient for large strings.

    Time Complexity: O(n * k!) where k is length of p
    Space Complexity: O(k!) where k is length of p

    Args:
        s: The string to search for anagrams in.
        p: The string to find anagrams of.

    Returns:
        List[int]: List of starting indices of anagrams of p in s.
    """
    if len(p) > len(s):
        return []

    # Generate all unique permutations of p based on a previous exercise
    # (taken from https://github.com/rjvitorino/gists-catalogue/blob/main/gists/20250106-permute-gist/index.md)
    perms = set("".join(perm) for perm in permutations(p))

    # Find all starting indices where a substring matches any permutation
    result = [
        start_index
        for start_index in range(len(s) - len(p) + 1)
        if s[start_index : start_index + len(p)] in perms
    ]

    return sorted(result)


def find_anagrams_sliding_window(s: str, p: str) -> List[int]:
    """
    Find anagrams using a sliding window approach.

    Time Complexity: O(n) where n is length of s
    Space Complexity: O(k) where k is size of character set

    Args:
        s: The string to search for anagrams in.
        p: The string to find anagrams of.

    Returns:
        List[int]: List of starting indices of anagrams of p in s.
    """
    if len(p) > len(s):
        return []

    # Create a frequency map of characters in the pattern
    # Counter({'a': 1, 'b': 1, 'c': 1}) for pattern "abc"
    # This allows us to efficiently check if two strings are anagrams
    # by comparing their character frequencies instead of sorting
    pattern_frequencies = Counter(p)
    result = []

    # Start window with first len(p) characters
    window = Counter(s[: len(p)])
    if window == pattern_frequencies:
        result.append(0)

    # Slide window through the string, updating character frequencies:
    # - Remove leftmost char of previous window
    # - Add rightmost char of new window
    # - Check if new window matches pattern
    for i in range(len(s) - len(p)):
        left_char = s[i]
        right_char = s[i + len(p)]

        # Remove left character from window
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]

        # Add right character to window
        window[right_char] += 1

        if window == pattern_frequencies:
            result.append(i + 1)

    return result


def run_tests() -> None:
    """Run test cases for both anagram finding implementations."""
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("fish", "cake", []),
        ("abab", "ab", [0, 1, 2]),
    ]

    # Test sliding window implementation
    print("Testing sliding window implementation:")
    for text, pattern, expected in test_cases:
        result = find_anagrams_sliding_window(text, pattern)
        assert (
            result == expected
        ), f"Expected {expected}, but got {result} for input '{text}', '{pattern}'"
        print(f"Found anagrams of '{pattern}' in '{text}' at indices: {result}")

    # Test permutation implementation
    print("\nTesting permutation implementation:")
    for text, pattern, expected in test_cases:
        result = find_anagrams_permutation(text, pattern)
        assert (
            result == expected
        ), f"Expected {expected}, but got {result} for input '{text}', '{pattern}'"
        print(f"Found anagrams of '{pattern}' in '{text}' at indices: {result}")

    print("\nAll checks passed!")


def main() -> None:
    """Main function to demonstrate usage."""
    example_text = "cbaebabacd"
    example_pattern = "abc"
    result = find_anagrams_sliding_window(example_text, example_pattern)
    print(f"Example: Finding anagrams of '{example_pattern}' in '{example_text}'")
    print(f"Result: {result}")


if __name__ == "__main__":
    # Uncomment to run demonstration example
    # main()
    run_tests()

```