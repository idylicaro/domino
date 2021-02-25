from src.board.board import Board
from src.pieces.Piece import Piece


class TestBoard:
    def test_play(self):
        board = Board()
        assert board.play((Piece(6, 6)), 'L').compare(Piece(6, 6))
        assert board.play((Piece(6, 0)), 'R').compare(Piece(6, 0))
        assert board.play((Piece(1, 0)), 'R').compare(Piece(0, 1))
        assert board.play((Piece(2, 6)), 'L').compare(Piece(2, 6))
        assert board.play((Piece(2, 3)), 'L').compare(Piece(3, 2))