import tkinter
win = tkinter.Tk()
ent1 = tkinter.Entry(win,
                      relief='ridge',
                      borderwidth=3,
                      highlightcolor="red",
                      highlightthickness=3,
                      highlightbackground='yellow',
                      takefocus=True)

ent1.pack()

ent2 = tkinter.Entry(win,
                      relief='ridge',
                      borderwidth=3,
                      highlightcolor="red",
                      highlightthickness=3,
                      highlightbackground='yellow',
                      takefocus=True)
ent2.pack()
win.mainloop()
