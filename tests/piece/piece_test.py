from src.pieces.Piece import Piece


class TestPiece:
    def test_get(self):
        piece = Piece(0, 1)
        (L, R) = piece.get()
        assert L == 0 and R == 1

    def test_get_side(self):
        piece = Piece(0, 1)
        assert piece.get_left_side() == 0
        assert piece.get_right_side() == 1

    def test_flip(self):
        piece = Piece(0, 1)
        piece.flip()
        (L, R) = piece.get()
        assert L == 1 and R == 0

    def test_compare_invalid(self):
        piece = Piece(0, 1)
        assert piece.compare(Piece(2, 5)) == False

    def test_compare_with_fliped_piece(self):
        piece = Piece(0, 1)
        assert piece.compare(Piece(1, 0)) == True