# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-24"


class TrainData(object):
    # '车次','发车时间', '到达时间', '商务座', '一等座', '二等座', '高级软卧','软卧','动卧', '硬卧', '硬座', '无座'
    def __init__(self,trainNum,startTime,endTime,busessSeat,firstSeat,
                                secondSeat,hightSoftSeat,softSeat,moveSeat,hardSleepSeat,hardSeat,noneSeat):
        self.m_trainNum = trainNum
        self.fromStation=''
        self.toStation=''
        self.m_startTime=startTime
        self.m_endTime=endTime
        self.m_busessSeat=busessSeat
        self.m_firstSeat=firstSeat
        self.m_secondSeat=secondSeat
        self.m_hightSoftSeat=hightSoftSeat
        self.m_softSeat=softSeat
        self.m_moveSeat=moveSeat
        self.m_hardSleepSeat=hardSleepSeat
        self.m_hardSeat=hardSeat
        self.m_noneSeat=noneSeat
