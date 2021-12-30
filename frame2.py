from tkinter import *
root = Tk()
root.title('使用frame组件的例子1')
f1=Frame(root)
f1.pack()

f2=Frame(root)
f2.pack()

f3=LabelFrame(root,text='第3个frame')
f3.pack(side=BOTTOM)
redbutton=Button(f1,text='Red',fg="red")
redbutton.pack(side=LEFT)

brownbutton=Button(f1,text="brown",fg="brown")
brownbutton.pack(side=LEFT)

blackbutton=Button(f2,text='black',fg="black")
blackbutton.pack()
greenbutton=Button(f3,text='green',fg="Green")
greenbutton.pack()

root.mainloop()
