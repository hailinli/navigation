#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/9/15 下午4:56
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : get_navigation_req.py
# @Software: PyCharm

from lxml import etree
import requests
import util
import parse_result


FILE_PATH_IN = 'data'
FILE_NAME_NEED_CONTAIN = 'net-internals'
# URL_CONTAIN = 'blmcgi?sign='
URL_CONTAIN = 'cmd=0x011a'

def get_navigation_req(lines):
    """
    从html文本字符串解析出需要的链接
    :param lines:
    :return:
    """
    sel = etree.HTML(lines)
    tds = sel.xpath('//tbody[@id="events-view-source-list-tbody"]/tr/td[4]')
    ls = []
    for td in tds:
        if td.text == None:
            continue
        if URL_CONTAIN in td.text:
            ls.append(td.text)
            # print(td.text)
    # print(ls)
    return ls


def req_res(url):
    """
    请求url并返回
    :param url:
    :return:
    """
    # print(url)
    rs = requests.get(url)
    return rs.text


def start(file_path_in, file_name_need_contain):
    """
    得到该文件夹下的所有包含指定字符串的html文件,并解析出每个文件中的链接,而后进行get请求,请求完后再解析
    :param file_path_in:
    :param file_name_need_contain:
    :return:
    """
    fs = util.get_files(file_path_in, file_name_need_contain)
    for f in fs:
        rf = util.open_file_r(f)  # 打开文件流
        if rf == -1:
            continue
        html_s = rf.read()  # 读取该文件, html文件
        rf.close()
        urls = list(set(get_navigation_req(html_s)))  # 解析出链接
        for url in urls:
            print(url)
            res = req_res(url)
            parse_result.parser(res)


def main():
    """
    :return:
    """
    parse_result.print_header()
    start(FILE_PATH_IN, FILE_NAME_NEED_CONTAIN)


if __name__ == "__main__":
    main()

