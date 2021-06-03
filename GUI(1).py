import tkinter as tk
import tkinter.messagebox
import tkinter.font as tf
import os
from main import *
import cv2 as cv
from PIL import ImageTk
from PIL import Image
from com import *

# 打开串口
cap = 启动相机()
ser = open_serial()

def catall(Log, Weight, LogCost, LogSolo):
    Log.insert('insert','nmd ,dsb')
    Log.edit_undo()
    Weight.insert('insert','nmd ,dsb')
    Weight.edit_undo()
    LogCost.insert('insert','nmd ,dsb')
    LogCost.edit_undo()
    LogSolo.insert('insert','nmd ,dsb')
    LogSolo.edit_undo()
def updateWin(cap, canvas):
    while(True):
        ret, frame = cap.read()
        cov = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        img = Image.fromarray(cov)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0,0, anchor='nw', image = img)
        canvas.pack()
        win.update()

    
win = tk.Tk()
win.geometry('800x700')
win.title('蔬果')

imgFile1 = os.getcwd() + r"\logo\Button1.png"
imgFile2 = os.getcwd() + r"\logo\Button2.png"
imgBtn1 = tk.PhotoImage(file=imgFile1)
imgBtn2 = tk.PhotoImage(file=imgFile2)

ft = tf.Font(family='黑体', size= 30)
Log = tk.Text(win,
                bd=0,
                height=1,
                width=15,
                bg='#87CEEB',
                highlightthickness=5,
                highlightbackground='#AFFEEE',
                highlightcolor='#6495ED',
                undo = True,
                font = ft)
Log.place(x=400, y=470)

类型 = tk.Label(win, text="类型:", font=("黑体", 25))
类型.place(x = 300 ,y = 477)

Weight = tk.Text(win,
                bd=0,
                height=1,
                width=8,
                bg='#87CEEB',
                highlightthickness=5,
                highlightbackground='#AFFEEE',
                highlightcolor='#6495ED',
                undo = True,
                font = ft)
Weight.place(x=830, y=470)

重量 = tk.Label(win, text="重量:", font=("黑体", 25))
重量.place(x = 730 ,y = 477)

LogSolo = tk.Text(win,
                bd=0,
                height=1,
                width=8,
                bg='#87CEEB',
                highlightthickness=5,
                highlightbackground='#AFFEEE',
                highlightcolor='#6495ED',
                undo = True,
                font = ft)
LogSolo.place(x=400, y=525)

单价 = tk.Label(win, text="单价:", font=("黑体", 25))
单价.place(x = 300 ,y = 530)

LogCost = tk.Text(win,
                bd=0,
                height=1,
                width=9,
                bg='#87CEEB',
                highlightthickness=5,
                highlightbackground='#AFFEEE',
                highlightcolor='#6495ED',
                undo = True,
                font = ft)
LogCost.place(x=700, y=525)

总价 = tk.Label(win, text="总价:", font=("黑体", 25))
总价.place(x = 600 ,y = 530)

canvas = tk.Canvas(win,
                   width=800,
                   height=450)
canvas.place(x=-400, y= 400)


Start = tk.Button(win,bd=0, image=imgBtn1, command = lambda: kaishi(cap, Log, ser, Weight, LogCost, LogSolo))
Start.place(x=330,y=600)

Exit = tk.Button(win,bd=0,image=imgBtn2, command= lambda: catall(Log, Weight, LogCost, LogSolo))
Exit.place(x=810,y=600)

updateWin(cap, canvas)       
win.mainloop()
