# -*- coding: cp936 -*-
def Getchecknum(input):
    n = 10
    for num in range(len(input)):
        n = (int(input[num])+n)%10
        if n ==0:
            n =10
        n = n*2%11
    if n ==0:
        s=1
    elif n==1:
        s =0
    else:
        s = 11-n
    return str(s)
code = raw_input(u'���������ҵ15λע���룺')
while True:
    try:
        len(code) == 15
        num= code[:14]
        check_num=int(code[14])
        if check_num == int(Getchecknum(num)):
            print u'��ϲ�㣬ע������ȷ'
        else:
            print u'��ע�⣬��ע�������'
        break
    except:
        print u'��������ȷ����ҵ15λע����'
raw_input(u'��������˳�')
