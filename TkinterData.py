# -*- coding: utf-8 -*-

__author__ = 'sun hai lang'

from Utils.VersionData import VersionData

import tkinter

class TkinterData(object):

    def __init__(self, _titil):
        self.version = VersionData()
        self.tk = tkinter.Tk()

        self.tk.title(_titil)
        self.tk.geometry('450x300')
        # 阻止Python GUI的大小调整
        self.tk.resizable(0, 0)

    def __del__(self):
        self.version = None

    def GUIShow(self):
        # 标签布局
        # tkinter.Label(self.tk, text='name: ').grid(row=0, column=1)
        # entry1 = tkinter.Entry(self.tk)
        # entry1.grid(row=0, column=2)

        self.tk.mainloop()





