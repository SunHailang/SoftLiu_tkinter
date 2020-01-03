

import tkinter
from tkinter import ttk

if __name__ == "__main__":
    win = tkinter.Tk()
    win.title("表格数据")
    win.geometry("800x600+600+100")
    sb = tkinter.Scrollbar(win)
    sb.place(x=520, y=0, width=15, height=100)
    tree = ttk.Treeview(win,yscrollcommand= sb.set)  # 表格
    tree["columns"] = ("姓名", "年龄", "身高")
    tree.column("姓名", width=100, anchor='center')  # 表示列,不显示
    tree.column("年龄", width=100, anchor='center')
    tree.column("身高", width=100, anchor='center')

    tree.heading("姓名", text="姓名-name")  # 显示表头
    tree.heading("年龄", text="年龄-age")
    tree.heading("身高", text="身高-tall")

    tree.insert("", 0, text="line1", values=("1", "2", "3"))  # 插入数据，
    tree.insert("", 1, text="line2", values=("1", "2", "3"))
    tree.insert("", 2, text="line3", values=("1", "2", "3"))
    tree.insert("", 3, text="line4", values=("1", "2", "3"))  # 插入数据，
    tree.insert("", 4, text="line5", values=("1", "2", "3"))
    tree.insert("", 5, text="line6", values=("1", "2", "3"))
    tree.insert("", 6, text="line7", values=("1", "2", "3"))  # 插入数据，
    tree.insert("", 7, text="line8", values=("1", "2", "3"))
    tree.insert("", 8, text="line9", values=("1", "2", "3"))
    tree.place(x=5, y=5, width=500, height=100)

    
    # sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    # lb = tkinter.Listbox(win,yscrollcommand= sb.set)
    #for i in range(1000):
    #    lb.insert(tkinter.END,i)
    # lb.pack(side=tkinter.RIGHT)
    sb.config(command=tree.yview)
    win.mainloop()