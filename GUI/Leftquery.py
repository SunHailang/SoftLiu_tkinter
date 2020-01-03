# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-23"

import os
import sys
# o_path = os.getcwd()
# sys.path.append(o_path)

import json
import datetime
import calendar
import CalendarUtils
import Login
import ResourcesUtils
from Utils import TkinterMessageBox
from Data.TrainData import TrainData
from PIL import Image
from Application import Application
from tkinter.font import Font
from tkinter import ttk
import tkinter.messagebox
import tkinter


class LeftqueryTkinter(object):
    def __init__(self, loginState):
        self.app_width = 1000
        self.app_height = 750
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
        # c初始化查询 url
        self.url_station = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        self.url_query = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
        self.headers = {
            'Host': 'kyfw.12306.cn',
            'If-Modified-Since': '0',
            'Cache-Control': 'no-cache',
            'Referer': 'ttps://kyfw.12306.cn/otn/leftTicket/init',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # 创建一个日历
        self.calendarLis = []
        self.dateStrList = []
        self.dateSelectCheckBoxList = []
        self.calendarLeftX = 2
        self.calendarLeftY = 40
        self.calendarX, self.calenderY = (self.tk.winfo_screenwidth(
        ) - self.app_width)/2, (self.tk.winfo_screenheight() - self.app_height)/2
        # 获取当前的时间戳
        timeStamp = ResourcesUtils.timeUtils.GetTicks()
        # 获取时间戳转换的时间
        localtime = ResourcesUtils.timeUtils.GetTime(timeStamp)
        cb_list = ['日期0','日期1','日期2','日期3','日期4']
        for inx, item in enumerate(cb_list):
            date_str = tkinter.StringVar()
            date_entry = ttk.Entry(
                self.tk, state='readonly', textvariable=date_str)
            date_entry.place(x=90,
                            y=self.calendarLeftY*inx+12.5, width=100, heigh=25)
            date_str.set("%s-%s-%s" % (localtime.tm_year,
                                    localtime.tm_mon, localtime.tm_mday))
            checkPwVar = tkinter.IntVar()
            checkPw = tkinter.Checkbutton(self.tk, text='', variable=checkPwVar,
                                        onvalue=1, offvalue=0)
            checkPw.place(x=190, y=self.calendarLeftY*inx+12.5)
            # CalendarTickter((x, y), 'ur').selection() 获取日期，x,y为点坐标
            def date_str_gain(index): return [
                self.dateStrList[index].set(date)
                for date in [CalendarUtils.CalendarTickter((self.calendarX, self.calenderY), 'ur').selection()]
                if date]
            btnDate = tkinter.Button(self.tk, text='{}'.format(item), command=lambda arg=inx:date_str_gain(arg))
            btnDate.place(x=2, y=self.calendarLeftY*inx+10, width=80, heigh=30)
            self.calendarLis.append(date_entry)
            self.dateStrList.append(date_str)
            self.dateSelectCheckBoxList.append(checkPw)

        # 创建一个下拉列表 
        # number = tkinter.StringVar() 
        # numberChosen = ttk.Combobox(self.tk, width=12, textvariable=number) 
        # numberChosen['values'] = (1, 2, 4, 42, 100) # 设置下拉列表的值 
        # numberChosen.place(x=230, y=12.5)
        # numberChosen.current(0) # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        # 设置出发站和到达站
        trainStationX = 230
        self.fromStation_Label = tkinter.Label(self.tk, text='出发站:', anchor='center')
        self.fromStation_Label.place(x=trainStationX, y=12.5, width=60, heigh=25)
        self.fromStation_EntryVar = tkinter.StringVar()
        self.fromStation_Entry = tkinter.Entry(self.tk, textvariable=self.fromStation_EntryVar)
        self.fromStation_Entry.place(x=trainStationX+60, y=12.5, width=100, heigh=25)
        self.fromStation_EntryVar.set('宿州东')        
        self.toStation_Label = tkinter.Label(self.tk, text='到达站:', anchor='center')
        self.toStation_Label.place(x=trainStationX+240, y=12.5, width=60, heigh=25)
        self.toStation_EntryVar = tkinter.StringVar()
        self.toStation_Entry = tkinter.Entry(self.tk, textvariable=self.toStation_EntryVar)
        self.toStation_Entry.place(x=trainStationX+300, y=12.5, width=100, heigh=25)
        self.toStation_EntryVar.set('上海虹桥')      
        btnExcharge = tkinter.Button(self.tk, text='交换', anchor='center', command=self.btnExchargeClick)
        btnExcharge.place(x=trainStationX+180, y=12.5, width=50, heigh=25)
        # 设置使用车次刷，或是时间段刷
        self.selectTrainNum = [] # 记录筛选的车次
        trainNumX = 67
        trainNumY = 50
        trainnum_Label= tkinter.Label(self.tk, text='车次筛选:')
        trainnum_Label.place(x=230, y=trainNumY, width=60, heigh=25)
        for item in range(5):
            trainNum_EntryVar = tkinter.StringVar()
            trainNum_Entry = tkinter.Entry(self.tk, textvariable=trainNum_EntryVar)
            trainNum_Entry.place(x=trainNumX*item+300, y=trainNumY, width=60, heigh=25)
            self.selectTrainNum.append(trainNum_Entry)
        # 设置 选择车次或是时间
        self.checkTrainVar = tkinter.IntVar()
        self.checkTrain = tkinter.Checkbutton(self.tk, text='是否使用时间筛选', variable=self.checkTrainVar,
                                        onvalue=1, offvalue=0)
        self.checkTrain.place(x=650, y=70)
        # 设置时间筛选
        trainTimeY = trainNumY+37.5
        trainTimeX = 300
        trainTime_Label= tkinter.Label(self.tk, text='时间筛选:')
        trainTime_Label.place(x=230, y=trainTimeY, width=60, heigh=25)

        trainTime_Label= tkinter.Label(self.tk, text='起始时间:')
        trainTime_Label.place(x=trainTimeX, y=trainTimeY, width=60, heigh=25)
        self.trainStartTime_EntryVar = tkinter.StringVar()
        self.trainStartTime_Entry = tkinter.Entry(self.tk, textvariable=self.trainStartTime_EntryVar)
        self.trainStartTime_Entry.place(x=trainTimeX+60, y=trainTimeY, width=90, heigh=25)
        self.trainStartTime_EntryVar.set('9:00')
        trainTime_Label= tkinter.Label(self.tk, text='终止时间:')
        trainTime_Label.place(x=trainTimeX+178, y=trainTimeY, width=60, heigh=25)
        self.trainEndTime_EntryVar = tkinter.StringVar()
        self.trainEndTime_Entry = tkinter.Entry(self.tk, textvariable=self.trainEndTime_EntryVar)
        self.trainEndTime_Entry.place(x=trainTimeX+238, y=trainTimeY, width=90, heigh=25)
        self.trainEndTime_EntryVar.set('16:00')
        # 创建表格 显示数据
        self.m_treeView = ttk.Treeview(self.tk)
        self.m_scrollbarTrewView = tkinter.Scrollbar(self.tk)        
        self.m_treeView = ttk.Treeview(self.tk, show="headings", yscrollcommand= self.m_scrollbarTrewView.set)  # 表格
        
        self.m_treeView["columns"] = ('车次','发车时间', '到达时间', '商务座', '一等座', '二等座', '高级软卧','软卧','动卧', '硬卧', '硬座', '无座')
        self.m_treeView.column('车次', width=50, anchor='center')  # 表示列
        self.m_treeView.column('发车时间', width=50, anchor='center')  
        self.m_treeView.column('到达时间', width=50, anchor='center')
        self.m_treeView.column('商务座', width=50, anchor='center')
        self.m_treeView.column('一等座', width=50, anchor='center')
        self.m_treeView.column('二等座', width=50, anchor='center')
        self.m_treeView.column('高级软卧', width=50, anchor='center')
        self.m_treeView.column('软卧', width=50, anchor='center')
        self.m_treeView.column('动卧', width=50, anchor='center')
        self.m_treeView.column('硬卧', width=50, anchor='center')
        self.m_treeView.column('硬座', width=50, anchor='center')
        self.m_treeView.column('无座', width=50, anchor='center')

        self.m_treeView.heading('车次', text='车次')
        self.m_treeView.heading('发车时间', text='发车时间') # 显示表头
        self.m_treeView.heading('到达时间', text='到达时间')
        self.m_treeView.heading('商务座', text='商务座')
        self.m_treeView.heading('一等座', text='一等座')
        self.m_treeView.heading('二等座', text='二等座')
        self.m_treeView.heading('高级软卧', text='高级软卧')
        self.m_treeView.heading('软卧', text='软卧')
        self.m_treeView.heading('动卧', text='动卧')
        self.m_treeView.heading('硬卧', text='硬卧')
        self.m_treeView.heading('硬座', text='硬座')
        self.m_treeView.heading('无座', text='无座')

        self.m_treeView.insert("", 0, text='G123', values=('G123','12:00','13:00','有','有','有','有','有','有','有','有','有'))  # 插入数据
        self.m_treeView.place(x=10, y=210, width=970, height=530)
        self.m_scrollbarTrewView.place(x=980, y=210, width=15, height=530)
        self.m_scrollbarTrewView.config(command=self.m_treeView.yview)
        # print(self.m_treeView)
        # show login state
        self.m_loginState = loginState
        if self.m_loginState:
            loginStr = '已登录'
        else:
            loginStr = '未登录'
        tkinter.Button(self.tk, text=loginStr, command=self.BtnLogin_OnClick).place(
            x=self.app_width-90, y=10, width=80, heigh=30)
        self.trainDataList = []
        self.treeView_Insert(self.trainDataList)
        #self.m_scrollbar = tkinter.Scrollbar(self.tk)
        #self.m_scrollbar.place(x=10, y=210, width=15, height=200)
        # 多日期查询 输入
        # self.m_muiltDateFindEntryVar = tkinter.StringVar()
        # self.m_MuiltDateFind_Entry = tkinter.Entry(self.tk, textvariable=self.m_muiltDateFindEntryVar)
        # self.m_MuiltDateFind_Entry.place(x=2, y=50, width=200, heigh=20)
    def btnExchargeClick(self):
            station = self.fromStation_Entry.get()
            self.fromStation_EntryVar.set(self.toStation_Entry.get())
            self.toStation_EntryVar.set(station)
        
    def treeView_Insert(self, dataList):
        items = self.m_treeView.get_children() 
        [self.m_treeView.delete(item) for item in items]

        for item in range(100):
            data = TrainData('G123{}'.format(item),'12:00','13:00','有','有','有','有','有','有','有','有','有')
            dataList.append(data)
        for index, item in  enumerate(dataList):
            print(index, item)
            self.m_treeView.insert("", index, text='{}'.format(index), values=(item.m_trainNum,item.m_startTime,item.m_endTime,item.m_busessSeat,item.m_firstSeat,
                                item.m_secondSeat,item.m_hightSoftSeat,item.m_softSeat,item.m_moveSeat,item.m_hardSleepSeat,item.m_hardSeat,item.m_noneSeat))

    def station_name(self):
        # get station name
        html_req = ResourcesUtils.requestUtils.get(self.url_station, verify=False)
        print(html_req.status_code)
        html = html_req.text
        result = html.split('@')[1:]
        # print('station_name:', result)
        dict = {}
        for i in result:
            key = str(i.split('|')[1])
            value = str(i.split('|')[2])
            dict[key] = value
        # fo = open('station_name.json', 'w+')
        # fo.write(html)
        # fo.close()
        return dict

    def query(self, form_station, to_station, date):
        station_name = self.station_name()
        
        fromstation = station_name[form_station]
        print('from station name: {} -> {}'.format(form_station, fromstation))
        tostation = station_name[to_station]
        print('to station name: {} -> {}'.format(to_station, tostation))
        url = self.url_query.format(date, fromstation, tostation)
        print('url: ', url)
        try:
            html_req = self.requestUtil.get(url, headers=self.headers, verify=False)
            print(html_req.status_code)
            print(html_req.text)
            html = json.loads(html_req.content)
            result = html['data']['result']
            if result == []:
                print('Result None.')
                return ''
            else:
                print("Result Success.")
                num = 1
                for i in result:
                    info = i.split('|')
                    if info[0] != '' and info[0] != 'null':
                        print(info)
                        trainNum = info[3]
                        startTime = info[8]
                        endTime = info[9]
                        if trainNum.find('G') != -1:
                            if startTime>='12:00' and ((info[30]!='无' and info[30]!='') or(info[26]!='' and info[26]!='无')):
                                print(str(num) + '.' + info[3] + '车次有余票')
                                seatTrain = {21: '高级软卧', 23: '软卧', 26: '无座', 28: '硬卧', 29: '硬座', 30: '二等座', 31: '一等座', 32: '商务座', 33: '动卧'}
                return result
        except:
           return 'query error.'

    def BtnLogin_OnClick(self):
        if self.m_loginState:
            return
        if TkinterMessageBox.MessageBoxAskOkCancel('提示', '是否打开登录界面？'):
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
