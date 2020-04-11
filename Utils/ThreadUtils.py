# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-24"

import threading
import time

class ThreadUtils(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def CreateThread(self, action, args={}):
        self.m_action = action
        self.m_args = args
        return self

    def run(self):
        self.m_action(self.m_args)


if __name__ == "__main__":
    pass