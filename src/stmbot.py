#!/usr/bin/python3
# coding=utf-8

from telebot import TeleBot
from stchk import SteamChecker


class STMBot:
    def runbot(self):
        # Handle /start and /help commands...
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_start(message):
            self.bot.send_message(message.chat.id, self.__msgs['stm_welcome'])

        # Handle all other user input...
        @self.bot.message_handler(func=lambda m: True, content_types=['text'])
        def handle_msg(message):
            try:
                chk = SteamChecker(message.text, self.__tfkey)
                msg = self.__msgs['stm_result'] % (chk.Nickname, chk.SteamID32, chk.SteamIDv3, chk.get_vacstatus(),
                                                 chk.get_gamebanstatus(), chk.get_tradestatus(), chk.get_f2pstatus(),
                                                 chk.SteamID64, chk.Permalink, chk.get_sitestatus(), chk.SRStatus)
                self.bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown')
            except:
                self.bot.reply_to(message, self.__msgs['stm_error'])

        # Run bot forever...
        self.bot.polling(none_stop=True)

    def __init__(self, tgkey, tfkey):
        self.bot = TeleBot(tgkey)
        self.__tfkey = tfkey
        self.__msgs = {
            'stm_welcome': 'Приветствую вас! Я специальный робот для проверки Steam профилей, созданный EasyCoding Team. Отправьте мне ссылку на любой профиль Steam, который вы желаете проверить, либо SteamID в любом формате записи и через несколько секунд получите результат.',
            'stm_result': 'Никнейм: *%s.*\nSteamID32: *%s*.\nSteamIDv3: *%s*.\nVAC-статус: *%s*.\nИгровые баны: *%s*.\nСтатус торговли: *%s.*\nБесплатный аккаунт: *%s*.\nСсылка на профиль: [%s](%s).\n\nПроверка на сайте тф.су: *%s*.\nПроверка на SteamRep: *%s*.',
            'stm_error': 'Не удалось обработать ваш запрос! Повторите попытку позднее.'
        }
