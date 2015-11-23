import os,sys
def copyline(filename):
    for msg in open('test.txt','r').readlines():
        a=msg*10
        T=open('reslut.txt','a')
        T.write(a)
    T.close()
if __name__=='__main__':
    filename="test.txt"
    copyline(filename)
    
