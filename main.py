from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from bot_commands import *


updater = Updater('5729408340:AAEzop2b8TIxU9n6dBXx506svghZgbpMIHE')

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('new_game', start_game))
updater.dispatcher.add_handler(MessageHandler(Filters.text, playerX))
updater.dispatcher.add_handler(MessageHandler(Filters.text, playerO))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, place_sign_botX))
print('server start')
updater.start_polling()
updater.idle()


#updater.dispatcher.add_handler(CommandHandler('time', time_command))
#updater.dispatcher.add_handler(CommandHandler('echo', echo_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))