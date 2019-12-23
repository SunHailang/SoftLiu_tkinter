# -*- coding: utf-8 -*-

__author__ = "sun hai lang"
__date__ = "2019-12-23"

# tkinter.messagebox

import tkinter.messagebox
import tkinter.filedialog

# 1、提示消息框
def MessageBoxShowInfo(title, message):
    tkinter.messagebox.showinfo(title,message)

# 2、消息警告框
def MessageBoxShowWarning(title, message):
    tkinter.messagebox.showwarning(title, message)

# 3、错误消息框
def MessageBoxShowError(title, message):
    tkinter.messagebox.showerror(title, message)

# 4、对话框

# 确定/取消，返回值true/false
def MessageBoxAskOkCancel(title, message):
    tkinter.messagebox.askokcancel(title, message)

# 是/否，返回值yes/no
def MessageBoxAskQuestion(title, message):
    tkinter.messagebox.askquestion(title, message)

# 是/否，返回值true/false
def MessageBoxAskYesNo(title, message):
    tkinter.messagebox.askyesno(title, message)

# 重试/取消，返回值true/false
def MessageBoxAskRetryCancel(title, message):
    tkinter.messagebox.askretrycancel(title, message)

# 5、文件对话框

# 返回文件名
def FileDialogAskSaveAsFileName():
    return tkinter.filedialog.asksaveasfilename()

# 会创建文件
def FileDialogAskSaveasFile():
    return tkinter.filedialog.asksaveasfile()

# 返回文件名
def FileDialogAskOpenFileName():
    return tkinter.filedialog.askopenfilename()

# 返回文件流对象
def FileDialogAskOpenFile():
    return tkinter.filedialog.askopenfile()
    
# 返回目录名
def FileDialogAskDirectory():
    return tkinter.filedialog.askdirectory()

# 可以返回多个文件名
def FileDialogAskOpenFileNames():
    return tkinter.filedialog.askopenfilenames()

# 多个文件流对象
def FileDialogAskOpenFiles():
    return tkinter.filedialog.askopenfiles()
