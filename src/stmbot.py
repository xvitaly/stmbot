#!/usr/bin/python3
# coding=utf-8

from telebot import TeleBot
from stchk import SteamChecker


class STMBot:
    def runbot(self):
        # Handle /start and /help commands...
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_start(message):
            self.bot.send_message(message.chat.id, self.msgs['stm_welcome'])

        # Handle all other user input...
        @self.bot.message_handler(func=lambda m: True, content_types=['text'])
        def handle_msg(message):
            try:
                chk = SteamChecker(message.text, self.__tfkey)
                msg = self.msgs['stm_result'] % (chk.Nickname, chk.SteamID32, chk.SteamIDv3, chk.get_vacstatus(),
                                                 chk.get_gamebanstatus(), chk.get_tradestatus(), chk.get_f2pstatus(),
                                                 chk.SteamID64, chk.Permalink, chk.get_sitestatus(), chk.SRStatus)
                self.bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown')
            except:
                self.bot.reply_to(message, self.msgs['stm_error'])

        # Run bot forever...
        self.bot.polling(none_stop=True)

    def __init__(self, tgkey, tfkey):
        self.bot = TeleBot(tgkey)
        self.__tfkey = tfkey
        self.msgs = {
            'stm_welcome': 'Я - робот, созданный EasyCoding Team. отправьте мне ссылку на профиль Steam пользователя, которого желаете проверить, либо SteamID в любом формате записи.',
            'stm_result': 'Никнейм: *%s.*\nSteamID32: *%s*.\nSteamIDv3: *%s*.\nVAC-статус: *%s*.\nИгровые баны: *%s*.\nСтатус торговли: *%s.*\nБесплатный аккаунт: *%s*.\nСсылка на профиль: [%s](%s).\n\nПроверка на сайте тф.су: *%s*.\nПроверка на SteamRep: *%s*.',
            'stm_error': 'Не удалось обработать ваш запрос! Повторите попытку позднее.'
        }
