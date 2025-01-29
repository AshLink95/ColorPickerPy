from tkinter import*
from tkinter.colorchooser import*

NR=NG=NB=0
def NewR(self):
    global NR
    NR=R.get()
    hex = '#%02x%02x%02x' % (NR, NG, NB)
    Colorsee.config(bg=str(hex))

def NewG(self):
    global NG
    NG=G.get()
    hex = '#%02x%02x%02x' % (NR, NG, NB)
    Colorsee.config(bg=str(hex))

def NewB(self):
    global NB
    NB=B.get()
    hex = '#%02x%02x%02x' % (NR, NG, NB)
    Colorsee.config(bg=str(hex))

Window=Tk()
Window.geometry('500x650')

Colorsee=Label(Window,bg='black',relief=RIDGE,bd=2,padx=12,pady=10)
Colorsee.place(relwidth=0.5,relheight=0.25,relx=0.25,rely=0.08)

R=IntVar()
G=IntVar()
B=IntVar()

Red=Scale(Window, variable=R,from_=0, to=250, fg='Red',orient=HORIZONTAL, command=NewR)
Red.place(relwidth=0.75,relx=0.125,rely=0.4)
Green=Scale(Window, variable=G, from_=0, to=250, fg='Green',orient=HORIZONTAL,length=275, command=NewG)
Green.place(relwidth=0.75,relx=0.125,rely=0.5)
Blue=Scale(Window, variable=B,from_=0, to=250, fg='Blue',orient=HORIZONTAL,length=275, command=NewB)
Blue.place(relwidth=0.75,relx=0.125,rely=0.6)

Window.mainloop()
