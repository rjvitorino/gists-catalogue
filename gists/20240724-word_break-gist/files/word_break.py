import logging
from typing import List
from typing import Set
from typing import Tuple

# Configure logging, change level to DEBUG to trace all checks
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determine if a given string can be segmented into the sequence of words from the given word list.

    :param s: The string to be segmented.
    :param word_dict: A list of words to be used for segmentation.
    :return: True if the string can be segmented using all the words from the list, False otherwise.
    """
    word_dict.sort(key=len, reverse=True)  # Sort words by length in descending order
    stack = [
        (s, word_dict)
    ]  # Use a stack to keep track of the string `s` and `word_dict` while we try to remove its words from `s`

    logging.info(
        f" >>> WORD BREAK: Checking if '{s}' contains all of the following words: {word_dict}"
    )

    def remove_word_from_string(s: str, word: str) -> str:
        """Removes the first occurrence of word from s."""
        index = s.find(word)
        return s[:index] + s[index + len(word) :]

    def get_new_state(
        current_string: str, word: str, remaining_words: Set[str]
    ) -> Tuple[str, Set[str]]:
        """Generates the new state after removing the word from the current string."""
        new_string = remove_word_from_string(current_string, word)
        new_remaining_words = remaining_words.copy()
        new_remaining_words.remove(word)
        return new_string, new_remaining_words

    while stack:
        # Pop the current state from the stack
        current_string, remaining_words = stack.pop()

        logging.debug(
            f" Current state: string='{current_string}', remaining_words={remaining_words}"
        )

        # If the current string is empty, check remaining words
        if not current_string:
            logging.debug(
                " All words used and string is empty. Returning True."
                if not remaining_words
                else " String is empty but there are still remaining words. Returning False."
            )
            return not remaining_words

        # If there are no remaining words but the string is not empty
        if not remaining_words:
            logging.debug(
                " No remaining words to use, and string is not empty. Returning True."
            )
            return True

        # Try to find each word in the current string and generate new states
        for word in remaining_words:
            if word in current_string:
                # Removes a string from `remaining_words` and updates `current_string` if it contains the string
                new_string, new_remaining_words = get_new_state(
                    current_string, word, remaining_words
                )
                logging.debug(
                    f" Found '{word}' in '{current_string}'! Resuming with '{new_string}' and remaining_words={new_remaining_words}"
                )
                stack.append((new_string, new_remaining_words))

    logging.debug(" No valid segmentation found. Returning False.")
    return False


assert word_break("leetcode", ["leet", "code"]) is True, "Test case 1 failed"
assert (
    word_break("catsandog", ["cat", "cats", "and", "sand", "dog"]) is False
), "Test case 2 failed"
assert word_break("aaaaaa", ["aa", "aaa"]) is True, "Test case 3 failed"
assert word_break("aaabaa", ["aa", "aaa"]) is True, "Test case 4 failed"
assert word_break("aaaaa", ["aaa", "aaa"]) is False, "Test case 5 failed"
assert word_break("applepenapple", ["apple", "pen"]) is True, "Test case 6 failed"
assert (
    word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    is False
), "Test case 7 failed"
assert (
    word_break("pineapplepenapple", ["apple", "pen", "pine", "apple"]) is True
), "Test case 8 failed"
assert (
    word_break("catsandogcat", ["cats", "dog", "sand", "and", "cat"]) is False
), "Test case 9 failed"
assert word_break("carscars", ["car", "ca", "rs"]) is True, "Test case 10 failed"
assert (
    word_break("thedogbarked", ["dog", "barked", "the"]) is True
), "Test case 11 failed"
assert (
    word_break("thedogbark", ["the", "dog", "barked"]) is False
), "Test case 12 failed"
logging.info(" All test cases passed!")
