# 20240826-equal_letters_digits-gist

**Gist file**: [https://gist.github.com/rjvitorino/6b1a96d6c1f157627108b72b9aef85eb](https://gist.github.com/rjvitorino/6b1a96d6c1f157627108b72b9aef85eb)

**Description**: Cassidy's interview question of the week: a function that finds the longest substring in the input string `s` where the number of distinct letters equals the number of distinct digits

## equal_letters_digits.py

```Python
from typing import Set


def equal_letters_digits(s: str) -> str:
    """
    Finds the longest substring in the input string `s` where the number of distinct letters equals the number of distinct digits.
    If there are multiple substrings with the same length, return the one that appears first.

    :param s: The input string containing letters and digits.
    :return: The longest valid substring according to the conditions, or an empty string if no such substring exists.
    """
    longest_substring = ""
    max_length = 0

    # Iterate over all possible starting points for substrings
    for start_index in range(len(s)):
        letters: Set[str] = set()
        digits: Set[str] = set()

        # Expand the window from the start_index to find valid substrings
        for end_index in range(start_index, len(s)):
            current_char = s[end_index]

            # Assign the target set based on whether current_char is a letter or digit
            target_set = letters if current_char.isalpha() else digits

            # Stop checking when a repeated character is found (invalid substring)
            if current_char in target_set:
                break
            target_set.add(current_char)

            # Check if the current longest substring is valid (even length + equal letters and digits)
            current_length = end_index - start_index + 1
            if (
                current_length % 2 == 0
                and len(letters) == len(digits)
                and current_length > max_length
            ):
                max_length = current_length
                longest_substring = s[start_index : end_index + 1]

    # print(f"Longest for {s} is {longest_substring}")
    return longest_substring


assert equal_letters_digits("abc12345") == "abc123"
assert equal_letters_digits("a123b4c") == "3b4c"
assert equal_letters_digits("a12bc34") == "a12bc3"
assert equal_letters_digits("123abc456def789ghi") == "123abc456def789ghi"
assert equal_letters_digits("a1b2c3d4") == "a1b2c3d4"
assert equal_letters_digits("abc") == ""
assert equal_letters_digits("1234") == ""
assert equal_letters_digits("aa12") == "a1"
assert equal_letters_digits("ab11cc22") == "b1"
assert equal_letters_digits("123abcc456def789ghi") == "c456def789gh"
assert equal_letters_digits("a1b2c3d4e5f6g7h8i9") == "a1b2c3d4e5f6g7h8i9"
assert equal_letters_digits("ab123ba45678cd9") == "ab12"
assert equal_letters_digits("123a1b2c456d789e") == "3a1b2c"
assert equal_letters_digits("a1b2c3d4e5f6g7h8i9j0a1b2c3") == "a1b2c3d4e5f6g7h8i9j0"
assert equal_letters_digits("12ab34cd56ef78gh90ij12kl34") == "12ab34cd56ef78gh90ij"
assert equal_letters_digits("a1b1c2d2") == "b1c2"
assert equal_letters_digits("abc1def2ghi3jkl4mnop5qrst6uvwxyz7890") == "wxyz7890"

print("All tests passed!")

```