from player import Player
from game import Game


def print_game(game_session: Game):
    table = game_session.board
    cell_mask = {0: '▴', 1: 'X', 2: 'O'}

    for i in range(3):
        for j in range(3):
            print(cell_mask[table.get_cell_at(i, j)], end=' ')
        print()


print('Welcome to Tic-tac-toe game!!!\n\n')

name1 = input('Player1 username: ')
player1 = Player(name1)

name2 = input('Player2 username: ')
player2 = Player(name2)

game = Game(player1, player2)

while not game.is_over():
    print_game(game)
    x, y = (int(i) for i in input(f'{game.to_move.name}\'s move: ').split())
    game.choose(x, y)

print_game(game)

if not game.winner:
    print('\t!!!DRAW!!!\t')
else:
    print(f'{game.winner.name} won the match. Congratulations!')
