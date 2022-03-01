import uuid as uuid_lib
from termcolor import colored
from random import *
from typing import *

from common.data_structures import Player, Move, Message
from common.data_structures.profiles import Profile


def manhattan(index1: str, index2: str) -> int:
    return abs(ord(index1[:1]) - ord(index2[:1])) + abs(
        int(index1[1:]) - int(index2[1:])
    )


def get_adjacent(board: dict, index: str) -> List[str]:
    l1 = list()
    for i in [-1, 1]:
        w = chr(ord(index[:1]) + i) + index[1:]
        b = index[:1] + str(int(index[1:]) + i)
        l1.append(w) if w in board else l1
        l1.append(b) if b in board else l1
    return l1


class LocalGame:
    """
    Data class containing the game, not intended to be sent through the network.
    """

    def __init__(
        self,
        name: str,
        game_creator: Player,
        tiles_remaining: int,
    ):
        self.s: int = 13
        self.chat: List[Message] = list()
        self.moves: List[Move] = list()
        self.board: Dict[str, Tuple[str, int]] = dict()
        for i in range(self.s):
            for j in range(self.s):
                self.board[(chr(i + ord("A")) + str(j))] = ("None", 0)
        self.game_creator: Player = game_creator
        self.white_player: Union[Player, None] = None
        self.red_player: Union[Player, None] = None
        self.nb_towers: int = 0
        self.tiles_remaining: int = tiles_remaining
        self.name: str = name
        self.game_uuid: uuid_lib.UUID = uuid_lib.uuid4()
        self.status: str = "waiting_player"

    """
    Class builder.
    """

    def __str__(self):
        token = {
            "Tower": colored("♖", "magenta"),
            "Red": colored("⛀", "red"),
            "White": colored("⛀", "yellow"),
            "None": colored("▯", "blue"),
        }
        print("ㅤ" * 2, end="")
        for i in range(self.s):
            print(str(i)[-1] + "ㅤ", end="")
        for i, j in zip(self.board, range(len(self.board))):
            if j % self.s == 0:
                print("\n" + chr(int(j / self.s) + ord("A")) + "  ", end="")
            print(token[self.board[i][0]] + " ", end=colored(""))
        return ""

    """
    Method to quickly display the status of a game.
    """

    def get_uuid(self) -> uuid_lib.UUID:
        return self.game_uuid

    def get_towers_remaining(self) -> int:
        return 5 - self.nb_towers

    """
    Method to get the UUID and towers remaining.
    """

    def get_current_player(self) -> Union[Player, None]:
        if len(self.moves) % 2 == 0:
            return self.red_player
        else:
            return self.white_player

    """
    Method to know who should play.
    """

    def define_white_player(self, white_player: Player):
        if self.white_player is None:
            self.white_player = white_player

    def define_red_player(self, red_player: Player):
        if self.red_player is None:
            self.red_player = red_player

    """
    Methods to define the red player and the white player.
    """

    def get_str_player(self) -> str:
        return "White" if self.get_current_player() == self.white_player else "Red"

    def add_move(self, m_move: Move):
        if m_move.get_type() == "":
            self.moves.append(m_move)
        else:
            if self.check_move_in_local_game(m_move):
                if m_move.get_type() == "Pown":
                    self.board[m_move.get_index()] = (
                        self.get_str_player(),
                        self.board[m_move.get_index()][1] + 1,
                    )
                    self.tiles_remaining -= 1
                    self.moves.append(m_move)
                if m_move.get_type() == "Tower":
                    self.board[m_move.get_index()] = (
                        "Tower",
                        self.board[m_move.get_index()][1] + 1,
                    )
                    self.nb_towers += 1
                    self.moves.append(m_move)

    """
    Method to add a pown to the game.
    """

    def valid_moves_pown(self) -> List[str]:
        moves = list()
        if self.tiles_remaining and self.nb_towers >= 2:
            current_player = self.get_str_player()
            for i in self.board:
                if self.board[i][0] != "Tower":
                    if self.board[i][0] == "None":
                        moves.append(i)
                    else:
                        if self.board[i][0] == current_player:
                            for j in get_adjacent(self.board, i):
                                if self.board[j][0] == current_player:
                                    if self.board[j][1] >= self.board[i][1]:
                                        moves.append(i)
                                        break
        return moves

    def valid_moves_tower(self):
        moves = list()
        if self.nb_towers < 5:
            towers = self.get_tower_list()
            not_a_move = list()
            for i in self.board:
                for j in towers:
                    if manhattan(i, j) <= 3:
                        not_a_move.append(i)
                        break
            moves = [i for i in self.board if not (i in not_a_move)]
        return moves

    """
    Two methods to recover all possible moves for the current player.
    """

    def check_move_in_local_game_slow(self, my_move: Move) -> bool:
        if my_move.get_type() == "Tower":
            return my_move.get_index() in self.valid_moves_tower()
        else:
            if my_move.get_type() == "Pown":
                return my_move.get_index() in self.valid_moves_pown()
            else:
                return True

    def check_move_in_local_game(self, my_move: Move) -> bool:
        if my_move.get_type() == "Tower":
            if self.nb_towers < 5:
                for j in self.get_tower_list():
                    if manhattan(my_move.get_index(), j) <= 3:
                        return False
                return True
            return False
        else:
            if my_move.get_type() == "Pown":
                if self.tiles_remaining and self.nb_towers >= 2:
                    if self.board[my_move.get_index()][0] != "Tower":
                        if self.board[my_move.get_index()][0] == "None":
                            return True
                        for j in get_adjacent(self.board, my_move.get_index()):
                            if self.board[j][0] == self.get_str_player():
                                if (
                                    self.board[j][1]
                                    >= self.board[my_move.get_index()][1]
                                ):
                                    return True
                return False
            else:
                return True

    """
    Two methods to check if the given move is valid (a fast and a slow).
    """

    def get_local_game_grid(self) -> Dict[str, Tuple[str, int]]:
        return self.board

    """
    Method to get the dict which represents the game board.
    """

    def get_local_players(self) -> Tuple[Union[Player, None], Union[Player, None]]:
        return self.red_player, self.white_player

    """
    This method returns a tuple with all two players in the game.
    """

    def check_path(self, debut: str, fin: str, player: str) -> bool:
        dic = {fin: 0}
        for i in self.board:
            if self.board[i][0] == player:
                dic[i] = 0

        li = {debut: manhattan(debut, fin)}

        while not (fin in li):

            if len(list(li.keys())) == 0:
                return False
            first_key = list(li.keys())[0]
            li[first_key] = li[first_key] + 1

            for a in get_adjacent(dic, first_key):
                if not (a in li):
                    li[a] = manhattan(a, fin) + (
                        li[first_key] - manhattan(first_key, fin)
                    )
                del dic[a]

            del li[first_key]

            li = dict(sorted(li.items(), key=lambda x: x[1]))
        return True

    """
    This method checks if there is a path of one colour between two towers.
    """

    def get_tower_list(self) -> List[str]:
        towers: List[str] = list()
        for i in self.board:
            if self.board[i][0] == "Tower":
                towers.append(i)
        return towers

    def get_winner(self) -> List[Union[Player, None, List[int]]]:
        towers = self.get_tower_list()
        red_nb = 0
        white_nb = 0
        for i in range(len(towers)):
            for j in range(i + 1, len(towers)):
                if self.check_path(towers[i], towers[j], "Red"):
                    red_nb += 1
                if self.check_path(towers[i], towers[j], "White"):
                    white_nb += 1
        score = [white_nb, red_nb]
        score.sort(reverse=True)
        if white_nb > red_nb:
            return [self.white_player, score]
        else:
            return (
                [self.white_player, self.red_player, score]
                if white_nb == red_nb
                else [self.red_player, score]
            )

    """
    Method that checks who won the game.
    """

    def add_message(self, message: Message):
        self.chat.append(message)

    def get_chat(self) -> List[Message]:
        return self.chat

    """
    Getter and setter for the chat
    """


if __name__ == "__main__":
    joris = Player("Joris", uuid_lib.uuid4())
    clem = Player("Clem", uuid_lib.uuid4())
    test = LocalGame("TheFistGame", clem, 250)
    test.define_white_player(clem)
    test.define_red_player(joris)

    a_move: Move

    for i in range(5):
        keys = [i for i in test.valid_moves_tower()]
        a_move = Move(
            test.get_uuid(),
            test.get_current_player(),
            keys[randint(0, len(keys) - 1)],
            "Tower",
        )
        if test.check_move_in_local_game(a_move):
            test.add_move(a_move)

    print(test)

    for i in range(250):
        keys = [i for i in test.valid_moves_pown()]
        a_move = Move(
            test.get_uuid(),
            test.get_current_player(),
            keys[randint(0, len(keys) - 1)],
            "Pown",
        )
        if test.check_move_in_local_game(a_move):
            test.add_move(a_move)

    print(test)
    print(test.get_winner())
