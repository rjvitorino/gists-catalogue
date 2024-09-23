# 20240923-min_laundry_loads-gist

**Gist file**: [https://gist.github.com/rjvitorino/252a95c3414fc9f740a649639760216e](https://gist.github.com/rjvitorino/252a95c3414fc9f740a649639760216e)

**Description**: Cassidy's interview question of the week: a function to sort laundry items into the minimum number of loads, where items of the same colour can be washed together, and some different fabric types cannot be mixed together

## min_laundry_loads.py

```Python
from collections import defaultdict
from typing import List, Tuple

# Define the type alias for better readability (colour and fabric tuple)
ClothingItem = Tuple[str, str]


def min_laundry_loads(items: List[ClothingItem]) -> int:
    """
    This function takes a list of clothing items, each represented by a tuple
    of (colour, fabric type), and returns the minimum number of loads required
    to wash them while following the fabric and colour sorting rules.

    Fabric rules:
    - "delicate" items cannot be washed with any other type, but can be grouped by colour.
    - "normal" and "heavy" items can be washed together if they are the same colour.

    Args:
        items (List[ClothingItem]): List of tuples where each tuple contains a colour and a fabric type.

    Returns:
        int: Minimum number of loads required.
    """
    # Group items by colour with a dictionary
    colour_groups: defaultdict[str, List[str]] = defaultdict(list)
    for colour, fabric in items:
        colour_groups[colour].append(fabric)

    return sum(
        # Add a load if there is any delicate fabric
        (1 if "delicate" in fabrics else 0)
        # Add a load if there are any non-delicate fabrics
        + (1 if any(fabric in {"normal", "heavy"} for fabric in fabrics) else 0)
        for fabrics in colour_groups.values()
    )


def test_min_laundry_loads():
    # Provided test cases
    load1: List[ClothingItem] = [
        ("red", "normal"),
        ("blue", "normal"),
        ("red", "delicate"),
        ("blue", "heavy"),
    ]
    assert min_laundry_loads(load1) == 3, "Test case 1 failed"

    load2: List[ClothingItem] = [
        ("white", "normal"),
        ("white", "delicate"),
        ("white", "normal"),
        ("white", "heavy"),
    ]
    assert min_laundry_loads(load2) == 2, "Test case 2 failed"

    # New test cases
    load3: List[ClothingItem] = [
        ("green", "normal"),
        ("green", "heavy"),
        ("green", "delicate"),
        ("yellow", "normal"),
    ]
    # One load for green normal and heavy, one for green delicate, one for yellow normal
    assert min_laundry_loads(load3) == 3, "Test case 3 failed"

    load4: List[ClothingItem] = [
        ("black", "delicate"),
        ("black", "delicate"),
        ("black", "normal"),
        ("black", "heavy"),
        ("black", "normal"),
    ]
    # One load for black delicate, one load for black normal and heavy
    assert min_laundry_loads(load4) == 2, "Test case 4 failed"

    load5: List[ClothingItem] = [
        ("blue", "normal"),
        ("blue", "heavy"),
        ("blue", "normal"),
        ("red", "delicate"),
        ("red", "delicate"),
    ]
    # One load for blue normal and heavy, one load for red delicate
    assert min_laundry_loads(load5) == 2, "Test case 5 failed"

    load6: List[ClothingItem] = [
        ("orange", "delicate"),
        ("orange", "delicate"),
        ("orange", "delicate"),
    ]
    # One load for all orange delicate items
    assert min_laundry_loads(load6) == 1, "Test case 6 failed"

    load7: List[ClothingItem] = [
        ("purple", "normal"),
        ("purple", "normal"),
        ("purple", "heavy"),
        ("green", "normal"),
        ("green", "heavy"),
    ]
    # One load for purple normal and heavy, one load for green normal and heavy
    assert min_laundry_loads(load7) == 2, "Test case 7 failed"

    load8: List[ClothingItem] = [
        ("red", "normal"),
        ("blue", "normal"),
        ("blue", "normal"),
        ("green", "normal"),
    ]
    # One load for red normal, one for blue normals, one for green normal
    assert min_laundry_loads(load8) == 3, "Test case 8 failed"


test_min_laundry_loads()
print("All test cases passed!")

```