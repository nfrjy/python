#!/usr/bin/python
import random
from DB.db_init import  MyDB
import redis
from DB.redis_connect import  redis_poll

def create_code(num,lang):
    str = "abcdefghijklmnopqrstuvwxyz0123456789"
    code = []
    for i in range(num):
        code_target = ''
        for j in range(lang):
            code_target += random.choice(str)
        code.append(code_target)
    return code

def insert_code_to_DB(code):
    with MyDB(host='localhost',port=3306,user='root',passwd='aixocm',db='pythontest') as db:
        for codenumber in code:
            db.execute('insert into activecode(code) values(%s)',(codenumber))

def insert_code_to_redis(code):
    with redis_poll(host='localhost',port=6379,passwd='aixocm') as rediscon:
        p = rediscon.pipeline()
        for codenumber in code:
            p.sadd('code',codenumber)
        p.execute()
        return  rediscon.rsave('code')

def save_code_to_redis(code):
    r = redis.Redis(host='localhost',port=6379,password='aixocm')
    p = r.pipeline()
    for codenumber in code:
        p.sadd('code',codenumber)
    p.execute()
    return r.scard('code')


if __name__=='__main__':
    #insert_code_to_DB(create_code(200,10))
    insert_code_to_redis(create_code(200,10))


