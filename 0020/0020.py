#! /usr/bin/python3
# -*-coding:utf-8-*-

import xlrd
import datetime


infos = []
info_file = xlrd.open_workbook('语音通信.xls')
table = info_file.sheet_by_index(0)
rownum = table.nrows
for row in range(1,rownum):
    timestr = table.cell(row,3).value
    hsp = timestr.find('时')
    msp = timestr.find('分')
    ssp = timestr.find('秒')
    h = 0
    m = 0
    s = 0
    if hsp != -1:
        h = int(timestr[0:hsp])
    if msp != -1:
        m = int(timestr[hsp+1:msp])
    if ssp != -1:
        s = int(timestr[msp+1:ssp])
    infos.append(datetime.timedelta(
        hours=h,minutes=m,seconds=s
    ))

alltime = datetime.timedelta(seconds=0)
for info in infos:
    alltime += info

print("总通话时长{0}".format(alltime))





