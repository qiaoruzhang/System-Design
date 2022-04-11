"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/12/13
Last Updated: 2021/12/13

===== Module Description =====

This module contains the RedeemItems classes.
"""
from typing import Optional


class RedeemItems:
    # Define a class RedeemItems

    """
    A class representing a RedeemItems，which is a parent class for three
    abstract classes: Thermos, Pillow and Mug. Each RedeemItems class has
    two private attributes: which are _item_name The name for this RedeemItems,
    and _item_points: The price for this RedeemItems.

    === Private Attributes ===
    _item_name: The name for this RedeemItems.
    _item_points: The price for this RedeemItems.

    === Representation Variants ===
    - _item_points is a valid float >= 0

    === Sample Usage ===
    >>> thermos = Thermos()
    >>> thermos.get_item_name()
    'Thermos'
    >>> thermos.get_item_points()
    25.0
    >>> pillow = Pillow()
    >>> pillow.get_item_name()
    'Pillow'
    >>> pillow.get_item_points()
    15.0
    >>> mug = Mug()
    >>> mug.get_item_name()
    'Mug'
    >>> mug.get_item_points()
    10.0
    """
    # Define private attributes type
    _item_name: Optional[str]
    _item_points: Optional[float]

    def __init__(self, item_name: str, item_price: float) -> None:
        """
        Initialize the RedeemItems class.
        """
        self._item_name = item_name
        # Initialize item name to given name.

        self._item_points = item_price
        # Initialize item price to given price.

    def get_item_name(self) -> Optional[str]:
        """
        A getter method to get the item name.
        """
        return self._item_name
        # Return the item name.

    def get_item_points(self) -> Optional[float]:
        """
        A getter method to get the item price.
        """
        return self._item_points
        # Return the item price.

    def print_item_info(self) -> None:
        print('Redeem Item Name: ', self.get_item_name())
        print('Redeem Item Points: ', self.get_item_points())


class Thermos(RedeemItems):
    # Define a class Thermos.

    """
    A class representing a Thermos. Each Thermos class has
    two private attributes:which are _item_name The name for this Thermos,
    and _item_points: The price for this Thermos.

    === Private Attributes ===
    _item_name: The name for this Thermos.
    _item_points: The price for this Thermos.

    === Representation Variants ===
    - _item_points is a valid float >= 0

    === Sample Usage ===
    >>> thermos = Thermos()
    >>> thermos.get_item_name()
    'Thermos'
    >>> thermos.get_item_points()
    25.0
    """

    def __init__(self) -> None:
        """
        Initial a class Thermos.
        >>> thermos = Thermos()
        >>> thermos.get_item_name()
        'Thermos'
        >>> thermos.get_item_points()
        25.0
        """
        item_name = "Thermos"
        # Initialize the _item_name

        item_points = 25.0
        # Initialize the _item_points

        super().__init__(item_name, item_points)
        # Inherit the super class RedeemItems.


class Pillow(RedeemItems):
    # Define a class Thermos.

    """
    A class representing a Pillow. Each Pillow class has
    two private attributes:which are _item_name The name for this Pillow,
    and _item_points: The price for this Pillow.

    === Private Attributes ===
    _item_name: The name for this Pillow.
    _item_points: The price for this Pillow.

    === Representation Variants ===
    - _item_points is a valid float >= 0

    === Sample Usage ===
    >>> pillow = Pillow()
    >>> pillow.get_item_name()
    'Pillow'
    >>> pillow.get_item_points()
    15.0
    """

    def __init__(self) -> None:
        """
        Initial a class Pillow.
        >>> pillow = Pillow()
        >>> pillow.get_item_name()
        'Pillow'
        >>> pillow.get_item_points()
        15.0
        """
        item_name = "Pillow"
        # Initialize the _item_name

        item_points = 15.0
        # Initialize the _item_points

        super().__init__(item_name, item_points)
        # Inherit the super class RedeemItems.


class Mug(RedeemItems):
    # Define a class Mug.

    """
    A class representing a Mug. Each Mug class has
    two private attributes:which are _item_name The name for this Mug,
    and _item_points: The price for this Mug.

    === Private Attributes ===
    _item_name: The name for this Mug.
    _item_points: The price for this Mug.

    === Representation Variants ===
    - _item_points is a valid float >= 0

    === Sample Usage ===
    >>> mug = Mug()
    >>> mug.get_item_name()
    'Mug'
    >>> mug.get_item_points()
    10.0
    """

    def __init__(self) -> None:
        """
        Initial a class Mug.
        >>> mug = Mug()
        >>> mug.get_item_name()
        'Mug'
        >>> mug.get_item_points()
        10.0
        """
        item_name = "Mug"
        # Initialize the _item_name

        item_points = 10.0
        # Initialize the _item_points

        super().__init__(item_name, item_points)
        # Inherit the super class RedeemItems.


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

    print("Test get Thermos's name and price\n")
    thermos = Thermos()
    print("The name for Thermos is: ", thermos.get_item_name())
    print("The price for Thermos is: ", thermos.get_item_points())
    print("--------------------------------------------------------------------"
          "------------\n")
    print("Test get Pillow's name and price\n")
    pillow = Pillow()
    print("The name for Pillow is: ", pillow.get_item_name())
    print("The price for Pillow is: ", pillow.get_item_points())
    print("--------------------------------------------------------------------"
          "------------\n")
    print("Test get Mug's name and price\n")
    mug = Mug()
    print("The name for Mug is: ", mug.get_item_name())
    print("The price for Mug is: ", mug.get_item_points())
    print("--------------------------------------------------------------------"
          "------------\n")
