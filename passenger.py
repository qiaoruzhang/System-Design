"""
Student Name: Qiaoru Zhang
Date Created: 2021/11/05
Last Updated: 2021/11/09

===== Module Description =====

This module contains the Passenger classes.
"""
from typing import Optional  # Import optional

from RedeemItems import *
from flight import *
# Import another file flight
from time_in_strings import Time


# Import another file time_in_strings

class Passenger:
    # Define a class Passenger

    """
    A class representing a passenger.
    Each passenger has one instance attributes <passenger_name> for the name
    of this passenger, one instance attributes <passenger_passport> for the
    passport of this passenger,one instance attributes <account_username> for
    the username of this passenger's account,.one instance attributes
    <account_password> for the password of this passenger's account,
    one instance attributes <account_balance> for the valid floating point value
    representing the Passenger’s account balance amount.one instance attributes
    <membership_status> for the membership status of this passenger's account,
    one instance attributes <passenger_information_dictionary> for the
    dictionary to store all passenger information.

    === Public Attributes ===
    passenger_name: The name of this passenger.
    passenger_passport: The passport of this passenger.
    account_username:  The username of this passenger's account.
    account_password:  The password of this passenger's account.
    account_balance: A valid floating point value representing the Passenger’s
    account balance amount.
    membership_status: The membership status of this passenger's account.
    passenger_information_dictionary: The dictionary to store all
    passenger information.
    mileage: The total mileage for this passenger.
    redeem_points: The total redeemable points for this passenger.
    purchase_history: The purchase histories for this passenger.

    === Representation Variants ===
    - account_balance is a valid float >= 0

    === Sample Usage ===
    >>> passenger_jay = Passenger("Jay Chou", "JC123456")
    >>> passenger_jay.create_account("JayChou","JC123456")
    >>> passenger_jay.get_passenger_name()
    'Jay Chou'
    >>> passenger_jay.get_passenger_passport()
    'JC123456'
    >>> passenger_jay.get_account_username()
    'JayChou'
    >>> passenger_jay.get_account_password()
    'JC123456'
    >>> passenger_jay.get_account_balance()
    0.0
    >>> passenger_jay.get_membership_status()
    False
    >>> passenger_jay.print_passenger_information()
    Passenger Name:  Jay Chou
    Passenger Passport:  JC123456
    Passenger Account Username:  JayChou
    Passenger Account Password:  JC123456
    Passenger Account Balance:  0.0
    Passenger Membership Status:  False
    Passenger Mileage:  0.0
    Passenger Redeem Points:  0.0
    """
    # Define public attributes type
    passenger_name: str
    passenger_passport: str
    account_username: Optional[str]
    account_password: Optional[str]
    account_balance: float
    membership_status: bool
    mileage: Optional[float]
    redeem_points: Optional[float]
    passenger_information_dictionary: dict
    purchase_history: dict

    def __init__(self, passenger_name: str, passenger_passport: str) -> None:
        """
        Create a new passenger with unique <passenger_name>,
        <passenger_passport>.

        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> print(passenger_jay.passenger_name)
        Jay Chou
        >>> print(passenger_jay.passenger_passport)
        JC123456
        >>> print(passenger_jay.account_balance)
        0.0
        >>> print(passenger_jay.membership_status)
        False
        """
        self.passenger_name = passenger_name
        # Initialize passenger_name to be the given passenger_name.

        self.passenger_passport = passenger_passport
        # Initialize passenger_passport to be the given passenger_passport.

        self.account_username = None
        # Initialize account_username to be None.

        self.account_password = None
        # Initialize account_password to be None.

        self.account_balance = 0.0
        # Initialize account_balance to be 0.0.

        self.membership_status = False
        # Initialize membership_status to be False.

        self.mileage = 0.0
        # Initialize mileage to be 0.0.

        self.redeem_points = self.get_redeem_points() / 10
        # Set the redeem_points to be redeem_points / 10.

        self.purchase_history = {"Tickets": [], "RedeemItems": []}

        self.passenger_information_dictionary = self.get_passenger_information()
        # Add all the related value and keys to the
        # passenger_information_dictionary.

    def create_account(self, account_username: str,
                       account_password: str) -> None:
        """
        Register a account for this passenger.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        >>> passenger_jay.get_account_password()
        'JC123456'
        """
        self.account_username = account_username
        # Initialize account_username to be the given account_username.

        self.account_password = account_password
        # Initialize account_password to be the given account_password.

    def get_passenger_name(self) -> str:
        """
        The getter function to return the passenger's <passenger_name>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        """
        return self.passenger_name
        # return the passenger's <ticket_id>.

    def change_passenger_name(self, new_passenger_name: str) -> None:
        """
        Change the passenger's current <passenger_name> to the given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        >>> passenger_jay.change_passenger_name("Maggie Zhang")
        >>> passenger_jay.get_passenger_name()
        'Maggie Zhang'
        """
        self.passenger_name = new_passenger_name
        # Set passenger_name to be the given new_passenger_name.

    def get_passenger_passport(self) -> str:
        """
        The getter function to return the passenger's <passenger_passport>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_passenger_passport()
        'JC123456'
        """
        return self.passenger_passport
        # return the passenger's <passenger_passport>.

    def change_passenger_passport(self, new_passenger_passport: str) -> None:
        """
        Change the passenger's current <passenger_passport> to the given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_passenger_passport()
        'JC123456'
        >>> passenger_jay.change_passenger_passport("MZ123456")
        >>> passenger_jay.get_passenger_passport()
        'MZ123456'
        """
        self.passenger_passport = new_passenger_passport
        # Set passenger_passport to be the given new_passenger_passport.

    def get_account_username(self) -> str:
        """
        The getter function to return the passenger's <account_username>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        """
        return self.account_username
        # return the passenger's <account_username>.

    def get_account_password(self) -> str:
        """
        The getter function to return the passenger's <account_password>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_account_password()
        'JC123456'
        """
        return self.account_password
        # return the passenger's <account_password>.

    def get_mileage(self) -> float:
        """
        The getter function to return the passenger's <mileage>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_mileage()
        0.0
        """
        return self.mileage
        # return the passenger's <mileage>.

    def get_membership_status(self) -> bool:
        """
        The getter function to return the passenger's <membership_status>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_membership_status()
        False
        """
        return self.membership_status
        # return the passenger's <membership_status>.

    def get_redeem_points(self) -> float:
        """
        The getter function to return the passenger's <redeem_points>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_redeem_points()
        0.0
        """
        self.calculate_redeem_points()
        return self.redeem_points
        # return the passenger's <redeem_points>.

    def calculate_redeem_points(self) -> None:
        """
        Update the passenger's <redeem_points>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_redeem_points()
        0.0
        """
        self.redeem_points = self.mileage / 10
        # return the passenger's <redeem_points>.

    def change_account_username(self, new_account_username: str) -> None:
        """
        Change the passenger's current <account_username> to the given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        >>> passenger_jay.change_account_username("MaggieZhang")
        >>> passenger_jay.get_account_username()
        'MaggieZhang'
        """
        self.account_username = new_account_username
        # Set account_username to be the given new_account_username.

    def change_account_password(self, new_account_password: str) -> None:
        """
        Change the passenger's current <account_password> to the given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.get_account_password()
        'JC123456'
        >>> passenger_jay.change_account_password("MZ123456")
        >>> passenger_jay.get_account_password()
        'MZ123456'
        """
        self.account_password = new_account_password
        # Set account_password to be the given new_account_password.

    def get_account_balance(self) -> float:
        """
        The getter function to return the passenger's <account_balance>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_account_balance()
        0.0
        """
        return self.account_balance
        # return the passenger's <account_balance>.

    def update_account_balance(self,
                               update_balance_amount: float) -> None:
        """
        Update the passenger's current <account_balance> to the given float.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_account_balance()
        0.0
        >>> passenger_jay.update_account_balance(100.0)
        >>> passenger_jay.get_account_balance()
        100.0
        >>> passenger_jay.update_account_balance(-200.0)
        Current account balance is not enough.
        >>> passenger_jay.get_account_balance()
        -100.0
        """
        current_account_balance = self.account_balance
        # Get the current account balance

        if update_balance_amount >= 0:
            # if the update balance amount larger than 0

            self.account_balance += update_balance_amount
            # update balance amount

        elif current_account_balance >= abs(update_balance_amount):
            # if the update balance amount larger than current account balance

            self.account_balance += update_balance_amount
            # update balance amount

        else:
            self.account_balance += update_balance_amount
            # update balance amount

            print("Current account balance is not enough.")

    def update_membership_status(self) -> None:
        """
        Change the passenger's current <membership_status> to the given float.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_membership_status()
        False
        >>> passenger_jay.update_membership_status()
        >>> passenger_jay.get_membership_status()
        True
        """
        if not self.membership_status:
            # if the passenger's <membership_status> is False.

            self.membership_status = True
            # change the passenger's <membership_status> to True.

    def update_mileage(self, new_mileage: float) -> None:
        """
        Change the passenger's current <mileage> to the given float.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")

        """
        self.mileage += new_mileage
        # Update the mileage amount

    def update_redeem_points(self, redeem_points: float) -> None:
        """
        Change the passenger's current <mileage> to the given float.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_membership_status()
        False
        >>> passenger_jay.update_membership_status()
        >>> passenger_jay.get_membership_status()
        True
        """
        self.redeem_points += redeem_points
        # Update the mileage amount

    def add_redeem_item(self, redeem_items: RedeemItems) -> bool:
        """
        Add the redeem item to purchase history.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> thermos = Thermos()
        >>> passenger_jay.add_redeem_item(thermos)
        False
        """
        if self.redeem_points >= redeem_items.get_item_points():
            self.purchase_history["RedeemItems"].append(redeem_items)
            self.redeem_points -= redeem_items.get_item_points()
            return True
        else:
            return False

    def get_voucher(self, rating_level: int) -> None:
        """
        Add the voucher to account balance.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.get_account_balance()
        0.0
        >>> rating_level = 5
        >>> passenger_jay.get_voucher(rating_level)
        >>> passenger_jay.get_account_balance()
        5.0
        """
        if rating_level == 5:
            # If passenger give 5 starts rating
            self.account_balance += 5.0
            # The passenger will get $5 voucher.

    def calculate_ticket_price(self, flight: Flight) -> float:
        """
        Calculate the ticket price based on the flight type and passenger
        membership status.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> passenger_jay.calculate_ticket_price(flight_helicopter)
        180.0
        >>> passenger_jay.update_membership_status()
        >>> passenger_jay.calculate_ticket_price(flight_helicopter)
        153.0
        """
        ticket_price = flight.get_flight_price()
        # get the ticket price

        if self.membership_status:
            # check the membership_status

            ticket_price = ticket_price * 0.85
            # reduce 15% off.

        return ticket_price
        # return the ticket's <ticket_price>.

    def get_passenger_information(self) -> dict:
        """
        Store the passenger related information into dictionary.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> information_dictionary = passenger_jay.get_passenger_information()
        >>> information_dictionary["passenger_name"]
        'Jay Chou'
        """
        self.passenger_information_dictionary = {
            "passenger_name": self.passenger_name,
            "passenger_passport": self.passenger_passport,
            "account_username": self.account_username,
            "account_password": self.account_password,
            "account_balance": self.account_balance,
            "membership_status": self.membership_status,
            "mileage": self.mileage,
            "redeem_points": self.redeem_points}
        # Add all the related value and keys to the
        # passenger_information_dictionary.

        return self.passenger_information_dictionary
        # return the passenger's <passenger_information_dictionary>.

    def print_passenger_information(self) -> None:
        """
        Return the passenger related information.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_jay.print_passenger_information()
        Passenger Name:  Jay Chou
        Passenger Passport:  JC123456
        Passenger Account Username:  JayChou
        Passenger Account Password:  JC123456
        Passenger Account Balance:  0.0
        Passenger Membership Status:  False
        Passenger Mileage:  0.0
        Passenger Redeem Points:  0.0
        """
        print('Passenger Name: ', self.passenger_name)
        print('Passenger Passport: ', self.passenger_passport)
        print('Passenger Account Username: ', self.account_username)
        print('Passenger Account Password: ', self.account_password)
        print('Passenger Account Balance: ', self.account_balance)
        print('Passenger Membership Status: ', self.membership_status)
        print('Passenger Mileage: ', self.mileage)
        print('Passenger Redeem Points: ', self.redeem_points)
        # return the Passenger's related information.


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

    print('\nTesting first passenger:')

    print('Passenger Jay Chou Status: \n')
    passenger_jay_Chou = Passenger("Jay Chou", "JC123456")
    # initial a Passenger Jay Chou

    passenger_jay_Chou.create_account("JayChou", "JC123456")
    # register an online account

    passenger_jay_Chou.print_passenger_information()
    # return the Passenger's related information.

    print('\n-----------------------------------------------------------------')

    print('\nTesting second passenger:')

    print('Passenger Maggie Zhang Status: \n')
    passenger_maggie_zhang = Passenger("Maggie Zhang", "MZ123456")
    # initial a Passenger Maggie Zhang

    passenger_maggie_zhang.print_passenger_information()
    # return the Passenger's related information.
