from src.pieces.Piece import Piece


class TestPiece:
    def test_get(self):
        piece = Piece(0, 1)
        (L, R) = piece.get()
        assert L == 0 and R == 1

    def test_flip(self):
        piece = Piece(0, 1)
        piece.flip()
        (L, R) = piece.get()
        assert L == 1 and R == 0
