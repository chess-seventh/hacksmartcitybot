"""
Smart City Hackathon
"""
import telegram as Tg
import logging
from telegram.ext import Updater
from constants import BOT_TOKEN
from constants import BOT_API_TOKEN


class BotBuilder(object):
    """docstring for BotBuilder"""
    def __init__(self):
        self.updater = Updater(BOT_TOKEN)
        self.bot = Tg.Bot(BOT_API_TOKEN)





logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s ', level = logging.INFO)
