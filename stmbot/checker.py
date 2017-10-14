#!/usr/bin/python3
# coding=utf-8

# Simple Steam profile checker Telegram bot
# Copyright (c) 2017 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from urllib.request import Request, urlopen
from xml.dom import minidom
from re import sub


class SteamChecker:
    def __fetchxml(self):
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self.__Token, self.__ID)
        req = Request(apiuri, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:52.0.0) Gecko/20100101 Firefox/52.0.0'})
        with urlopen(req) as xmlres:
            return xmlres.read().decode('utf-8')

    @property
    def sitestatus(self):
        # Set dictionary with API return codes...
        stv = {
            '1': 'гарант',
            '2': 'в белом списке',
            '3': 'в чёрном списке',
            '4': 'нет в базе',
            '5': 'в чёрном списке аукциона',
            '6': 'сотрудник сайта',
            '7': 'донатер',
            '8': 'ненадёжный'
        }

        # Return result using dictionary...
        return stv[self.__sitestatus]

    @property
    def vacstatus(self):
        stv = {
            '0': 'чист',
            '1': 'забанен'
        }
        return stv[self.__vacstatus]

    @property
    def f2pstatus(self):
        stv = {
            '0': 'нет',
            '1': 'да'
        }
        return stv[self.__f2pstatus]

    def get_tradestatus(self):
        stv = {
            '0': 'нет ограничений',
            '1': 'заблокирована',
            '2': 'испытательный срок'
        }
        return stv[self.TradeStatus]

    def get_gamebanstatus(self):
        return 'нет' if self.GameBans == '0' else 'есть (%s)' % self.GameBans

    def __init__(self, tid, token):
        # Setting token and unique identifier to pseudo-private properties...
        self.__ID = tid
        self.__Token = token

        # Fetching XML from API...
        rxml = self.__fetchxml()

        # Parsing received XML...
        xmlp = minidom.parseString(rxml)

        # Checking API result...
        if xmlp.getElementsByTagName('qstatus')[0].firstChild.data != 'OK':
            raise Exception('Incorrect API return code')

        # Setting public properties...
        self.SteamID32 = xmlp.getElementsByTagName('steamID')[0].firstChild.data
        self.SteamID64 = xmlp.getElementsByTagName('steamID64')[0].firstChild.data
        self.SteamIDv3 = xmlp.getElementsByTagName('steamIDv3')[0].firstChild.data
        self.Nickname = xmlp.getElementsByTagName('nickname')[0].firstChild.data
        self.Avatar = xmlp.getElementsByTagName('avatar')[0].firstChild.data
        self.Permalink = xmlp.getElementsByTagName('permalink')[0].firstChild.data
        self.SRStatus = sub('<[^<]+?>', '', xmlp.getElementsByTagName('steamrep')[0].firstChild.data)
        self.__sitestatus = xmlp.getElementsByTagName('sitestatus')[0].firstChild.data
        self.__vacstatus = xmlp.getElementsByTagName('isbanned')[0].firstChild.data
        self.__f2pstatus = xmlp.getElementsByTagName('isf2p')[0].firstChild.data
        self.__tradestatus = xmlp.getElementsByTagName('istrbanned')[0].firstChild.data
        self.__premium = xmlp.getElementsByTagName('ispremium')[0].firstChild.data
        self.__gameBans = xmlp.getElementsByTagName('gamebans')[0].firstChild.data

        # Fetching custom description...
        try:
            self.Description = xmlp.getElementsByTagName('customdescr')[0].firstChild.data
        except:
            self.Description = ''

