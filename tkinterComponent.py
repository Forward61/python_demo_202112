from tkinter import *

root =Tk()
# btn1=Button(root,text="确定")
#
# btn1.grid(row=2,column=20)
# lab1=Label(root,text="你好",anchor='nw')
# lab1.pack
#
# btn2=Button(root,text="不确定")
# btn2.grid()
# lab1.grid(row=0,column=0)
#
# lab3=Label(root,bitmap='question')
# lab3.grid()
# # 好像只能识别 png 格式
# bm=PhotoImage(file=r'/Users/ningli/Pictures/a.png')
# lab4=Label(root,image=bm)
# lab4.bm=bm
# lab4.grid()
#
# s=StringVar()
# s.set("大家好，这是测试")
# entryCd=Entry(root,textvariable=s)
# entryCd.grid()
# print(s.get())
# lab1=Label(root,text="你好",anchor='nw')
# lab1.pack()


def callbtn1():
    for i in listb.curselection():
        listb2.insert(0,listb.get(i))
def callbtn2():
    for i in listb2.curselection():
        listb2.delete(2)

li=['C','Python','php']
listb=Listbox(root)
listb2=Listbox(root)
for item in li:
    listb.insert(0,item)
listb.grid(row=0,column=0,rowspan=2)
b1=Button(root,text='添加》》',command=callbtn1,width=20)
b2=Button(root,text='删除《《',command=callbtn2,width=20)
b1.grid(row=0,column=1,rowspan=2)
b2.grid(row=0,column=2,rowspan=2)
listb2.grid(row=0,column=2,rowspan=2)

# Listbox
root.mainloop()