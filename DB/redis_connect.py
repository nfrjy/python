#!/usr/bin/pyton
import redis
from redis import ConnectionPool

class redis_poll():
    def __init__(self,host,port,passwd):
        self.host = host
        self.port = port
        self.passwd = passwd
    def connect_poll(self):
        Pool = ConnectionPool(host=self.host,port=self.port,passwd=self.passwd)
        conn = redis.Redis(connection_pool= Pool)




