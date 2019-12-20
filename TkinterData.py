# -*- coding: utf-8 -*-

__author__ = 'sun hai lang'

from Utils.VersionData import VersionData

import tkinter
from tkinter.font import Font
from GUI.Application import Application


class TkinterData(object):

    def __init__(self, _titil):
        self.app_width = 450
        self.app_height = 300
        self.tk = tkinter.Tk()
        self.tk.title(_titil)
        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()
        self.x_coord = (self.screen_width/2) - (self.app_width/2)
        self.y_coord = (self.screen_height/2) - (self.app_height/2)
        self.tk.geometry("%dx%d+%d+%d" % (self.app_width,
                                          self.app_height, self.x_coord, self.y_coord))
        # 阻止Python GUI的大小调整
        #self.tk.resizable(0, 0)

    def __del__(self):
        self.version = None

    def ShowVersion(self, version):
        text = 'version: ' + version
        fontSize = 10
        font = Font(family="Helvetica", size=fontSize)
        fram = Application(self.tk, 2, fontSize*2, side=tkinter.BOTTOM)
        # 返回一个 int 的值
        value = fram.ShowLabel(text=text, x=1, y=fontSize, font=font)
        print('value:{}'.format(value))

    def GUIShow(self):
        # 标签布局
        # tkinter.Label(self.tk, text='name: ').grid(row=0, column=1)
        # entry1 = tkinter.Entry(self.tk)
        # entry1.grid(row=0, column=2)
        self.tk.mainloop()
