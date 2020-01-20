#!/usr/bin/python
#coding: utf8
import re
def contextcount(file):
    context = open(file,'r')
    str = context.read()
    reObj = re.compile('\b?(\w+)\b?')
    restr = reObj.findall(str)

    wordDict = dict()
    for word in restr:
        if word.lower() in wordDict:
            wordDict[word.lower()] += 1
        else:
            wordDict[word] = 1
    for key,value in wordDict.items():
        print ("%s 单词出现次数: %s" %(key,value))

if __name__=="__main__":
    file = r'F:\CodeUp\python\test.txt'
    contextcount(file)


