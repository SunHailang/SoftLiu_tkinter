# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-23"

import requests
import ssl
import urllib3

from Utils.TimeUtils import TimeUtils

# don't show warning information
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
requestUtils = requests.Session()

# show TimeUtils
timeUtils = TimeUtils()

# app config db path
appPath = 'Resources/app.json'
# button image path
btnImagePath = 'Resources\\Art\\ButtonImage\\{}'
# login check code position
m_loginAnswer = {
    '0': (31, 35),
    '1': (116, 46),
    '2': (191, 24),
    '3': (243, 50),
    '4': (22, 114),
    '5': (117, 94),
    '6': (167, 120),
    '7': (251, 105)
}

