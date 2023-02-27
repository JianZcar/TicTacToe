import tkinter as tk
from tkinter import ttk


turn = 1
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
winner = ''
win = False


def display_text(widget, text_):
    widget.configure(text=text_)


def winner_check(grid, column, row):
    columns = []
    rows = []

    if column == 0:
        columns = [column, column + 1, column + 2]
    elif column == 1:
        columns = [column + 1, column, column - 1]
    elif column == 2:
        columns = [column - 2, column - 1, column]

    if row == 0:
        rows = [row, row + 1, row + 2]
    elif row == 1:
        rows = [row + 1, row, row - 1]
    elif row == 2:
        rows = [row - 2, row - 1, row]

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
    global win
    global winner
    global turn
    if grid[row][column] == '':
        if not win:
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
    if not win:
        win = winner_check(grid, column, row)
        if winner_check(grid, column, row):
            winner = grid[row][column]
            display_text(label, f'Winner : {winner}')
        print(win, winner)


def button_tic_tac_toe(master, column_, row_, label):
    style = ttk.Style()
    style.configure('Custom.TButton', width=0, font=("Helvetica", 30))

    button = ttk.Button(master, style='Custom.TButton', takefocus=False,
                        command=lambda: update_board(board, column_, row_, button, label=label))
    button.grid_configure(column=column_, row=row_, sticky="nsew")
    master.rowconfigure(row_, minsize=65)
    master.columnconfigure(column_, minsize=65)
    return button


def restart_game(window, winner_):
    global turn
    global board
    global win
    global winner
    turn = 1
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    winner = ''
    win = False
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
        self.label_winner.configure(font=("Helvetica", 15))
        self.restart_button = ttk.Button(self.frame2, text='Restart', takefocus=False, command=lambda: restart_game(
            self.frame, self.label_winner))
        self.restart_button.grid_configure(row=1, column=0)

        self.button0 = button_tic_tac_toe(self.frame, 0, 0, self.label_winner)
        self.button1 = button_tic_tac_toe(self.frame, 1, 0, self.label_winner)
        self.button2 = button_tic_tac_toe(self.frame, 2, 0, self.label_winner)
        self.button3 = button_tic_tac_toe(self.frame, 0, 1, self.label_winner)
        self.button4 = button_tic_tac_toe(self.frame, 1, 1, self.label_winner)
        self.button5 = button_tic_tac_toe(self.frame, 2, 1, self.label_winner)
        self.button6 = button_tic_tac_toe(self.frame, 0, 2, self.label_winner)
        self.button7 = button_tic_tac_toe(self.frame, 1, 2, self.label_winner)
        self.button8 = button_tic_tac_toe(self.frame, 2, 2, self.label_winner)


if __name__ == '__main__':
    root = tk.Tk()
    tic_tac_toe = GameWindow(root)
    root.mainloop()
