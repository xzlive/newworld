#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wanghz 
@file: war2.py 
@time: 2018/05/07 
"""


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


# print(fibs(20))

#data = fibs(20)


def binary_search(dateset, find_num):
    print(dateset)

    if len(dateset) > 1:
        mid = int(len(dateset) / 2)
        if dateset[mid] == find_num:
            print("找到数字", dateset[mid])
        elif dateset[mid] > find_num:
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dateset[mid])
            return binary_search(dateset[0:mid], find_num)
        else:
            print("\033[31;1m找的数在mid[%s]右面\033[0m" % dateset[mid])
            return binary_search(dateset[mid + 1:], find_num)
    else:
        if dateset[0] == find_num:
            print("找到数字啦", dateset[0])
        else:
            print("没有分了，要找的数字[%s]不在列表里" % find_num)


binary_search(fibs(20), 89)
