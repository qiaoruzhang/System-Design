"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/11/05
Last Updated: 2021/11/09

===== Module Description =====

This module contains the Passenger classes.
"""
from RedeemItems import *
# Import RedeemItems

from passenger import Passenger
# Import another file passenger

from ticket import Ticket
# Import another file ticket

from flight import *
# Import another file flight

from time_in_strings import Time
# Import another file time_in_strings

from ticket_manager import TicketManager


# Import another file ticket_manager

class PassengerManager:
    # Define a class PassengerManager

    """
    A class representing a Passenger Manager.
    Each Passenger Manager has one instance attributes passengers_dictionary
    which is a dictionary which store all the passengers.
    The dictionary key is the passenger, and the values are the passenger
    related information.

    === Public Attributes ===
    passengers_dictionary: A dictionary which store all the passengers.
    The dictionary key is the passenger, and the values are the passenger
    related information.

    === Representation Variants ===
    - len(passengers_dictionary) >= 0

    === Sample Usage ===
    >>> passenger_manager = PassengerManager()
    >>> passenger_jay = Passenger("Jay Chou","JC123456")
    >>> passenger_manager.add_passengers(passenger_jay)
    >>> passenger_manager.create_account(passenger_jay,"JayChou","JC123456")
    >>> passenger_manager.print_passenger_information(passenger_jay)
    Passenger Name:  Jay Chou
    Passenger Passport:  JC123456
    Passenger Account Username:  JayChou
    Passenger Account Password:  JC123456
    Passenger Account Balance:  0.0
    Passenger Membership Status:  False
    Passenger Mileage:  0.0
    Passenger Redeem Points:  0.0
    >>> passenger_manager.change_passenger_name(passenger_jay,"Maggie Zhang")
    >>> passenger_manager.change_passenger_passport(passenger_jay,"MZ123456")
    >>> passenger_manager.change_account_username(passenger_jay,"MaggieZhang")
    >>> passenger_manager.change_account_password(passenger_jay,"MZ123456")
    >>> passenger_manager.update_account_balance(passenger_jay,100.0)
    >>> passenger_manager.update_membership_status(passenger_jay)
    >>> passenger_manager.print_passenger_information(passenger_jay)
    Passenger Name:  Maggie Zhang
    Passenger Passport:  MZ123456
    Passenger Account Username:  MaggieZhang
    Passenger Account Password:  MZ123456
    Passenger Account Balance:  100.0
    Passenger Membership Status:  True
    Passenger Mileage:  0.0
    Passenger Redeem Points:  0.0
    """
    # Define public attributes type
    passengers_dictionary: dict

    def __init__(self) -> None:
        """
        Initialize the passengers_dictionary.
        """
        self.passengers_dictionary = {}
        # Initialize passengers_dictionary to be empty dictionary.

    def add_passengers(self, passenger: Passenger) -> None:
        """
        Add the passenger to passengers_dictionary.
        """
        if passenger not in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            self.passengers_dictionary[passenger] \
                = passenger.get_passenger_information()
            # add the get_passenger_information as value to the
            # passengers_dictionary.

    def create_account(self, passenger: Passenger, account_username: str,
                       account_password: str) -> None:
        """
        Register a account for this passenger.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.create_account(passenger_jay,"JayChou","JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        >>> passenger_jay.get_account_password()
        'JC123456'
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.create_account(account_username, account_password)
            # create a new account.

        else:
            print("This passenger is not in system.")

    def get_current_passenger(self, passenger_username: str) -> Passenger:
        """
        Check the passenger's current <passenger_name> to the given string
        exsit or not.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        >>> passenger_manager.change_passenger_name(passenger_jay,
        ...     "Maggie Zhang")
        >>> passenger_jay.get_passenger_name()
        'Maggie Zhang'
        """
        for passenger in self.passengers_dictionary:
            # For each passenger in the passengers_dictionary.

            if passenger.get_account_username() == passenger_username:
                # check if the username is same with the
                # given passenger_username.

                return passenger
                # if same, return the passenger.

        else:
            print("This passenger is not in system.")

    def check_current_passenger(self, passenger_name: str) -> Passenger:
        """
        Check the passenger's current <passenger_name> to the given string
        exsit or not.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        >>> passenger_manager.change_passenger_name(passenger_jay,
        ...     "Maggie Zhang")
        >>> passenger_jay.get_passenger_name()
        'Maggie Zhang'
        """
        for passenger in self.passengers_dictionary:
            # For each passenger in the passengers_dictionary.

            if passenger.get_passenger_name() == passenger_name:
                # check if the name is same with the
                # given passenger_name.

                return passenger
                # if same, return the passenger.

        else:
            print("This passenger is not in system.")

    def change_passenger_name(self, passenger: Passenger,
                              new_passenger_name: str) -> None:
        """
        Change the passenger's current <passenger_name> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        >>> passenger_manager.change_passenger_name(passenger_jay,
        ...     "Maggie Zhang")
        >>> passenger_jay.get_passenger_name()
        'Maggie Zhang'
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.change_passenger_name(new_passenger_name)
            # Set passenger_name to be the given new_passenger_name.

        else:
            print("This passenger is not in system.")

    def check_passenger_name(self, passenger_name: str) -> bool:
        """
        Check the passenger's current <passenger_name> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_passport()
        'JC123456'
        >>> passenger_manager.check_passenger_name("Jay Chou")
        True
        >>> passenger_jay.get_passenger_name()
        'Jay Chou'
        """
        for passenger in self.passengers_dictionary:
            # For each passenger in the passengers_dictionary.

            if passenger.get_passenger_name() == passenger_name:
                # check if the passport is same with the
                # given passenger_passport.

                return True
                # if same, return True

        else:
            return False
            # if passenger not in the passengers_dictionary, return False

    def check_passenger_passport(self, passenger: Passenger,
                                 passenger_passport: str) -> bool:
        """
        Check the passenger's current <passenger_passport> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_passport()
        'JC123456'
        >>> passenger_manager.change_passenger_passport(passenger_jay,
        ...     "MZ123456")
        >>> passenger_jay.get_passenger_passport()
        'MZ123456'
        """
        if passenger in self.passengers_dictionary:
            # For each passenger in the passengers_dictionary.

            if passenger.get_passenger_passport() == passenger_passport:
                # check if the passport is same with the
                # given passenger_passport.

                return True
                # if same, return True

        else:
            return False
            # if passenger not in the passengers_dictionary, return False

    def change_passenger_passport(self, passenger: Passenger,
                                  new_passenger_passport: str) -> None:
        """
        Change the passenger's current <passenger_name> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_passenger_passport()
        'JC123456'
        >>> passenger_manager.change_passenger_passport(passenger_jay,
        ...     "MZ123456")
        >>> passenger_jay.get_passenger_passport()
        'MZ123456'
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.change_passenger_passport(new_passenger_passport)
            # Set passenger_passport to be the given new_passenger_passport.

        else:
            print("This passenger is not in system.")

    def change_account_username(self, passenger: Passenger,
                                new_account_username: str) -> None:
        """
        Change the passenger's current <account_username> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.create_account(passenger_jay, "JayChou",
        ...     "JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        >>> passenger_manager.change_account_username(passenger_jay,
        ...     "MaggieZhang")
        >>> passenger_jay.get_account_username()
        'MaggieZhang'
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.change_account_username(new_account_username)
            # Set account_username to be the given new_account_username.

        else:
            print("This passenger is not in system.")

    def check_account_username(self, input_account_username: str) -> bool:
        """
        Change the passenger's current <account_username> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.create_account(passenger_jay, "JayChou",
        ...     "JC123456")
        >>> passenger_jay.get_account_username()
        'JayChou'
        >>> passenger_manager.change_account_username(passenger_jay,
        ...     "MaggieZhang")
        >>> passenger_jay.get_account_username()
        'MaggieZhang'
        >>> passenger_manager.check_account_username("hahah")
        False
        """
        for one_passenger in self.passengers_dictionary.keys():
            # For each passenger in the passengers_dictionary.

            if one_passenger.get_account_username() == input_account_username:
                # check if the one_passenger's username in the
                # passengers_dictionary is same with the given username.

                return True
                # If same, return True.
        else:
            return False
            # if passenger not in the passengers_dictionary, return False

    def change_account_password(self, passenger: Passenger,
                                new_account_password: str) -> None:
        """
        Change the passenger's current <account_password> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.create_account(passenger_jay, "JayChou",
        ...     "JC123456")
        >>> passenger_jay.get_account_password()
        'JC123456'
        >>> passenger_manager.change_account_password(passenger_jay,
        ...     "MZ123456")
        >>> passenger_jay.get_account_password()
        'MZ123456'
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.change_account_password(new_account_password)
            # Set account_password to be the given new_account_password.

        else:
            print("This passenger is not in system.")

    def check_account_password(self, passenger: Passenger,
                               input_account_password: str) -> bool:
        """
        Check the passenger's current <account_password> to the given string.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.create_account(passenger_jay, "JayChou",
        ...     "JC123456")
        >>> passenger_jay.get_account_password()
        'JC123456'
        >>> passenger_manager.change_account_password(passenger_jay,
        ...     "MZ123456")
        >>> passenger_jay.get_account_password()
        'MZ123456'
        >>> passenger_manager.check_account_password(passenger_jay,"MZ123456")
        True
        >>> passenger_manager.check_account_password(passenger_jay,"w")
        False
        """
        if passenger in self.passengers_dictionary.keys():
            # For each passenger in the passengers_dictionary.

            if passenger.get_account_password() == input_account_password:
                # check if the one_passenger's password in the
                # passengers_dictionary is same with the given password.

                return True
                # If same, return True.

            else:
                return False
                # If not same, return False.

        else:
            return False
            # if passenger not in the passengers_dictionary, return False

    def calculate_ticket_price(self, passenger: Passenger,
                               flight: Flight) -> Union[float, str]:
        """
        Calculate the ticket price based on the flight type and passenger
        membership status.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>>
        >>> passenger_manager.calculate_ticket_price(passenger_jay,flight_helicopter)
        180.0
        >>> passenger_jay.update_membership_status()
        >>> passenger_manager.calculate_ticket_price(passenger_jay,flight_helicopter)
        153.0
        """
        ticket_price = flight.get_flight_price()
        # get the ticket price

        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            if passenger.membership_status:
                # check the membership_status

                ticket_price = passenger.calculate_ticket_price(flight)
                # reduce 15% off.

            return ticket_price
            # return the ticket's <ticket_price>.
        else:
            print("This passenger is not in system.")

    def check_account_balance(self, passenger: Passenger,
                              needed_balance_amount: float) -> float:
        """
        Check the passenger's current <account_balance> to the given float.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_account_balance()
        0.0
        >>> passenger_manager.update_account_balance(passenger_jay,100.0)
        >>> passenger_jay.get_account_balance()
        100.0
        >>> passenger_manager.update_account_balance(passenger_jay,-200.0)
        Current account balance is not enough.
        >>> passenger_jay.get_account_balance()
        -100.0
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            if passenger.get_account_balance() <= needed_balance_amount:
                # check if the current balance is enough.

                return needed_balance_amount - passenger.get_account_balance()
                # return the required amount.

            else:
                return 0.0
                # return the required amount.
        else:
            return 0.0
            # return the required amount.

    def update_account_balance(self, passenger: Passenger,
                               update_balance_amount: float) -> None:
        """
        Update the passenger's current <account_balance> to the given float.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_account_balance()
        0.0
        >>> passenger_manager.update_account_balance(passenger_jay,100.0)
        >>> passenger_jay.get_account_balance()
        100.0
        >>> passenger_manager.update_account_balance(passenger_jay,-200.0)
        Current account balance is not enough.
        >>> passenger_jay.get_account_balance()
        -100.0
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.update_account_balance(update_balance_amount)
            # update balance amount

        else:
            print("This passenger is not in system.")

    def update_membership_status(self, passenger: Passenger) -> None:
        """
        Change the passenger's current <membership_status>.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_membership_status()
        False
        >>> passenger_manager.update_membership_status(passenger_jay)
        >>> passenger_jay.get_membership_status()
        True
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.update_membership_status()
            # change the passenger's <membership_status> to True.

        else:
            print("This passenger is not in system.")

    def update_mileage(self, passenger: Passenger, new_mileage: float) -> None:
        """
        Change the passenger's current <mileage> to the given float.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_mileage()
        0.0
        >>> new_mileage = 200
        >>> passenger_manager.update_mileage(passenger_jay, new_mileage)
        >>> passenger_jay.get_mileage()
        200.0
        """
        passenger.update_mileage(new_mileage)
        # Update the mileage amount

    def add_redeem_item(self, passenger: Passenger,
                        redeem_items: RedeemItems) -> None:
        """
        Add the redeem item to purchase history.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> thermos = Thermos()
        >>> passenger_manager.add_redeem_item(passenger_jay, thermos)
        The redeem_points is not enough
        """
        if passenger in self.passengers_dictionary:
            # If this passenger in passengers_dictionary

            if passenger.get_redeem_points() >= redeem_items.get_item_points():
                # If passenger's redeem_points is enough.

                passenger.add_redeem_item(redeem_items)
                # Add the redeem item to purchase_history.

            else:
                print("The redeem_points is not enough")
        else:
            print("This passenger is not in system.")

    def get_voucher(self, passenger: Passenger, rating_level: int) -> None:
        """
        Add the voucher to account balance.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_jay.get_account_balance()
        0.0
        >>> rating_level = 5
        >>> passenger_manager.get_voucher(passenger_jay, rating_level)
        >>> passenger_jay.get_account_balance()
        5.0
        """
        if passenger in self.passengers_dictionary:
            # If this passenger in passengers_dictionary

            passenger.get_voucher(rating_level)
            # Add the voucher to passenger.

        else:
            print("This passenger is not in system.")

    def update_ticket_history(self, passenger: Passenger,
                              ticket: Ticket) -> None:
        """
        Return the passenger related information.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> SA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
        >>> SA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
        >>> SA321small_airliner = SmallAirliner()
        >>> SA321small_airliner_capacity = SA321small_airliner.get_max_capacity()
        >>> SA321flight_small_airliner = Flight("SA321", "Toronto", "Montreal",
        ...                                 SA321departure_time,
        ...                                 SA321arrival_time, "2A",
        ...                                 SA321small_airliner,
        ...                                 SA321small_airliner_capacity)
        >>> ticket_321 = Ticket("321", "2B", passenger_jay, SA321flight_small_airliner)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_123)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_321)
        >>> passenger_manager.all_passenger_tickets_number(passenger_jay)
        ['123', '321']
        """
        if passenger in self.passengers_dictionary:
            if ticket not in passenger.purchase_history["Tickets"]:
                passenger.purchase_history["Tickets"].append(ticket)
        else:
            print("This passenger is not in system.")

    def all_passenger_tickets_number(self, passenger: Passenger) -> list[str]:
        """
        Return the passenger related information.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> SA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
        >>> SA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
        >>> SA321small_airliner = SmallAirliner()
        >>> SA321small_airliner_capacity = SA321small_airliner.get_max_capacity()
        >>> SA321flight_small_airliner = Flight("SA321", "Toronto", "Montreal",
        ...                                 SA321departure_time,
        ...                                 SA321arrival_time, "2A",
        ...                                 SA321small_airliner,
        ...                                 SA321small_airliner_capacity)
        >>> ticket_321 = Ticket("321", "2B", passenger_jay, SA321flight_small_airliner)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_123)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_321)
        >>> passenger_manager.all_passenger_tickets_number(passenger_jay)
        ['123', '321']
        """
        ticket_list = []
        if passenger in self.passengers_dictionary:
            for one_ticket in passenger.purchase_history["Tickets"]:
                # for each ticket in passenger's history

                if one_ticket is not None:
                    # if the ticket is not None
                    ticket_list.append(one_ticket.get_ticket_id())
            return ticket_list
        else:
            print("This passenger is not in system.")

    def print_passenger_ticket_history(self, passenger: Passenger) -> None:
        """
        Return the passenger related information.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> SA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
        >>> SA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
        >>> SA321small_airliner = SmallAirliner()
        >>> SA321small_airliner_capacity = SA321small_airliner.get_max_capacity()
        >>> SA321flight_small_airliner = Flight("SA321", "Toronto", "Montreal",
        ...                                 SA321departure_time,
        ...                                 SA321arrival_time, "2A",
        ...                                 SA321small_airliner,
        ...                                 SA321small_airliner_capacity)
        >>> ticket_321 = Ticket("321", "2B", passenger_jay, SA321flight_small_airliner)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_123)
        >>> passenger_manager.update_ticket_history(passenger_jay, ticket_321)
        >>> passenger_manager.print_passenger_ticket_history(passenger_jay)
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        <BLANKLINE>
        -----------------------------------------
        <BLANKLINE>
        Ticket ID:  321
        Ticket Price:  1200.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  SA321
        <BLANKLINE>
        -----------------------------------------
        <BLANKLINE>
        """
        if passenger in self.passengers_dictionary:

            for one_ticket in passenger.purchase_history["Tickets"]:
                # for each ticket in passenger's history

                if one_ticket is not None:
                    # if the ticket is not None

                    one_ticket.print_ticket_information()
                    print("\n-----------------------------------------\n")
                    # print the ticket information
        else:
            print("This passenger is not in system.")

    def print_passenger_redeem_history(self, passenger: Passenger) -> None:
        """
        Return the passenger related information.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> SA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
        >>> SA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
        >>> SA321small_airliner = SmallAirliner()
        >>> SA321small_airliner_capacity = SA321small_airliner.get_max_capacity()
        >>> SA321flight_small_airliner = Flight("SA321", "Toronto", "Montreal",
        ...                                 SA321departure_time,
        ...                                 SA321arrival_time, "2A",
        ...                                 SA321small_airliner,
        ...                                 SA321small_airliner_capacity)
        >>> ticket_321 = Ticket("321", "2B", passenger_jay, SA321flight_small_airliner)
        >>> passenger_jay.get_redeem_points()
        108.7
        >>> thermos = Thermos()
        >>> passenger_manager.add_redeem_item(passenger_jay, thermos)
        >>> pillow = Pillow()
        >>> passenger_manager.add_redeem_item(passenger_jay, pillow)
        >>> passenger_manager.print_passenger_redeem_history(passenger_jay)
        Redeem Item Name:  Thermos
        Redeem Item Points:  25.0
        <BLANKLINE>
        -----------------------------------------
        <BLANKLINE>
        Redeem Item Name:  Pillow
        Redeem Item Points:  15.0
        <BLANKLINE>
        -----------------------------------------
        <BLANKLINE>
        """
        if passenger in self.passengers_dictionary:

            for item in passenger.purchase_history["RedeemItems"]:
                # for each ticket in passenger's history

                if item is not None:
                    # if the ticket is not None

                    item.print_item_info()
                    print("\n-----------------------------------------\n")
                    # print the ticket information
        else:
            print("This passenger is not in system.")

    def print_passenger_information(self, passenger: Passenger) -> None:
        """
        Return the passenger related information.
        >>> passenger_manager = PassengerManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> passenger_jay.create_account("JayChou","JC123456")
        >>> passenger_manager.add_passengers(passenger_jay)
        >>> passenger_manager.print_passenger_information(passenger_jay)
        Passenger Name:  Jay Chou
        Passenger Passport:  JC123456
        Passenger Account Username:  JayChou
        Passenger Account Password:  JC123456
        Passenger Account Balance:  0.0
        Passenger Membership Status:  False
        Passenger Mileage:  0.0
        Passenger Redeem Points:  0.0
        """
        if passenger in self.passengers_dictionary:
            # check if the given passenger in the passengers_dictionary or not.

            passenger.print_passenger_information()
            # return the Passenger's related information.

        else:
            print("This passenger is not in system.")


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
    passenger_manager = PassengerManager()
    # initial a PassengerManager

    passenger_jay = Passenger("Jay Chou", "JC123456")
    # initial a Passenger Jay Chou

    passenger_manager.add_passengers(passenger_jay)
    # add the passenger to passenger_manager

    passenger_manager.create_account(passenger_jay, "JayChou", "JC123456")
    # register an online account

    passenger_manager.print_passenger_information(passenger_jay)
    # return the Passenger's related information.

    print('\n-----------------------------------------------------------------')

    print('\nTesting account management:')
    passenger_manager.change_passenger_name(passenger_jay, "Maggie Zhang")
    # initial a Passenger Maggie Zhang

    passenger_manager.change_passenger_passport(passenger_jay, "MZ123456")
    # change the passenger_passport

    passenger_manager.change_account_username(passenger_jay, "MaggieZhang")
    # change the username

    passenger_manager.change_account_password(passenger_jay, "MZ123456")
    # change the password

    passenger_manager.update_account_balance(passenger_jay, 100.0)
    # load money to account balance

    passenger_manager.update_membership_status(passenger_jay)
    # register membership_status

    passenger_manager.print_passenger_information(passenger_jay)
    # return the Passenger's related information.
