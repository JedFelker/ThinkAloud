"""
    Name: trivia_1.py
    Author: Jed Felker
    Created: 3/9/23
    GOAL: Create the first window of the GUI
"""
# Import the tkinter module with tk standards widgets
from tkinter import *
# Override tk widgets with themed ttk widgets if available
from tkinter.ttk import *

class Trivia:

    def __init__(self):
        # Create the root window
        self.root = Tk()
        self.supWindow = Toplevel(self.root)
        self.movWindow = Toplevel(self.root)
        self.gamWindow = Toplevel(self.root)
        self.carWindow = Toplevel(self.root)
        self.root.title("Jed's Trivia Game")

        # Prevent window from resizing
        self.root.resizable(False, False)
        self.root.geometry("275x150")
        self.supWindow.withdraw()
        self.gamWindow.withdraw()
        self.movWindow.withdraw()
        self.carWindow.withdraw()

        # Create the GUI widgets in a seperate method
        self.create_widgets()

        # Call the mainloop method to start program
        mainloop()

    def create_widgets(self):
        self.main_frame = LabelFrame(
            self.root,                            # Assign to parent window
            text="Which topic would you like?",  # Text for the frame
            relief=GROOVE
        )

        self.btn_movies = Button(
            self.main_frame,     # Assign to parent frame
            text="MOVIES",           # Text shown on button
            width=37,
            # Connect convert method to button click
            command=lambda: [self.movies(), self.root.withdraw()]
        )

        self.btn_games = Button(
            self.main_frame,     # Assign to parent frame
            text="GAMES",           # Text shown on button
            width=37,
            # Connect convert method to button click
            command=lambda: [self.games(), self.root.withdraw()]
        )

        self.btn_superheroes = Button(
            self.main_frame,     # Assign to parent frame
            text="SUPERHEROES",           # Text shown on button
            width=37,
            # Connect convert method to button click
            command=lambda: [self.superheroes(), self.root.withdraw()]
        )

        self.btn_cartoons = Button(
            self.main_frame,     # Assign to parent frame
            text="CARTOONS",           # Text shown on button
            width=37,
            # Connect convert method to button click
            command=lambda: [self.cartoons(), self.root.withdraw()]
        )

        # Set padding between frame and window
        self.main_frame.grid_configure(padx=20, pady=20)

        self.btn_movies.grid(row=0, column=0)
        self.btn_games.grid(row=1, column=0)
        self.btn_superheroes.grid(row=2, column=0)
        self.btn_cartoons.grid(row=3, column=0)

    def superheroes(self):
        self.supWindow.deiconify()
        self.supWindow.title("Superheroes")
        self.supWindow.geometry("275x150")

        self.newLabel = Label(
            self.supWindow,
            
            text="new window"
        )

        self.newLabel.grid(row=0, column=0)

    def movies(self):
        self.movWindow.deiconify()
        self.movWindow.title("Movies")
        self.movWindow.geometry("275x150")

        self.newLabel = Label(
            self.movWindow,
            text="new window"
        )

        self.newLabel.grid(row=0, column=0)

    def games(self):
        self.gamWindow.deiconify()
        self.gamWindow.title("Movies")
        self.gamWindow.geometry("275x150")

        self.newLabel = Label(
            self.gamWindow,
            text="new window"
        )

        self.newLabel.grid(row=0, column=0)

    def cartoons(self): 
        self.carWindow.deiconify()
        self.carWindow.title("Movies")
        self.carWindow.geometry("275x150")

        self.newLabel = Label(
            self.carWindow,
            text="new window"
        )

        self.newLabel.grid(row=0, column=0)


"""Create program objet from the program class to run the program."""
trivia_game = Trivia()
