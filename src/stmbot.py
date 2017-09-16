#!/usr/bin/python3
# coding=utf-8

from platform import system, release
from settings import tgkey, tfkey
from stchk import SteamChecker
from telebot import TeleBot, types


def runbot(key):
    # Initialize bot...
    bot = TeleBot(key)

    # Initialize command handlers...
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(message):
        # Sending message...
        bot.send_message(message.chat.id, 'Я - робот, созданный EasyCoding Team. Для продолжения работы со мной '
                                          'сначала выберите один из пунктов меню.', reply_markup=get_mainkbd())

    @bot.message_handler(commands=['version'])
    def handle_start(message):
        bot.send_message(message.chat.id, 'EasyCoding Robot версии %s.\nРаботает на %s %s.' %
                         ('0.1pre', system(), release()), reply_markup=get_mainkbd())

    @bot.message_handler(commands=['steam'])
    def handle_steam(message):
        msg = bot.reply_to(message, 'Хорошо. Теперь отправьте мне ссылку на профиль Steam пользователя, которого '
                                    'желаете проверить, либо SteamID в любом формате записи.')
        bot.register_next_step_handler(msg, check_steam)

    @bot.message_handler(commands=['id'])
    def handle_id(message):
        bot.send_message(message.chat.id, 'Ваш идентификатор пользователя в Telegram: *%s*.' % bot.get_me().id,
                         reply_to_message_id=message.message_id, parse_mode='Markdown', reply_markup=get_mainkbd())

    # Initialize additional bot routines...
    def get_mainkbd():
        # Creating bot keyboard...
        kbd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=False, row_width=2)
        kbd.add(types.KeyboardButton('/help'), types.KeyboardButton('/steam'), types.KeyboardButton('/id'),
                types.KeyboardButton('/version'))
        return kbd

    def check_steam(message):
        try:
            chk = SteamChecker(message.text, tfkey)
            msg = 'Никнейм: *{}.*\nSteamID32: *{}*.\nSteamIDv3: *{}*.\nVAC-статус: *{}*.\nИгровые баны: *{}*.\nСтатус ' \
                  'торговли: *{}.*\nБесплатный аккаунт: *{}*.\nСсылка на профиль: [{}]({}).\n\nПроверка на сайте ' \
                  'тф.су: *{}*.\nПроверка на SteamRep: *{}*.'.format(chk.Nickname, chk.SteamID32, chk.SteamIDv3,
                                                                     chk.get_vacstatus(), chk.get_gamebanstatus(),
                                                                     chk.get_tradestatus(), chk.get_f2pstatus(),
                                                                     chk.SteamID64, chk.Permalink,
                                                                     chk.get_sitestatus(), chk.SRStatus)
            bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown',
                             reply_markup=get_mainkbd())
        except:
            bot.reply_to(message, 'Произошла ошибка при работе со Steam Web API! Повторите попытку позднее.')

    # Run bot forever...
    bot.polling(none_stop=True)


def main():
    try:
        print('Бот запущен.')
        runbot(tgkey)
        print('Бот завершил работу.')

    except Exception as ex:
        # Exception detected...
        print('Произошло исключение во время работы бота.\n\nТекст исключения: %s' % ex)


if __name__ == '__main__':
    main()
