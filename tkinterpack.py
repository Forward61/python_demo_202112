import tkinter
root=tkinter.Tk()
# label=tkinter.Label(root,text='hello,python')
# label.pack()
#
#
# button1= tkinter.Button(root,text='button1')
# button1.pack(side=tkinter.LEFT)
#
# button2=tkinter.Button(root,text='button2')
# button2.pack(side=tkinter.RIGHT)
# root.geometry('600x400')
# root.mainloop()

root.geometry('200x200+280+280')
root.title('计算器示例')


L1=tkinter.Button(root, text='1',width=5,bg='yellow')
L=tkinter.Button(root, text='',width=5)


L0=tkinter.Button(root, text='0')


L1.grid(row=0,column=0)
L0.grid(row=3,columnspan=2,sticky='ew')
btn1=tkinter.Button(root,text="确定")
btn1.grid(row=4,column=0)

def callback():
    showinfo("python")
btn2=tkinter.Button(root,text='设置调用命令',command=callback)
btn2.grid()









root.mainloop()