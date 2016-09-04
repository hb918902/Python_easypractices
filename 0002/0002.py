#! /usr/bin/env python3
# coding = utf-8

import random
import pymysql


# 连接数据库函数
def connDB(data):
    conn = pymysql.connect(host='localhost',user='root',passwd='xxwl_hb123',db='test',)
    cur = conn.cursor()
    cur.execute('create database if not exists test;')
    cur.execute('create table if not exists test1(id INT NOT NULL, num VARCHAR(40) );')
    for i in range(len(data)):
        cur.execute('insert into test1 (id,num) values("{0}","{1}");'.format(i,data[i]))
    cur.close()
    conn.commit()
    conn.close()

# 产生激活码
def make_number(num,length):
    lstr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    a = []
    cnt = 0
    while cnt < num:
        a_str = ''
        for j in range(length):
            a_str += random.choice(lstr)
        if a_str not in a:
            a.append(a_str)
            cnt +=1
    return a


if __name__ == "__main__":
    nums = make_number(100,20)
    print(nums)
    connDB(nums)

