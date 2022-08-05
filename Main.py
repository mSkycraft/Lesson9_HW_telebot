
from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters,MessageHandler
from bot_commands import *
from API import APIstore



updater = Updater(APIstore)
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserStep))
print('server start')
updater.start_polling()
updater.idle()