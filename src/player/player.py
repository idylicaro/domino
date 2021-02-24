from typing import List

from src.pieces.Piece import Piece


class Player(object):
    """
    This Class representing a piece on game
    ...
    Attributes
    ----------
    name : str
        the player name
    pieces : list
        list of pieces
    Methods
    -------
    get()
        Return a tuple with values of player
    """

    def __init__(self, name: str, pieces: list):
        """
            Parameters
            ----------
            name : str
                player name
            pieces : list
                player pieces list
        """
        self.name = name
        self.pieces: List[Piece] = pieces

    def get(self):
        """ Return a tuple with values of piece """
        return self.name, self.pieces

    def play(self, piece: Piece) -> Piece or None:
        """ Remove the specified piece and return this """
        for x in range(len(self.pieces)):
            if self.pieces[x].compare(piece):
                self.pieces.pop(x)
                return piece
        return None

