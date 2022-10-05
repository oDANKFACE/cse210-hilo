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

    def start_game(self):
        while self.is_playing:
            pass

    def get_input(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
