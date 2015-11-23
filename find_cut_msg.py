# -*- coding: cp936 -*-
import re
import os
def find_cut_msg(filename):
    target=re.compile('^135.*')
    new_txt=[]
    for msg in open(filename,'r').readlines():
        R=re.findall(target,msg)
        if R:
            continue
        else:
            new_txt.append(msg)
    open(filename,'r+').seek(0)
    open(filename,'r+').truncate(0)
    open(filename,'r+').writelines(new_txt)

if __name__=='__main__':
    filename='test.txt'
    find_cut_msg(filename)
