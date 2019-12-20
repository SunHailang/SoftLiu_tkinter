# -*- coding: utf-8 -*-

__author__ = 'sun hai lang'


from TkinterData import TkinterData
import AppDB


top = TkinterData("Hello World")


versionList = []

appPath = 'Resources/app.json'

if __name__ == '__main__':
    appData = AppDB.fileUtils.ReadJsonData(appPath)
    print(type(appData))
    AppDB.AddVersionList(appData['version'])
    windows = AppDB.GetVersion('Windows')
    print(type(windows))
    # switch = AppDB.GetVersion('Switch')
    # print()
    top.ShowVersion(windows.m_code)
    top.GUIShow()




















