#!/usr/bin/python3
# coding=utf-8

from urllib.request import Request, urlopen
from xml.dom import minidom


class SteamChecker:
    def __fetchxml(self):
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self.__Token, self.__ID)
        req = Request(apiuri, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.7) Gecko/20100101 Firefox/10.0.7'})
        with urlopen(req) as xmlres:
            return xmlres.read().decode('utf-8')

    def __init__(self, tid, token):
        # Setting token and unique identifier to pseudo-private properties...
        self.__ID = tid
        self.__Token = token

        # Fetching XML from API...
        rxml = self.__fetchxml()

        # Parsing received XML...
        xmlp = minidom.parseString(rxml)

        # Setting public properties...
        self.APIStatus = xmlp.getElementsByTagName("qstatus")[0].firstChild.data
        self.SteamID32 = xmlp.getElementsByTagName("steamID")[0].firstChild.data
        self.SteamID64 = xmlp.getElementsByTagName("steamID64")[0].firstChild.data
        self.SteamIDv3 = xmlp.getElementsByTagName("steamIDv3")[0].firstChild.data
        self.Nickname = xmlp.getElementsByTagName("nickname")[0].firstChild.data
        self.Avatar = xmlp.getElementsByTagName("avatar")[0].firstChild.data
        self.Description = xmlp.getElementsByTagName("customdescr")[0].firstChild.data
        self.SiteStatus = xmlp.getElementsByTagName("sitestatus")[0].firstChild.data
        self.VACStatus = xmlp.getElementsByTagName("isbanned")[0].firstChild.data
        self.F2PStatus = xmlp.getElementsByTagName("isf2p")[0].firstChild.data
        self.TradeStatus = xmlp.getElementsByTagName("istrbanned")[0].firstChild.data
        self.Premium = xmlp.getElementsByTagName("ispremium")[0].firstChild.data
        self.Permalink = xmlp.getElementsByTagName("permalink")[0].firstChild.data

