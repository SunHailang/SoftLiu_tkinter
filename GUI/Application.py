# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-20"


import tkinter

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
                                height=self.m_height)# ,background='red')
        self.m_canvas.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.m_canvas.pack(side=side)

    def ShowLabel(self, text, x, y, font):
        # The 'menu' of the application. The selection labels
        application_label = tkinter.Label(self.m_master, text=text, font=font)
        return self.m_canvas.create_window(x, y, window=application_label)

    def ShowInage(self, filePath, x, y):
        imageFile = tkinter.PhotoImage(file=filePath)
        return self.m_canvas.create_window(x, y, window=imageFile)

    def ShowInputEntry(self, x, y, setInfo='', show=''):
        entry_var = tkinter.StringVar()
        entry = tkinter.Entry(self.m_master,width=20,textvariable=entry_var,show=show)
        entry_var.set(setInfo)
        return self.m_canvas.create_window(x, y, window=entry)
    
        
