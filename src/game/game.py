from src.pieces.Piece import Piece
from src.board.board import Board
from src.player.player import Player


class Game(object):
    def __init__(self, board: Board, players: [Player]):
        self.__board = board
        self.__players: {int: Player} = {1: players[0], 2: players[1], 3: players[2], 4: players[3]}
        self.__round = 0
        self.__remaining_pieces = {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7}
        self.__player_selected = 1
        self.__winner = None
        self.__draw = False
        self.__end_game = False

    def start(self):
        while self.__end_game:
            # TODO: validate player to play
            # TODO: if player is not a bot, catch input for play
            # TODO: call board and player to play
            # TODO: if player are a bot, implementing your play
            self.__update_endgame()
            self.__next_player()

    def __next_player(self):
        if self.__player_selected < 4:
            self.__player_selected += 1
        else:
            self.__player_selected = 1

    def __update_endgame(self):
        not_remaining_piece = True
        for i in range(1, 6):
            if self.__remaining_pieces[i] > 0:
                not_remaining_piece = False

        left_piece: Piece = self.__board.get_first_piece()
        right_piece: Piece = self.__board.get_last_piece()
        pieces = {'L': left_piece.get_left_side(), 'R': right_piece.get_right_side()}

        if self.__remaining_pieces[pieces['L']] == 0 and self.__remaining_pieces[pieces['R']] == 0:
            self.__count_points_and_finish_game()
        elif not_remaining_piece:
            self.__winner = self.__players[self.__player_selected]
            self.__end_game = True
        else:
            return

    def __count_points_and_finish_game(self):
        self.__end_game = True
        players_points = [0, 0, 0, 0]
        for i in range(1, 4):
            for j in range(len(self.__players[i].pieces)):
                (l, r) = self.__players[i].pieces[j].get()
                players_points[i] += (l + r)

        if players_points[0] == players_points[1] or players_points[0] == players_points[2] or \
                players_points[0] == players_points[3] or players_points[1] == players_points[2] or \
                players_points[1] == players_points[3] or players_points[2] == players_points[3]:
            self.__draw = True
            return
        elif players_points[0] < players_points[1] and players_points[0] < players_points[2] and players_points[0] < \
                players_points[3]:
            self.__winner = self.__players[0]
        elif players_points[1] < players_points[0] and players_points[1] < players_points[2] and players_points[1] < \
                players_points[3]:
            self.__winner = self.__players[1]
        elif players_points[2] < players_points[0] and players_points[2] < players_points[1] and players_points[2] < \
                players_points[3]:
            self.__winner = self.__players[2]
        elif players_points[3] < players_points[0] and players_points[3] < players_points[1] and players_points[3] < \
                players_points[2]:
            self.__winner = self.__players[3]

    def get_board(self) -> Board:
        return self.__board
