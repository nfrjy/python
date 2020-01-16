# -*- coding: cp936 -*-
import random
import os,sys
import urllib2,urllib
import re,json
def pasteurl(filename):
    with open(filename,'r') as f:
        for urls in f.readlines():
            url=urls.strip('\n')
            num=str(random.randint(1,999999))
            targetfile=open('targeturl.txt','a')
            targetfile.write(url+'?'+num+'\n')
def longurltoshort(longurl):
    with open(longurl,'r') as L:
        for urls in L.readlines():
            url=urls.strip('\n')
            api="http://api.t.sina.com.cn/short_url/shorten.json?source=3213676317&url_long="
            apiurl=api+url
            request=urllib2.Request(apiurl)
            handler=urllib2.urlopen(request)
            change=json.load(handler)
            rs=change[0]
            shorturl=rs['url_short']
            result=open('result.txt','a')
            result.write(shorturl+'\n')
            
if __name__=='__main__':
    filename=input("请输入要粘贴的URL文件名:")
    pasteurl(filename)
    longurl='targeturl.txt'
    longurltoshort(longurl)
    os.remove('targeturl.txt')
    os.remove('shortfile.txt')
