# from tkinter import *
import tkinter

root =tkinter.Tk()
# c=tkinter.Intvar()
# c=tkinter.IntVar()
# c.set(2)
# check=tkinter.Checkbutton(root,text='喜欢',variable=c,onvalue=1,offvalue=2)
# check.pack()
r=tkinter.StringVar()
r.set('1')
radio=tkinter.Radiobutton(root,variable=r,value='1',text='中国')
radio.pack()
radio=tkinter.Radiobutton(root,variable=r,value='2',text='美国')
radio.pack()



root.mainloop()
print(r.get())

# print(check.get())
