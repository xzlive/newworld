#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wanghz 
@file: war1.py 
@time: 2018/05/05 
"""
# 九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j), end='')
    print()


# 斐波那契数列 方式一

def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fibs(4))

# 打印三角
for i in range(10):
    for j in (0, i):
        print("-", end='')
    for j in range(i, 10):
        print("$", end='')
    print("")
print("----------")
