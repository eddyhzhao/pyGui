#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#import Tkinter
#
#top = Tkinter.Tk()
## 进入消息循环
#top.mainloop()

import tkMessageBox
import Tkinter

def helloCallBack():
    tkMessageBox.showinfo("Hello PythonXXX", "Hello Runoob")

top = Tkinter.Tk()
B = Tkinter.Button(top, text = "点击我", command = helloCallBack)
B.pack()

top.mainloop()  # 进入消息循环
