#!/usr/bin/python3
# coding=utf-8

from urllib.request import Request, urlopen
from xml.dom import minidom


class SteamChecker:
    def __fetchxml(self):
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self.__Token, self.__ID)
        req = Request(apiuri, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:52.0.0) Gecko/20100101 Firefox/52.0.0'})
        with urlopen(req) as xmlres:
            return xmlres.read().decode('utf-8')

    def get_sitestatus(self):
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
        return stv[self.SiteStatus]

    def get_vacstatus(self):
        stv = {
            '0': 'чист',
            '1': 'забанен'
        }
        return stv[self.VACStatus]

    def get_f2pstatus(self):
        stv = {
            '0': 'нет',
            '1': 'да'
        }
        return stv[self.F2PStatus]

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
        if xmlp.getElementsByTagName("qstatus")[0].firstChild.data != 'OK':
            raise Exception('Incorrect API return code')

        # Setting public properties...
        self.SteamID32 = xmlp.getElementsByTagName("steamID")[0].firstChild.data
        self.SteamID64 = xmlp.getElementsByTagName("steamID64")[0].firstChild.data
        self.SteamIDv3 = xmlp.getElementsByTagName("steamIDv3")[0].firstChild.data
        self.Nickname = xmlp.getElementsByTagName("nickname")[0].firstChild.data
        self.Avatar = xmlp.getElementsByTagName("avatar")[0].firstChild.data
        self.SiteStatus = xmlp.getElementsByTagName("sitestatus")[0].firstChild.data
        self.VACStatus = xmlp.getElementsByTagName("isbanned")[0].firstChild.data
        self.F2PStatus = xmlp.getElementsByTagName("isf2p")[0].firstChild.data
        self.TradeStatus = xmlp.getElementsByTagName("istrbanned")[0].firstChild.data
        self.Premium = xmlp.getElementsByTagName("ispremium")[0].firstChild.data
        self.Permalink = xmlp.getElementsByTagName("permalink")[0].firstChild.data
        self.GameBans = xmlp.getElementsByTagName("gamebans")[0].firstChild.data
        self.SRStatus = xmlp.getElementsByTagName("steamrep")[0].firstChild.data

        # Fetching custom description...
        try:
            self.Description = xmlp.getElementsByTagName("customdescr")[0].firstChild.data
        except:
            self.Description = ''

