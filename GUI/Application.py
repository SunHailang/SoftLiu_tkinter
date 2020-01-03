# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-20"


import tkinter
from PIL import Image

# Define the application class where we will implement our widgets


class Application(tkinter.Frame):
    def __init__(self, master, width, height, side):
        self.m_master = master
        self.m_width = width
        self.m_height = height
        super(Application, self).__init__(self.m_master)
        # CANVAS COLOUR DEFAULTS TO THE COLOUR OF THE WORKING WINDOW
        # IF YOU DO .PACK() HERE IT WILL RETURN NONE AND THEN YOU WILL HAVE PROBLEMS BECAUSE .PACK() RETURNS A 'NONE' TYPE OBJECT
        self.m_canvas = tkinter.Canvas(self.m_master, width=self.m_width,
                                       height=self.m_height)  # ,background='red')
        self.m_canvas.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.m_canvas.pack(side=side)

    def ShowLabel(self, text, x, y, font):
        # The 'menu' of the application. The selection labels
        application_label = tkinter.Label(self.m_master, text=text, font=font)
        return self.m_canvas.create_window(x, y, window=application_label)

    def ShowImage(self, filePath, x, y):
        imageFile = tkinter.PhotoImage(file=filePath)
        self.m_canvas.create_image(x, y, anchor='nw', image=imageFile)

    def ShowInputEntry(self, x, y):
        entry_var = tkinter.StringVar()
        entry = tkinter.Entry(self.m_master, width=20,
                              textvariable=entry_var, show='*')
        entry.pack()
        entry_var.set('我是一个Entry')
        return entry


if __name__ == "__main__":
    app_width = 450
    app_height = 350
    tk = tkinter.Tk()
    tk.title('登录')
    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()
    x_coord = (screen_width/2) - (app_width/2)
    y_coord = (screen_height/2) - (app_height/2)
    tk.geometry("%dx%d+%d+%d" % (app_width,
                                 app_height, x_coord, y_coord))
    # 阻止Python GUI的大小调整
    tk.resizable(0, 0)

    user_var = tkinter.StringVar()
    tkinter.Label(tk, text='User Name:').place(x=80, y=20)
    m_entry_user = tkinter.Entry(
        tk, width=27, textvariable=user_var)
    m_entry_user.place(x=180, y=20)
    tkinter.Label(tk, text='Password:').place(x=80, y=50)
    pw_var = tkinter.StringVar()
    m_entry_pw = tkinter.Entry(
        tk, width=27, textvariable=pw_var, show='*')
    m_entry_pw.place(x=180, y=50)

    canvas = tkinter.Canvas(tk, width=293,
                            height=180, background='white')
    canvas.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    print(Image.open('2.gif'))
    imageFile = tkinter.PhotoImage(file='2.gif')
    index = canvas.create_image(4, 2, anchor='nw', image=imageFile)
    m_btn = tkinter.Button(
        tk, text="    Sure    ")  # , command=self.Login_OnClick)
    print(m_btn)
    m_btn.place(x=200, y=310)
    tk.mainloop()
