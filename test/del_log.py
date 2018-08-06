#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wanghz 
@file: del_log.py 
@time: 2018/08/06 
"""
import time
import os

N = 10  # 设置删除多少天前的文件


def deletefile(path):
    for eachfile in os.listdir(path):
        filename = os.path.join(path, eachfile)
        if os.path.isfile(filename):
            lastmodifytime = os.stat(filename).st_mtime
            endfiletime = time.time() - 3600 * 24 * N  # 设置删除多久之前的文件
            if endfiletime > lastmodifytime:
                if filename.split(filename)[1]==".log":
                    os.remove(filename)
        elif os.path.isdir(filename):  # 如果是目录则递归调用当前函数
            deletefile(filename)



if __name__ == '__main__':
    path = r"/Users/wanghz/Downloads"  # 指定删除的目录位置
    deletefile(path)
