# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-23"

import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)

import json
import datetime
import calendar
import CalendarUtils
import Login
from ResourcesUtils import *
from Utils.TkinterMessageBox import *
from PIL import Image
from Application import Application
from tkinter.font import Font
from tkinter import ttk
import tkinter.messagebox
import tkinter



class LeftqueryTkinter(object):
    def __init__(self, loginState):
        self.app_width = 800
        self.app_height = 550
        self.tk = tkinter.Tk()
        self.tk.title('查询')
        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()
        self.x_coord = (self.screen_width/2) - (self.app_width/2)
        self.y_coord = (self.screen_height/2) - (self.app_height/2)
        self.tk.geometry("%dx%d+%d+%d" % (self.app_width,
                                          self.app_height, self.x_coord, self.y_coord))
        # 阻止Python GUI的大小调整
        self.tk.resizable(0, 0)

        # 创建一个日历
        self.calendarX, self.calenderY = (self.tk.winfo_screenwidth() - self.app_width)/2, (self.tk.winfo_screenheight() - self.app_height)/2
        # 获取当前的时间戳
        timeStamp = timeUtils.GetTicks()
        # 获取时间戳转换的时间
        localtime = timeUtils.GetTime(timeStamp)
        self.date_str = tkinter.StringVar()
        self.date_entry = ttk.Entry(
            self.tk, state='readonly', textvariable=self.date_str)
        self.date_entry.place(x=90, y=12.5,  width=100, heigh=25)
        self.date_str.set("%s-%s-%s" % (localtime.tm_year, localtime.tm_mon, localtime.tm_mday))
        # CalendarTickter((x, y), 'ur').selection() 获取日期，x,y为点坐标

        def date_str_gain(): return [
            self.date_str.set(date)
            for date in [CalendarUtils.CalendarTickter((self.calendarX, self.calenderY), 'ur').selection()]
            if date]
        tkinter.Button(self.tk, text='日期:', command=date_str_gain).place(
            x=2, y=10, width=80, heigh=30)

        # show login state
        self.m_loginState = loginState
        if self.m_loginState:
            loginStr = '已登录'
        else:
            loginStr = '未登录'
        tkinter.Button(self.tk, text=loginStr, command=self.BtnLogin_OnClick).place(
            x=self.app_width-90, y=10, width=80, heigh=30)

    
    def BtnLogin_OnClick(self):
        if self.m_loginState:
            return
        if MessageBoxAskOkCancel('提示', '是否打开登录界面？'):
            # self.leftqueryTkinter.destroy()
            self.tk.destroy()
            Login.LoginTkinter()
        else:
            pass

    def GUIShow(self):
        self.tk.mainloop()


if __name__ == "__main__":
    top = LeftqueryTkinter(False)
    top.GUIShow()
