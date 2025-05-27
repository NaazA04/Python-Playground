# import tkinter
# top=tkinter.Tk()
# top.mainloop()


# from tkinter import *
# root= Tk()
# w= Label(root, text='B.Tech CSE', fg='red')
# w.pack()
# root.mainloop()

from tkinter import *

def getCheckValue1():
    print(CheckVar1.get())

top= Tk()
CheckVar1= IntVar()
CheckVar2= IntVar()
C1= Checkbutton (top,text="Music", variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20,command=getCheckValue1)
C2= Checkbutton (top,text="Video", variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C1.pack()
C2.pack()
top.mainloop()