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
        self.side_left = side_left
        self.side_right = side_right

    def get(self):
        """ Return a tuple with values of piece """
        return self.side_left, self.side_right

    def flip(self):
        """ Turn over side left with side right """
        temp = self.side_left
        self.side_left = self.side_right
        self.side_right = temp

    def compare(self, piece) -> bool:
        if self.get() == piece.get():
            return True

        piece.flip()
        if self.get() == piece.get():
            return True

        return False
