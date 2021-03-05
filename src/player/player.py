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
    play(piece:Piece)
        Remove the specified piece and return this
    is_bot()
        return value of is_bot (True | False)
    """

    def __init__(self, name: str, pieces: list, is_bot=False):
        """
            Parameters
            ----------
            is_bot: bool
                defines if the player is a bot or not
            name : str
                player name
            pieces : list
                player pieces list
        """
        self.__is_bot = is_bot
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

    def is_bot(self):
        return self.__is_bot

    def has_piece_to_play(self, board):
        """ Verify has possible play """
        left: Piece = board.get_first_piece()
        right: Piece = board.get_last_piece()
        for x in self.pieces:
            if x.get_left_side() == left.get_left_side() or x.get_right_side() == left.get_left_side():
                return True
            elif x.get_right_side() == right.get_right_side() or x.get_right_side() == left.get_right_side():
                return True
        return False
