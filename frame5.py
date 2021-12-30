from tkinter import *
root=Tk ()
f=Frame(root , height=200 , width=200)

labl=Label (f,text='欢迦参观中原工学院 ')

x=0
def foo () :

    global x
    x=x+10
    if x>200:

        x=0
    labl . place(x=x , y=0)
    f. after (500 , foo)

#隔 500ms 执行 foo （）函数刷新屏幕

f . pack ()
f.after (500 , foo)
root . mainloop ()