#!/usr/bin/python3
# coding=utf-8

from .stmbot import STMBot
from .settings import tgkey, tfkey


def main():
    try:
        print('Бот запущен.')
        bot = STMBot(tgkey, tfkey)
        bot.runbot()
        print('Бот завершил работу.')

    except Exception as ex:
        # Exception detected...
        print('Произошло исключение во время работы бота.\n\nТекст исключения: %s' % ex)


if __name__ == '__main__':
    main()
