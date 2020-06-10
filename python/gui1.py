import matplotlib.pyplot as plt
from math import*
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
window.mainloop()
