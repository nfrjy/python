#!/usr/bin/python
#codeing:utf-8
from typing import Union

import psutil
import os
import smtplib
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os


class MyMail:
    def __init__(self,mail_config_file):
        config =  configparser.ConfigParser()
        config.read(mail_config_file)
        self.smtp = smtplib.SMTP()
        self.login_user = config.get('SMTP','login_user')
        self.login_pwd = config.get("SMTP","login_pwd")
        self.from_addr = config.get("SMTP","from_user")
        self.to_addrs = config.get("SMTP","to_user")
        self.host = config.get("SMTP","host")
        self.port = config.get("SMTP","port")

    def connect(self):
        self.smtp.connect(self.host,self.port)

    def login(self):
        try:
            self.smtp.login(self.login_user,self.login_pwd)
        except Exception as e:
            print ('%s' % e)

    def sendmessage(self,mail_subject,mail_content,attachment_path_set):
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(eval(self.to_addrs))
        msg['Subject'] = mail_subject
        Content = MIMEText(mail_content, _charset='gbk')
        msg.attach(Content)
        for attachment_path in attachment_path_set:
            if os.path.exists(attachment_path):
                type, coding = mimetypes.guess_type(attachment_path)
                if type == None:
                    type = 'application/octet-stream'
                    major_type, minor_type = type.split('/', 1)
                    with open(attachment_path, 'rb') as file:
                        if major_type == 'text':
                            attachment = MIMEText(file.read(), _subtype=minor_type)
                        elif major_type == 'image':
                            attachment = MIMEImage(file.read(), _subtype=minor_type)
                        elif major_type == 'application':
                            attachment = MIMEApplication(file.read(), _subtype=minor_type)
                        elif major_type == 'audio':
                            attachment = MIMEAudio(file.read(), _subtype=minor_type)
                            attachment_name = os.path.basename(attachment_path)
                            attachment.add_header('Content-Disposition', 'attachment', filename=('gbk', '', attachment_name))
                            msg.attach(attachment)
        full_text = msg.as_string()
        self.smtp.sendmail(self.from_addr, eval(self.to_addrs), full_text)

    def logout(self):
        self.smtp.quit()

class Mem_Monitor:
    def Get_MemTotal(self):
        self.MemTotal = psutil.virtual_memory().total
        return self.MemTotal
    def Get_MemUsed(self):
        self.MemUsed = psutil.virtual_memory().used
        return self.MemUsed
    def Used_Percent(self):
        self.used_percent = float(self.MemUsed / self.MemTotal) * 100
        return self.used_percent

if __name__=="__main__":
    Monitor = True
    gitlabMem = Mem_Monitor()
    gitlabMem.Get_MemTotal()
    gitlabMem.Get_MemUsed()
    gitlabMem.Used_Percent()
    if int(gitlabMem.Used_Percent()) > 80:
        if Monitor == True:
            mymail = MyMail('./mail.conf')
            mymail.connect()
            mymail.login()
            mail_content = "Gitlab服务器内存详情：总内存: %s,已使用内存: %s,使用占比: %s %%," % (gitlabMem.Get_MemUsed(),gitlabMem.Get_MemUsed(),gitlabMem.Used_Percent())
            mymail.sendmessage("Gitlab 服务器内存告警",mail_content,"None")
            mymail.logout()
            Monitor = False
    else:
        Monitor = True
