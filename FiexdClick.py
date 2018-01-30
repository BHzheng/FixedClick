import win32api
import win32con
import time
from datetime import datetime
from tkinter import *
import threading
import time
import sys

#5min 锁屏

def buttonFrame():
    #按钮布局
    frame = Tk()
    frame.title("退出点击右上角的X按钮")
    button_start=Button(frame,text="开始阻止屏幕锁定",width=20,height=2)
    button_cancel=Button(frame,text="算了",width=20,height=2)
    frame.resizable(False,False)
    button_start.bind("<Button-1>",buttonStart)
    button_cancel.bind("<Button-1>",buttonCancel)
    button_start.grid(row=3,column=0)
    button_cancel.grid(row=3,column=1)
    frame.mainloop()

def buttonStart(event):     
    #循环休眠，一段时间后点击对应坐标
    #warning.........................程序运行后，开始执行阻止锁定，再次点击将导致程序无响应。
    #尚未找到解决方法
    while True:
        try:
            startEvent(1270,200)
            time.sleep(250)
        except (Exception,e):
            print("error")
        

def buttonCancel(event):
    cancelEvent()

def cancelEvent():
    sys.exit()

def startEvent(x,y):
    #鼠标点击传入的坐标位置
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0)        
        

if __name__ == '__main__':
    buttonFrame()


