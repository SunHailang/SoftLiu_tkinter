# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-20"

import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)

import tkinter
import tkinter.messagebox
from tkinter.font import Font
from Application import Application
from PIL import Image
import ResourcesUtils
from Utils import TkinterMessageBox
import Leftquery
import json


class LoginTkinter(object):
    def __init__(self):
        self.m_userName = ''
        self.m_passWord = ''
        self.m_loginState = False
        self.app_width = 500
        self.app_height = 350
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

        self.url_check = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        self.url_login = 'https://kyfw.12306.cn/passport/web/login'
        self.headers = {
                'Host':'kyfw.12306.cn',
                'Referer':'https://kyfw.12306.cn/otn/login/init',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                }

        leftX = 125
        leftY = 20
        user_var = tkinter.StringVar()
        tkinter.Label(self.tk, text='User Name:').place(x=leftX, y=leftY)
        self.m_entry_user = tkinter.Entry(
            self.tk, width=27, textvariable=user_var)
        self.m_entry_user.place(x=leftX+80, y=leftY)
        tkinter.Label(self.tk, text='Password:').place(x=leftX, y=leftY+30)
        pw_var = tkinter.StringVar()
        self.m_entry_pw = tkinter.Entry(
            self.tk, width=27, textvariable=pw_var, show='*')
        self.m_entry_pw.place(x=leftX+80, y=leftY+30)
        # 是否显示 密码 (默认不显示)
        self.checkPwVar = tkinter.IntVar()
        self.checkPw = tkinter.Checkbutton(self.tk, text='显示密码', variable=self.checkPwVar,
                                        onvalue=1, offvalue=0, command=self.ShowPwOrNot)
        self.checkPw.place(x=380, y=48)
        # 绘制选择的 CheckBox
        self.m_checkList = []
        checkLeftX = 50
        checkLeftY = 75
        for item in range(8):
            # print(item)
            checkVar = tkinter.IntVar()
            check = tkinter.Checkbutton(self.tk, text='{}'.format(item + 1), variable=checkVar,
                                        onvalue=1, offvalue=0)
            check.place(x=checkLeftX+len(self.m_checkList)*50, y=checkLeftY)
            self.m_checkList.append(checkVar)
        # 绘制显示验证码图片的Canvas的
        self.m_canvas = tkinter.Canvas(self.tk, width=293,
                                       height=190, background='white')
        self.m_canvas.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
        self.m_btn = tkinter.Button(
            self.tk, text="    Sure    ", command=self.Login_OnClick)
        self.m_btn.place(relx=0.5, y=self.app_height-20, anchor=tkinter.CENTER)
        # 存放canvas上显示的图片，所以必须用全局变量
        self.imageFile = None
        self.CanvasImage('2.gif')

    def ShowPwOrNot(self):
        if self.checkPwVar.get() == 1:
            # print('显示密码')
            self.m_entry_pw['show'] = ''
        else:
            # print('不显示密码')
            self.m_entry_pw['show'] = '*'

    def CheckCode_Answer(self):
        answer_list = []
        for i in range(len(self.m_checkList)):
            if self.m_checkList[i].get() == 1:                
                for j in ResourcesUtils.m_loginAnswer.keys():
                    if i == j:
                        answer_list.append(ResourcesUtils.m_loginAnswer[j][0])
                        answer_list.append(',')
                        answer_list.append(ResourcesUtils.m_loginAnswer[j][1])
                        answer_list.append(',')
        s = ''
        for i in answer_list:
            s += str(i)
        answer = s[:-1]
        form_check = {
            'answer': answer,
            'login_site': 'E',
            'rand': 'sjrand'
        }
        print(form_check)
        result = -1
        try:
            loginpost = ResourcesUtils.requestUtils.post(self.url_login, data=form_check, headers=self.headers)
            print(loginpost.text)
            html_login = json.loads(loginpost.text)
            print(html_login)
            if html_login['result_code'] == 0:
                print('login success.')
                result = 0
            else:
                print('login failed.')
        finally:
            return result

    def Login_OnClick(self):
        self.m_userName = self.m_entry_user.get()
        self.m_passWord = self.m_entry_pw.get()
        print('Login_OnClick user name:{} , password:{}'.format(
            self.m_userName, self.m_passWord))
        if self.m_userName=='' or self.m_passWord=='':
            # mesBox = tkinter.messagebox.askyesno(title='hi', message='Are you sure to cancel it?')  #返回True或者False
            mesBox = TkinterMessageBox.MessageBoxShowError('错误','用户名或密码为空.')
            print(mesBox)            
            # self.loginTkinter.destroy()    
            self.tk.destroy()      
            Leftquery.LeftqueryTkinter(self.m_loginState)
            return -1
        form_login = {
            'username': self.m_userName,
            'password': self.m_passWord,
            'appid': 'otn'
        }
        result = -1
        try:
            loginPost = self.reqestUtil.post(self.url_login, data=form_login, headers=self.headers)
            print('login status: ', loginPost.status_code)
            print(loginPost.text)
            html_login = json.loads(loginPost.text)
            if html_login['result_code'] == 0:
                result = 0
        except:
            return result

    # 显示 登录验证码
    def CanvasImage(self, imagePath):
        print(Image.open(imagePath))
        self.imageFile = tkinter.PhotoImage(file=imagePath)
        self.m_canvas.create_image(4, 2, anchor='nw', image=self.imageFile)

    def GUIShow(self):
        self.tk.mainloop()

if __name__ == "__main__":
    top = LoginTkinter()
    #top.CanvasImage('2.gif')
    top.GUIShow()
