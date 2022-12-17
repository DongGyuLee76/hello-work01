import tkinter
win = tkinter.Tk()
win.title('윈도우 생성하기')
lbl=tkinter.Label(win, text= " 안녕 파이썬~")
lbl.pack()
lbl2=tkinter.Label(win, text="hello world~", bg='red', fg='white')
lbl2.pack(fill='x')
win.mainloop()
