import tkinter as tk
from mysqldb import *
import re


err = tk.Tk()
err.geometry('300x200')
err.title('插入数据')

单价 = tk.Label(err, text='单价：', font=("黑体", 15))
单价.place(x=20, y= 70)

Text = tk.Text(err, bd=0, height=1, width= 16, font=('黑体', 15))
Text.place(x= 80, y= 70)

def submitData(name, cost):
    print(cost.strip() .lstrip() .rstrip(','))
    if len(cost) == 1:
        Text.delete(1.0,tk.END)
        Text.insert('insert','请输入价格')
        return
    log = re.match(r'^[0-9]+(\.[0-9]{1,2})?$', cost, flags=0)
    if log:
        result = 添加菜品(name, cost)
        if result == '成功':
            Text.delete(1.0,tk.END)
            Text.insert('insert','成功')
        else:
            Text.delete(1.0,tk.END)
            Text.insert('insert','失败')
    else:
        Text.delete(1.0,tk.END)
        Text.insert('insert','请正确输入价格')
        return

def showErr(name):

    菜名 = tk.Label(err, text=name, font=("黑体", 15))
    菜名.place(x=100, y= 20)

    bt = tk.Button(err, bd=1, text='记录', width=12, height=2, command = lambda: submitData(name, Text.get('0.0','end')))
    bt.place(x = 80, y = 115)
    err.mainloop()



