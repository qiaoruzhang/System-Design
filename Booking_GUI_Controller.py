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
# import sys
#
# sys.setrecursionlimit(100000)

from flight import *
# Import another file flight
from ticket import Ticket
# Import another file ticket
from time_in_strings import Time
# Import another file time_in_strings
from passenger import Passenger
# Import another file passenger
from passenger_manager import PassengerManager
# Import another file passenger_manager
from ticket_manager import TicketManager
# Import another file ticket_manager
from flight_manager import FlightManager
# Import another file flight_manager
from Meal import *
# Import Meal file
from RedeemItems import *
# Import RedeemItems file

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Import tkinter,PIL

passenger_manager = PassengerManager()
# initial a PassengerManager
passenger_jay = Passenger("Jay Chou", "JC123456")
# Create passenger Jay Chou
passenger_manager.add_passengers(passenger_jay)
# add the passenger to passenger_manager
passenger_manager.create_account(passenger_jay, "JayChou", "JC123456")
# register an online account
passenger_manager.update_account_balance(passenger_jay, 3000)
# load 3000.0 to account balance

# Create passenger Maggie Zhang
passenger_maggie = Passenger("Maggie Zhang", "MZ123456")
# Create passenger Maggie Zhang
passenger_manager.add_passengers(passenger_maggie)
# add the passenger to passenger_manager
passenger_manager.create_account(passenger_maggie, "MaggieZhang", "MZ123456")
# register an online account
passenger_manager.update_account_balance(passenger_maggie, 2000)
# load 3000.0 to account balance

# Create flights and add then into system.
# setup helicopter flights
AC123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
# Define the departure_time
AC123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
# Define the arrival_time
AC123helicopter = Helicopter()
# initial a helicopter
AC123helicopter_capacity = AC123helicopter.get_max_capacity()
# calculate the helicopter capacity
AC123flight_helicopter = Flight("AC123", "Montreal", "Toronto",
                                AC123departure_time,
                                AC123arrival_time, "1A",
                                AC123helicopter,
                                AC123helicopter_capacity)
# Initial a flight.

# Initial a flight.
AC321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
# Define the departure_time
AC321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
# Define the arrival_time
AC321helicopter = Helicopter()
# initial a helicopter
AC321helicopter_capacity = AC321helicopter.get_max_capacity()
# calculate the helicopter capacity
AC321flight_helicopter = Flight("AC321", "Toronto", "Montreal",
                                AC321departure_time,
                                AC321arrival_time, "1A",
                                AC321helicopter,
                                AC321helicopter_capacity)
# Initial a flight.

# Initial a flight.
# setup small airliner flights
SA123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
# Define the departure_time
SA123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
# Define the arrival_time
SA123small_airliner = SmallAirliner()
# initial a SmallAirliner
SA123small_airliner_capacity = SA123small_airliner.get_max_capacity()
# calculate the SmallAirliner capacity
SA123flight_small_airliner = Flight("SA123", "Montreal", "Toronto",
                                    SA123departure_time,
                                    SA123arrival_time, "2A",
                                    SA123small_airliner,
                                    SA123small_airliner_capacity)
# Initial a flight.

# Initial a flight.
SA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
# Define the departure_time
SA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
# Define the arrival_time
SA321small_airliner = SmallAirliner()
# initial a SmallAirliner
SA321small_airliner_capacity = SA321small_airliner.get_max_capacity()
# calculate the SmallAirliner capacity
SA321flight_small_airliner = Flight("SA321", "Toronto", "Montreal",
                                    SA321departure_time,
                                    SA321arrival_time, "2A",
                                    SA321small_airliner,
                                    SA321small_airliner_capacity)
# Initial a flight.

# Initial a flight.
# setup large airliner flights
LA123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
# Define the departure_time
LA123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
# Define the arrival_time
LA123large_airliner = LargeAirliner()
# initial a LargeAirliner
LA123large_airliner_capacity = LA123large_airliner.get_max_capacity()
# calculate the LargeAirliner capacity
LA123flight_large_airliner = Flight("LA123", "Montreal", "Toronto",
                                    LA123departure_time,
                                    LA123arrival_time, "3A",
                                    LA123large_airliner,
                                    LA123large_airliner_capacity)
# Initial a flight.

# Initial a flight.
LA321departure_time = Time(2021, 11, 19, 19, 20).time_in_string()
# Define the departure_time
LA321arrival_time = Time(2021, 11, 20, 2, 30).time_in_string()
# Define the arrival_time
LA321large_airliner = LargeAirliner()
# initial a LargeAirliner
LA321large_airliner_capacity = LA321large_airliner.get_max_capacity()
# calculate the LargeAirliner capacity
LA321flight_large_airliner = Flight("LA321", "Toronto", "Montreal",
                                    LA321departure_time,
                                    LA321arrival_time, "3A",
                                    LA321large_airliner,
                                    LA321large_airliner_capacity)
# Initial a flight.

# create a fight manager
flight_manager = FlightManager()
# add the flights to the flight_manager
flight_manager.add_flight(AC123flight_helicopter)
flight_manager.add_flight(AC321flight_helicopter)
flight_manager.add_flight(SA123flight_small_airliner)
flight_manager.add_flight(SA321flight_small_airliner)
flight_manager.add_flight(LA123flight_large_airliner)
flight_manager.add_flight(LA321flight_large_airliner)

# generate route to the flight_manager
flight_manager.generate_route(AC123flight_helicopter)
flight_manager.generate_route(AC321flight_helicopter)
flight_manager.generate_route(SA123flight_small_airliner)
flight_manager.generate_route(SA321flight_small_airliner)
flight_manager.generate_route(LA123flight_large_airliner)
flight_manager.generate_route(LA321flight_large_airliner)

# create a ticket manager and add existing tickets.
ticket_manager = TicketManager()
# Initialize a new ticket manager.
ticket_123 = Ticket("123", "2B", passenger_jay, AC123flight_helicopter)
# Create a new ticket
ticket_321 = Ticket("321", "2B", passenger_maggie, SA321flight_small_airliner)
# Create a new ticket

ticket_manager.add_ticket(ticket_123)
# add the ticket to the ticket_manager
ticket_manager.add_ticket(ticket_321)
# add the ticket to the ticket_manager

ticket_123.calculate_ticket_price()
# calculate ticket price
ticket_321.calculate_ticket_price()
# calculate ticket price

passenger_manager.update_account_balance(passenger_jay,
                                         -ticket_123.calculate_ticket_price())
# update passenger jay membership status
passenger_manager.update_account_balance(passenger_maggie,
                                         -ticket_321.calculate_ticket_price())
# update passenger maggie membership status

flight_manager.update_flight_seat(AC123flight_helicopter, ticket_123)
# update flight seat
flight_manager.update_flight_seat(SA321flight_small_airliner, ticket_321)
# update flight seat

LARGEFONT = ("Verdana", 35)


class BookingTicket(tk.Tk):
    frames = {}

    # __init__ function for class BookingTicket
    def __init__(self, *args, **kw) -> None:

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kw)
        self.shared_data = {"username": tk.StringVar(),
                            "new_name": tk.StringVar(),
                            "passenger": None,
                            "flight_number": tk.StringVar(),
                            "ticket": None,
                            "modify_ticket": tk.StringVar()}

        # creating a container
        self.geometry("1000x2000")
        container = tk.Frame(self, background="grey")
        container.place(x=1000, y=0, anchor="nw", width=2000, height=2000)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        # self.frames = {}
        self.pages = ()
        self.pages += (StartPage,
                       Login,
                       CreateAccount,
                       MainMenu,
                       CreateOnlineAccount,
                       ManageAccount,
                       ShowPersonalInfo,
                       ModifyPersonalInformation,
                       ChangeName,
                       ChangePassport,
                       ChangeUserName,
                       ChangePassword,
                       LoadBalance,
                       LoadBalanceBuyTicket,
                       LoadBalanceBuyMeal,
                       UpdateMembership,
                       BookFlightNumber,
                       BookSeatNumber,
                       ShowTicket,
                       RedeemItemsMenu,
                       CheckBookedTicket,
                       UpdateCheckIn,
                       ModifyTicketSeat,
                       CancelTicket,
                       RatingSystem
                       )

        # iterating through a tuple consisting
        # of the different page layouts
        for F in self.pages:
            frame = F(container, self)
            # initializing frame of that object from
            # startpage, Login, CreateAccount ... respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        print("---------------", cont, "---------------")
        if len(frame.controller.shared_data["username"].get()) > 0:

            print("***********", frame.controller.shared_data["username"].get(),
                  "***********")
            print(frame.controller.shared_data["username"].get())
            print(passenger_manager.get_current_passenger(
                frame.controller.shared_data[
                    "username"].get()).print_passenger_information())
            frame.controller.shared_data[
                "passenger"] = passenger_manager.get_current_passenger(
                frame.controller.shared_data["username"].get())
            print(frame.controller.shared_data["flight_number"].get())
            print(frame.controller.shared_data["modify_ticket"].get())
            if len(frame.controller.shared_data["modify_ticket"].get()) > 0:
                print(ticket_manager.get_ticket(frame.controller.shared_data[
                                                    "modify_ticket"].get()).print_ticket_information())
        elif len(frame.controller.shared_data["new_name"].get()) > 0:
            print("***********", frame.controller.shared_data["new_name"].get(),
                  "***********")
            print(frame.controller.shared_data["new_name"].get())
            print(passenger_manager.check_current_passenger(
                frame.controller.shared_data[
                    "new_name"].get()).print_passenger_information())
            frame.controller.shared_data[
                "passenger"] = passenger_manager.check_current_passenger(
                frame.controller.shared_data["new_name"].get())
            print(frame.controller.shared_data["flight_number"].get())
            print(frame.controller.shared_data["modify_ticket"].get())
            if len(frame.controller.shared_data["modify_ticket"].get()) > 0:
                if ticket_manager.get_ticket(frame.controller.shared_data[
                                                 "modify_ticket"].get()) is not None:
                    print(
                        ticket_manager.get_ticket(frame.controller.shared_data[
                                                      "modify_ticket"].get()).print_ticket_information())
            print(
                passenger_manager.print_passenger_ticket_history(
                    frame.controller.shared_data["passenger"])
            )
        frame.tkraise()


