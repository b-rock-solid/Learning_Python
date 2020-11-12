from random import randint
from time import sleep

"""Simulates the death roll gamble from WoW."""


class Player:
    """Basic template of a player."""

    def __init__(self, player_name, wallet=50):
        """Initialize the players and the amount wagered."""
        self.player_name = player_name
        self.wallet = wallet

    def welcome_player(self):
        """Prints the player a welcome message."""
        print(f"\nWelcome to Deathroll {self.player_name.title()}!"
              f"\nYou have ${self.wallet} to spend.")

    def player_wallet(self):
        """Prompts players to enter the amount they have available in their wallet."""
        while True:
            try:
                self.wallet = (int(input(f"Enter the wallet amount for {self.player_name.title()}: ")))
                if self.wallet <= 0:
                    raise ValueError
                wallet_confirm = input(f"Are you sure you wish to start with ${self.wallet}(yes/no/cancel)? ")
                if wallet_confirm == 'cancel' or wallet_confirm == 'c':
                    exit(10)
                elif wallet_confirm == 'no' or wallet_confirm == 'n':
                    print("Please choose an amount to start with.")
                elif wallet_confirm == 'yes' or wallet_confirm == 'y':
                    break
                else:
                    print("Please confirm your wallet starting amount.")
            except ValueError:
                print("Please enter a positive whole number.")

    def show_wallet(self):
        """Shows the current balance of the players wallet."""
        print(f"{self.player_name.title()}, you have ${self.wallet} remaining!")




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
                print(f"\n{player01.player_name.title()} is now rolling:")
                sleep(2)
                roll_range = self.nrange
                roll_result = randint(1, roll_range)
                print(f"{player01.player_name.title()} has rolled: {roll_result}")
                self.nrange = roll_result
                player_rolling = 'player02'
            elif player_rolling == 'player02':
                print(f"\n{player02.player_name.title()} is now rolling:")
                sleep(2)
                roll_range = self.nrange
                roll_result = randint(1, roll_range)
                print(f"{player02.player_name.title()} has rolled: {roll_result}")
                self.nrange = roll_result
                player_rolling = 'player01'
        if player_rolling == 'player01':
            player01.wallet = player01.wallet + wager
            player02.wallet = player02.wallet - wager
            print(f"\nCongratulations {player01.player_name.title()} you win ${wager}")
        elif player_rolling == 'player02':
            player02.wallet = player02.wallet + wager
            player01.wallet = player01.wallet - wager
            print(f"\nCongratulations {player02.player_name.title()} you win ${wager}")


class WagerError01(Exception):
    """Raised error when insufficient funds are in player01's wallet."""
    pass


class WagerError02(Exception):
    """Raised error when insufficient funds are in player02's wallet."""
    pass


# Create players
player01 = Player(input("Enter player 1's name: "))
player02 = Player(input("Enter player 2's name: "))

# Set players starting wallet balance
player01.player_wallet()
player02.player_wallet()

# Welcome the players
player01.welcome_player()
player02.welcome_player()

# Begin the game loop
active = True
while active:
    # Prompt for the wager:
    while True:
        try:
            wager = int(input('\nHow much do you wager? '))
            if wager <= 0:
                raise ValueError
            elif wager > player01.wallet:
                raise WagerError01
            elif wager > player02.wallet:
                raise WagerError02
            confirmation = input(f"Are you sure you wish to wager ${wager}(yes/no/cancel)? ")
            if confirmation == 'cancel' or confirmation == 'c':
                exit(10)
            elif confirmation == 'no' or confirmation == 'n':
                print("Please choose an amount to wager wisely.")
            elif confirmation == 'yes' or confirmation == 'y':
                print(f"Good Luck!\nYou're wager is ${wager}.")
                break
        except ValueError:
            print("Please enter a value above 0")
        except WagerError01:
            print(f"{player01.player_name.title()} has insufficient funds for this wager."
                  f"\nCurrently {player01.player_name.title()} has ${player01.wallet} available.")
        except WagerError02:
            print(f"{player02.player_name.title()} has insufficient funds for this wager."
                  f"\nCurrently {player02.player_name.title()} has ${player02.wallet} available.")


    # Gather the starting roll max number
    roll_start_count = wager * 10

    # Begin game
    game_start = Deathroll(roll_start_count)
    game_start.roll()

    # Show wallet balances
    player01.show_wallet()
    player02.show_wallet()

    # Check that wallet balances aren't 0
    if player01.wallet == 0:
        print(f"{player01.player_name.title()} is now broke!"
              f"\n{player02.player_name.title()} is the winner!"
              f"\nBut can you really call yourself a winner?"
              f"\n\nHope you enjoyed rolling to the death!")
        sleep(5)
        exit(0)
    if player02.wallet == 0:
        print(f"{player02.player_name.title()} is now broke!"
              f"\n{player01.player_name.title()} is the winner!"
              f"\nBut can you really call yourself a winner?"
              f"\n\nHope you enjoyed rolling to the death!")
        sleep(5)
        exit(0)

    # Prompt to play again
    while True:
        try:
            play_again = input("\nDo you wish to play again(y/n)? ")
            if play_again == "n":
                print("\nThanks for playing Death Roll! =)")
                sleep(3)
                exit(0)
            elif play_again == "y":
                print("\nLets do it!")
                break
            else:
                raise (ValueError)
        except ValueError:
            print("Sorry, I don't understand that.")
