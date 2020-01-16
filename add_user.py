#!/usr/bin/python
#encoding: utf-8
Userlist=[]
class Add_user:
    def check_user(self,user):
        self.username = user
        if self.username in Userlist:
            print ("%s is exist in userList") % (self.username)
    def add_user(self,user):
        self.username = user
        Userlist.append(self.username)
        print (Userlist)


if __name__ == '__main__':
    user = input("请输入要添加的名字：")
    Add_user().check_user(user)
    Add_user().add_user(user)