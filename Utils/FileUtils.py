# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-06-11"

import json

class FileUtils(object):

    def __init__(self):
        pass
    
    @staticmethod
    def ReadJsonData(path):
        with open(path,'r') as load_f:
           return json.load(load_f)


