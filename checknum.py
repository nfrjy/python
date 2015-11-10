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
code = raw_input(u'请输入该企业15位注册码：')
while True:
    try:
        len(code) == 15
        num= code[:14]
        check_num=int(code[14])
        if check_num == int(Getchecknum(num)):
            print u'恭喜你，注册码正确'
        else:
            print u'请注意，该注册码错误'
        break
    except:
        print u'请输入正确的企业15位注册码'
raw_input(u'按任意键退出')
