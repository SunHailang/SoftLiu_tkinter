# -*- coding: utf-8 -*-

__author__ = 'sun hai lang'

from Utils.VersionData import VersionData
from TkinterData import TkinterData

version = VersionData()
top = TkinterData("Hello World")

if __name__ == '__main__':
    print(version.GetVersion())
    top.GUIShow()




















