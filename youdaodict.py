#!/usr/bin/python
#coding:utf8
import requests
import json
import tkinter


def get_translate_date(word=None):
    global  entry_word
    global  target_word
    word = entry_word.get()
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    hostFrom_data = {'i': word, 'from': 'zh-CHS', 'to': 'en', 'smartresult': 'dict', 'client': 'fanyideskweb',
                     'salt': '15792260843195', 'sign': '8d811af1a78ebdb1af8368ca33a664bc', 'ts': '1579226084319',
                     'bv': '75a84f6fbcebd913f0a4e81b6ee54608', 'doctype': 'json', 'version': '2.1',
                     'keyfrom': 'fanyi.web', 'action': 'FY_BY_CLICKBUTTION', 'typoResult': 'false'}
    response = requests.post(url,data=hostFrom_data)
    content = json.loads(response.text)
    target_word = content['translateResult'][0][0]['tgt']
    print(target_word)

root = tkinter.Tk()
root.title("有道字典查询")
root.geometry("200x200")
lbl_source_language = tkinter.Label(root,text="源语言")
lbl_source_language.grid(row=0,column=0)
entry_word = tkinter.Entry(root)
entry_word.grid(row=0,column=1)

lbl_target_language = tkinter.Label(root,text="目标语言")
lbl_target_language.grid(row=1,column=0)
target_word = tkinter.Text(root,width=20,height=1)
#target_word.grid(row=1,column=1)
target_word.insert(tkinter.END,'target_word')
target_word.see(tkinter.END)
target_word.update()

button_transfrmer = tkinter.Button(root,text="翻译")
button_transfrmer.grid(row=2,column=0)
button_transfrmer["command"] = get_translate_date

root.mainloop()