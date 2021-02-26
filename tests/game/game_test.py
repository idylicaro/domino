from src.game.game import Game, Board, Piece, Player


def stub_pack_pieces() -> [[Piece]]:
    pack1 = [
        Piece(0, 0), Piece(0, 1), Piece(0, 2), Piece(0, 3),
        Piece(0, 4), Piece(0, 5), Piece(0, 6)
    ]
    pack2 = [
        Piece(1, 2), Piece(1, 3), Piece(1, 4), Piece(1, 5),
        Piece(1, 6), Piece(2, 2), Piece(2, 3)
    ]
    pack3 = [
        Piece(4, 5), Piece(4, 6), Piece(5, 5), Piece(5, 6),
        Piece(6, 6), Piece(2, 4), Piece(1, 1)
    ]
    pack4 = [
        Piece(2, 5), Piece(2, 6), Piece(3, 3), Piece(3, 4),
        Piece(3, 5), Piece(3, 6), Piece(4, 4)
    ]
    return [pack1, pack2, pack3, pack4]


def stub_players_factory():
    pieces_packs = stub_pack_pieces()
    players = [
        Player('player1', pieces_packs[0]),
        Player('player2', pieces_packs[1]),
        Player('player3', pieces_packs[2]),
        Player('player4', pieces_packs[3])
    ]
    return players


class TestGame:
    def test_init_game(self):
        board = Board()
        game = Game(board, stub_players_factory())
        assert game.get_board() is board
