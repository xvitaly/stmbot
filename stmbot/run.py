#!/usr/bin/python3
# coding=utf-8

from stmbot import STMBot
from settings import tgkey, tfkey

if __name__ == '__main__':
    print('Starting bot...')
    STMBot(tgkey, tfkey).runbot()
