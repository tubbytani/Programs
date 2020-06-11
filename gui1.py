import matplotlib.pyplot as plt
from math import*
import sqlite3 as sq
'''
def register():
    conn=sq.connect('hello.db')
    cur=conn.cursor()
    qry='create table if not exists ste(id,name)'
    cur.execute(qry)
    qry='''insert into ste(id,name)values('1','tan')'''
    cur.execute(qry)
    conn.close()
def login():
    conn=sq.connect('hello.db')
    cur=conn.cursor()
    qry='select * from ste where id=1'
    data=cur.execute(qry)
    print(data.fetchone())
    conn.close()
'''
def draw():
    x=list(range(0,180))
    y=[]
    for i in x:
        y.append(sin(i))
    plt.plot(x,y)
    plt.show()
def draw1():
    x=list(range(0,180))
    y=[]
    for i in x:
        y.append(cos(i))
    plt.plot(x,y)
    plt.show()
import tkinter as tk
window=tk.Tk()
window.title('My First gui')
window.geometry('480x640')
btn=tk.Button(text='Plot sine graph',command=draw)
btn.grid(row=1,column=1)

btn2=tk.Button(text='Plot cos graph',command=draw1)
btn2.grid(row=2,column=1)

btn3=tk.Button(text='Login',command=login)
btn3.grid(row=3,column=1)

btn4=tk.Button(text='register',command=login)
btn4.grid(row=4,column=1)
window.mainloop()

