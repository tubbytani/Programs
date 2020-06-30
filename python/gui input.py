import tkinter as tk

def store_entry_fields():
    store=e1.get()
    print(store)

master = tk.Tk()
master.title("Form")
tk.Label(master,text="Enter your review about the situation").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
tk.Button(master,text='Submit',command=store_entry_fields).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.mainloop()
