#!/usr/bin/python3
# coding=utf-8

import telebot
from settings import tgkey


def runbot(key):
    # Initialize bot...
    bot = telebot.TeleBot(key)

    # Initialize command handlers...
    @bot.message_handler(commands=['start', 'help'])
    def handlestart(message):
        bot.send_message(message.chat.id, 'Приветствую вас!')

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def handleother(message):
        bot.send_message(message.chat.id, message.text)

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
