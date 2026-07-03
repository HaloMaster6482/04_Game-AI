import random
from colorama import Fore, Style, init

init(autoreset=True)

win_conditions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0, 3, 6), (1, 4, 7), (2,5,8),
    (0,4,8), (2,4,6)   
]

def display_board(board):
    print()
    def cell_color(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else: 
            Fore.WHITE + cell + Style.RESET_ALL
    print(" ", cell_color(board[0]) + " | " + cell_color(board[1]))