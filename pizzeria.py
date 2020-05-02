from tkinter import *

def s1_click(val):
    k1 = int(val)
    x1 = int(p1.get())
    y1 = x1 * k1
    var1.set(y1)
    if k1:
        tk.geometry("650x300")
    else:
        tk.geometry("440x300")

def s2_click(val):
    k2 = int(val)
    x2 = int(p2.get())
    y2 = x2 * k2
    var2.set(y2)

def s3_click(val):
    global y3
    k3 = int(val)
    x3 = int(p3.get())
    y3 = x3 * k3
    var3.set(y3)

def s4_click(val):
    k4 = int(val)
    x4 = int(p4.get())
    y4 = x4 * k4
    var4.set(y4)

def btn_click():
    y = rez(var1.get()) + \
        rez(var2.get()) + \
        rez(var3.get()) + \
        rez(var4.get()) + \
        rez(var11.get()) * 3 + \
        rez(var12.get()) * 3 + \
        rez(var13.get()) * 3 + \
        rez(var14.get()) * 3
    var5.set(y)

def rez(value):
    if value:
        return int(value)
    else:
        return 0

tk = Tk()
tk.geometry("440x300")
tk.title("Піцерія")

name = Label(text="Найменування", font=("Arial", 12, "bold"))
name.place(x=20, y=20)
price = Label(text="Ціна, грн.", font=("Arial", 12, "bold"))
price.place(x=150, y=20)
number = Label(text="Кількість", font=("Arial", 12, "bold"))
number.place(x=230, y=20)
cost = Label(text="Вартість, грн", font=("Arial", 12, "bold"))
cost.place(x=310, y=20)

p1 = Entry(font="Arial 12", bg="sky blue", justify="center")
p1.insert(END, "75")
p1.place(x=150, y=60, width=60, height=30)
s1 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s1_click)
s1.place(x=230, y=50)
var1 = StringVar()
c1 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var1)
c1.place(x=310, y=60, width=60, height=30)

p2 = Entry(font="Arial 12", bg="sky blue", justify="center")
p2.insert(END, "12")
p2.place(x=150, y=100, width=60, height=30)
s2 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s2_click)
s2.place(x=230, y=90)
var2 = StringVar()
c2 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var2)
c2.place(x=310, y=100, width=60, height=30)

p3 = Entry(font="Arial 12", bg="sky blue", justify="center")
p3.insert(END, "16")
p3.place(x=150, y=140, width=60, height=30)
s3 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s3_click)
s3.place(x=230, y=130)
var3 = StringVar()
c3 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var3)
c3.place(x=310, y=140, width=60, height=30)

p4 = Entry(font="Arial 12", bg="sky blue", justify="center")
p4.insert(END, "8")
p4.place(x=150, y=180, width=60, height=30)
s4 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s4_click)
s4.place(x=230, y=170)
var4 = StringVar()
c4 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var4)
c4.place(x=310, y=180, width=60, height=30)

var5 = StringVar()
c5 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var5)
c5.place(x=200, y=240, width=60, height=30)
btn = Button(text="Розрахувати", font="Arial 12", command=btn_click)
btn.place(x=330, y=240)

name2 = Label(text="Піца", font=("Arial", 12,))
name2.place(x=20, y=60)
name3 = Label(text="Морозиво", font=("Arial", 12,))
name3.place(x=20, y=100)
name4 = Label(text="Тістечко", font=("Arial", 12,))
name4.place(x=20, y=140)
name5 = Label(text="Сік", font=("Arial", 12,))
name5.place(x=20, y=180)
name6 = Label(text="Вартість замовлення:", font=("Arial", 12,))
name6.place(x=20, y=240)
name6 = Label(text="грн.", font=("Arial", 12,))
name6.place(x=280, y=240)

lbl7 = Label(text="Добавки до піци, 3 грн", font=("Arial", 12, "bold"))
lbl7.place(x=440, y=20)

var11 = BooleanVar()
ch1 = Checkbutton(text="Майонез", font="Arial 12", variable=var11)
ch1.place(x=440, y=60)
var12 = BooleanVar()
ch2 = Checkbutton(text="Кетчуп", font="Arial 12", variable=var12)
ch2.place(x=440, y=100)
var13 = BooleanVar()
ch3 = Checkbutton(text="Соус", font="Arial 12", variable=var13)
ch3.place(x=440, y=140)
var14 = BooleanVar()
ch4 = Checkbutton(text="Ананаси", font="Arial 12", variable=var14)
ch4.place(x=440, y=180)

tk.mainloop()


