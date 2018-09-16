#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/9/15 下午7:33
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : parse_result.py
# @Software: PyCharm

import time
import util
import json
JSON_LINES_SPLIT = '},{'
ITEM_BETWEEN_SPLIT = ','
ITEM_INTERNAL_SPLIT = ':'
FILE_OUT = 'data/output.csv'

KEYS = ['time', 'mmsi', 'stat', 'rot', 'sog', 'pos_acc', 'x', 'y', 'cog', 'truehead', 'nm', 'tp', 'imo', 'cs', 'length', 'width', 'draught', 'eta', 'dest', 'iso3', 'dwt']

def line2jsons(line):
    """
    将一行数据转化成json数据
    :param line:
    :return:
    """
    r_json = dict()
    items = line.split(ITEM_BETWEEN_SPLIT)
    for item_s in items:
        item = item_s.split(ITEM_INTERNAL_SPLIT)
        value = item[1][1:-1]  # 截掉首尾
        if item[0] == 'time':
            time_local = time.localtime(int(value))
            value = time.strftime("%Y/%m/%d %H:%M:%S", time_local)
        r_json[item[0]] = value
    return r_json


def print_item_csv(r_json):
    """

    :return:
    """
    #
    # print(json.dumps(r_json))
    values = []  # 因为要保证顺序,所以必须按key添加value
    for k in KEYS:
        values.append(r_json[k])
    # print(','.join(values))
    util.write_file(FILE_OUT, ','.join(values) + '\n', 'a')


def parser(line):
    """
    切分处理
    :param line:
    :return:
    """
    line = line[2:-2]
    json_strs = line.split(JSON_LINES_SPLIT)
    for json_str in json_strs:
        js_one = line2jsons(json_str)
        print_item_csv(js_one)


def print_header():
    """
    判断文件路径是否存在,不存在就创建,存在就写入
    :return:
    """
    util.mk_dirname(FILE_OUT)
    # print(','.join(KEYS))
    util.write_file(FILE_OUT, ','.join((KEYS)) + '\n', 'a')


### 测试 ###
def main():
    print_header()
    parser('[{time:"1536862699",mmsi:"248563000",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.095993",y:"38.901234",cog:"627",truehead:"120",nm:"OCEAN ZENON",tp:"70",imo:"9427029",cs:"9HA4706",length:"225",width:"32",draught:"0",eta:"0",dest:"0@",iso3:"MLT",dwt:"5"},{time:"1536862799",mmsi:"412199000",stat:"0",rot:"0",sog:"92",pos_acc:"0",x:"118.022316",y:"38.935322",cog:"1011",truehead:"102",nm:"SHEN HUA 806",tp:"70",imo:"9662942",cs:"BRLE",length:"225",width:"32",draught:"0",eta:"0",dest:"603584@TJ CN",iso3:"CHN",dwt:"14145"},{time:"1536862788",mmsi:"412283567",stat:"0",rot:"0",sog:"1",pos_acc:"0",x:"118.033737",y:"38.888165",cog:"0",truehead:"511",nm:"",tp:"0",imo:"0",cs:"",length:"0",width:"0",draught:"0",eta:"0",dest:"0@",iso3:"",dwt:"0"},{time:"1536862629",mmsi:"412737000",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.070290",y:"38.902260",cog:"299",truehead:"129",nm:"SHEN HUA 505",tp:"70",imo:"0",cs:"BRMC",length:"190",width:"32",draught:"0",eta:"0",dest:"552832@YANGZHOU",iso3:"CHN",dwt:"24774"},{time:"1536862794",mmsi:"413350640",stat:"0",rot:"128",sog:"0",pos_acc:"0",x:"118.062485",y:"38.885578",cog:"167",truehead:"511",nm:"",tp:"0",imo:"0",cs:"",length:"0",width:"0",draught:"0",eta:"0",dest:"616960@TIANJIN",iso3:"CHN",dwt:"14093"},{time:"1536862778",mmsi:"413361860",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.052048",y:"38.889236",cog:"2333",truehead:"112",nm:"",tp:"0",imo:"0",cs:"",length:"0",width:"0",draught:"0",eta:"0",dest:"592640@SH",iso3:"",dwt:"3306"},{time:"1536862793",mmsi:"413441350",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.002632",y:"38.900116",cog:"1896",truehead:"117",nm:"",tp:"0",imo:"0",cs:"",length:"0",width:"0",draught:"0",eta:"0",dest:"601246@TIAN JIN",iso3:"",dwt:"3306"},{time:"1536862774",mmsi:"413503810",stat:"1",rot:"0",sog:"1",pos_acc:"0",x:"118.022446",y:"38.890129",cog:"1863",truehead:"120",nm:"XIN HONG XIANG 76",tp:"70",imo:"0",cs:"BMKX",length:"140",width:"20",draught:"0",eta:"0",dest:"614720@TIANJIN",iso3:"CHN",dwt:"27440"},{time:"1536862621",mmsi:"413727000",stat:"1",rot:"0",sog:"2",pos_acc:"0",x:"118.078033",y:"38.886204",cog:"558",truehead:"114",nm:"YUEANYUN182",tp:"70",imo:"0",cs:"BRVQ",length:"150",width:"22",draught:"0",eta:"0",dest:"615360@TIAN JIN",iso3:"CHN",dwt:"33750"},{time:"1536862796",mmsi:"414137000",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.017860",y:"38.900543",cog:"382",truehead:"121",nm:"GUO DIAN 11",tp:"70",imo:"9636589",cs:"BFAU3",length:"225",width:"32",draught:"0",eta:"0",dest:"588918@CHANGJIANGKOU",iso3:"",dwt:"3306"},{time:"1536862725",mmsi:"538002403",stat:"1",rot:"0",sog:"0",pos_acc:"0",x:"118.056442",y:"38.899712",cog:"0",truehead:"132",nm:"BANASOL",tp:"72",imo:"9214135",cs:"V7IL8",length:"225",width:"32",draught:"0",eta:"0",dest:"613504@CN TXG",iso3:"MHL",dwt:"72562"},{time:"1536862637",mmsi:"538005781",stat:"1",rot:"0",sog:"1",pos_acc:"0",x:"118.086510",y:"38.906376",cog:"1282",truehead:"133",nm:"NAVIG8 AMMOLITE",tp:"80",imo:"9727534",cs:"V7GX7",length:"184",width:"27",draught:"0",eta:"0",dest:"0@",iso3:"",dwt:"3306"},{time:"1536862785",mmsi:"624021000",stat:"1",rot:"2",sog:"1",pos_acc:"0",x:"118.030266",y:"38.895599",cog:"316",truehead:"129",nm:"JIGJIGA",tp:"70",imo:"9617404",cs:"ETJJ",length:"166",width:"27",draught:"0",eta:"0",dest:"0@",iso3:"",dwt:"3306"}]')

if __name__ == "__main__":
    main()
