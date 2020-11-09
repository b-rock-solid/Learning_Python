# Try It Yourself Exercise - Pg.181
# 9-13 Dice
########################################################################################################################
# Make a class Die with one attribute called sides
# Give it a default value of 6
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has
# Make a 6-sided die and roll it 10 times
# Make a 10-sided die and a 20-sided die. Roll each die 10 times
########################################################################################################################

from random import randint

class Die:
    """Creating a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, rolls=10):
        """A method to roll the selected die."""
        self.rolls = rolls
        roll_count = 0
        print(f"Rolling a {self.sides} sided die {rolls} times:")
        while roll_count < rolls:
            print(randint(1, self.sides))
            roll_count += 1

dice_6 = Die()
dice_6.roll_die()

dice_10 = Die(sides=10)
dice_10.roll_die()

dice_20 = Die(sides=20)
dice_20.roll_die()