from src.board.board import Board
from src.pieces.Piece import Piece


class TestBoard:
    def test_play(self):
        board = Board()
        assert board.play((Piece(6, 6)), 'LEFT').compare(Piece(6, 6))
        assert board.play((Piece(6, 0)), 'RIGHT').compare(Piece(6, 0))
        assert board.play((Piece(1, 0)), 'RIGHT').compare(Piece(0, 1))
        assert board.play((Piece(2, 6)), 'LEFT').compare(Piece(2, 6))
        assert board.play((Piece(2, 3)), 'LEFT').compare(Piece(3, 2))

    def test_play_first_round_not_six_bomb(self):
        board = Board()
        assert (board.play((Piece(6, 5)), 'LEFT')) is None

    def test_play_invalid_move(self):
        board = Board()
        assert board.play((Piece(6, 6)), 'LEFT').compare(Piece(6, 6))
        assert (board.play((Piece(0, 0)), 'RIGHT')) is None
        assert (board.play((Piece(0, 0)), 'LEFT')) is None

    def test_get_first_and_last_piece(self):
        board = Board()
        board.play((Piece(6, 6)), 'LEFT')
        assert board.get_first_piece().compare(Piece(6, 6))
        assert board.get_last_piece().compare(Piece(6, 6))
