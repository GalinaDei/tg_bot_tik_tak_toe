import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

from tik_tak_toe import *
from spy import *


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}! Для начала игры введи команду /new_game.')


global n
global board
global win_coord


def start_game(update: Update, context: CallbackContext):
    take_board()
    take_win_coord()
    global n
    print(get_win_coord())
    print("New game")
    n = random.randint(0, 1)
    if n:
        log(update, context)
        update.message.reply_text(f'Ваша партия - Х')
        update.message.reply_text(f'Это игровое поле:\n{draw_board()}')
        update.message.reply_text(f"{update.effective_user.first_name}, Ваш ход. "
                                      f"Введите номер ячейки на игровом поле, которую хотите занять")
    else:
        update.message.reply_text(f'Ваша партия - О')
        update.message.reply_text(f'Это игровое поле:\n{draw_board()}')
        rnd = None
        while str(rnd) not in get_board():
            rnd = random.randint(1, 9)
        get_board()[get_board().index(str(rnd))] = "X"
        update.message.reply_text(f"Бот сделал ход. \n{draw_board()}")
        update.message.reply_text(f"{update.effective_user.first_name}, Ваш следующий ход. "
                                  f"Введите номер свободной ячейки на игровом поле")


def playerX(update: Update, context: CallbackContext):
    global n
    if n:
        msg = update.message.text
        log(update, context)
        if msg in get_board():
            get_board()[get_board().index(msg)] = "X"
            check_winX(msg)
            check_winO(msg)
            if check_win():
                update.message.reply_text(f"{update.effective_user.first_name} сделал ход и выиграл. \n{draw_board()}")
                update.message.reply_text(f"Новая игра - /new_game")
            else:
                update.message.reply_text(f"{update.effective_user.first_name}, сделал ход. Ваш ход, бот!")
                update.message.reply_text(f"{draw_board()}")
                rnd = None
                while str(rnd) not in get_board():
                    rnd = random.randint(1,9)
                get_board()[get_board().index(str(rnd))] = "O"
                check_winO(str(rnd))
                if check_win():
                    update.message.reply_text(f"Бот сделал ход и выиграл. \n{draw_board()}")
                    update.message.reply_text(f"Новая игра - /new_game")
                else:
                    update.message.reply_text(f"Бот сделал ход. \n{draw_board()}")
                    update.message.reply_text(f"{update.effective_user.first_name}, Ваш следующий ход. "
                                                      f"Введите номер свободной ячейки на игровом поле")
        else:
            update.message.reply_text(f"Некорректный ввод")
    else:
        playerO(update, context)


def playerO(update: Update, context: CallbackContext):
    global n
    if not n:
        msg = update.message.text
        log(update, context)
        if msg in get_board():
            get_board()[get_board().index(msg)] = "O"
            check_winO(msg)
            if check_win():
                update.message.reply_text(f"{update.effective_user.first_name} сделал ход и выиграл. \n{draw_board()}")
                update.message.reply_text(f"Новая игра - /new_game")
            else:
                update.message.reply_text(f"{update.effective_user.first_name}, сделал ход. Ваш ход, бот!")
                update.message.reply_text(f"{draw_board()}")
                rnd = None
                while str(rnd) not in get_board():
                    rnd = random.randint(1,9)
                get_board()[get_board().index(str(rnd))] = "X"
                check_winX(str(rnd))
                if check_win():
                    update.message.reply_text(f"Бот сделал ход и выиграл. \n{draw_board()}")
                    update.message.reply_text(f"Новая игра - /new_game")
                else:
                    update.message.reply_text(f"Бот сделал ход. \n{draw_board()}")
                    update.message.reply_text(f"{update.effective_user.first_name}, Ваш следующий ход. "
                                              f"Введите номер свободной ячейки на игровом поле")
        else:
            update.message.reply_text(f"Некорректный ввод")
    else:
        playerX(update, context)



# def say_hi(update, context):
#     # Получаем информацию о чате и сохраняем в переменную chat
#     chat = update.effective_chat
#     # В ответ на любое текстовое сообщение будет отправлен ответ 'Привет, я бот'
#     context.bot.send_message(chat_id=chat.id, text='Привет, я бот')


#     def echo_command(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     update.message.reply_text(f'{msg}')
# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

# def help_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'Доступные команды:\n/start\n/hi\n/time\n/help\n/new_game')
