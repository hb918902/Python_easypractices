#! /usr/bin/python3
# -*-coding:utf-8-*-

import uuid
import hashlib


def encrypt_password(password,salt=None):
    if salt is None:
        salt = uuid.uuid4().hex
    result = password
    for i in range(10):
        result = hashlib.sha256(salt.encode() + result.encode()).hexdigest()
    return result + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return hashed_password == encrypt_password(user_password,salt)
    # return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    first = input('Please input your password:')
    second = input('Please input your password again:')
    if check_password(encrypt_password(first),second):
        print('right')
    else:
        print('wrong')
