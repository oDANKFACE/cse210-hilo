import random


class Card:
    """
    The Game Card

    Simulates a deck of cards

    Attributes:
        values (list(int)): a list of all possible values of the card
        value (int): the number value of the card
    """

    def __init__(self):
        self.value = 0
        self.values = []

        for i in range (13):
            self.values.append(i + 1)

    def get_value(self):
        self.value = random.choice(self.values)
        return self.value

