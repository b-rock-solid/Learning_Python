from random import randint

"""Simulates the death roll gamble from WoW."""


class Player:
    """Basic template of a player."""

    def __init__(self, player_name):
        """Initialize the players and the amount wagered."""
        self.player_name = player_name

    def welcome_player(self):
        """Prints the player a welcome message."""
        print(f"Welcome to Deathroll {self.player_name.title()}!")


class Deathroll:
    """Creates the Death Roll functions."""

    def __init__(self, nrange):
        """Stores the range for the initial roll."""
        self.nrange = nrange

    def roll(self):
        """A method to roll to the selected range."""
        print("Your deathroll is beginning! Good Luck!")
        player_rolling = 'player01'
        while self.nrange != 1:
            if player_rolling == 'player01':
                roll_range = self.nrange
                roll_result = randint(1, roll_range)
                print(f"{player01.player_name.title()} has rolled: {roll_result}")
                self.nrange = roll_result
                player_rolling = 'player02'
            elif player_rolling == 'player02':
                roll_range = self.nrange
                roll_result = randint(1, roll_range)
                print(f"{player02.player_name.title()} has rolled: {roll_result}")
                self.nrange = roll_result
                player_rolling = 'player01'


# Create players
player01 = Player(input("Enter player 1's name: "))
player02 = Player(input("Enter player 2's name: "))

# Welcome the players
player01.welcome_player()
player02.welcome_player()

# Prompt for the wager:
while True:
    try:
        wager = int(input('How much do you wager? '))
        if wager <= 0:
            raise(ValueError)
        confirmation = input(f"Are you sure you wish to wager ${wager}? yes/no/cancel ")
        if confirmation == 'cancel':
            break
        elif confirmation == 'no':
            print("Please choose an amount to wager wisely.")
        elif confirmation == 'yes':
            print(f"Good Luck!\nYou're wager is ${wager}.")
            break
    except ValueError:
        print("Please enter a value above 0")

roll_start_count = wager * 10
game_start = Deathroll(roll_start_count)

game_start.roll()




#print(roll_start_count)
# print(type(wager))
# print(wager)