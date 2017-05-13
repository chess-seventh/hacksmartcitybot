"""
Smart City Hackathon
"""
import os
import time
import sys
import logging as lg
#import telegram as Tg
from telegram.ext import Updater, CommandHandler
from constants import BOT_API_TOKEN

def reboot_bot(update):
    """ Reboot the bot """
    #bot.send_message(update.message.chat_id, "Bot is restarting... Hold on !")
    update.message.reply_text("Bot is restarting... Hold tight !")
    time.sleep(0.5)
    os.execl(sys.executable, sys.executable, *sys.argv)

def teamday(bot, update):
    """ Team score of a team for the given day """
    update.message.reply_text('hello show data of teamday here')

def teammonth(bot, update):
    """ Team score of a team for the current month """
    update.message.reply_text('hello show data of teammonth here')

def globalmonth(bot, update):
    """ Overall scores for the current month """
    update.message.reply_text('hello show data of global month  here')

def globalday(bot, update):
    """ Overall scores for the current day """
    update.message.reply_text('hello show data of global day  here')


updater = Updater(BOT_API_TOKEN)
# mybot = Tg.Bot(BOT_API_TOKEN)
#add_commands(updater, 'teamday', 'teamday')
#add_commands(updater, 'teammonth', 'teammonth')
#add_commands(updater, 'globalmonth', 'globalmonth')
#add_commands(updater, 'globalday', 'globalday')

updater.dispatcher.add_handler(CommandHandler('teamday', teamday))
updater.dispatcher.add_handler(CommandHandler('teammonth', teammonth))
updater.dispatcher.add_handler(CommandHandler('globalmonth', globalmonth))
updater.dispatcher.add_handler(CommandHandler('globalday', globalday))

lg.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=lg.INFO)
updater.start_polling()
updater.idle()
