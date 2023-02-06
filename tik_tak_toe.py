import logging
import random

global board
global win_coord


def take_win_coord():
    global win_coord
    win_coord = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"],
             ["1", "5", "9"], ["3", "5", "7"]]
    return win_coord


def get_win_coord():
    global win_coord
    return win_coord


def take_board():
    global board
    board = ['1', '  ', '2', '  ', '3', '\n', '4', '  ', '5', '  ', '6', '\n', '7', '  ', '8', '  ', '9']
    return board

def get_board():
    global board
    return board


def draw_board():
    global board
    return (
        f"{board[0]}  {board[2]}  {board[4]}\n{board[6]}  {board[8]}  {board[10]}\n{board[12]}  {board[14]}  {board[16]}")


def check_winX(str):
    global win_coord
    for s in win_coord:
        for i in range(3):
            if s[i] == str:
                s[i] = "X"
    return win_coord


def check_winO(str):
    global win_coord
    for s in win_coord:
        for i in range(3):
            if s[i] == str:
                s[i] = "O"
    return win_coord


def check_win():
    global win_coord
    if ['X', 'X', 'X'] in win_coord or ['O', 'O', 'O'] in win_coord:
        return True
    else:
        return False
