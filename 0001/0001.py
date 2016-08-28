#! /usr/bin/env python3
# coding = utf-8

import random


def make_number(num,length):
    lstr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    a = []
    cnt = 0
    while cnt <num:
        a_str = ''
        for j in range(length):
            a_str += random.choice(lstr)
        if a_str not in a:
            a.append(a_str)
            cnt +=1
    print(a)
    return a


make_number(10,20)
