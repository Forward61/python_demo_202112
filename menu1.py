from tkinter import *
root=Tk()
def hello():
    print('你单击主菜单')

m=Menu(root)
for item in ['文件','编辑','视图']:
    m.add_command(label=item,command=hello)
root['menu']=m
root.mainloop()

# from  tkinter import *
#
# root = Tk()
#
# menubar = Menu(root)
#
# def callback():
#     pass
# filemenu = Menu(menubar, tearoff=False)
# filemenu.add_command(label="打开",command=callback)
# filemenu.add_command(label="保存",command=callback)
# filemenu.add_separator()
# filemenu.add_command(label="退出",command=callback)
# menubar.add_cascade(label="文件",menu=filemenu)
#
# editmenu = Menu(menubar, tearoff=False)
# editmenu.add_command(label="复制",command=callback)
# editmenu.add_command(label="粘贴",command=callback)
# editmenu.add_separator()
# editmenu.add_command(label="退出",command=callback)
# menubar.add_cascade(label="编辑",menu=editmenu)
#
# root.config(menu=menubar)
# mainloop()