from game.card import Card


class Director:
    """
    Game Director

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: an instance of the Card class.
        is_playing (boolean): Whether the game is being played.
        score (int): The running score for the game.
    """

    def __init__(self):
        self.is_playing = True
        self.card = Card()
        self.score = 300
        self.choice = ""

    def start_game(self):
        print(f"Your score is: {self.score}")
        while self.is_playing:
            self.pose_card()
            self.get_input()
            self.do_updates()
            self.do_outputs()

    def pose_card(self):
        print(f"The card is: {self.card.get_value()}")

    def get_input(self):
        self.choice = ""
        while self.choice not in ("h", "l"):
            self.choice = (input("Higher or lower? [h/l] ")).lower()

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
