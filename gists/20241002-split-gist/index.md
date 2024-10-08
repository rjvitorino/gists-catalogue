# 20241002-split-gist

**Gist file**: [https://gist.github.com/rjvitorino/a33cfae8897f666f34e23900dea6c8e8](https://gist.github.com/rjvitorino/a33cfae8897f666f34e23900dea6c8e8)

**Description**: Cassidy's interview question of the week: implementation of String split() function in my preferred programming language (Python)

## split.py

```Python
from typing import List, Optional


class StringSplitter:
    @staticmethod
    def split(string: str, delimiter: Optional[str] = None) -> List[str]:
        """
        Splits the input string by the specified delimiter.

        Args:
            string (str): The string to split.
            delimiter (Optional[str]): The character to split the string on.
                                       If None, splits by each character.

        Returns:
            List[str]: A list of substrings from the original string.
        """
        # Handle the case where delimiter is None (split by character)
        if delimiter is None or delimiter == "":
            return list(string)

        # Lists are more efficient than string concatenation
        result: List[str] = []
        current_word: List[str] = []

        for char in string:
            if char == delimiter:
                result.append("".join(current_word))
                current_word = []  # Reset the list for the next word
            else:
                current_word.append(char)

        # Append the last word after the loop ends
        result.append("".join(current_word))

        return result


splitter = StringSplitter()

# Regular case, split by space
assert splitter.split("This is so, so silly!", " ") == [
    "This",
    "is",
    "so,",
    "so",
    "silly!",
]

# Split by character (None)
assert splitter.split("This is so, so silly!") == [
    "T",
    "h",
    "i",
    "s",
    " ",
    "i",
    "s",
    " ",
    "s",
    "o",
    ",",
    " ",
    "s",
    "o",
    " ",
    "s",
    "i",
    "l",
    "l",
    "y",
    "!",
]

# Split by comma
assert splitter.split("This is so, so silly!", ",") == ["This is so", " so silly!"]

# Split with multiple spaces
assert splitter.split("This  has  multiple  spaces", " ") == [
    "This",
    "",
    "has",
    "",
    "multiple",
    "",
    "spaces",
]

# Split with delimiter at the beginning
assert splitter.split("  leading spaces", " ") == ["", "", "leading", "spaces"]

# Split with delimiter at the end
assert splitter.split("trailing spaces  ", " ") == ["trailing", "spaces", "", ""]

# Empty string case
assert splitter.split("", " ") == [""]

# Delimiter not found
assert splitter.split("no commas here", ",") == ["no commas here"]

# Single character string
assert splitter.split("A", " ") == ["A"]

print("All tests passed!")

```