#!/usr/bin/python3
# coding=utf-8

import telebot
from settings import tgkey


def main():
    try:
        # Show message...
        print(tgkey)

    except:
        # Exception detected...
        print('An error occurred while querying backend.')


if __name__ == '__main__':
    main()
