#!/usr/bin/python3
# coding=utf-8

from urllib.request import urlopen
from xml.dom import minidom


class SteamChecker:
    def _fetchxml(self):
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self._Token, self._ID)
        with urlopen(apiuri) as xmlres:
            return xmlres.read()

    def __init__(self, tid, token):
        # Setting token and unique identifier to pseudo-private properties...
        self._ID = tid
        self._Token = token

        # Fetching XML from API...
        rxml = self._fetchxml()

        # Parsing received XML...
        xmlp = minidom.parse(rxml)
        for up in xmlp.getElementsByTagName('userprofile'):
            self.APIStatus = up.getElementsByTagName("qstatus")[0].firstChild.data
            self.SteamID32 = up.getElementsByTagName("steamID")[0].firstChild.data
            self.SteamID64 = up.getElementsByTagName("steamID64")[0].firstChild.data
            self.SteamIDv3 = up.getElementsByTagName("steamIDv3")[0].firstChild.data
            self.Nickname = up.getElementsByTagName("nickname")[0].firstChild.data
            self.Avatar = up.getElementsByTagName("avatar")[0].firstChild.data
            self.Description = up.getElementsByTagName("customdescr")[0].firstChild.data
            self.SiteStatus = up.getElementsByTagName("sitestatus")[0].firstChild.data
            self.VACStatus = up.getElementsByTagName("isbanned")[0].firstChild.data
            self.F2PStatus = up.getElementsByTagName("isf2p")[0].firstChild.data
            self.TradeStatus = up.getElementsByTagName("istrbanned")[0].firstChild.data
            self.SRStatus = up.getElementsByTagName("steamrep")[0].firstChild.data
            self.Premium = up.getElementsByTagName("ispremium")[0].firstChild.data
            self.Permalink = up.getElementsByTagName("permalink")[0].firstChild.data
