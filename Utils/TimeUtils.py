# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-06-11"

import time
import math
import calendar
import datetime

class TimeUtils(object):

    def __init__(self):
        pass

    # 获取时间戳转换的时间
    @staticmethod
    def GetTime(_ticks):
        localtime = time.localtime(_ticks)
        return localtime

    # 获取当前时间的时间戳 (向下取整得到一个(int)的整数)
    @staticmethod
    def GetTicks():
        return math.floor(time.time())

    # 获取某年某月的日历
    @staticmethod
    def GetCalendarMonth( _year, _month):
        return calendar.month(_year, _month)
    
    @staticmethod
    def ShowNowTime(_data):
        return '{}-{}-{}'.format(_data.year(), _data.mondth(), _data.day())
    


if __name__ == "__main__":

    timeUtils = TimeUtils()
    # 获取当前的时间戳
    timeStamp = timeUtils.GetTicks()
    print(timeStamp)
    # 获取时间戳转换的时间
    localtime = timeUtils.GetTime(timeStamp)
    # localtime = timeUtils.GetTime(1000)
    print("year:%s , mon:%s , day:%s , hour:%s , min:%s , sec:%s" % (localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec))
    # 一年中第几天 (1 ~ 366)
    print("year days(1~366): %s" % localtime.tm_yday)
    # 一周的天数 (0 ~ 6) 0是周一
    print("week days(0(monday)~6(sunday)): %s" % localtime.tm_wday)
    # 格式化时间
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", localtime))
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    calendarMonth = timeUtils.GetCalendarMonth(localtime.tm_year, localtime.tm_mon)
    print(calendarMonth)

    # datetime 获取当前的时间
    print(datetime.datetime.now().da)



