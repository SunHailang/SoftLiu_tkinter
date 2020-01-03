# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-20"


import tkinter
from tkinter.font import Font
from Application import Application
from PIL import Image


class LoginTkinter(object):
    def __init__(self):
        self.m_userName = ''
        self.m_passWord = ''
        self.app_width = 450
        self.app_height = 300
        self.tk = tkinter.Tk()
        self.tk.title('登录')
        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()
        self.x_coord = (self.screen_width/2) - (self.app_width/2)
        self.y_coord = (self.screen_height/2) - (self.app_height/2)
        self.tk.geometry("%dx%d+%d+%d" % (self.app_width,
                                          self.app_height, self.x_coord, self.y_coord))
        # 阻止Python GUI的大小调整
        self.tk.resizable(0, 0)
        user_var = tkinter.StringVar()
        tkinter.Label(self.tk, text='User Name:').place(x=50, y=20)
        self.m_entry_user = tkinter.Entry(
            self.tk, width=20, textvariable=user_var)
        self.m_entry_user.place(x=150, y=20)
        tkinter.Label(self.tk, text='Password:').place(x=50, y=50)
        pw_var = tkinter.StringVar()
        self.m_entry_pw = tkinter.Entry(
            self.tk, width=20, textvariable=pw_var, show='*')
        self.m_entry_pw.place(x=150, y=50)
        self.m_btn = tkinter.Button(self.tk, text="  Sure  ")
        self.m_btn.place(x=100, y=200)
        canvas = tkinter.Canvas(self.tk, height=190, width=295)
        canvas.pack()
        im = tkinter.PhotoImage(file='GUI/pic.jpg')
        canvas.create_image(height=190, width=295, anchor='nw', image=im)

    def Login_OnClick(self):
        print('Login_OnClick user name:{} , password:{}'.format(
            self.m_userName, self.m_passWord))

    def GUIShow(self):
        '''
        canv = Application(self.tk, self.app_width,
                           self.app_height, side=tkinter.TOP)
        fontSize = 10
        font = Font(family="Helvetica", size=fontSize)
        canv.ShowLabel('User Name:', 50, 10, font)
        canv.ShowLabel('User Name:', 150, 10, font)
        #canv.ShowInputEntry(100, 10)
        '''

        self.tk.mainloop()


if __name__ == "__main__":
    top = LoginTkinter()
    top.GUIShow()