# first window frame start page

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self,
                          text="Welcome to Flight-ticket booking system! ",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=150, y=200)

        # label of frame Layout 2
        label2 = ttk.Label(self, text="Do you already have an account? ",
                           font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label2.grid(row=0, column=4, padx=300, pady=10)
        label2.place(x=220, y=300)

        button1 = ttk.Button(self, text="Yes",
                             command=lambda: controller.show_frame(
                                 Login))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
        button1.place(x=450, y=450)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="No",
                             command=lambda: controller.show_frame(
                                 CreateAccount))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
        button2.place(x=450, y=500)


# second window frame page1
class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Log In Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=400, y=200)

        # label of frame Layout 2
        label_username = ttk.Label(self, text="Username",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_username.grid(row=0, column=4, padx=300, pady=10)
        label_username.place(x=200, y=300)

        # Entry 1
        # create a text entry box
        username_textbox = ttk.Entry(self,
                                     textvariable=self.controller.shared_data[
                                         "username"])
        # Place the text entry box
        username_textbox.place(x=400, y=300)

        # label of frame Layout 2
        label_Password = ttk.Label(self, text="Password",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_Password.grid(row=0, column=4, padx=300, pady=10)
        label_Password.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        password = tk.StringVar()
        password_textbox = ttk.Entry(self, textvariable=password)
        # Place the text entry box
        password_textbox.place(x=400, y=350)

        # wrong_name_message = "      "

        wrong_name = tk.Label(self,
                              text="      ",
                              font=("Verdana", 20))
        # putting the grid in its place by using
        # grid
        wrong_name.grid(row=0, column=4, padx=300, pady=10)
        wrong_name.place(x=600, y=300)

        # wrong_password_message = "      "

        wrong_password = tk.Label(self,
                                  text="      ",
                                  font=("Verdana", 20))
        # putting the grid in its place by using
        # grid
        wrong_password.grid(row=0, column=4, padx=300, pady=10)
        wrong_password.place(x=600, y=350)

        def check_username_and_password(user_input_username,
                                        user_input_password) -> None:
            if not passenger_manager.check_account_username(
                    user_input_username):
                wrong_name.config(text="Your input username is not exits")
            elif passenger_manager.check_account_username(
                    user_input_username):
                wrong_name.config(text="Your input username is correct")
                if not passenger_manager.check_account_password(
                        user_input_username, user_input_password):
                    wrong_password.config(
                        text="Your input password is not correct")
                elif passenger_manager.check_account_password(
                        user_input_username, user_input_password):
                    wrong_password.config(text="Your input password is correct")

        def login() -> None:
            user_input_username = username_textbox.get()
            user_input_password = password_textbox.get()
            if not passenger_manager.check_account_username(
                    user_input_username) or \
                    not passenger_manager.check_account_password(
                        user_input_username, user_input_password):
                check_username_and_password(user_input_username,
                                            user_input_password)
            else:
                self.controller.shared_data[
                    "passenger"] = passenger_manager.get_current_passenger(
                    user_input_username)
                controller.show_frame(MainMenu)

        # layout2
        button_confirm = ttk.Button(self, text="Confirm",
                                    command=login)
        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Start Page",
                                 command=lambda: controller.show_frame(
                                     StartPage))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Create Account Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_name = ttk.Label(self, text="Name",
                               font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_name.grid(row=0, column=4, padx=300, pady=10)
        label_name.place(x=250, y=300)

        # Entry 1
        # create a text entry box
        name_textbox = ttk.Entry(self,
                                 textvariable=self.controller.shared_data[
                                     "new_name"])
        # Place the text entry box
        name_textbox.place(x=400, y=300)

        # label of frame Layout 2
        label_Passport = ttk.Label(self, text="Passport Number",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_Passport.grid(row=0, column=4, padx=300, pady=10)
        label_Passport.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        passport = tk.StringVar()
        passport_textbox = ttk.Entry(self, textvariable=passport)
        # Place the text entry box
        passport_textbox.place(x=400, y=350)

        def create_account():
            new_passenger_name = name_textbox.get()
            # Get the name from input

            new_passenger_passport = passport_textbox.get()
            # Let user enter their passport

            # create a new passenger
            new_passenger = Passenger(new_passenger_name,
                                      new_passenger_passport)

            # add the passenger to passenger_manager
            passenger_manager.add_passengers(new_passenger)

            # Create new passenger
            self.controller.shared_data["passenger"] = new_passenger
            controller.show_frame(MainMenu)

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=create_account)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Start Page",
                                 command=lambda: controller.show_frame(
                                     StartPage))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)

    # def return_new_passenger(self) -> Passenger:
    #     return self.passenger


# third window frame page2
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Ticket Reservation System Menu",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=200)

        # button_Register
        button_Register = ttk.Button(self,
                                     text="Register an online account",
                                     command=lambda: controller.show_frame(
                                         CreateOnlineAccount
                                     ))

        # putting the button in its place by
        # using grid
        button_Register.grid(row=2, column=1, padx=10, pady=10)
        button_Register.place(x=350, y=300)

        # button_Manage
        button_Manage = ttk.Button(self, text="Manage your account",
                                   command=lambda: controller.show_frame(
                                       ManageAccount))

        # putting the button in its place by
        # using grid
        button_Manage.grid(row=2, column=1, padx=10, pady=10)
        button_Manage.place(x=350, y=350)

        # button_Book
        button_Book = ttk.Button(self, text="Book ticket",
                                 command=lambda: controller.show_frame(
                                     BookFlightNumber))
        # putting the button in its place by
        # using grid
        button_Book.grid(row=2, column=1, padx=10, pady=10)
        button_Book.place(x=350, y=400)

        # button_Manage_Ticket
        button_Manage_Ticket = ttk.Button(self,
                                          text="Manage your booked ticket",
                                          command=lambda: controller.show_frame(
                                              CheckBookedTicket))
        # putting the button in its place by
        # using grid
        button_Manage_Ticket.grid(row=2, column=1, padx=10, pady=10)
        button_Manage_Ticket.place(x=350, y=450)

        # button_Manage_Ticket
        button_Manage_Ticket = ttk.Button(self,
                                          text="Redeem Items",
                                          command=lambda: controller.show_frame(
                                              RedeemItemsMenu))
        # putting the button in its place by
        # using grid
        button_Manage_Ticket.grid(row=2, column=1, padx=10, pady=10)
        button_Manage_Ticket.place(x=350, y=500)

        # button_Manage_Ticket
        button_Manage_Ticket = ttk.Button(self,
                                          text="Rating this System",
                                          command=lambda: controller.show_frame(
                                              RatingSystem))
        # putting the button in its place by
        # using grid
        button_Manage_Ticket.grid(row=2, column=1, padx=10, pady=10)
        button_Manage_Ticket.place(x=350, y=550)

        # layout2
        button_back = ttk.Button(self, text="Back to Start Page",
                                 command=lambda: controller.show_frame(
                                     StartPage))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


