from src.pieces.Piece import Piece
from src.player.player import Player


class TestPlayer:
    def test_get(self):
        player = Player('player', [])
        (name, _pieces) = player.get()
        assert name == 'player' and _pieces == []

    def test_play_return_piece_and_none_if_play_again(self):
        player = Player('player', [Piece(1, 0)])
        returned_piece = player.play(Piece(1, 0))
        assert returned_piece.compare(Piece(1, 0))
        returned_piece = player.play(Piece(1, 0))
        assert returned_piece is None

    def test_is_bot(self):
        player = Player('player', [])
        player1 = Player('player', [], True)
        assert player.is_bot() == False
        assert player1.is_bot() == True
