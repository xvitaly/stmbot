#!/usr/bin/python3
# coding=utf-8

from telebot import TeleBot, types
from settings import tgkey, tfkey
from stchk import SteamChecker


def runbot(key):
    # Initialize bot...
    bot = TeleBot(key)

    # Initialize command handlers...
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(message):
        # Creating bot keyboard...
        kbd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=False, row_width=1)
        item1 = types.KeyboardButton('/help')
        item2 = types.KeyboardButton('/steam')
        item3 = types.KeyboardButton('/id')
        kbd.add(item1, item2, item3)

        # Sending message...
        bot.send_message(message.chat.id, 'Приветствую вас!', reply_markup=kbd)

    @bot.message_handler(commands=['steam'])
    def handle_steam(message):
        msg = bot.reply_to(message, 'Now please send me a link to Steam profile or SteamID.')
        bot.register_next_step_handler(msg, check_steam)

    @bot.message_handler(commands=['id'])
    def handle_id(message):
        user = bot.get_me()
        bot.reply_to(message, 'Your ID is %s.' % user.id)

    # Initialize additional bot routines...
    def check_steam(message):
        try:
            chk = SteamChecker(message.text, tfkey)
            msg = 'Никнейм: *{}.*\nSteamID32: *{}*.\nSteamIDv3: *{}*.\nVAC-статус: *{}*.\nИгровые баны: ' \
                  '*{}*.\nСтатус торговли: *{}.*\nБесплатный аккаунт: *{}*.\nСсылка на профиль: [{}]({}).\n\nПроверка ' \
                  'на сайте тф.су: {}.\nПроверка на SteamRep: {}.'.format(chk.Nickname, chk.SteamID32, chk.SteamIDv3, chk.get_vacstatus(),
                                               chk.get_gamebanstatus(), chk.get_tradestatus(), chk.get_f2pstatus(),
                                               chk.SteamID64, chk.Permalink, chk.get_sitestatus(), 'не выполнялась')
            bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown')
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
