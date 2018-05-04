#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wanghz 
@file: war.py 
@time: 2018/05/04 
"""

print('Hello World !')

"""
#website = 'http://www.baidu.com'
"""


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


a = fibs(10)
print(a)
print(fibs(100))

name = "Hengzhi Wang"

name2 = name
print(name, name2)

name = "Jack"

print("What is the value of name2 now?", name, name2)

"""
name = input("What is your name?")
print("Hello " + name)

import getpass

pwd = getpass.getpass("请输入密码：")

print(pwd)
"""
import sys

print(sys.argv)

import os

print(os.system("df -h"))

import os, sys

os.system(''.join(sys.argv[1:]))
