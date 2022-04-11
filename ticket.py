"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/11/05
Last Updated: 2021/12/13

===== Module Description =====

This module contains the Passenger classes.
"""
from typing import Optional
# Import Optional

from passenger import Passenger
# Import another file passenger

from flight import *
# Import another file flight

from time_in_strings import Time
# Import another file time_in_strings

from Meal import *


class Ticket:
    # Define a class Ticket
    """
    A class representing a ticket.
    Each ticket has one instance attributes ticket_id for the ticket id of this
    ticket. One instance attributes ticket_price for the price for this ticket.
    One instance attributes seat_number for the seat number for this ticket.
    One instance attributes passenger for the passenger who booked this ticket.
    One instance attributes flight for the flight for this ticket.
    One instance attributes ticket_information_dictionary for the dictionary
    too store all ticket information.

    === Public Attributes ===
    ticket_id: The ticket id of this ticket.
    ticket_price: The price for this ticket.
    seat_number: The seat number for this ticket.
    passenger: The passenger who booked this ticket.
    flight: The flight for this ticket.
    ticket_information_dictionary: The dictionary too store all ticket
    information.
    check_in_status: The check in status for this ticket.
    meal: The meal for this ticket.

    === Representation Variants ===
    - ticket_price is a valid int >= 0

    === Sample Usage ===
    >>> passenger_jay = Passenger("Jay Chou","JC123456")
    >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
    >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
    >>> helicopter = Helicopter()
    >>> helicopter_capacity = helicopter.get_max_capacity()
    >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
    ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
    ...     helicopter_capacity)
    >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
    >>> ticket_123.get_ticket_id()
    '123'
    >>> ticket_123.get_seat_number()
    '2B'
    >>> ticket_123.get_passenger_name()
    'Jay Chou'
    >>> ticket_123.get_flight_number()
    'AC123'
    >>> ticket_123.calculate_ticket_price()
    180.0
    >>> ticket_123.print_ticket_information()
    Ticket ID:  123
    Ticket Price:  180.0
    Ticket Seat Number:  2B
    Passenger Name For This Ticket:  Jay Chou
    Check-In status For This Ticket:  False
    Selected Meal For This Ticket:  None
    Flight Number For This Ticket:  AC123
    >>> passenger_jay.update_membership_status()
    >>> ticket_123.calculate_ticket_price()
    153.0
    >>> burger = Burger()
    >>> ticket_123.set_meal(burger)
    >>> ticket_123.get_ticket_meal().get_meal_name()
    'Burger'
    >>> ticket_123.update_check_in_status()
    >>> ticket_123.print_ticket_information()
    Ticket ID:  123
    Ticket Price:  153.0
    Ticket Seat Number:  2B
    Passenger Name For This Ticket:  Jay Chou
    Check-In status For This Ticket:  True
    Selected Meal For This Ticket:  Burger
    Flight Number For This Ticket:  AC123
    """
    # Define public attributes type
    ticket_id: str
    ticket_price: float
    seat_number: Optional[str]
    passenger: Optional[Passenger]
    flight: Flight
    ticket_information_dictionary: dict
    check_in_status: bool
    meal: Optional[Meal]

    def __init__(self, ticket_id: str, seat_number: Optional[str],
                 passenger: Optional[Passenger], flight: Flight) -> None:
        """
        Create a new ticket with unique <ticket_id>,
        <seat_number>, <passenger>, <flight>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> print(ticket_123.ticket_id)
        123
        >>> print(ticket_123.seat_number)
        2B
        >>> print(ticket_123.passenger.passenger_name)
        Jay Chou
        >>> print(ticket_123.flight.get_flight_number())
        AC123
        """
        self.ticket_id = ticket_id
        # Initialize ticket_id to be the given ticket_id.

        self.seat_number = seat_number
        # Initialize seat_number to be the given seat_number.

        self.passenger = passenger
        # Initialize passenger to be the given passenger.

        self.flight = flight
        # Initialize flight to be the given flight.

        self.ticket_price = self.calculate_ticket_price()
        # Initialize ticket_price.

        self.check_in_status = False
        # default check_in_status to be False

        self.meal = None
        # default ticket meal to be None

        passenger.update_mileage(flight.get_flight_mileage())
        # Update the passenger's mileage

        passenger.calculate_redeem_points()
        # Update the passenger's redeem_points

        self.ticket_information_dictionary = {
            "ticket_id": self.ticket_id,
            "ticket_price": self.ticket_price,
            "seat_number": self.seat_number,
            "passenger name": self.passenger.get_passenger_name(),
            "flight number": self.flight.get_flight_number(),
            "check_in_status": self.get_ticket_check_in_status(),
            "meal": self.get_ticket_meal()
        }
        # Add all the related value and keys to the
        # ticket_information_dictionary.

    def get_ticket_id(self) -> str:
        """
        The getter function to get the <ticket_id>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_ticket_id()
        '123'
        """
        return self.ticket_id
        # return the ticket's <ticket_id>.

    def calculate_ticket_price(self) -> float:
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
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.calculate_ticket_price()
        180.0
        >>> passenger_jay.update_membership_status()
        >>> ticket_123.calculate_ticket_price()
        153.0
        """
        self.ticket_price = \
            self.flight.get_flight_price()
        # get the ticket price

        if self.passenger.membership_status:
            # check the membership_status

            self.ticket_price = self.ticket_price * 0.85
            # reduce 15% off.

        return self.ticket_price
        # return the ticket's <ticket_price>.

    def get_ticket_price(self) -> float:
        """
        The getter function to get the <ticket_price>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.calculate_ticket_price()
        180.0
        >>> ticket_123.get_ticket_price()
        180.0
        """
        return self.ticket_price
        # return the ticket's <ticket_price>.

    def get_seat_number(self) -> str:
        """
        The getter function to get the <seat_number>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_seat_number()
        '2B'
        """
        return self.seat_number
        # return the ticket's <seat_number>.

    def get_ticket_meal(self) -> Meal:
        """
        The getter function to get the <meal>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_seat_number()
        '2B'
        >>> burger = Burger()
        >>> ticket_123.set_meal(burger)
        >>> ticket_123.get_ticket_meal().get_meal_name()
        'Burger'
        """
        return self.meal
        # return the ticket's <meal>.

    def set_meal(self, meal: Meal) -> None:
        """
        The setter function add the <meal> to Ticket.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_seat_number()
        '2B'
        >>> burger = Burger()
        >>> ticket_123.set_meal(burger)
        >>> ticket_123.get_ticket_meal().get_meal_name()
        'Burger'
        """
        self.meal = meal
        # self.passenger.update_account_balance(-meal.get_meal_price())
        # set the ticket's <meal>.

    def cancel_seat_number(self) -> None:
        """
        Cancel the seat number.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_seat_number()
        '2B'
        """
        self.seat_number = None
        # define the ticket's <seat_number> to be none.

    def change_seat_number(self, new_seat_number: str) -> None:
        """
        Change the seat_number to given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_seat_number()
        '2B'
        """
        self.seat_number = new_seat_number
        # set the ticket's <new_seat_number> to be the given new_seat_number.

    def get_passenger_name(self) -> str:
        """
        The getter function to get the <passenger_name>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_passenger_name()
        'Jay Chou'
        """
        return self.passenger.get_passenger_name()
        # return the ticket's <passenger_name>.

    def cancel_passenger(self) -> None:
        """
        Cancel the passenger for this ticket.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_passenger_name()
        'Jay Chou'
        >>> ticket_123.cancel_passenger()
        """
        self.passenger = None
        # define the ticket's <passenger> to be none.

    def refund_ticket_price(self) -> None:
        """
        Cancel the passenger for this ticket.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_passenger_name()
        'Jay Chou'
        >>> ticket_123.passenger.get_account_balance()
        0.0
        >>> ticket_123.refund_ticket_price()
        >>> ticket_123.passenger.get_account_balance()
        180.0
        """
        self.passenger.update_account_balance(self.get_ticket_price())
        # refund the ticket price to passenger.

    def change_passenger_name(self, new_passenger_name: Passenger) -> None:
        """
        Change the passenger_name to given string.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_passenger_name()
        'Jay Chou'
        """
        self.passenger = new_passenger_name
        # set the ticket's <passenger> to be the given new_passenger_name.

    def update_check_in_status(self) -> None:
        """
        Change the check_in_status to true.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_passenger_name()
        'Jay Chou'
        >>> ticket_123.get_ticket_check_in_status()
        False
        >>> ticket_123.update_check_in_status()
        >>> ticket_123.get_ticket_check_in_status()
        True
        """
        self.check_in_status = True
        # set the ticket's <check_in_status> to be True.

    def get_flight_number(self) -> str:
        """
        The getter function to get the <flight_number>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_flight_number()
        'AC123'
        """
        return self.flight.get_flight_number()
        # return the ticket's <flight_number>.

    def get_ticket_information_dictionary(self) -> dict:
        """
        The getter function to get the <flight_number>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_flight_number()
        'AC123'
        >>> ticket_123.get_ticket_information_dictionary()["ticket_id"]
        '123'
        """
        return self.ticket_information_dictionary
        # return the ticket's <ticket_information_dictionary>.

    def get_ticket_check_in_status(self) -> bool:
        """
        The getter function to get the <flight_number>.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.get_flight_number()
        'AC123'
        >>> ticket_123.get_ticket_information_dictionary()["ticket_id"]
        '123'
        >>> ticket_123.get_ticket_check_in_status()
        False
        """
        return self.check_in_status
        # return the ticket's <ticket_information_dictionary>.

    def print_ticket_information(self) -> None:
        """
        Print the ticket related information.
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_123.calculate_ticket_price()
        180.0
        >>> ticket_123.update_check_in_status()
        >>> ticket_123.print_ticket_information()
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  True
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        """
        print('Ticket ID: ', self.ticket_id)
        print('Ticket Price: ', self.ticket_price)
        print('Ticket Seat Number: ', self.seat_number)
        if self.passenger is not None:
            print('Passenger Name For This Ticket: ',
                  self.passenger.passenger_name)
        else:
            print('Passenger Name For This Ticket: ', self.passenger)
        print('Check-In status For This Ticket: ',
              self.get_ticket_check_in_status())
        if self.meal is not None:
            print('Selected Meal For This Ticket: ',
                  self.get_ticket_meal().get_meal_name())
        else:
            print('Selected Meal For This Ticket: ', self.meal)
        print('Flight Number For This Ticket: ',
              self.flight.get_flight_number())

        # return the flight's related information.


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
    passenger_jay = Passenger("Jay Chou", "JC123456")
    # Define new passenger.

    ac123departure_time = Time(2020, 11, 18, 19, 20).time_in_string()
    # Define the departure_time

    ac123arrival_time = Time(2020, 11, 19, 2, 30).time_in_string()
    # Define the arrival_time

    helicopter = Helicopter()
    # initial a helicopter

    helicopter_capacity = helicopter.get_max_capacity()
    # calculate the helicopter capacity

    flight_helicopter = Flight("AC123", "Montreal", "Toronto",
                               ac123departure_time, ac123arrival_time,
                               "1A", helicopter, helicopter_capacity)
    # Initial a flight.

    ticket_123 = Ticket("123", "2B", passenger_jay, flight_helicopter)
    # Create a new ticket

    ticket_123.get_ticket_id()
    # Get the ticket id

    ticket_123.get_seat_number()
    # Get the ticket seat_number

    ticket_123.get_passenger_name()
    # Get the ticket passenger_name

    ticket_123.get_flight_number()
    # Get the ticket flight_number

    ticket_123.calculate_ticket_price()
    # Get the ticket price

    ticket_123.print_ticket_information()
    # Get the ticket information

    print('\n-----------------------------------------------------------------')
    print('\nAfter update membership status:')
    passenger_jay.update_membership_status()
    # update passenger jay membership status

    ticket_123.calculate_ticket_price()
    # Get the ticket price

    ticket_123.print_ticket_information()
    # Get the ticket information
