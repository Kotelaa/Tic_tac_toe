
def create_game_board ():
    game_board = [[None, 0, 1, 2],
                  [0, "-", "-", "-"],
                  [1, "-", "-", "-"],
                  [2, "-", "-", "-"]]
    return game_board


def show_board(current_board):
    col_name = current_board[0][1: ]
    col_name = "  " + "  ".join(list(map(str, col_name)))
    print (col_name)

    for row in range(1, len(current_board)):
        row_name = current_board[row][0]
        play_filed = current_board[row][1: ]
        play_field = "  " + "  ".join(list(map(str, play_filed)))
        print (f"{row_name}{play_field}")


def get_play_field(current_board):
    play_field = []
    for row in range(1, len(current_board)):
        play_field.append(current_board[row][1: ])
    return play_field


def get_clean_player_move (player, current_board):
    print (f"Ход игрока {player}")

    while True:
        players_move = input(f"Введите строку и столбик, куда разместить {player}: ")

        # мы получили строку, из которой нужно удалить пробелы и запятые
        clean_player_move = players_move.replace(" ", "").split(",")

        if not clean_player_move[0].isdigit() or not clean_player_move[1].isdigit():
            print (f"Введите два числа (строку и столбик), куда разместить {player}!")
            continue

        # если игрок чисел != 2 --> повторный ввод
        if len(clean_player_move) != 2:
            print ("Введите два значения! ")
            continue

        player_move = [int(item) for item in clean_player_move]

        if not (0 <= player_move[0] <= 2 or 0 <= player_move[1] <= 2):
            print ("Ход за пределами доски! ")
            continue

        # проверить != "-"
        row_index = player_move[0] + 1
        col_index = player_move[1] + 1
        if current_board[row_index][col_index] != "-":
            print ("Место уже занято! Введите новые координаты! ")
            continue

        return player_move


def place_player_move (player, current_board):
    player_move = get_clean_player_move(player, current_board)
    row_index = player_move[0] + 1
    col_index = player_move[1] + 1
    current_board[row_index][col_index] = player
    print(f"Игрок {player} сделал свой ход на клетку {player_move}!")
    return current_board


def win_check (player, current_board):
    play_field = get_play_field(current_board)

    row_win = [all(cell == player for cell in row) for row in play_field]
    if any(row_win):
        print (f"Игрок {player} выиграл!")
        return True

    # play_field [0][0] == player and play_field [1][0] == player and play_field [2][0] == player
    # play_field [0][1] == player and play_field [1][1] == player and play_field [2][1] == player
    # play_field [0][2] == player and play_field [1][2] == player and play_field [2][2] == player
    col_win = []
    for col in range(3):
        win = all(play_field[row][col] == player for row in range(3))
        col_win.append(win)
    if any(col_win):
        print(f"Игрок {player} выиграл!")
        return True


    if (play_field[0][0] == player and play_field[1][1] == player
            and play_field[2][2] == player) or (play_field[0][2] == player and play_field[1][1] == player
    and play_field[2][0] == player):
        print(f"Игрок {player} выиграл!")
        return True


def tic_tac_toe():
    # создаем и показываем доску --> даем походить игроку
    # --> проверяем на победу --> заменяем игрока
    board = create_game_board()
    show_board(board)

    player = "X"

    while True:
        place_player_move(player, board)
        show_board(board)
        winner = win_check(player, board)
        if winner:
            break
        player = "0" if player == "X" else "X"
        draw = all(all(cell != "-" for cell in row) for row in board)
        if draw:
            print("Ничья!")
            break


tic_tac_toe()

