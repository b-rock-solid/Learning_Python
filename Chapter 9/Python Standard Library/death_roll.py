"""Simulates the death roll gamble from WoW."""


class Player:
    """Begin the deathroll"""

    def __init__(self, player_name):
        """Initialize the players and the amount wagered."""
        self.player_name = player_name

    def welcome_player(self):
        """Formats the players name neatly"""
        print(f"Welcome to Deathroll {self.player_name.title()}!")


# Create players
player01 = Player(input("Enter player 1's name: "))
player02 = Player(input("Enter player 2's name: "))

player01.welcome_player()
player02.welcome_player()

# Prompt for the wager:
while True:
    try:
        wager = float(input('How much do you wager? '))
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
        else:
            print("Please enter a numerical value for your wager.")
    except ValueError:
        print("Please enter a value above 0")

print(type(wager))
print(wager)