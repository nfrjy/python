import datetime
import sys
import os,re
def search():
    Flag_result=set()
    Now=(datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S')).split()
    Fivemin=(datetime.datetime.now()+datetime.timedelta(seconds=-300)).strftime('%d/%b/%Y:%H:%M:%S').split()
    target=re.compile('.*Flag=(.*)&.*')
    with open(r'C:\Users\Administrator\Desktop\test.txt','r') as f:
        for msg in f.readlines():
            a=re.split("[- -]",msg)
            if a[5][1:].split()>=Fivemin and a[5][1:].split() <= Now:
                m=re.search(target,msg)
                if m:
                    with open(r'C:\Users\Administrator\Desktop\result.txt','a') as w:
                        w.write(m.group(1)+'\n')
                    Flagresult=open(r'C:\Users\Administrator\Desktop\Flagresult.txt','a')
                    for line in open(r'C:\Users\Administrator\Desktop\result.txt','r'):
                        if line not in Flag_result:
                            Flagresult.write(line)
                            Flag_result.add(line)
                    Flagresult.close()
                            
            else:
                print "no"
if __name__=='__main__':
    search()
