# -*- coding: utf-8 -*-

__author__ = 'sun hai lang'


import sys, os
#o_path = os.getcwd()
# sys.path.append(o_path)

from TkinterData import TkinterData
import AppDB
import ResourcesUtils
from PIL import Image


top = TkinterData("Hello World")


versionList = []



if __name__ == '__main__':
    path = ResourcesUtils.btnImagePath.format('FE_butt_idle.png')
    Image.open(path)
    appData = AppDB.fileUtils.ReadJsonData(ResourcesUtils.appPath)
    print(type(appData))
    AppDB.AddVersionList(appData['version'])
    windows = AppDB.GetVersion('Windows')
    print(type(windows))
    # switch = AppDB.GetVersion('Switch')
    # print()
    top.ShowVersion(windows.m_code)
    top.GUIShow()




















