"""
Smart City Hackathon
"""
import os
import time
import sys
import logging as lg
import telegram as Tg
from telegram.ext import Updater, CommandHandler
from constants import BOT_API_TOKEN

def reboot_bot(update):
    """ Reboot the bot """
    #bot.send_message(update.message.chat_id, "Bot is restarting... Hold on !")
    update.message.reply_text("Bot is restarting... Hold tight !")
    time.sleep(0.5)
    os.execl(sys.executable, sys.executable, *sys.argv)

def add_commands(my_updater, name, func):
    """ Add commands the bot """
    my_updater.dispatcher.add_handler(CommandHandler(name, func))

def start_bot(myupdater):
    """ Start the bot """
    #bot.send_message(chat_id=update.message.chat_id, text="Your Hackathon bot, talk!")
    myupdater.start_webhook('', 80, 'urlpath')
    myupdater.start_polling()

def teamday(bot, update):
    """ Team score of a team for the given day """
    print("hello")

def teammonth(bot, update):
    """ Team score of a team for the current month """
    print("hello")

def globalmonth(bot, update):
    """ Overall scores for the current month """
    print("hello")

def globalday(bot, update):
    """ Overall scores for the current day """
    print("hello")


updater = Updater(BOT_API_TOKEN)
mybot = Tg.Bot(BOT_API_TOKEN)
lg.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=lg.INFO)
