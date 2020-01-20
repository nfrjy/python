#!/usr/bin/python
#-*- coding：utf-8 --*-
import os
import time
import tkinter

def backup():
    global  entry_source
    global  entry_target
    source = entry_source.get()
    target = entry_target.get()

    taday_dir = target + time.strftime("%Y%m%d")
    time_strf = time.strftime("%H%M%S")
    target_file = taday_dir + os.sep + time_strf + ".zip"
    cmd_commond = "zip -rq " + target_file + " ".join(source)
    if os.path.exists(taday_dir):
        print("%s 文件夹存在") % taday_dir
    else:
        os.mkdir(taday_dir)
    if os.system(cmd_commond) == 0:
        print ("Successful back")
    else:
        print("Failure back")

root = tkinter.Tk()
root.title("备份")
root.geometry("500x200")

lbl_source = tkinter.Label(root, text="源文件")
lbl_source.grid(row=0,column=0)
entry_source = tkinter.Entry(root)
entry_source.grid(row=0,column=1)

lbl_target = tkinter.Label(root,text="目标")
lbl_target.grid(row=1,column=0)
entry_target = tkinter.Entry(root)
entry_target.grid(row=1,column=1)

but_back = tkinter.Button(root,text="备份")
but_back.grid(row=2,column=0)
but_back["command"] = backup

root.mainloop()