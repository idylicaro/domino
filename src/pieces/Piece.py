class Piece(object):
    """
    This Class representing a piece on game
    ...
    Attributes
    ----------
    side_left : int
        value of Left side of piece (0-6)
    side_right : int
        value of Left side of piece (0-6)

    Methods
    -------
    get()
        Return a tuple with values of piece
    flip():
        Turn over side left with side right
    compare()
        Compare himself with other pieces
    """

    def __init__(self, side_left, side_right):
        """
            Parameters
            ----------
            side_left : int
                value of Left side of piece (0-6)
            side_right : int
                value of Left side of piece (0-6)
        """
        self.__side_left = side_left
        self.__side_right = side_right

    def get(self):
        """ Return a tuple with values of piece """
        return self.__side_left, self.__side_right

    def get_left_side(self):
        """ Return left side of piece"""
        return self.__side_left

    def get_right_side(self):
        """ Return right side of piece"""
        return self.__side_right

    def flip(self):
        """ Turn over side left with side right """
        temp = self.__side_left
        self.__side_left = self.__side_right
        self.__side_right = temp

    def compare(self, piece) -> bool:
        """ Compare himself with other pieces """
        if self.get() == piece.get():
            return True

        piece.flip()
        if self.get() == piece.get():
            return True

        return False
