#!/usr/bin/python3
# coding=utf-8

from telebot import TeleBot
from settings import tgkey, tfkey
from stchk import SteamChecker


def runbot(key):
    # Initialize bot...
    bot = TeleBot(key)

    # Initialize command handlers...
    @bot.message_handler(commands=['start', 'help'])
    def handlestart(message):
        bot.send_message(message.chat.id, 'Приветствую вас!')

    @bot.message_handler(commands=['steam'])
    def handlesteam(message):
        msg = bot.reply_to(message, 'Now please send me a link to Steam profile or SteamID.')
        bot.register_next_step_handler(msg, checksteam)

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def handleother(message):
        bot.send_message(message.chat.id, message.text)

    # Initialize additional bot routines...
    def checksteam(message):
        try:
            chk = SteamChecker(message.text, tfkey)
            bot.reply_to(message, 'Result nickname: %s.' % chk.Nickname)
        except:
            bot.reply_to(message, 'An error occured while fetching API!')

    # Run bot forever...
    bot.polling(none_stop=True)


def main():
    try:
        print('Launching bot with token %s...' % tgkey)
        runbot(tgkey)

    except:
        # Exception detected...
        print('An error occurred while running bot!')


if __name__ == '__main__':
    main()
