from tkinter import *
import turtle
root = Tk()

#mylabel1=Label(root, text="hello world").grid(row=1, column=1)
#mylabel2=Label(root, text="iam rsd").grid(row=2, column=1)
#mylabel.pack()
#mylabel1.grid(row=1, column=1)
#mylabel2.grid(row=2, column=1)

#mybutton=Button(root,text="click here",state=DISABLED)

e=Entry(root, width=50, bg="yellow", borderwidth=5)
e.pack()
e.insert(10,"enter your name")




def myclick():
    hello = "hello " + e.get()
    mylabel1 = Label(root, text= hello)
    mylabel1.pack()

mybutton = Button(root,text="click here", padx=5, pady=5, command=myclick, bg="blue")
mybutton.pack()
root.mainloop()
