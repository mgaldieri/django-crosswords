# -*- coding=utf-8 -*-
__author__ = 'mgaldieri'


class _pt_BR():
    def __init__(self):
        self.lowerchars = list(u'abcdefghijklmnopqrstuvwxyz')
        self.upperchars = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.loweraccented = list(u'áàâãéêíóôõúüç')
        self.upperaccented = list(u'ÁÀÂÃÉÊÍÓÔÕÚÜÇ')
        self.lowercase = self.lowerchars + self.loweraccented
        self.uppercase = self.upperchars + self.upperaccented
        self.allchars = self.lowercase + self.uppercase


class _en_US():
    def __init__(self):
        self.lowerchars = list(u'abcdefghijklmnopqrstuvwxyz')
        self.upperchars = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.loweraccented = list(u'')
        self.upperaccented = list(u'')
        self.lowercase = self.lowerchars + self.loweraccented
        self.uppercase = self.upperchars + self.upperaccented
        self.allchars = self.lowercase + self.uppercase


class _es_ES():
    def __init__(self):
        self.lowerchars = list(u'abcdefghijklmnopqrstuvwxyz')
        self.upperchars = list(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.loweraccented = list(u'áàâéíóúüñ')
        self.upperaccented = list(u'ÁÀÂÉÍÓÚÜÑ')
        self.lowercase = self.lowerchars + self.loweraccented
        self.uppercase = self.upperchars + self.upperaccented
        self.allchars = self.lowercase + self.uppercase

pt_BR = _pt_BR()
en_US = _en_US()
es_ES = _es_ES()