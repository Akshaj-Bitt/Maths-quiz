board = [" "] * 9

scores = {"X": 0, "O": 0, "Draw": 0}

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def display_guide():
    print("\n  Position Guide:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()


def player_move(player):
    while True:
        try:
            position = input(f"Player {player}, enter your position (1-9): ")
            position = int(position)

            if position < 1 or position > 9:
                print("Invalid! Please enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already taken! Try another.")
                continue

            board[index] = player
            break

        except ValueError:
            print("Invalid input! Please enter a number, not letters or symbols.")


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def check_draw():
    if " " not in board:
        return True
    return False



def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"




def reset_game():
    for i in range(9):
        board[i] = " "

def display_scores():
    print("====== SCOREBOARD ======")
    print(f"  Player X : {scores['X']} wins")
    print(f"  Player O : {scores['O']} wins")
    print(f"  Draws    : {scores['Draw']}")

def play_game():
    print("   WELCOME TO TIC TAC TOE! ")

    display_guide()

    current_player = "X"

    while True:
        display_board()
        print(f"  Player {current_player}'s turn")

        player_move(current_player)

        if check_winner(current_player):
            display_board()
            print(f"Congratulations! Player {current_player} WINS!")
            scores[current_player] += 1
            break

        if check_draw():
            display_board()
            print(" DRAW! Well played both!")
            scores["Draw"] += 1
            break

        current_player = switch_player(current_player)

while True:
    reset_game()
    play_game()
    display_scores()

    again = input("\nDo you want to play again? (yes / no): ").strip().lower()

    if again == "yes" or again == "y":
        print("\n Starting a new game...\n")
    else:
        print("\nThanks for playing! Goodbye!")
        break