# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-20"


from Utils.FileUtils import FileUtils
from Utils.VersionData import VersionData

fileUtils = FileUtils()

__versionList__ = []

def AddVersionList(verlist):
    print(type(verlist))
    for ver in verlist:
        version = VersionData()
        version.__dict__ = ver
        __versionList__.append(version)

def GetVersion(platfrom):
    pfList = [item for item in __versionList__ if item.m_key == platfrom]
    if len(pfList) > 0:
        return pfList[0]
    else:
        return VersionData()
