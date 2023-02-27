import tkinter as tk
from tkinter import ttk


turn = 1
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
winner = ''
game_over = False


def display_text(widget, text_):
    widget.configure(text=text_)


def winning_combi(x):
    list_ = []
    if x == 0:
        list_ = [x, x + 1, x + 2]
    elif x == 1:
        list_ = [x + 1, x, x - 1]
    elif x == 2:
        list_ = [x - 2, x - 1, x]
    return list_


def winner_check(grid, column, row):
    columns = winning_combi(column)
    rows = winning_combi(row)

    r_columns = reversed(rows)

    for y in rows:
        if grid[y][column] != grid[row][column]:
            break
    else:
        return True

    for x in columns:
        if grid[row][x] != grid[row][column]:
            break
    else:
        return True

    for (y, x) in zip(rows, columns):
        if grid[y][x] != grid[row][column]:
            break
    else:
        return True

    for (y, x) in zip(rows, r_columns):
        if grid[y][x] != grid[row][column]:
            break
    else:
        return True
    return False


def update_board(grid, column, row, button, label):
    global game_over
    global winner
    global turn
    if grid[row][column] == '':
        if not game_over:
            if turn == 1:
                grid[row][column] = 'O'
                display_text(button, 'O')
                turn = 2
            else:
                grid[row][column] = 'X'
                display_text(button, 'X')
                turn = 1

            for x in grid:
                print(x)
    if not game_over:
        game_over = winner_check(grid, column, row)
        if winner_check(grid, column, row):
            winner = grid[row][column]
            display_text(label, f'Winner : {winner}')
        print(game_over, winner)


def button_tic_tac_toe(master, column_, row_, label):
    style = ttk.Style()
    style.configure('Custom.TButton', width=0, font=('Helvetica', 30))

    button = ttk.Button(master, style='Custom.TButton', takefocus=False,
                        command=lambda: update_board(board, column_, row_, button, label=label))
    button.grid_configure(column=column_, row=row_, sticky='nsew')
    master.rowconfigure(row_, minsize=65)
    master.columnconfigure(column_, minsize=65)
    return button


def restart_game(window, winner_):
    global turn
    global board
    global game_over
    global winner
    turn = 1
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    winner = ''
    game_over = False
    for widgets in window.winfo_children():
        display_text(widgets, '')
    display_text(winner_, '')


class GameWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry()
        self.master.resizable(False, False)

        self.label_txt = ttk.Label(self.master, text='Tic Tac Toe', font=("Helvetica", 25))
        self.label_txt.grid_configure(row=0)

        self.frame = ttk.Frame(self.master)
        self.frame.grid_configure(row=1)

        self.frame2 = ttk.Frame(self.master, padding=10)
        self.frame2.grid_configure(row=2)
        self.frame2.columnconfigure(0, minsize=100)

        self.label_winner = ttk.Label(self.frame2, text='')
        self.label_winner.grid_configure(row=0, column=0, pady=5)
        self.label_winner.configure(font=('Helvetica', 15))
        self.restart_button = ttk.Button(self.frame2, text='Reset', takefocus=False, command=lambda: restart_game(
            self.frame, self.label_winner))
        self.restart_button.grid_configure(row=1, column=0)
        self.game_grid = []
        for y in range(3):
            row_ = []
            for x in range(3):
                row_.append(button_tic_tac_toe(self.frame, x, y, self.label_winner))
            self.game_grid.append(row_)


if __name__ == '__main__':
    root = tk.Tk()
    tic_tac_toe = GameWindow(root)
    root.mainloop()
