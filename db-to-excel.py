#!/usr/bin/python
#coding:utf8
from DB.db_init import MyDB as db
import xlwt
import pandas as pd
import matplotlib.pyplot as plt

def w_execl(rep):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("测试")
    title = ["ID","姓名","年龄","户籍"]
    i = 0
    for header in title:
        worksheet.write(0,i,header)
        i += 1

    for row in range(1,len(rep)):
        for col in range(0,len(rep[row])):
            worksheet.write(row,col,rep[row][col])
            col +=1
        row +=1
    workbook.save("测试.xls")
    print("导出成功")

def execl_to_chart(datafile):
    reviewer = pd.read_csv('date.csv')



if __name__=="__main__":
    with db(host='localhost',port=3306,user='root',passwd='aixocm',db='pythontest') as dbtest:
        dbtest.execute("select name,addr from student;")
        rep = dbtest.fetchall()

        w_execl(rep)
