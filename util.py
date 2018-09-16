#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/9/15 下午5:19
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : util.py
# @Software: PyCharm

import os


def mk_dirname(f):
    """
    根据文件名f,判断文件目录是否存在,如果不存在那么创建
    :param f:
    :return:
    """
    dir_name = os.path.dirname(f)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def get_files(dir_path, file_str):
    """
    得到DIR_PATH路径下所有文件名含file_str的文件
    :param dir_path: 文件夹的路径
    :param file_str: 文件名中所含词缀
    :return:
    """
    ret_l = []
    fs = os.listdir(dir_path)
    for f in fs:
        if file_str in f:
            f = '%s/%s' %(dir_path, f)
            ret_l.append(f)
    return ret_l

def open_file_r(f):
    """
    打开文件, 返回文件流
    :param f: str, 文件名
    :return:
    """
    rf = ''
    try:
        rf = open(f, 'rb')
    except:
        return -1
    return rf

def write_file(f, out_str, mode='w'):
    """
    写文件
    :param f: str, 文件名
    :param out_str: str
    :return:
    """

    mk_dirname(f)
    try:
        wf = open(f, mode, encoding='utf-8')
        wf.write(out_str)
        # wf.write('\n')
        wf.close()
    except:
        return -1
    return 0
