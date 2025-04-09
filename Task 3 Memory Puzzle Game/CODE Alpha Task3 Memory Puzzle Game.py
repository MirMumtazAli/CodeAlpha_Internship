import tkinter as tk
from tkinter import messagebox
import random

# Constants
CARD_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2  # Pairs of non-graphic symbols
BOARD_SIZE = 4  # 4x4 grid (16 cards)
TIME_LIMIT = 30  # Time limit in seconds

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.cards = CARD_VALUES.copy()
        random.shuffle(self.cards)  # Shuffle the cards
        self.flipped = []  # Track flipped cards
        self.matched = 0  # Track matched pairs
        self.start_time = None  # Timer start time

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Timer Label
        self.timer_label = tk.Label(self.root, text=f"Time Left: {TIME_LIMIT}s", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # Game Board Frame
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        # Create card buttons
        self.buttons = []
        for i in range(BOARD_SIZE * BOARD_SIZE):
            button = tk.Button(self.board_frame, text="", width=5, height=2,
                               command=lambda idx=i: self.flip_card(idx))
            button.grid(row=i // BOARD_SIZE, column=i % BOARD_SIZE, padx=5, pady=5)
            self.buttons.append(button)

        # Control Buttons Frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Replay Button
        tk.Button(control_frame, text="Replay", font=("Arial", 12), command=self.restart_game).pack(side=tk.LEFT, padx=10)

        # Exit Button
        tk.Button(control_frame, text="Exit", font=("Arial", 12), command=self.root.quit).pack(side=tk.LEFT, padx=10)

    def flip_card(self, index):
        """
        Flips a card when clicked.
        If two cards are flipped, checks if they match.
        """
        if self.start_time is None:
            self.start_timer()  # Start timer on first move

        button = self.buttons[index]
        if button["text"] != "" or len(self.flipped) == 2:
            return  # Ignore clicks on already flipped or matched cards

        button.config(text=self.cards[index])
        self.flipped.append((index, self.cards[index]))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)  # Check for a match after 1 second

    def check_match(self):
        """
        Checks if the two flipped cards match.
        If they match, leave them face-up. Otherwise, flip them back.
        """
        idx1, val1 = self.flipped[0]
        idx2, val2 = self.flipped[1]

        if val1 == val2:
            self.matched += 1
            if self.matched == len(CARD_VALUES) // 2:
                self.end_game("Congratulations! You won!")
        else:
            self.buttons[idx1].config(text="")
            self.buttons[idx2].config(text="")

        self.flipped.clear()  # Reset flipped cards list

    def start_timer(self):
        """
        Starts the countdown timer.
        Ends the game if the time runs out.
        """
        self.start_time = TIME_LIMIT
        self.update_timer()

    def update_timer(self):
        """
        Updates the timer every second.
        Ends the game if the time runs out.
        """
        if self.start_time > 0:
            self.start_time -= 1
            self.timer_label.config(text=f"Time Left: {self.start_time}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game("Time's up! You lost.")

    def end_game(self, message):
        """
        Ends the game and displays a message.
        Disables all buttons except the Replay button.
        """
        for button in self.buttons:
            button.config(state=tk.DISABLED)  # Disable all game buttons
        messagebox.showinfo("Game Over", message)

    def restart_game(self):
        """
        Restarts the game by resetting all variables and shuffling the cards.
        """
        self.cards = CARD_VALUES.copy()
        random.shuffle(self.cards)
        self.flipped = []
        self.matched = 0
        self.start_time = None

        # Reset card buttons
        for i, button in enumerate(self.buttons):
            button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")

        # Reset timer label
        self.timer_label.config(text=f"Time Left: {TIME_LIMIT}s")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGame(root)
    root.mainloop()