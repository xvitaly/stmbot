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

from urllib.request import Request as request, urlopen
from xml.dom import minidom
from re import sub


class SteamChecker:
    @staticmethod
    def striptags(str):
        """
        Strip HTML tags from string.
        :param str: String to strip tags
        :return: String without HTML tags
        """
        return sub('<[^<]+?>', '', str)

    def __fetchxml(self):
        """
        Format query to API, fetch results and return them as string.
        :return: API check results
        """
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self.__token, self.__id)
        req = request(apiuri, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:52.0.0)'
                                                                'Gecko/20100101 Firefox/52.0.0'})
        with urlopen(req) as xmlres:
            return xmlres.read().decode('utf-8')

    @property
    def sitestatus(self):
        """
        TEAM-FORTRESS.SU user friendly status of checked user profile.
        :return: TEAM-FORTRESS.SU check results
        """
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
        """
        VAC status of checked user profile.
        :return: VAC status
        """
        stv = {
            '0': 'чист',
            '1': 'забанен'
        }
        return stv[self.__vacstatus]

    @property
    def f2pstatus(self):
        """
        Free-to-Play status (has no purchased games) of checked user profile.
        :return: Free-to-Play status
        """
        stv = {
            '0': 'нет',
            '1': 'да'
        }
        return stv[self.__f2pstatus]

    @property
    def tradestatus(self):
        """
        Current trade status of checked user profile.
        :return: Trade status
        """
        stv = {
            '0': 'нет ограничений',
            '1': 'заблокирована',
            '2': 'испытательный срок'
        }
        return stv[self.__tradestatus]

    @property
    def gamebanstatus(self):
        """
        Current game bans on checked user profile.
        :return: Game bans status and their count
        """
        return 'нет' if self.__gamebans == '0' else 'есть (%s)' % self.__gamebans

    def __init__(self, tid, token):
        """
        Main SteamChecker constructor.
        :param tid: Profile link, username or SteamID
        :param token: API token
        """
        # Setting token and unique identifier to pseudo-private properties...
        self.__id = tid
        self.__token = token

        # Fetching XML from API...
        rxml = self.__fetchxml()

        # Parsing received XML...
        xmlp = minidom.parseString(rxml)

        # Checking API result...
        if xmlp.getElementsByTagName('qstatus')[0].firstChild.data != 'OK':
            raise Exception('Incorrect API return code')

        # Setting public fields...
        self.steamid32 = xmlp.getElementsByTagName('steamID')[0].firstChild.data
        self.steamid64 = xmlp.getElementsByTagName('steamID64')[0].firstChild.data
        self.steamidv3 = xmlp.getElementsByTagName('steamIDv3')[0].firstChild.data
        self.nickname = xmlp.getElementsByTagName('nickname')[0].firstChild.data
        self.avatar = xmlp.getElementsByTagName('avatar')[0].firstChild.data
        self.permalink = xmlp.getElementsByTagName('permalink')[0].firstChild.data
        self.srstatus = self.striptags(xmlp.getElementsByTagName('steamrep')[0].firstChild.data)

        # Setting private fields...
        self.__sitestatus = xmlp.getElementsByTagName('sitestatus')[0].firstChild.data
        self.__vacstatus = xmlp.getElementsByTagName('isbanned')[0].firstChild.data
        self.__f2pstatus = xmlp.getElementsByTagName('isf2p')[0].firstChild.data
        self.__tradestatus = xmlp.getElementsByTagName('istrbanned')[0].firstChild.data
        self.__premium = xmlp.getElementsByTagName('ispremium')[0].firstChild.data
        self.__gamebans = xmlp.getElementsByTagName('gamebans')[0].firstChild.data

        # Fetching custom description...
        try:
            self.description = xmlp.getElementsByTagName('customdescr')[0].firstChild.data
        except:
            self.description = 'отсутствует'
