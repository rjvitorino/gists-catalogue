# 20240701-fruit_stand-gist

**Description**: Cassidoo's interview question of the week: a FruitStand class that allows you to add different types of fruits with their quantities and prices, update them, and calculate the total value of all the fruits in the stand.

## fruit_stand.py

```Python
from typing import Dict
from typing import List

class FruitStand:
    """
    The FruitStand class allows you to add different types of fruits
    with their quantities and prices, update them, and calculate the 
    total value of all the fruits in the stand. It supports the following
    functions to change the contents in the stand as well as get the stand's
    total value and the list of fruits without stock:

    - add_fruit(name, quantity, price)
    - update_quantity(name, quantity)
    - update_price(name, price)
    - total_value()
    - missing_stock()
    """

    def __init__(self) -> None:
        """
        Initialise the fruit stand with an empty dictionary to store fruits.
        
        :type self: FruitStand
        :rtype: None
        """
        self.fruits: Dict[str, Dict[str, float]] = {}

    def add_fruit(self, name: str, quantity: int, price: float) -> None:
        """
        Add a fruit to the stand with the given quantity and price.
        
        :type self: FruitStand
        :type name: str
        :type quantity: int
        :type price: float
        :rtype: None
        """
        if name in self.fruits:
            self.fruits[name]['quantity'] += quantity
            self.fruits[name]['price'] = price
        else:
            self.fruits[name] = {'quantity': quantity, 'price': price}

    def update_quantity(self, name: str, quantity: int) -> None:
        """
        Update the quantity of an existing fruit.
        
        :type self: FruitStand
        :type name: str
        :type quantity: int
        :rtype: None
        :raises ValueError: If the fruit is not found in the stand.
        """
        if name in self.fruits:
            self.fruits[name]['quantity'] = quantity
        else:
            raise ValueError(f"Fruit '{name}' not found in the stand.")
        
    def update_price(self, name: str, price: float) -> None:
        """
        Update the price of an existing fruit.
        
        :type self: FruitStand
        :type name: str
        :type price: float
        :rtype: None
        :raises ValueError: If the fruit is not found in the stand.
        """
        if name in self.fruits:
            self.fruits[name]['price'] = price
        else:
            raise ValueError(f"Fruit '{name}' not found in the stand.")

    def total_value(self) -> float:
        """
        Calculate the total value of all fruits in the stand.
        
        :type self: FruitStand
        :rtype: float
        """
        total = sum(info['quantity'] * info['price'] for info in self.fruits.values())
        return total
    
    def missing_stock(self) -> List[str]:
        """
        Return a list of fruits with zero quantity.
        
        :type self: FruitStand
        :rtype: List[str]
        """
        return [name for name, info in self.fruits.items() if info['quantity'] == 0]


def main() -> None:
    """
    Demonstrate the usage of the FruitStand class.
    
    :rtype: None
    """
    stand = FruitStand()
    stand.add_fruit("apple", 10, 0.5)
    stand.add_fruit("banana", 5, 0.2)
    stand.add_fruit("cherry", 20, 0.1)
    stand.update_quantity("banana", 10)
    stand.update_price("apple", 0.6)
    # Calculate the total value of all fruits in the stand
    print("FruitStand's total value is:", stand.total_value())  # Output: 10.0

    # Check for missing stock
    stand.add_fruit("orange", 0, 0.3)
    print("FruitStand is missing stock for the following fruits:", ','.join(stand.missing_stock()))  # Output: ['orange']


def test_fruit_stand() -> None:
    """
    Test the functionality of the FruitStand class.
    
    :rtype: None
    """
    stand = FruitStand()
    
    stand.add_fruit("apple", 10, 0.5)
    assert stand.fruits["apple"] == {"quantity": 10, "price": 0.5}
    
    stand.add_fruit("banana", 5, 0.2)
    assert stand.fruits["banana"] == {"quantity": 5, "price": 0.2}
    
    stand.update_quantity("banana", 10)
    assert stand.fruits["banana"]["quantity"] == 10
    
    stand.update_price("apple", 0.6)
    assert stand.fruits["apple"]["price"] == 0.6

    assert stand.missing_stock() == []  # No missing stock
    stand.add_fruit("orange", 0, 0.3)
    assert stand.missing_stock() == ["orange"]  # Orange has zero quantity

    assert abs(stand.total_value() - 8.0) < 1e-9  # Considering floating point precision

    # Test error handling for updating non-existent fruit
    try:
        stand.update_quantity("grape", 5)
    except ValueError as e:
        assert str(e) == "Fruit 'grape' not found in the stand."
    else:
        assert False, "Expected ValueError"
    
    try:
        stand.update_price("grape", 0.3)
    except ValueError as e:
        assert str(e) == "Fruit 'grape' not found in the stand."
    else:
        assert False, "Expected ValueError"

    print("All tests passed!")

if __name__ == "__main__":
    main()
    test_fruit_stand()

```