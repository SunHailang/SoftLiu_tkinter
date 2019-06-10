# -*- coding: utf-8 -*-

__author__ = "sun hai lang"

class VersionData(object):

    __version__ = '1.0.0.0'

    def __init__(self):
        self.__version__ = '1.0.0.0'

    def GetVersion(self):
        return self.__version__

    def __del__(self):
        self.__version__ = None














