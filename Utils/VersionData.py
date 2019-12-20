# -*- coding: utf-8 -*-

__author__ = "sun hai lang"

class VersionData(object):

    def __init__(self):
        self.m_key = 'None'
        self.m_name = 'none'
        self.m_code = '0.0.0.0'

    def GetVersion(self):
        return self

    def __del__(self):
        self.__version__ = None














