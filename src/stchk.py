#!/usr/bin/python3
# coding=utf-8


from urllib.request import urlopen


class SteamChecker:
    def _fetchxml(self):
        apiuri = 'https://check.team-fortress.su/api.php?action=check&token=%s&id=%s' % (self._Token, self._ID)
        with urlopen(apiuri) as xmlres:
            return xmlres.read()

    def __init__(self, tid, token):
        self._ID = tid
        self._Token = token

