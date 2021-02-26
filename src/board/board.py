from src.pieces.Piece import Piece


class Board:
    def __init__(self):
        self.pieces_on: [Piece] = list()

    def play(self, piece: Piece, position: str):
        if len(self.pieces_on) == 0:
            if (piece.get()) == (6, 6):
                self.pieces_on.append(piece)
            else:
                return None

        if position == "LEFT":
            first_piece_copy: Piece = self.pieces_on[0]
            if first_piece_copy.get_left_side() != piece.get_right_side():
                piece.flip()
                if first_piece_copy.get_left_side() != piece.get_right_side():
                    return None
            self.pieces_on.insert(0, piece)
        elif position == "RIGHT":
            last_piece_copy: Piece = self.pieces_on[len(self.pieces_on) - 1]
            if last_piece_copy.get_right_side() != piece.get_left_side():
                piece.flip()
                if last_piece_copy.get_right_side() != piece.get_left_side():
                    return None
            self.pieces_on.append(piece)
        return piece

    def get_first_piece(self):
        return self.pieces_on[0] if len(self.pieces_on) != 0 else None

    def get_last_piece(self):
        return self.pieces_on[len(self.pieces_on) - 1] if len(self.pieces_on) != 0 else None
