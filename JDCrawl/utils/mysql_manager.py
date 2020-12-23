# -*- coding: utf-8 -*-
import datetime
from JDCrawl.utils.mysql_connection import MySQLConnection

"""
MySQL数据库控制工具
"""


class MySql_Utils(object):
    def __init__(self):
        self.connect=MySQLConnection("local1")
        
    def connect_close(self):
        self.connect.close()
        print("MySQL工具类断开连接")

    def __del__(self):
        self.connect.close()
        print("MySQL工具类对象被回收")

    #添加/替换商品信息
    def replace_good(self,item):
        param = item._values
        param["create_time"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "REPLACE INTO t_goods(search_word,title,pic_url,detail_url,view_price,nick,create_time) VALUES (%(search_word)s,%(title)s,%(pic_url)s,%(detail_url)s,%(view_price)s,%(nick)s,%(create_time)s)"
        effect_num =  self.connect.update(sql, param)
        self.connect.commit()
        return effect_num


