# 20241008-missing_ingredients-gist

**Gist file**: [https://gist.github.com/rjvitorino/abbbe5be143b0196552d30dca895a4f5](https://gist.github.com/rjvitorino/abbbe5be143b0196552d30dca895a4f5)

**Description**: Cassidy's interview question of the week: a function that, given a list of ingredients needed for a recipe (represented as strings), and a list of ingredients available in the pantry, returns the minimum number of additional ingredients one needs to buy to make the recipe

## missing_ingredients.py

```Python
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


@dataclass
class Ingredient:
    """
    Class to represent an ingredient and its expiration date.

    Attributes:
        name (`str`): The name of the ingredient
        expiration_date (`str`): Expiration date in "YYYY-MM-DD" format
    """

    name: str
    expiration_date: str

    def is_expired(self) -> bool:
        """
        Check if the ingredient is expired.

        Returns:
            `bool`: True if the ingredient is expired, False otherwise.
        """
        expiration = datetime.strptime(self.expiration_date, "%Y-%m-%d")
        return expiration < datetime.now()


def missing_ingredients(recipe: List[str], pantry: List[Ingredient]) -> int:
    """
    Calculate the number of ingredients missing from the pantry to make a recipe.

    Args:
        recipe (`List[str]`): The list of ingredients needed for the recipe.
        pantry (`List[Ingredient]`): A list of Ingredient objects representing pantry items.

    Returns:
        `int`: The minimum number of additional ingredients needed to buy.
    """
    # Create a list of pantry items that are not expired
    valid_pantry_items = [
        ingredient.name for ingredient in pantry if not ingredient.is_expired()
    ]

    # Create counters for recipe and valid pantry items to account for quantities
    recipe_counter = Counter(recipe)
    pantry_counter = Counter(valid_pantry_items)

    # Calculate missing ingredients by comparing the counts in the recipe to the counts in the pantry
    missing_items = sum(
        max(needed_qty - pantry_counter.get(ingredient, 0), 0)
        for ingredient, needed_qty in recipe_counter.items()
    )

    return missing_items


def get_expiration_date(days_from_today: int) -> str:
    """
    Generate an expiration date string relative to today.

    Args:
        days_from_today (`int`): The number of days from today for the expiration date.

    Returns:
        `str`: Expiration date in 'YYYY-MM-DD' format.
    """
    return (datetime.today() + timedelta(days=days_from_today)).strftime("%Y-%m-%d")


def test_missing_ingredients():
    # Test 1: Basic test case, some items missing
    recipe_1 = ["eggs", "flour", "sugar", "butter"]
    pantry_1 = [
        Ingredient(name="sugar", expiration_date=get_expiration_date(60)),
        Ingredient(name="butter", expiration_date=get_expiration_date(30)),
        Ingredient(name="milk", expiration_date=get_expiration_date(-2)),
    ]
    assert missing_ingredients(recipe_1, pantry_1) == 2, "Test 1 Failed"

    # Test 2: All ingredients available, no missing items
    recipe_2 = ["eggs", "flour", "sugar"]
    pantry_2 = [
        Ingredient(name="eggs", expiration_date=get_expiration_date(10)),
        Ingredient(name="flour", expiration_date=get_expiration_date(20)),
        Ingredient(name="sugar", expiration_date=get_expiration_date(1)),
    ]
    assert missing_ingredients(recipe_2, pantry_2) == 0, "Test 2 Failed"

    # Test 3: All pantry items expired
    recipe_3 = ["eggs", "milk"]
    pantry_3 = [
        Ingredient(name="eggs", expiration_date=get_expiration_date(-10)),
        Ingredient(name="milk", expiration_date=get_expiration_date(-5)),
    ]
    assert missing_ingredients(recipe_3, pantry_3) == 2, "Test 3 Failed"

    # Test 4: Some items expired, some still valid
    recipe_4 = ["flour", "butter", "milk"]
    pantry_4 = [
        Ingredient(name="flour", expiration_date=get_expiration_date(150)),
        Ingredient(name="butter", expiration_date=get_expiration_date(20)),
        Ingredient(name="milk", expiration_date=get_expiration_date(-2)),
    ]
    assert missing_ingredients(recipe_4, pantry_4) == 1, "Test 4 Failed"

    # Test 5: Empty recipe, no ingredients needed
    recipe_5 = []
    pantry_5 = [
        Ingredient(name="sugar", expiration_date=get_expiration_date(30)),
        Ingredient(name="butter", expiration_date=get_expiration_date(20)),
        Ingredient(name="milk", expiration_date=get_expiration_date(5)),
    ]
    assert missing_ingredients(recipe_5, pantry_5) == 0, "Test 5 Failed"

    # Test 6: Empty pantry, need all recipe items
    recipe_6 = ["eggs", "flour", "sugar"]
    pantry_6 = []
    assert missing_ingredients(recipe_6, pantry_6) == 3, "Test 6 Failed"

    # Test 7: Recipe with duplicate ingredients
    recipe_7 = ["eggs", "flour", "eggs", "sugar"]
    pantry_7 = [
        Ingredient(name="eggs", expiration_date=get_expiration_date(10)),
        Ingredient(name="sugar", expiration_date=get_expiration_date(5)),
    ]
    assert missing_ingredients(recipe_7, pantry_7) == 2, "Test 7 Failed"

    print("All tests passed!")


test_missing_ingredients()

```