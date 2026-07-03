import random
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.WHITE + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + f'{Fore.CYAN} | ' + colored(board[1]) + f'{Fore.CYAN} | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + f'{Fore.CYAN} | ' + colored(board[4]) + f'{Fore.CYAN} | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + f'{Fore.CYAN} | ' + colored(board[7]) + f'{Fore.CYAN} | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(f"Do you want to be {Fore.RED}X{Fore.WHITE} or{Fore.BLUE} O{Fore.WHITE}? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def minimax(board, ai_symbol, player_symbol, is_maximizing, depth=0):
    if check_win(board, ai_symbol):
        return 10 - depth
    if check_win(board, player_symbol):
        return depth - 10
    if check_full(board):
        return 0

    possible_moves = [i for i in range(9) if board[i].isdigit()]

    if is_maximizing:
        best_score = -float('inf')
        for i in possible_moves:
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            score = minimax(board_copy, ai_symbol, player_symbol, False, depth + 1)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in possible_moves:
            board_copy = board.copy()
            board_copy[i] = player_symbol
            score = minimax(board_copy, ai_symbol, player_symbol, True, depth + 1)
            best_score = min(best_score, score)
        return best_score

def ai_move(board, ai_symbol, player_symbol):
    possible_moves = [i for i in range(9) if board[i].isdigit()]

    # If the AI is moving first (empty board), pick randomly among
    # equally strong opening moves to keep the game interesting while
    # still remaining unbeatable.
    if len(possible_moves) == 9:
        move = random.choice(possible_moves)
        board[move] = ai_symbol
        return

    best_score = -float('inf')
    best_moves = []
    for i in possible_moves:
        board_copy = board.copy()
        board_copy[i] = ai_symbol
        score = minimax(board_copy, ai_symbol, player_symbol, False, 0)
        if score > best_score:
            best_score = score
            best_moves = [i]
        elif score == best_score:
            best_moves.append(i)

    move = random.choice(best_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
        (0, 4, 8), (2, 4, 6) # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print(f"Welcome to{Fore.RED} Tic{Fore.WHITE}-{Fore.GREEN}Tac{Fore.WHITE}-{Fore.BLUE}Toe {Fore.WHITE}by Tavish!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulations! " + player_name + ", you have won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                print(Fore.RED + "AI is thinking...")
                sleep(1)

                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input(f"Do you want to play again? ({Fore.GREEN}yes{Fore.WHITE}/{Fore.RED}no{Fore.WHITE}): ").lower()
        if play_again != 'yes':
            print(Fore.MAGENTA +"Thank you for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()