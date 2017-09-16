#!/usr/bin/python3
# coding=utf-8

from telebot import TeleBot
from stchk import SteamChecker


class STMBot:
    def runbot(self):
        # Handle /start and /help commands...
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_start(message):
            self.bot.send_message(message.chat.id, 'Я - робот, созданный EasyCoding Team. отправьте мне ссылку на профиль Steam пользователя, которого желаете проверить, либо SteamID в любом формате записи.')

        # Handle all other user input...
        @self.bot.message_handler(func=lambda m: True, content_types=['text'])
        def handle_msg(message):
            try:
                chk = SteamChecker(message.text, self.__tfkey)
                msg = 'Никнейм: *{}.*\nSteamID32: *{}*.\nSteamIDv3: *{}*.\nVAC-статус: *{}*.\nИгровые баны: *{}*.\nСтатус ' \
                      'торговли: *{}.*\nБесплатный аккаунт: *{}*.\nСсылка на профиль: [{}]({}).\n\nПроверка на сайте ' \
                      'тф.су: *{}*.\nПроверка на SteamRep: *{}*.'.format(chk.Nickname, chk.SteamID32, chk.SteamIDv3,
                                                                         chk.get_vacstatus(), chk.get_gamebanstatus(),
                                                                         chk.get_tradestatus(), chk.get_f2pstatus(),
                                                                         chk.SteamID64, chk.Permalink,
                                                                         chk.get_sitestatus(), chk.SRStatus)
                self.bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown')
            except:
                self.bot.reply_to(message, 'Не удалось обработать ваш запрос! Повторите попытку позднее.')

        # Run bot forever...
        self.bot.polling(none_stop=True)

    def __init__(self, tgkey, tfkey):
        self.bot = TeleBot(tgkey)
        self.__tfkey = tfkey
