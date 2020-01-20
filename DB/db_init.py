#!/usr/bin/python
#coding:utf-8
import pymysql
class MyDB:
    def __init__(self,host='localhost',port=3306,user='root',passwd='aixocm',db='', charset='utf8'):
        self.conn = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return  self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()



