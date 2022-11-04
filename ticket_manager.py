"""
Student Name: Qiaoru Zhang
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

from ticket import Ticket
# Import another file ticket

from datetime import datetime
# Import datetime

from Meal import *


class TicketManager:
    # Define a class TicketManager
    """
    A class representing a Ticket Manager.
    Each Ticket Manager has one instance attributes ticket_dictionary which is
    a dictionary which store all the tickets.
    The dictionary key is the tickets, and the values are the tickets
    related information.

    === Public Attributes ===
    ticket_dictionary: A dictionary which store all the tickets.
    The dictionary key is the tickets, and the values are the tickets
    related information

    === Representation Variants ===
    - len(ticket_dictionary) >= 0

    === Sample Usage ===
    >>> ticket_manager = TicketManager()
    >>> passenger_jay = Passenger("Jay Chou","JC123456")
    >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
    >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
    >>> helicopter = Helicopter()
    >>> helicopter_capacity = helicopter.get_max_capacity()
    >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
    ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
    ...     helicopter_capacity)
    >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
    >>> ticket_manager.add_ticket(ticket_123)
    >>> ticket_manager.calculate_ticket_price(ticket_123)
    180.0
    >>> passenger_jay.update_membership_status()
    >>> ticket_manager.calculate_ticket_price(ticket_123)
    153.0
    >>> ticket_manager.check_ticket("123")
    True
    >>> ticket_manager.print_ticket_information(ticket_123)
    Ticket ID:  123
    Ticket Price:  153.0
    Ticket Seat Number:  2B
    Passenger Name For This Ticket:  Jay Chou
    Check-In status For This Ticket:  False
    Selected Meal For This Ticket:  None
    Flight Number For This Ticket:  AC123
    >>> ticket_manager.modify_ticket_seat_number(ticket_123,
    ...     flight_helicopter, '1A')
    >>> burger = Burger()
    >>> ticket_manager.set_meal(ticket_123, burger)
    >>> ticket_manager.print_ticket_information(ticket_123)
    Ticket ID:  123
    Ticket Price:  153.0
    Ticket Seat Number:  1A
    Passenger Name For This Ticket:  Jay Chou
    Check-In status For This Ticket:  False
    Selected Meal For This Ticket:  Burger
    Flight Number For This Ticket:  AC123
    >>> ticket_manager.cancel_ticket(ticket_123, flight_helicopter)
    >>> ticket_manager.print_ticket_information(ticket_123)
    This ticket is not in system.
    """
    # Define public attributes type
    ticket_dictionary: dict

    def __init__(self) -> None:
        """
        Create a new passenger with unique <ticket_id>,
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
        self.ticket_dictionary = {}
        # Initialize ticket_dictionary to be empty dictionary.

    def add_ticket(self, ticket: Ticket) -> None:
        """
        Add the ticket to the ticket_dictionary.
        """
        if ticket not in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            self.ticket_dictionary[ticket] \
                = ticket.get_ticket_information_dictionary()
            # Assign the ticket as the key and the dictionary as the value.

    def calculate_ticket_price(self, ticket: Ticket) -> float:
        """
        calculate the ticket price based on the flight type and passenger
        membership status.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        180.0
        >>> passenger_jay.update_membership_status()
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        153.0
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            ticket.calculate_ticket_price()
            # Get the ticket price

        return ticket.get_ticket_price()
        # return the ticket price

    def check_ticket(self, ticket_number: str) -> bool:
        """
        Check the ticket is in the ticket_dictionary or not.
        add back the booked seats to the flight.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.check_ticket("123")
        True
        """
        for ticket in self.ticket_dictionary:
            # for each ticket in ticket_dictionary

            if ticket.get_ticket_id() == ticket_number:
                # if the ticket id is same with the given ticket_number

                return True
                # return True

        return False
        # return False

    def update_check_in_status(self, ticket: Ticket) -> None:
        """
        Update check in status for the ticket.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        180.0
        >>> passenger_jay.update_membership_status()
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        153.0
        >>> ticket_manager.update_check_in_status(ticket_123)
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  153.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  True
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            ticket.update_check_in_status()
            # Check in the ticket

        else:
            print("This ticket is not in system.")

    def set_meal(self, ticket: Ticket, meal: Meal) -> None:
        """
        Set the meal for the ticket.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        180.0
        >>> passenger_jay.update_membership_status()
        >>> ticket_manager.calculate_ticket_price(ticket_123)
        153.0
        >>> ticket_manager.update_check_in_status(ticket_123)
        >>> burger = Burger()
        >>> ticket_manager.set_meal(ticket_123, burger)
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  153.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  True
        Selected Meal For This Ticket:  Burger
        Flight Number For This Ticket:  AC123
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            ticket.set_meal(meal)
            # Get the ticket price

        else:
            print("This ticket is not in system.")

    def get_ticket(self, ticket_number: str) -> Optional[Ticket]:
        """
        Return the ticket besed on the given ticket number in string format.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.check_ticket("123")
        True
        >>> ticket_manager.get_ticket("123").get_ticket_id()
        '123'
        """
        for ticket in self.ticket_dictionary:
            # for each ticket in ticket_dictionary

            if ticket.get_ticket_id() == ticket_number:
                # if the ticket id is same with the given ticket_number

                return ticket
                # return ticket

        return None
        # return None

    def cancel_ticket(self, ticket: Ticket, flight: Flight) -> None:
        """
        Cancel the ticket, delete the passenger and booked seat to None,
        add back the booked seats to the flight.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        >>> ticket_manager.cancel_ticket(ticket_123, flight_helicopter)
        >>> ticket_manager.print_ticket_information(ticket_123)
        This ticket is not in system.
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            current_time = datetime.now()
            # get the current time

            current_time_string = current_time.strftime("%Y/%m/%d %H:%M:%S")
            # convert current time to string.

            current_year = int(current_time_string[0:4])
            # get the current year.

            current_month = int(current_time_string[5:7])
            # get the current month.

            current_day = int(current_time_string[8:10])
            # get the current day.

            current_hour = int(current_time_string[11:13])
            # get the current hour.

            boarding_time = flight.get_departure_time()
            # get the departure time

            boarding_year = int(boarding_time[0:4])
            # get the boarding year.

            boarding_month = int(boarding_time[7:9])
            # get the boarding month.

            boarding_day = int(boarding_time[12:14])
            # get the boarding day.

            boarding_hour = int(boarding_time[16:18])
            # get the boarding hour.

            if current_year == boarding_year and \
                    current_month == boarding_month and \
                    (current_day <= (int(boarding_day) - 1)) and \
                    current_hour >= (boarding_hour - 24):
                # check if the current time is less than boarding_time in
                # 24 hours.

                ticket.passenger.update_account_balance(
                    -flight.get_flight_price() * 0.9)
                # delete 10% off for the ticket price to account balance.
            else:
                ticket.refund_ticket_price()

            flight.cancel_flight_seat(ticket.seat_number)
            # cancel the flight_seat

            if ticket in ticket.passenger.purchase_history["Tickets"]:
                ticket.passenger.purchase_history["Tickets"].remove(ticket)
                # remove ticket from purchase history.

                ticket.passenger.update_mileage(-
                                                ticket.flight.get_flight_mileage())

                ticket.passenger.update_redeem_points(
                    -ticket.flight.get_flight_mileage() / 10)

            del self.ticket_dictionary[ticket]
            # delete the ticket from the dictionary

        else:
            print("This ticket is not in system.")

    def modify_ticket_seat_number(self, ticket: Ticket, flight: Flight,
                                  new_seat_number: str) -> None:
        """
        Modify the ticket seat number to give string.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        >>> ticket_manager.modify_ticket_seat_number(ticket_123,
        ...     flight_helicopter, '1A')
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  1A
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            flight.cancel_flight_seat(ticket.seat_number)
            # cancel the flight to give new_seat_number.

            flight.update_flight_seat(new_seat_number)

            ticket.change_seat_number(new_seat_number)
            # change the seat_number to give new_seat_number.

        else:
            print("This ticket is not in system.")

    def return_ticket_flight(self, ticket_number: str) -> Flight:
        """
        Return the ticket flight by the give string.
        >>> ticket_manager = TicketManager()
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> ticket_manager.add_ticket(ticket_123)
        >>> ticket_manager.print_ticket_information(ticket_123)
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        >>> ticket_manager.return_ticket_flight("123").print_flight_information()
        Flight Number:  AC123
        Origin City:  Montreal
        Destination City:  Toronto
        Departure Time:  2020 / 11 / 18  19:20
        Arrival Time:  2020 / 11 / 19  2:30
        Boarding Gate:  1A
        Flight Type:  Helicopter
        Total Seats Capacity:  2
        Seat Occupancy Rate:  0.0 %
        Current Seat Number Lists:  ['1A', '2B']
        """
        for one_ticket in self.ticket_dictionary:
            if one_ticket.ticket_id == ticket_number:
                return one_ticket.flight
        else:
            print("This ticket is not in system.")

    def print_ticket_information(self, ticket: Ticket) -> None:
        """
        Return the ticket related information.
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
        >>> ticket_123.print_ticket_information()
        Ticket ID:  123
        Ticket Price:  180.0
        Ticket Seat Number:  2B
        Passenger Name For This Ticket:  Jay Chou
        Check-In status For This Ticket:  False
        Selected Meal For This Ticket:  None
        Flight Number For This Ticket:  AC123
        """
        if ticket in self.ticket_dictionary:
            # check if the given ticket in the flight_dictionary or not.

            ticket.print_ticket_information()
            # Get the ticket information

        else:
            print("This ticket is not in system.")


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
    ticket_manager = TicketManager()
    # Initialize a new ticket manager.

    passenger_jay = Passenger("Jay Chou", "JC123456")
    # Create passenger Jay Chou

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

    ticket_manager.add_ticket(ticket_123)
    # add the ticket to the ticket_manager

    ticket_manager.calculate_ticket_price(ticket_123)
    # calculate ticket price

    passenger_jay.update_membership_status()
    # update passenger jay membership status

    ticket_manager.calculate_ticket_price(ticket_123)
    # calculate ticket price

    ticket_manager.check_ticket("123")
    # check the ticket with the given ID

    print("--------------------------------------------------------------------"
          "------------\n")
    print('Ticket Information:')
    ticket_manager.print_ticket_information(ticket_123)
    # Get the ticket information

    ticket_manager.modify_ticket_seat_number(ticket_123,
                                             flight_helicopter, '1A')
    # modify ticket seat number

    print("--------------------------------------------------------------------"
          "------------\n")
    print('After update seat number:')
    ticket_manager.print_ticket_information(ticket_123)
    # Get the ticket information

    print("--------------------------------------------------------------------"
          "------------\n")
    print('After update meal and check in:')
    burger = Burger()
    ticket_manager.set_meal(ticket_123, burger)
    ticket_manager.update_check_in_status(ticket_123)
    ticket_manager.print_ticket_information(ticket_123)
    # Get the ticket information

    print("--------------------------------------------------------------------"
          "------------\n")
    print('After cancel the ticket:')
    ticket_manager.cancel_ticket(ticket_123, flight_helicopter)
    # cancel ticket
    ticket_manager.print_ticket_information(ticket_123)
    # Get the ticket information
