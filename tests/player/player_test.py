from src.pieces.Piece import Piece
from src.player.player import Player


class TestPlayer():
    def test_get(self):
        player = Player('player', [])
        (name, _pieces) = player.get()
        assert name == 'player' and _pieces == []

    def test_play_return_piece_and_raise_if_play_again(self):
        player = Player('player', [Piece(1, 0)])
        returned_piece = player.play(Piece(1, 0))
        assert returned_piece.compare(Piece(1, 0))
        returned_piece = player.play(Piece(1, 0))
        assert returned_piece is None
