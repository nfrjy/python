#!/usr/bin/python
#codeing:utf8
from DB.db_init import MyDB
if __name__=='__main__':
    with MyDB(host='localhost',port=3306,user='root',passwd='aixocm',db='mysql',charset='utf8') as db:
        db.execute("select version();")
        print(db)
        for i in db:
            print(i)







