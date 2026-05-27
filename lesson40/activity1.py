from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("main")
l = Label(root, text = "this is root window")

top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text = "This is toplevel window")
root.mainloop()