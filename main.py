# -*- coding: utf-8 -*-

from Utils.VersionData import VersionData
from TkinterData import TkinterData

version = VersionData()
top = TkinterData("Hello World")

if __name__ == '__main__':
    print(version.GetVersion())
    top.GUIShow()




