# third window frame page2
class CreateOnlineAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label of frame Layout
        label = ttk.Label(self,
                          text="Create Online Account Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=100)

        # label of frame Layout
        sucesslabel = ttk.Label(self,
                                text="Please press confirm button to register "
                                     "your online account",
                                font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        sucesslabel.grid(row=0, column=4, padx=300, pady=10)
        sucesslabel.place(x=200, y=200)

        # label of frame Layout 2
        label_new_username = ttk.Label(self, text="Username",
                                       font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_new_username.grid(row=0, column=4, padx=300, pady=10)
        label_new_username.place(x=250, y=300)

        # Entry 1
        # create a text entry box
        new_username = tk.StringVar()
        new_username_textbox = ttk.Entry(self, textvariable=new_username)
        # Place the text entry box
        new_username_textbox.place(x=400, y=300)

        # label of frame Layout 2
        label_new_Passport = ttk.Label(self, text="Password",
                                       font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_new_Passport.grid(row=0, column=4, padx=300, pady=10)
        label_new_Passport.place(x=250, y=350)

        # Entry 2
        # create a text entry box
        new_passport = tk.StringVar()
        new_passport_textbox = ttk.Entry(self, textvariable=new_passport)
        # Place the text entry box
        new_passport_textbox.place(x=400, y=350)

        def register_online() -> None:
            new_passenger_username = new_username_textbox.get()
            # Get the name from input
            new_passenger_password = new_passport_textbox.get()
            # Let user enter their passport
            if len(self.controller.shared_data["username"].get()) > 0:
                passenger_manager.create_account(
                    self.controller.shared_data["passenger"],
                    new_passenger_username,
                    new_passenger_password)
            elif len(self.controller.shared_data["new_name"].get()) > 0:
                passenger_manager.create_account(
                    self.controller.shared_data["passenger"],
                    new_passenger_username,
                    new_passenger_password)
            sucesslabel.config(
                text="Congratulations! Your Online Account has been "
                     "created successfully.", foreground="green")

        # layout2
        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=register_online)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=250, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu Page",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class ManageAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Account Manager Menu",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # button_Register
        button_Register = ttk.Button(self,
                                     text="Show personal information",
                                     command=lambda: controller.show_frame(
                                         ShowPersonalInfo
                                     ))
        # putting the button in its place by
        # using grid
        button_Register.grid(row=2, column=1, padx=10, pady=10)
        button_Register.place(x=350, y=300)

        # button_Manage
        button_Manage = ttk.Button(self, text="Modify personal information",
                                   command=lambda: controller.show_frame(
                                       ModifyPersonalInformation))
        # putting the button in its place by
        # using grid
        button_Manage.grid(row=2, column=1, padx=10, pady=10)
        button_Manage.place(x=350, y=350)

        # button_Book
        button_Book = ttk.Button(self, text="Load Balance Amount",
                                 command=lambda: controller.show_frame(
                                     LoadBalance))
        # putting the button in its place by
        # using grid
        button_Book.grid(row=2, column=1, padx=10, pady=10)
        button_Book.place(x=350, y=400)

        # button_Manage_Ticket
        button_Manage_Ticket = ttk.Button(self,
                                          text="Update Membership Status",
                                          command=lambda: controller.show_frame(
                                              UpdateMembership))
        # putting the button in its place by
        # using grid
        button_Manage_Ticket.grid(row=2, column=1, padx=10, pady=10)
        button_Manage_Ticket.place(x=350, y=450)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu Page",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class ShowPersonalInfo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Display Personal Information",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)
        # label of frame Layout

        # label of frame Layout
        personal_info_name = ttk.Label(self,
                                       text="Passenger Name:",
                                       font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_name.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_name.place(x=250, y=150)

        # label of frame Layout
        personal_name = ttk.Label(self,
                                  text="",
                                  font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_name.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_name.place(x=600, y=150)

        # label of frame Layout
        personal_info_Passport = ttk.Label(self,
                                           text="Passenger Passport:",
                                           font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Passport.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Passport.place(x=250, y=200)

        # label of frame Layout
        personal_Passport = ttk.Label(self,
                                      text="",
                                      font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Passport.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Passport.place(x=600, y=200)

        # label of frame Layout
        personal_info_Username = ttk.Label(self,
                                           text="Passenger Account Username:",
                                           font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Username.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Username.place(x=250, y=250)

        # label of frame Layout
        personal_Username = ttk.Label(self,
                                      text="",
                                      font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Username.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Username.place(x=600, y=250)

        # label of frame Layout
        personal_info_Password = ttk.Label(self,
                                           text="Passenger Account Password:",
                                           font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Password.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Password.place(x=250, y=300)

        # label of frame Layout
        personal_Password = ttk.Label(self,
                                      text="",
                                      font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Password.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Password.place(x=600, y=300)

        # label of frame Layout
        personal_info_Balance = ttk.Label(self,
                                          text="Passenger Account Balance:",
                                          font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Balance.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Balance.place(x=250, y=350)

        # label of frame Layout
        personal_Balance = ttk.Label(self,
                                     text="",
                                     font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Balance.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Balance.place(x=600, y=350)

        # label of frame Layout
        personal_info_Membership = ttk.Label(self,
                                             text="Passenger Membership Status:",
                                             font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Membership.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Membership.place(x=250, y=400)

        # label of frame Layout
        personal_Membership = ttk.Label(self,
                                        text="",
                                        font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Membership.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Membership.place(x=600, y=400)

        # label of frame Layout
        personal_info_Mileage = ttk.Label(self,
                                          text="Passenger Total Mileage:",
                                          font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Mileage.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Mileage.place(x=250, y=450)

        # label of frame Layout
        personal_Mileage = ttk.Label(self,
                                     text="",
                                     font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Mileage.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Mileage.place(x=600, y=450)

        # label of frame Layout
        personal_info_Points = ttk.Label(self,
                                         text="Passenger Redeem Points:",
                                         font=("Verdana", 20))
        # putting the grid in its place by using grid
        personal_info_Points.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_info_Points.place(x=250, y=500)

        # label of frame Layout
        personal_Points = ttk.Label(self,
                                    text="",
                                    font=("Verdana", 20, 'bold'))
        # putting the grid in its place by using grid
        personal_Points.grid(row=0, column=4, padx=300, pady=10)
        # label of frame Layout
        personal_Points.place(x=600, y=500)

        def show_personal_info() -> None:
            if len(self.controller.shared_data["username"].get()) > 0:
                personal_name.config(text=self.controller.shared_data[
                    "passenger"].get_passenger_name())
                personal_Passport.config(text=self.controller.shared_data[
                    "passenger"].get_passenger_passport())
                personal_Username.config(text=self.controller.shared_data[
                    "passenger"].get_account_username())
                personal_Password.config(text=self.controller.shared_data[
                    "passenger"].get_account_password())
                personal_Balance.config(text=self.controller.shared_data[
                    "passenger"].get_account_balance())
                personal_Membership.config(text=self.controller.shared_data[
                    "passenger"].get_membership_status())
                personal_Mileage.config(text=self.controller.shared_data[
                    "passenger"].get_mileage())
                personal_Points.config(text=self.controller.shared_data[
                    "passenger"].get_redeem_points())

            elif len(self.controller.shared_data["new_name"].get()) > 0:
                personal_name.config(text=self.controller.shared_data[
                    "passenger"].get_passenger_name()
                                     )
                personal_Passport.config(text=self.controller.shared_data[
                    "passenger"].get_passenger_passport())
                personal_Username.config(text=self.controller.shared_data[
                    "passenger"].get_account_username())
                personal_Password.config(text=self.controller.shared_data[
                    "passenger"].get_account_password())
                personal_Balance.config(text=self.controller.shared_data[
                    "passenger"].get_account_balance())
                personal_Membership.config(text=self.controller.shared_data[
                    "passenger"].get_membership_status())
                personal_Mileage.config(text=self.controller.shared_data[
                    "passenger"].get_mileage())
                personal_Points.config(text=self.controller.shared_data[
                    "passenger"].get_redeem_points())

        # layout2
        button_back = ttk.Button(self, text="Show Personal Info",
                                 command=show_personal_info)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=250, y=550)

        # layout2
        button_back = ttk.Button(self, text="Back to Manage Account Page",
                                 command=lambda: controller.show_frame(
                                     ManageAccount))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=650)


class ModifyPersonalInformation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Personal Information",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # button_Register
        button_Register = ttk.Button(self,
                                     text="Modify Personal Name",
                                     command=lambda: controller.show_frame(
                                         ChangeName))
        # putting the button in its place by
        # using grid
        button_Register.grid(row=2, column=1, padx=10, pady=10)
        button_Register.place(x=350, y=300)

        # button_Manage
        button_Manage = ttk.Button(self, text="Modify Personal Passport",
                                   command=lambda: controller.show_frame(
                                       ChangePassport))
        # putting the button in its place by
        # using grid
        button_Manage.grid(row=2, column=1, padx=10, pady=10)
        button_Manage.place(x=350, y=350)

        # button_Book
        button_Book = ttk.Button(self, text="Modify Personal Username",
                                 command=lambda: controller.show_frame(
                                     ChangeUserName))
        # putting the button in its place by
        # using grid
        button_Book.grid(row=2, column=1, padx=10, pady=10)
        button_Book.place(x=350, y=400)

        # button_Manage_Ticket
        button_Manage_Ticket = ttk.Button(self,
                                          text="Modify Personal Password",
                                          command=lambda: controller.show_frame(
                                              ChangePassword))
        # putting the button in its place by
        # using grid
        button_Manage_Ticket.grid(row=2, column=1, padx=10, pady=10)
        button_Manage_Ticket.place(x=350, y=450)

        # layout2
        button_back = ttk.Button(self, text="Back to Manage Account Page",
                                 command=lambda: controller.show_frame(
                                     ManageAccount))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class ChangeName(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Personal Name",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=100)

        # label of frame Layout
        namelabel = ttk.Label(self,
                              text="Please press confirm button to change your name",
                              font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        namelabel.grid(row=0, column=4, padx=300, pady=10)
        namelabel.place(x=300, y=200)

        # label of frame Layout 2
        label_name = ttk.Label(self, text="Please enter your original name",
                               font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_name.grid(row=0, column=4, padx=300, pady=10)
        label_name.place(x=200, y=300)

        # Entry 1
        # create a text entry box
        # create a text entry box
        original_name = tk.StringVar()
        original_name_textbox = ttk.Entry(self, textvariable=original_name)
        # Place the text entry box
        original_name_textbox.place(x=600, y=300)

        # label of frame Layout 2
        label_Passport = ttk.Label(self, text="Please enter your new name",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_Passport.grid(row=0, column=4, padx=300, pady=10)
        label_Passport.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        new_name = tk.StringVar()
        new_name_textbox = ttk.Entry(self, textvariable=new_name)
        # Place the text entry box
        new_name_textbox.place(x=600, y=350)

        def change_name():
            original_input_name = original_name_textbox.get()
            # Get the name from input
            new_input_name = new_name_textbox.get()
            # Let user enter their passport
            if len(self.controller.shared_data["username"].get()) > 0:
                if passenger_manager.check_passenger_name(
                        original_input_name) is True:
                    passenger_manager.change_passenger_name(
                        self.controller.shared_data["passenger"],
                        new_input_name)
                    label_name.config(text="Verified! Your name is in system",
                                      foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your name is update "
                                     "successfully!",
                                     foreground="green")
                else:
                    label_name.config(text="Sorry! Your name is not in system",
                                      foreground="red")

            elif len(self.controller.shared_data["new_name"].get()) > 0:
                if passenger_manager.check_passenger_name(
                        original_input_name) is True:
                    passenger_manager.change_passenger_name(
                        self.controller.shared_data["passenger"],
                        new_input_name)
                    label_name.config(text="Verified! Your name is in system",
                                      foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your name is update "
                                     "successfully!",
                                     foreground="green")
                    self.controller.shared_data["new_name"] = new_name
                else:
                    label_name.config(text="Sorry! Your name is not in system",
                                      foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=change_name)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self,
                                 text="Back to Modify Personal Information Page",
                                 command=lambda: controller.show_frame(
                                     ModifyPersonalInformation))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)

    # def return_new_passenger(self) -> Passenger:
    #     return self.passenger


class ChangePassport(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Personal Passport",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=100)

        # label of frame Layout
        namelabel = ttk.Label(self,
                              text="Please press confirm button to change your passport",
                              font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        namelabel.grid(row=0, column=4, padx=300, pady=10)
        namelabel.place(x=300, y=200)

        # label of frame Layout 2
        label_passport = ttk.Label(self,
                                   text="Please enter your original passport",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_passport.grid(row=0, column=4, padx=300, pady=10)
        label_passport.place(x=200, y=300)

        # Entry 1
        # create a text entry box
        # create a text entry box
        original_passport = tk.StringVar()
        original_passport_textbox = ttk.Entry(self,
                                              textvariable=original_passport)
        # Place the text entry box
        original_passport_textbox.place(x=600, y=300)

        # label of frame Layout 2
        label_new_Passport = ttk.Label(self,
                                       text="Please enter your new passport",
                                       font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_new_Passport.grid(row=0, column=4, padx=300, pady=10)
        label_new_Passport.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        new_passport = tk.StringVar()
        new_passport_textbox = ttk.Entry(self, textvariable=new_passport)
        # Place the text entry box
        new_passport_textbox.place(x=600, y=350)

        def change_passport():
            original_input_passport = original_passport_textbox.get()
            # Get the name from input
            new_input_passport = new_passport_textbox.get()
            # Let user enter their passport
            if len(self.controller.shared_data["username"].get()) > 0:
                if passenger_manager.check_passenger_passport(
                        self.controller.shared_data["passenger"],
                        original_input_passport) is True:
                    passenger_manager.change_passenger_passport(
                        self.controller.shared_data["passenger"],
                        new_input_passport)
                    label_passport.config(
                        text="Verified! Your passport is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your passport is "
                                     "update successfully!",
                                     foreground="green")
                else:
                    label_passport.config(
                        text="Sorry! Your passport is not in system",
                        foreground="red")

            elif len(self.controller.shared_data["new_name"].get()) > 0:
                if passenger_manager.check_passenger_passport(
                        self.controller.shared_data["passenger"],
                        original_input_passport) is True:
                    passenger_manager.change_passenger_passport(
                        self.controller.shared_data["passenger"],
                        new_input_passport)
                    label_passport.config(
                        text="Verified! Your passport is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your passport is update successfully!",
                                     foreground="green")
                else:
                    label_passport.config(
                        text="Sorry! Your passport is not in system",
                        foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=change_passport)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self,
                                 text="Back to Modify Personal Information Page",
                                 command=lambda: controller.show_frame(
                                     ModifyPersonalInformation))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class ChangeUserName(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Personal Username",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=100)

        # label of frame Layout
        namelabel = ttk.Label(self,
                              text="Please press confirm button to change your Username",
                              font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        namelabel.grid(row=0, column=4, padx=300, pady=10)
        namelabel.place(x=300, y=200)

        # label of frame Layout 2
        label_name = ttk.Label(self, text="Please enter your original Username",
                               font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_name.grid(row=0, column=4, padx=300, pady=10)
        label_name.place(x=200, y=300)

        # Entry 1
        # create a text entry box
        # create a text entry box
        original_username = tk.StringVar()
        original_username_textbox = ttk.Entry(self,
                                              textvariable=original_username)
        # Place the text entry box
        original_username_textbox.place(x=600, y=300)

        # label of frame Layout 2
        label_Passport = ttk.Label(self, text="Please enter your new Username",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_Passport.grid(row=0, column=4, padx=300, pady=10)
        label_Passport.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        new_username = tk.StringVar()
        new_username_textbox = ttk.Entry(self, textvariable=new_username)
        # Place the text entry box
        new_username_textbox.place(x=600, y=350)

        def change_user_name():
            original_input_username = original_username_textbox.get()
            # Get the name from input
            new_input_username = new_username_textbox.get()
            # Let user enter their passport
            if len(self.controller.shared_data["username"].get()) > 0:
                if passenger_manager.check_account_username(
                        original_input_username) is True:
                    passenger_manager.change_account_username(
                        self.controller.shared_data["passenger"],
                        new_input_username)
                    label_name.config(
                        text="Verified! Your username is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your username is "
                                     "update successfully!",
                                     foreground="green")
                    self.controller.shared_data["username"] = new_username
                else:
                    label_name.config(
                        text="Sorry! Your username is not in system",
                        foreground="red")

            elif len(self.controller.shared_data["new_name"].get()) > 0:
                if passenger_manager.check_account_username(
                        original_input_username) is True:
                    passenger_manager.change_account_username(
                        self.controller.shared_data["passenger"],
                        new_input_username)
                    label_name.config(
                        text="Verified! Your username is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your username is "
                                     "update successfully!",
                                     foreground="green")
                else:
                    label_name.config(
                        text="Sorry! Your username is not in system",
                        foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=change_user_name)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self,
                                 text="Back to Modify Personal Information Page",
                                 command=lambda: controller.show_frame(
                                     ModifyPersonalInformation))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class ChangePassword(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Personal Password",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=100)

        # label of frame Layout
        namelabel = ttk.Label(self,
                              text="Please press confirm button to change "
                                   "your Password",
                              font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        namelabel.grid(row=0, column=4, padx=300, pady=10)
        namelabel.place(x=300, y=200)

        # label of frame Layout 2
        label_Password = ttk.Label(self,
                                   text="Please enter your original Password",
                                   font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_Password.grid(row=0, column=4, padx=300, pady=10)
        label_Password.place(x=200, y=300)

        # Entry 1
        # create a text entry box
        # create a text entry box
        original_Password = tk.StringVar()
        original_Password_textbox = ttk.Entry(self,
                                              textvariable=original_Password)
        # Place the text entry box
        original_Password_textbox.place(x=600, y=300)

        # label of frame Layout 2
        label_new_password = ttk.Label(self,
                                       text="Please enter your new Password",
                                       font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_new_password.grid(row=0, column=4, padx=300, pady=10)
        label_new_password.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        new_password = tk.StringVar()
        new_password_textbox = ttk.Entry(self, textvariable=new_password)
        # Place the text entry box
        new_password_textbox.place(x=600, y=350)

        def change_user_name():
            original_input_username = original_Password_textbox.get()
            # Get the name from input
            new_input_username = new_password_textbox.get()
            # Let user enter their passport
            if len(self.controller.shared_data["username"].get()) > 0:
                if passenger_manager.check_account_password(
                        self.controller.shared_data["passenger"],
                        original_input_username) is True:
                    passenger_manager.change_account_password(
                        self.controller.shared_data["passenger"],
                        new_input_username)
                    label_Password.config(
                        text="Verified! Your Password is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your Password is "
                                     "update successfully!", foreground="green")
                else:
                    label_Password.config(
                        text="Sorry! Your Password is not in system",
                        foreground="red")

            elif len(self.controller.shared_data["new_name"].get()) > 0:
                if passenger_manager.check_account_password(
                        self.controller.shared_data["passenger"],
                        original_input_username) is True:
                    passenger_manager.change_account_password(
                        self.controller.shared_data["passenger"],
                        new_input_username)
                    label_Password.config(
                        text="Verified! Your Password is in system",
                        foreground="green")
                    namelabel.config(text=
                                     "Congregations! Your Password is "
                                     "update successfully!", foreground="green")
                else:
                    label_Password.config(
                        text="Sorry! Your Password is not in system",
                        foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=change_user_name)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=400)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self,
                                 text="Back to Modify Personal Information Page",
                                 command=lambda: controller.show_frame(
                                     ModifyPersonalInformation))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class LoadBalance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Load Balance Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_status = ttk.Label(self,
                                 text="",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_status.grid(row=0, column=4, padx=300, pady=10)
        label_status.place(x=200, y=300)

        # label of frame Layout 2
        label_amount = ttk.Label(self, text="Please enter your load amount "
                                            "and press confirm button",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_amount.grid(row=0, column=4, padx=300, pady=10)
        label_amount.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        amount = tk.StringVar()
        amount_textbox = ttk.Entry(self, textvariable=amount)
        # Place the text entry box
        amount_textbox.place(x=200, y=400)

        def load_balance():
            if amount_textbox.get().isdecimal() is True:
                input_amount = float(amount_textbox.get())
                if len(self.controller.shared_data["username"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)
                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")
                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")
                elif len(self.controller.shared_data["new_name"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)
                    # Let user enter their passport
                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")
                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")
            else:
                label_amount.configure(text="Sorry! You only can enter numbers",
                                       foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=load_balance)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=450)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Manage Account Page",
                                 command=lambda: controller.show_frame(
                                     ManageAccount))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class LoadBalanceBuyTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Load Balance Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_status = ttk.Label(self,
                                 text="",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_status.grid(row=0, column=4, padx=300, pady=10)
        label_status.place(x=200, y=300)

        # label of frame Layout 2
        label_amount = ttk.Label(self, text="Please enter your load amount "
                                            "and press confirm button",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_amount.grid(row=0, column=4, padx=300, pady=10)
        label_amount.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        amount = tk.StringVar()
        amount_textbox = ttk.Entry(self, textvariable=amount)
        # Place the text entry box
        amount_textbox.place(x=200, y=400)

        def load_balance():
            if amount_textbox.get().isdecimal() is True:

                input_amount = float(amount_textbox.get())
                if len(self.controller.shared_data["username"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)

                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")
                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")

                elif len(self.controller.shared_data["new_name"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)
                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")

                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")
            else:
                label_amount.configure(text="Sorry! You only can enter numbers",
                                       foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=load_balance)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=450)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Book Seats Page",
                                 command=lambda: controller.show_frame(
                                     BookSeatNumber))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class LoadBalanceBuyMeal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Load Balance Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_status = ttk.Label(self,
                                 text="",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_status.grid(row=0, column=4, padx=300, pady=10)
        label_status.place(x=200, y=300)

        # label of frame Layout 2
        label_amount = ttk.Label(self, text="Please enter your load amount "
                                            "and press confirm button",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_amount.grid(row=0, column=4, padx=300, pady=10)
        label_amount.place(x=200, y=350)

        # Entry 2
        # create a text entry box
        amount = tk.StringVar()
        amount_textbox = ttk.Entry(self, textvariable=amount)
        # Place the text entry box
        amount_textbox.place(x=200, y=400)

        def load_balance():
            if amount_textbox.get().isdecimal() is True:

                input_amount = float(amount_textbox.get())
                if len(self.controller.shared_data["username"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)

                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")
                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")

                elif len(self.controller.shared_data["new_name"].get()) > 0:
                    passenger_manager.update_account_balance(
                        self.controller.shared_data["passenger"],
                        input_amount)
                    label_amount.configure(
                        text="Congregations! Your Account Balance "
                             "has been updated", foreground="green")

                    label_status.config(
                        text="Your current account balance is " + str(
                            self.controller.shared_data[
                                "passenger"].get_account_balance()),
                        foreground="green")
            else:
                label_amount.configure(text="Sorry! You only can enter numbers",
                                       foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm",
                       command=load_balance)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=450)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Show Ticket Page",
                                 command=lambda: controller.show_frame(
                                     ShowTicket))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


class UpdateMembership(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Update MemberShip Status Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_status = ttk.Label(self,
                                 text="",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_status.grid(row=0, column=4, padx=300, pady=10)
        label_status.place(x=200, y=300)

        # label of frame Layout 2
        label_text = ttk.Label(self,
                               text="To update your membership status,"
                                    " please press confirm button",
                               font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_text.grid(row=0, column=4, padx=300, pady=10)
        label_text.place(x=200, y=350)

        def update_membership():
            if len(str(self.controller.shared_data["username"].get())) > 0:

                passenger_manager.update_membership_status(
                    self.controller.shared_data["passenger"])
                label_status.config(
                    text="Your current membership status is " + str(
                        self.controller.shared_data[
                            "passenger"].get_membership_status()),
                    foreground="green")
                label_text.configure(text="Congregations! Your Membership "
                                          "Status has been updated",
                                     foreground="green")
            elif len(self.controller.shared_data["new_name"].get()) > 0:
                passenger_manager.update_membership_status(
                    self.controller.shared_data["passenger"])
                label_status.config(
                    text="Your current membership status is " + str(
                        self.controller.shared_data[
                            "passenger"].get_membership_status()),
                    foreground="green")

                label_text.configure(text="Congregations! Your Membership "
                                          "Status has been updated",
                                     foreground="green")

        button_confirm = \
            ttk.Button(self, text="Confirm", command=update_membership)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=450)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Manage Account Page",
                                 command=lambda: controller.show_frame(
                                     ManageAccount))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


# Set default font and size

class PrintLogger(object):  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert("end", text)  # write text to textbox
        self.textbox.see("end")  # scroll to end
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self):  # needed for file like object
        pass


# third window frame page2
class BookFlightNumber(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.route_list = ""

        # label of frame Layout
        label = ttk.Label(self,
                          text="Ticket Booking System Menu",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please select one of the available routes below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=25, width=100,
                                       font=("consolas", "10", "normal"))
        self.log_widget.place(x=200, y=250)

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available flight number are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=600)

        # label of frame Layout
        self.label_available_list = ttk.Label(self,
                                              text="",
                                              font=("Verdana", 20, 'bold'))

        # putting the grid in its place by using
        # grid
        self.label_available_list.grid(row=0, column=4, padx=300, pady=10)
        self.label_available_list.place(x=600, y=600)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please enter the flight number you "
                                     "want to book a ticket: "
                                     "(For example, LA321)",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=650)

        # Entry 2
        # create a text entry box
        flight_number_textbox = ttk.Entry(self,
                                          textvariable=
                                          self.controller.shared_data[
                                              "flight_number"])
        # Place the text entry box
        flight_number_textbox.place(x=200, y=700)

        def get_flight_number():
            self.reset_logging()
            flight_number = flight_number_textbox.get()
            if len(self.route_list) > 0:
                if flight_number in flight_manager.generate_flight(
                        self.route_list):
                    label_input.config(
                        text="Confirm! The flight number "
                             + flight_number + " is in this routes "
                             + self.route_list,
                        foreground="green")
                else:
                    label_input.config(
                        text="Sorry! The flight number "
                             + flight_number
                             + " is not in this routes " + self.route_list,
                        foreground="red")

        # layout2
        button_back = ttk.Button(self, text="Check Flight Number",
                                 command=get_flight_number)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=400, y=700)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Montreal -> Toronto",
                                   command=lambda: [self.depart_montreal()])

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # button_Manage
        button_route2 = ttk.Button(self, text="Toronto -> Montreal",
                                   command=lambda: [self.depart_toronto()]
                                   )

        # putting the button in its place by
        # using grid
        button_route2.grid(row=2, column=1, padx=10, pady=10)
        button_route2.place(x=400, y=220)
        # button_route2.pack()

        # layout2
        button_back = ttk.Button(self, text="Go to next page to book seat",
                                 command=lambda: controller.show_frame(
                                     BookSeatNumber))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=750)

        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=600, y=750)

    def depart_montreal(self):
        self.route_list = 'Montreal -> Toronto'
        self.clear_content()
        self.flight_route()
        print("\nThe available flights for your selected routes",
              'Montreal -> Toronto', "are: \n")

        # Print all flights in this route
        print(
            flight_manager.print_all_flight_list(
                'Montreal -> Toronto'))
        self.label_available_list.config(
            text=" , ".join(
                flight_manager.generate_flight('Montreal -> Toronto')))

    def depart_toronto(self):
        self.route_list = 'Toronto -> Montreal'
        self.clear_content()
        self.flight_route()
        print("\nThe available flights for your selected routes",
              'Toronto -> Montreal', "are: \n")
        # Print all flights in this route
        print(
            flight_manager.print_all_flight_list(
                'Toronto -> Montreal'))
        self.label_available_list.config(
            text=" , ".join(
                flight_manager.generate_flight('Toronto -> Montreal')))

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def flight_route(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


# third window frame page2
class BookSeatNumber(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Ticket Booking System Menu",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please select one of the available seats below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=15, width=100)
        self.log_widget.place(x=200, y=250)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Available Seats Grid",
                                   command=lambda: [self.print_seat()])

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available seat number are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=450)

        # label of frame Layout
        self.label_available_list = ttk.Label(self,
                                              text="",
                                              font=("Verdana", 15, 'bold'))

        # putting the grid in its place by using
        # grid
        self.label_available_list.grid(row=2, column=4, padx=10, pady=10)
        self.label_available_list.place(x=200, y=500)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please enter the seat number you want "
                                     "to book a ticket below: "
                                     "(For example, 18F)",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=550)

        # Entry 2
        # create a text entry box
        ticket_number = tk.StringVar()
        ticket_number_textbox = ttk.Entry(self,
                                          textvariable=ticket_number)
        # self.controller.shared_data["ticket_number"]

        # Place the text entry box
        ticket_number_textbox.place(x=200, y=600)

        def get_ticket_number():
            seat_number = ticket_number_textbox.get()
            if seat_number in flight_manager.print_flight_current_seat_lists(
                    flight_manager.return_flight(
                        self.controller.shared_data["flight_number"].get())):
                label_input.config(
                    text="Confirm! The seat number is available "
                         "in this flight " +
                         self.controller.shared_data[
                             "flight_number"].get(), foreground="green")
            else:
                label_input.config(
                    text="Sorry! The seat number is not available "
                         "in this flight " +
                         self.controller.shared_data[
                             "flight_number"].get(), foreground="red")

        # layout2
        button_back = ttk.Button(self, text="Check Seat Number",
                                 command=get_ticket_number)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=400, y=600)

        def get_ticket() -> Ticket:

            if len(self.controller.shared_data["username"].get()) > 0:

                # Generate new ticket ID
                new_ticket_id = "{}{}{}".format(
                    self.controller.shared_data[
                        "passenger"].get_passenger_name()[
                    0:-1],
                    self.controller.shared_data["flight_number"].get()[:],
                    ticket_number_textbox.get())

                # Create a new ticket
                user_ticket = Ticket(new_ticket_id,
                                     ticket_number_textbox.get(),
                                     self.controller.shared_data["passenger"],
                                     flight_manager.return_flight(
                                         self.controller.shared_data[
                                             "flight_number"].get()))
                return user_ticket
            elif len(self.controller.shared_data["new_name"].get()) > 0:

                # Generate new ticket ID
                new_ticket_id = "{}{}{}".format(
                    self.controller.shared_data[
                        "passenger"].get_passenger_name()[:-1],
                    self.controller.shared_data["flight_number"].get()[:-1],
                    ticket_number_textbox.get())

                # Create a new ticket
                user_ticket = Ticket(new_ticket_id,
                                     ticket_number_textbox.get(),
                                     self.controller.shared_data["passenger"],
                                     flight_manager.return_flight(
                                         self.controller.shared_data[
                                             "flight_number"].get()))
                return user_ticket

        def check_balance():
            # calculate ticket price
            possible_ticket_price = passenger_manager.calculate_ticket_price(
                self.controller.shared_data["passenger"],
                flight_manager.return_flight(
                    self.controller.shared_data[
                        "flight_number"].get()))

            requests_amount = passenger_manager.check_account_balance(
                self.controller.shared_data["passenger"],
                possible_ticket_price)
            if requests_amount > 0.0:
                label_input.config(
                    text="Sorry! Your current account balance "
                         "is not enough. Please load $" + str(requests_amount)
                         + " first", foreground="red")
            else:

                # Assign the ticket to system
                self.controller.shared_data["ticket"] = get_ticket()

                ticket_price = self.controller.shared_data[
                    "ticket"].calculate_ticket_price()
                # Check the passenger's current <account_balance> to
                # the given float.

                # add the ticket to the ticket_manager
                ticket_manager.add_ticket(self.controller.shared_data["ticket"])

                # update flight seat
                flight_manager.update_flight_seat(flight_manager.return_flight(
                    self.controller.shared_data[
                        "flight_number"].get()),
                    self.controller.shared_data["ticket"])

                # load money to account balance
                passenger_manager.update_account_balance(
                    self.controller.shared_data["passenger"], -ticket_price)

                passenger_manager.update_ticket_history(
                    self.controller.shared_data["passenger"],
                    self.controller.shared_data["ticket"])

                controller.show_frame(ShowTicket)

        # layout2
        button_back = ttk.Button(self, text="Go to next page to book ticket",
                                 command=check_balance)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=650)

        # layout2
        button_load = ttk.Button(self, text="Go to load balance",
                                 command=lambda: controller.show_frame(
                                     LoadBalanceBuyTicket))

        # putting the button in its place
        # by using grid
        button_load.grid(row=1, column=1, padx=10, pady=10)
        button_load.place(x=435, y=650)

        # layout2
        button_back = ttk.Button(self, text="Back to Select Flight Number",
                                 command=lambda: controller.show_frame(
                                     BookFlightNumber))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=600, y=650)

    def print_seat(self):
        self.clear_content()
        self.seat_grid()
        print("\nThe available seats for your selected flight are: \n")
        print(
            flight_manager.print_current_seats(flight_manager.return_flight(
                self.controller.shared_data["flight_number"].get())))

        self.label_available_list.config(
            text=" , ".join(
                flight_manager.print_flight_current_seat_lists(
                    flight_manager.return_flight(
                        self.controller.shared_data["flight_number"].get()))))
        self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def seat_grid(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


# third window frame page2
class ShowTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Ticket Booking System Menu",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Booked Successfully! Please check your ticket "
                               "information below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=13, width=100)
        self.log_widget.place(x=200, y=250)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Ticket Information",
                                   command=lambda: self.print_ticket())

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available flight meals are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=420)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please press the meal button you want "
                                     "to add to ticket below: "
                                     "(For example, Burger)",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=470)

        def add_burger():
            burger = Burger()
            self.controller.shared_data["ticket"].set_meal(burger)
            self.print_ticket()
            label_input.config(text="You have select Burger as your "
                                    "ticket meal", foreground="green")

        # layout2
        button_burger = ttk.Button(self, text="Burger $25.0",
                                   command=add_burger)

        # putting the button in its place
        # by using grid
        button_burger.grid(row=1, column=1, padx=10, pady=10)
        button_burger.place(x=200, y=520)

        def add_hotdog():
            hotdog = HotDog()
            self.controller.shared_data["ticket"].set_meal(hotdog)
            self.print_ticket()
            label_input.config(text="You have select HotDog as your "
                                    "ticket meal", foreground="green")

            # layout2

        button_burger = ttk.Button(self, text="HotDog $15.0",
                                   command=add_hotdog)

        # putting the button in its place
        # by using grid
        button_burger.grid(row=1, column=1, padx=10, pady=10)
        button_burger.place(x=350, y=520)

        def add_fries():
            fries = FrenchFries()
            self.controller.shared_data["ticket"].set_meal(fries)
            self.print_ticket()
            label_input.config(text="You have select French Fries "
                                    "as your ticket meal", foreground="green")

        # layout2
        button_burger = ttk.Button(self, text="French Fries $10.0",
                                   command=add_fries)

        # putting the button in its place
        # by using grid
        button_burger.grid(row=1, column=1, padx=10, pady=10)
        button_burger.place(x=500, y=520)

        def remove_meal():
            self.controller.shared_data["ticket"].meal = None
            self.print_ticket()
            label_input.config(text="You have removed your ticket "
                                    "meal", foreground="red")

        # layout2
        button_burger = ttk.Button(self, text="Remove Meal",
                                   command=remove_meal)

        # putting the button in its place
        # by using grid
        button_burger.grid(row=1, column=1, padx=10, pady=10)
        button_burger.place(x=700, y=520)

        # layout2
        button_load = ttk.Button(self, text="Go to load balance",
                                 command=lambda: controller.show_frame(
                                     LoadBalanceBuyMeal))

        # putting the button in its place
        # by using grid
        button_load.grid(row=1, column=1, padx=10, pady=10)
        button_load.place(x=435, y=700)

        def minus_meal():
            meal = self.controller.shared_data["ticket"].get_ticket_meal()
            if meal is not None:
                meal_price = meal.get_meal_price()
                requests_amount = passenger_manager.check_account_balance(
                    self.controller.shared_data["passenger"],
                    meal_price)
                if requests_amount > 0:
                    label_input.config(text="Sorry! You need to upload "
                                            + str(meal_price)
                                            + " first to buy ticket meal",
                                       foreground="red")
                else:
                    self.controller.shared_data[
                        "passenger"].update_account_balance(
                        -meal.get_meal_price())
                    controller.show_frame(MainMenu)
            else:
                controller.show_frame(MainMenu)

        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu",
                                 command=minus_meal)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=700)

    def print_ticket(self):
        self.clear_content()
        self.seat_grid()
        print("\nYour Ticket information is:\n")
        if self.controller.shared_data["ticket"] is not None:
            print(
                self.controller.shared_data["ticket"].print_ticket_information()
            )
            # flight_manager.print_current_seats(flight_manager.return_flight(
            #     self.controller.shared_data["flight_number"].get())))

            # self.label_available_list.config(
            #     text=" , ".join(
            #         flight_manager.print_flight_current_seat_lists(
            #             flight_manager.return_flight(
            #                 self.controller.shared_data[
            #                     "flight_number"].get()))))
            self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def seat_grid(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


# third window frame page2
class CheckBookedTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Check Booked Ticket",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please check your booked ticket below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=25, width=100,
                                       font=("consolas", "10", "normal"))
        self.log_widget.place(x=200, y=250)

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available ticket number are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=600)

        # label of frame Layout
        self.label_available_list = ttk.Label(self,
                                              text="",
                                              font=("Verdana", 20, 'bold'))

        # putting the grid in its place by using
        # grid
        self.label_available_list.grid(row=0, column=4, padx=300, pady=10)
        self.label_available_list.place(x=600, y=600)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please enter the ticket number you "
                                     "want to manage: ",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=650)

        # Entry 2
        # create a text entry box
        ticket_number_textbox = ttk.Entry(self,
                                          textvariable=
                                          self.controller.shared_data[
                                              "modify_ticket"])
        # Place the text entry box
        ticket_number_textbox.place(x=200, y=700)

        def get_ticket_number():
            ticket_number_input = ticket_number_textbox.get()
            if ticket_number_input in passenger_manager.all_passenger_tickets_number(
                    self.controller.shared_data["passenger"]
            ):
                label_input.config(
                    text="Confirm! The Ticket number "
                         + ticket_number_input + " is in your purchase history",
                    foreground="green")
            else:
                label_input.config(
                    text="Sorry! The Ticket number "
                         + ticket_number_input
                         + " is not in your purchase history ",
                    foreground="red")

        # layout2
        button_back = ttk.Button(self, text="Check Ticket Number",
                                 command=get_ticket_number)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=400, y=700)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Ticket History",
                                   command=lambda: self.display_ticket_history())

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)

        # button_route1.pack()

        def check_input_for_check_in():
            if len(self.controller.shared_data["modify_ticket"].get()) > 0:
                controller.show_frame(UpdateCheckIn)
            else:
                label_input.config(
                    text="Sorry! You Need to enter Ticket Number First",
                    foreground="red")

        button_checkin = ttk.Button(self, text="Check In This Ticket",
                                    command=check_input_for_check_in)

        # putting the button in its place
        # by using grid
        button_checkin.grid(row=1, column=1, padx=10, pady=10)
        button_checkin.place(x=200, y=750)

        def check_input_for_modify_seat():
            if len(self.controller.shared_data["modify_ticket"].get()) > 0:
                controller.show_frame(ModifyTicketSeat)
            else:
                label_input.config(
                    text="Sorry! You Need to enter Ticket Number First",
                    foreground="red")

        # layout2
        button_modify_seat = ttk.Button(self, text="Modify Ticket Seat",
                                        command=check_input_for_modify_seat)

        # putting the button in its place
        # by using grid
        button_modify_seat.grid(row=1, column=1, padx=10, pady=10)
        button_modify_seat.place(x=370, y=750)

        def check_input_for_CancelTicket():
            if len(self.controller.shared_data["modify_ticket"].get()) > 0:
                controller.show_frame(CancelTicket)
            else:
                label_input.config(
                    text="Sorry! You Need to enter Ticket Number First",
                    foreground="red")

        # layout2
        button_back = ttk.Button(self, text="Cancel This Ticket",
                                 command=check_input_for_CancelTicket)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=530, y=750)

        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu Page",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=690, y=750)

    def display_ticket_history(self):
        self.clear_content()
        self.show_ticket_history()
        print("\nThe Tickets in your purchased history are \n")

        # Print all tickets in
        print(passenger_manager.print_passenger_ticket_history(
            self.controller.shared_data["passenger"])
        )
        self.label_available_list.config(
            text=" , ".join(
                passenger_manager.all_passenger_tickets_number(
                    self.controller.shared_data["passenger"]
                )))
        self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def show_ticket_history(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


class UpdateCheckIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Ticket Check In Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout 2
        label_notice = ttk.Label(self,
                                 text="Once you check in Ticket. "
                                      "You could only modify ticket "
                                      "seat but cannot cancel it",
                                 font=("Verdana", 15))

        # putting the grid in its place by using
        # grid
        label_notice.grid(row=2, column=4, padx=300, pady=10)
        label_notice.place(x=200, y=300)

        # label of frame Layout 2
        label_status = ttk.Label(self,
                                 text="",
                                 font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_status.grid(row=0, column=4, padx=300, pady=10)
        label_status.place(x=200, y=350)

        # label of frame Layout 2
        label_text = ttk.Label(self,
                               text="To update Check In status,"
                                    " please press confirm button",
                               font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_text.grid(row=0, column=4, padx=300, pady=10)
        label_text.place(x=200, y=400)

        def update_membership():
            if len(str(self.controller.shared_data["modify_ticket"].get())) > 0:
                if ticket_manager.get_ticket(self.controller.shared_data[
                                                 "modify_ticket"].get()) is not None:
                    ticket_manager.update_check_in_status(
                        ticket_manager.get_ticket(self.controller.shared_data[
                                                      "modify_ticket"].get()))

                    label_status.config(
                        text="The Ticket current check in status now is " + str(
                            ticket_manager.get_ticket(
                                self.controller.shared_data[
                                    "modify_ticket"
                                ].get()).get_ticket_check_in_status()
                        ),
                        foreground="green")
                    label_text.configure(
                        text="Congregations! Your Ticket Check In Status "
                             "has been updated",
                        foreground="green")
                else:
                    label_text.configure(
                        text="Sorry! This Ticket is not in our system",
                        foreground="red")

        button_confirm = \
            ttk.Button(self, text="Confirm", command=update_membership)

        # putting the button in its place by
        # using grid
        button_confirm.grid(row=2, column=1, padx=10, pady=10)
        button_confirm.place(x=200, y=500)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Check Booked Ticket Page",
                                 command=lambda: controller.show_frame(
                                     CheckBookedTicket))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


# third window frame page2
class ModifyTicketSeat(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Modify Ticket Seat Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please select one of the available seats below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=15, width=100)
        self.log_widget.place(x=200, y=250)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Available Seats Grid",
                                   command=lambda: [self.print_seat()])

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available seat number are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=450)

        # label of frame Layout
        self.label_available_list = ttk.Label(self,
                                              text="",
                                              font=("Verdana", 15, 'bold'))

        # putting the grid in its place by using
        # grid
        self.label_available_list.grid(row=2, column=4, padx=10, pady=10)
        self.label_available_list.place(x=200, y=500)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please enter the seat number you want "
                                     "to book a ticket below: "
                                     "(For example, 18F)",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=550)

        # Entry 2
        # create a text entry box
        seat_number = tk.StringVar()
        seat_number_textbox = ttk.Entry(self,
                                        textvariable=seat_number)
        # self.controller.shared_data["ticket_number"]

        # Place the text entry box
        seat_number_textbox.place(x=200, y=600)

        def get_seat_number():
            seat_number_input = seat_number_textbox.get()
            if seat_number_input in flight_manager.print_flight_current_seat_lists(
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data["modify_ticket"].get())):
                label_input.config(
                    text="Confirm! The seat number is available "
                         "in this flight " +
                         str(ticket_manager.return_ticket_flight(
                             self.controller.shared_data[
                                 "modify_ticket"].get()).get_flight_number())
                    , foreground="green")
            else:
                label_input.config(
                    text="Sorry! The seat number is not available "
                         "in this flight " +
                         str(ticket_manager.return_ticket_flight(
                             self.controller.shared_data[
                                 "modify_ticket"].get()).get_flight_number())
                    , foreground="red")

        # layout2
        button_back = ttk.Button(self, text="Check Seat Number",
                                 command=get_seat_number)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=400, y=600)

        def modify_ticket_seat() -> None:
            seat_number_input = seat_number_textbox.get()
            if len(self.controller.shared_data["username"].get()) > 0:
                flight_manager.cancel_flight_seat(
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get()),
                    ticket_manager.get_ticket(self.controller.shared_data[
                                                  "modify_ticket"].get())
                )

                ticket_manager.modify_ticket_seat_number(
                    ticket_manager.get_ticket(self.controller.shared_data[
                                                  "modify_ticket"].get()),
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get()), seat_number_input)
                if self.controller.shared_data[
                    "modify_ticket"].get() != seat_number_input:
                    label_input.config(
                        text="Congratulationn! The seat number is changed for this ticket "
                        , foreground="green")
                else:
                    label_input.config(
                        text="Sorry! You need to enter another seat number"
                        , foreground="red")
            elif len(self.controller.shared_data["new_name"].get()) > 0:
                flight_manager.cancel_flight_seat(
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get()
                    ),
                    ticket_manager.get_ticket(self.controller.shared_data[
                                                  "modify_ticket"].get())
                )

                ticket_manager.modify_ticket_seat_number(
                    ticket_manager.get_ticket(self.controller.shared_data[
                                                  "modify_ticket"].get()),
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get()), seat_number_input)
                if self.controller.shared_data[
                    "modify_ticket"].get() != seat_number_input:
                    label_input.config(
                        text="Congratulationn! The seat number is changed for this ticket "
                        , foreground="green")
                else:
                    label_input.config(
                        text="Sorry! You need to enter another seat number"
                        , foreground="red")
            self.print_seat()

        # layout2
        button_back = ttk.Button(self, text="Change Seat Number",
                                 command=modify_ticket_seat)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=600, y=600)

        # layout2
        button_back = ttk.Button(self, text="Back to Check Booked Ticket Page",
                                 command=lambda: controller.show_frame(
                                     CheckBookedTicket))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=650)

    def print_seat(self):
        self.clear_content()
        self.seat_grid()
        print("\nThe available seats for your selected flight are: \n")
        if len(self.controller.shared_data["modify_ticket"].get()) > 0:
            print(
                flight_manager.print_current_seats(
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get())
                )
            )
            self.label_available_list.config(
                text=" , ".join(
                    flight_manager.print_flight_current_seat_lists(
                        ticket_manager.return_ticket_flight(
                            self.controller.shared_data[
                                "modify_ticket"].get())
                    )
                )
            )
        else:
            print("Please go back to previous page to enter ticket number")
        self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def seat_grid(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


# third window frame page2
class CancelTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Cancel Ticket Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please select one of the available seats below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=15, width=100)
        self.log_widget.place(x=200, y=250)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Available Seats Grid",
                                   command=lambda: [self.print_seat()])

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available seat number are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=450)

        # label of frame Layout
        self.label_available_list = ttk.Label(self,
                                              text="",
                                              font=("Verdana", 15, 'bold'))

        # putting the grid in its place by using
        # grid
        self.label_available_list.grid(row=2, column=4, padx=10, pady=10)
        self.label_available_list.place(x=200, y=500)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text=" Please click the button below to cancel ticket",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=550)

        def cancel_ticket_seat():
            if len(self.controller.shared_data["modify_ticket"].get()) > 0:
                if ticket_manager.get_ticket(self.controller.shared_data[
                                                 "modify_ticket"].get()).get_ticket_check_in_status() is False:

                    flight_manager.cancel_flight_seat(
                        ticket_manager.return_ticket_flight(
                            self.controller.shared_data[
                                "modify_ticket"].get()
                        ),
                        ticket_manager.get_ticket(self.controller.shared_data[
                                                      "modify_ticket"].get())
                    )

                    self.print_seat()
                    label_input.config(
                        text="Congregations! Your Ticket has been cancelled",
                        foreground="green")
                else:
                    self.print_seat()
                    label_input.config(
                        text="Sorry! You cannot cancel a checked in ticket.",
                        foreground="red")

        def cancel_ticket():
            if ticket_manager.get_ticket(self.controller.shared_data[
                                             "modify_ticket"].get()).get_ticket_check_in_status() is False:

                ticket_manager.cancel_ticket(
                    ticket_manager.get_ticket(self.controller.shared_data[
                                                  "modify_ticket"].get()),
                    ticket_manager.return_ticket_flight(
                        self.controller.shared_data[
                            "modify_ticket"].get()))
            controller.show_frame(CheckBookedTicket)

        # layout2
        button_back = ttk.Button(self, text="Cancel This Ticket",
                                 command=cancel_ticket_seat)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)

        # layout2
        button_back = ttk.Button(self, text="Back to Check Booked Ticket Page",
                                 command=cancel_ticket)

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=650)

    def print_seat(self):
        self.clear_content()
        self.seat_grid()
        print("\nThe available seats for your selected flight are: \n")
        if len(self.controller.shared_data["modify_ticket"].get()) > 0:
            flight_id = ticket_manager.return_ticket_flight(
                self.controller.shared_data[
                    "modify_ticket"].get()).get_flight_number()
            print(
                flight_manager.print_current_seats(
                    flight_manager.return_flight(flight_id)
                )
            )
            self.label_available_list.config(
                text=" , ".join(
                    flight_manager.print_flight_current_seat_lists(
                        flight_manager.return_flight(flight_id)
                    )
                )
            )

        else:
            print("Please go back to previous page to enter ticket number")
        self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def seat_grid(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


# third window frame page2
class RedeemItemsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Redeem Items Page",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=100)

        # label of frame Layout
        label = ttk.Label(self,
                          text="Please Check Your Redeem Items History below",
                          font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=200, y=170)

        self.log_widget = ScrolledText(self, height=15, width=100)
        self.log_widget.place(x=200, y=250)

        # button_Register
        button_route1 = ttk.Button(self,
                                   text="Show Redeem Items History",
                                   command=lambda: [
                                       self.print_reedem_history()])

        # putting the button in its place by
        # using grid
        button_route1.grid(row=2, column=1, padx=10, pady=10)
        button_route1.place(x=200, y=220)
        # button_route1.pack()

        # label of frame Layout
        label_available = ttk.Label(self,
                                    text="The available redeemable item are:",
                                    font=("Verdana", 20))

        # putting the grid in its place by using
        # grid
        label_available.grid(row=0, column=4, padx=300, pady=10)
        label_available.place(x=200, y=450)

        # label of frame Layout
        label_input = ttk.Label(self,
                                text="Please press the item button which you want to redeem",
                                font=("Verdana", 15, "bold"))

        # putting the grid in its place by using
        # grid
        label_input.grid(row=0, column=4, padx=300, pady=10)
        label_input.place(x=200, y=500)

        def redeem_Thermos():
            redeem_item = Thermos()
            if self.controller.shared_data["passenger"].add_redeem_item(
                    redeem_item) is True:
                label_input.config(
                    text="Congregations! You have successfully redeemed item " + str(
                        redeem_item.get_item_name()), foreground="green")
            else:
                label_input.config(
                    text="Sorry! You do not have enough redeem points for item " + str(
                        redeem_item.get_item_name()), foreground="red")
            self.print_reedem_history()

        # layout2
        button_Thermos = ttk.Button(self, text="Thermos: 25 Points",
                                    command=redeem_Thermos)

        # putting the button in its place
        # by using grid
        button_Thermos.grid(row=1, column=1, padx=10, pady=10)
        button_Thermos.place(x=200, y=550)

        def redeem_Pillow():
            redeem_item = Pillow()
            if self.controller.shared_data["passenger"].add_redeem_item(
                    redeem_item) is True:
                label_input.config(
                    text="Congregations! You have successfully redeemed item " + str(
                        redeem_item.get_item_name()), foreground="green")
            else:
                label_input.config(
                    text="Sorry! You do not have enough redeem points for item " + str(
                        redeem_item.get_item_name()), foreground="red")
            self.print_reedem_history()

        # layout2
        button_Pillow = ttk.Button(self, text="Pillow: 15 Points",
                                   command=redeem_Pillow)

        # putting the button in its place
        # by using grid
        button_Pillow.grid(row=1, column=1, padx=10, pady=10)
        button_Pillow.place(x=400, y=550)

        def redeem_mug():
            redeem_item = Mug()
            if self.controller.shared_data["passenger"].add_redeem_item(
                    redeem_item) is True:
                label_input.config(
                    text="Congregations! You have successfully redeemed item " + str(
                        redeem_item.get_item_name()), foreground="green")
            else:
                label_input.config(
                    text="Sorry! You do not have enough redeem points for item " + str(
                        redeem_item.get_item_name()), foreground="red")
            self.print_reedem_history()

        # layout2
        button_Mug = ttk.Button(self, text="Mug: 10 Points",
                                command=redeem_mug)
        # putting the button in its place
        # by using grid
        button_Mug.grid(row=1, column=1, padx=10, pady=10)
        button_Mug.place(x=600, y=550)

        # layout2
        button_back = ttk.Button(self,
                                 text="Back to MainMenu",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=650)

    def print_reedem_history(self):
        self.clear_content()
        self.seat_grid()
        print("\nThe redeem items history for you are: \n")
        if self.controller.shared_data["passenger"] is not None:
            print(
                passenger_manager.print_passenger_redeem_history(
                    self.controller.shared_data["passenger"])

            )
        self.reset_logging()

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def seat_grid(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger

    def clear_content(self):
        self.log_widget.configure(state='normal')
        self.log_widget.delete('1.0', tk.END)
        self.log_widget.configure(state='disabled')


class RatingSystem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout
        label = ttk.Label(self,
                          text="Rating This System",
                          font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=300, pady=10)
        label.place(x=300, y=200)

        # label of frame Layout
        label_text = ttk.Label(self,
                               text="Please select option below to rate your booking ticket experience",
                               font=("Verdana", 15))

        # putting the grid in its place by using
        # grid
        label_text.grid(row=0, column=4, padx=300, pady=10)
        label_text.place(x=300, y=270)

        def give_voucher():
            label_text.config(
                text="Thank you so much. We will give you 5$ voucher ^0^",
                foreground="green")
            if self.controller.shared_data["passenger"] is not None:
                self.controller.shared_data["passenger"].get_voucher(5)

        # button_Register
        button_5 = ttk.Button(self,
                              text="5 Stars ☆☆☆☆☆",
                              command=give_voucher
                              )
        # putting the button in its place by
        # using grid
        button_5.grid(row=2, column=1, padx=10, pady=10)
        button_5.place(x=350, y=300)

        def thank():
            label_text.configure(
                text="Thank you so much for your ratings! ^0^",
                foreground="green")

        # button_Manage
        button_4 = ttk.Button(self, text="4 Stars ☆☆☆☆",
                              command=thank)
        # putting the button in its place by
        # using grid
        button_4.grid(row=2, column=1, padx=10, pady=10)
        button_4.place(x=350, y=350)

        # button_Manage
        button_3 = ttk.Button(self, text="3 Stars ☆☆☆",
                              command=thank)
        # putting the button in its place by
        # using grid
        button_3.grid(row=2, column=1, padx=10, pady=10)
        button_3.place(x=350, y=400)

        # button_Manage
        button_2 = ttk.Button(self, text="2 Stars ☆☆",
                              command=thank)
        # putting the button in its place by
        # using grid
        button_2.grid(row=2, column=1, padx=10, pady=10)
        button_2.place(x=350, y=450)

        # button_Manage
        button_1 = ttk.Button(self, text="1 Star ☆",
                              command=thank)
        # putting the button in its place by
        # using grid
        button_1.grid(row=2, column=1, padx=10, pady=10)
        button_1.place(x=350, y=500)

        # button to show frame 2 with text
        # layout2
        button_back = ttk.Button(self, text="Back to Main Menu Page",
                                 command=lambda: controller.show_frame(
                                     MainMenu))

        # putting the button in its place
        # by using grid
        button_back.grid(row=1, column=1, padx=10, pady=10)
        button_back.place(x=200, y=600)


if __name__ == "__main__":
    # Driver Code
    window = BookingTicket()
    # set window width and height
    window.configure(width=1000, height=2000)
    # move window center
    # Define the window width
    window_width = window.winfo_reqwidth()
    # Define the window height
    window_height = window.winfo_reqheight()
    # Define the window right position
    position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
    # Define the window down position
    position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
    # Define the window geometry position
    window.geometry("+{}+{}".format(position_right, position_down))
    # Display the window
    window.mainloop()
