# 20241104-group_anagram-gist

**Gist file**: [https://gist.github.com/rjvitorino/4e0b1a3d7c6689228aa9f660bce92548](https://gist.github.com/rjvitorino/4e0b1a3d7c6689228aa9f660bce92548)

**Description**: Cassidoo's interview question of the week: a function that given an array of strings, groups the anagrams together.

## group_anagram.py

```Python
from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    """Groups an array of strings into lists of anagrams.

    Args:
        words (List[str]): List of words to group by anagrams.

    Returns:
        List[List[str]]: A list of lists, where each sublist contains words that are anagrams of each other.
    """
    # anagrams is a dictionary that groups words by their sorted character tuple.
    # Each key is a tuple representing a sorted version of the word's characters.
    # The value is a list of words that match that character pattern.
    anagrams: defaultdict[tuple[str, ...], List[str]] = defaultdict(list)

    # Example: For "eat", "tea", and "ate", the key will be ('a', 'e', 't'),
    # and all these words will be added to the list in anagrams[('a', 'e', 't')].

    for word in words:
        # Create a key by sorting the characters of the word and converting to a tuple.
        # This ensures that anagrams will have the same key.
        key = tuple(sorted(word))
        # Append the word to the list corresponding to the sorted key.
        anagrams[key].append(word)

    # Convert the dictionary values to a list of lists for the final output.
    return list(anagrams.values())


if __name__ == "__main__":
    # Example 1: Basic grouping of anagrams
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 2: No anagrams present
    result = group_anagrams(["vote", "please"])
    expected = [["vote"], ["please"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 3: Words that are anagrams of each other
    result = group_anagrams(["debitcard", "badcredit"])
    expected = [["debitcard", "badcredit"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 4: All words are anagrams
    result = group_anagrams(["abc", "bca", "cab", "cba", "bac"])
    expected = [["abc", "bca", "cab", "cba", "bac"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 5: Mixed letters with spaces
    result = group_anagrams(["a cat", "act a", "cat a", "tac a"])
    expected = [["a cat", "act a", "cat a", "tac a"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 6: Case sensitivity
    result = group_anagrams(["Listen", "Silent", "enlist", "inlets", "tinsel", "hello"])
    expected = [["Listen"], ["Silent"], ["enlist", "inlets", "tinsel"], ["hello"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 7: Anagrams with different lengths
    result = group_anagrams(["an", "na", "and", "dan", "dana"])
    expected = [["an", "na"], ["and", "dan"], ["dana"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    # Example 8: Longer words and numbers
    result = group_anagrams(["123", "231", "321", "abc", "acb", "bac", "1234"])
    expected = [["123", "231", "321"], ["abc", "acb", "bac"], ["1234"]]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

    print("All tests passed!")

```