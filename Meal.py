"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/12/13
Last Updated: 2021/12/13

===== Module Description =====

This module contains the Meal classes.
"""
from typing import Optional


# Import Union

class Meal:
    # Define a class Meal

    """
    A class representing a Meal which is a parent class for three
    abstract classeses. Each Meal class has
    two private attributes:which are _meal_name The name for this Meal,
    and _meal_price: The price for this Meal.

    === Private Attributes ===
    _meal_name: The name for this Meal.
    _meal_price: The price for this Meal.

    === Representation Variants ===
    - _meal_price is a valid float >= 0

    === Sample Usage ===
    >>> burger = Burger()
    >>> burger.get_meal_name()
    'Burger'
    >>> burger.get_meal_price()
    25.0
    >>> hot_dog = HotDog()
    >>> hot_dog.get_meal_name()
    'HotDog'
    >>> hot_dog.get_meal_price()
    15.0
    >>> french_fries = FrenchFries()
    >>> french_fries.get_meal_name()
    'French Fries'
    >>> french_fries.get_meal_price()
    10.0
    """
    # Define private attributes type
    _meal_name: Optional[str]
    _meal_price: Optional[float]

    def __init__(self, meal_name: str, meal_price: float) -> None:
        """
        Initialize the Meal class.
        """
        self._meal_name = meal_name
        # Initialize meal name to given name.

        self._meal_price = meal_price
        # Initialize meal price to given price.

    def get_meal_name(self) -> Optional[str]:
        """
        A getter method to get the meal name.
        """
        return self._meal_name
        # Return the meal name.

    def get_meal_price(self) -> Optional[float]:
        """
        A getter method to get the meal price.
        """
        return self._meal_price
        # Return the meal price.


class Burger(Meal):
    # Define a class Burger.

    """
    A class representing a Burger. Each Burger class has
    two private attributes:which are _meal_name The name for this Meal,
    and _meal_price: The price for this Meal.

    === Private Attributes ===
    _meal_name: The name for this Meal.
    _meal_price: The price for this Meal.

    === Representation Variants ===
    - _meal_price is a valid float >= 0

    === Sample Usage ===
    >>> burger = Burger()
    >>> burger.get_meal_name()
    'Burger'
    >>> burger.get_meal_price()
    25.0
    """

    def __init__(self) -> None:
        """
        Initial a class Burger.
        >>> burger = Burger()
        >>> burger.get_meal_name()
        'Burger'
        >>> burger.get_meal_price()
        25.0
        """
        meal_name = "Burger"
        # Initialize the meal_name

        meal_price = 25.0
        # Initialize the meal_price

        super().__init__(meal_name, meal_price)
        # Inherit the super class Meal.


class HotDog(Meal):
    # Define a class HotDog.

    """
    A class representing a HotDog. Each HotDog class has
    two private attributes:which are _meal_name The name for this Meal,
    and _meal_price: The price for this Meal.

    === Private Attributes ===
    _meal_name: The name for this Meal.
    _meal_price: The price for this Meal.

    === Representation Variants ===
    - _meal_price is a valid float >= 0

    === Sample Usage ===
    >>> hot_dog = HotDog()
    >>> hot_dog.get_meal_name()
    'HotDog'
    >>> hot_dog.get_meal_price()
    15.0
    """

    def __init__(self) -> None:
        """
        Initial a class HotDog.
        >>> hotdog = HotDog()
        >>> hotdog.get_meal_name()
        'HotDog'
        >>> hotdog.get_meal_price()
        15.0
        """
        meal_name = "HotDog"
        # Initialize the meal_name

        meal_price = 15.0
        # Initialize the meal_price

        super().__init__(meal_name, meal_price)
        # Inherit the super class Meal.


class FrenchFries(Meal):
    # Define a class FrenchFries.

    """
    A class representing a FrenchFries. Each FrenchFries class has
    two private attributes:which are _meal_name The name for this Meal,
    and _meal_price: The price for this Meal.

    === Private Attributes ===
    _meal_name: The name for this Meal.
    _meal_price: The price for this Meal.

    === Representation Variants ===
    - _meal_price is a valid float >= 0

    === Sample Usage ===
    >>> french_fries = FrenchFries()
    >>> french_fries.get_meal_name()
    'French Fries'
    >>> french_fries.get_meal_price()
    10.0
    """

    def __init__(self) -> None:
        """
        Initial a class French Fries.
        >>> french_fries = FrenchFries()
        >>> french_fries.get_meal_name()
        'French Fries'
        >>> french_fries.get_meal_price()
        10.0
        """
        meal_name = "French Fries"
        # Initialize the meal_name

        meal_price = 10.0
        # Initialize the meal_price

        super().__init__(meal_name, meal_price)
        # Inherit the super class Meal.


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    print("Title: INF452 Midterm Project")
    print("Course Name: INF452 Design Studio V: Coding")
    print("Instructor: Dr. Maher Elshakankiri")
    print("Student Name: Qiaoru Zhang")
    print("Student Number: 1004607758")
    print("--------------------------------------------------------------------"
          "------------\n")

    print("Test get Burger's name and price\n")
    one_burger = Burger()
    print("The name for Burger is: ", one_burger.get_meal_name())
    print("The price for Burger is: ", one_burger.get_meal_price())
    print("--------------------------------------------------------------------"
          "------------\n")
    print("Test get HotDog's name and price\n")
    one_hotdog = HotDog()
    print("The name for HotDog is: ", one_hotdog.get_meal_name())
    print("The price for HotDog is: ", one_hotdog.get_meal_price())
    print("--------------------------------------------------------------------"
          "------------\n")
    print("Test get French Fries' name and price\n")
    one_french_fries = FrenchFries()
    print("The name for French Fries is: ", one_french_fries.get_meal_name())
    print("The price for French Fries is: ", one_french_fries.get_meal_price())
    print("--------------------------------------------------------------------"
          "------------\n")
