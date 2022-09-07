from tkinter import*
frame=Tk()
frame.geometry('400x500')
frame.configure(background= "darkcyan")
frame.title("Converter")

def convert():
    n=cc.get()
    c=n*1024
    nn.set(str(c)+" mb")

def ctof():
    f=cc.get()
    c=(f-32)*0.55
    nn.set(str(c)+" c")

def lml():
    n=cc.get()
    c=n*1000
    nn.set(str(c)+" ml")

def cont():
    n=cc.get()
    d=n*0.013
    nn.set(str(d)+" $")



cc=IntVar()
nn=IntVar()
name=Label(text="Enter Value")
name.place(x=30,y=50)

en=Entry(textvariable=cc)
en.place(x=110,y=30)

en1=Entry(textvariable=nn)
en1.place(x=110,y=80)

btn=Button(text="Gb to mb Convert",command=convert)
btn.place(x=140,y=160)

btn1=Button(text="l to ml Convert",command=lml)
btn1.place(x=140,y=190)

btn2=Button(text="f to c Convert",command=ctof)
btn2.place(x=140,y=220)

btn3=Button(text="Currency Convert in Dollor",command=cont)
btn3.place(x=140,y=250)






