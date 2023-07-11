import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x505+500+200")
root.resizable(False,False)
root.configure(bg='#17161b')

equation = ""

def show(value):
    global equation
    equation+=value
    lable_result.config(text=equation)

def clear():
    global equation
    equation = ""
    lable_result.config(text=equation)
    
def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    lable_result.config(text=result)
    
    
lable_result= Label(root, width=52, height=2, text ="", font=("arial",20))
lable_result.pack()

Button(root, text="C", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#3697f5", command=lambda: clear()).place(x=5, y=80)
Button(root, text="/", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("/")).place(x=95, y=80)
Button(root, text="%", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("%")).place(x=185, y=80)
Button(root, text="*", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("*")).place(x=275, y=80)

Button(root, text="7", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("7")).place(x=5, y=165)
Button(root, text="8", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("8")).place(x=95, y=165)
Button(root, text="9", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("9")).place(x=185, y=165)
Button(root, text="-", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("-")).place(x=275, y=165)

Button(root, text="4", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("4")).place(x=5, y=250)
Button(root, text="5", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("5")).place(x=95, y=250)
Button(root, text="6", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("6")).place(x=185, y=250)
Button(root, text="+", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("+")).place(x=275, y=250)

Button(root, text="1", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("1")).place(x=5, y=335)
Button(root, text="2", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("2")).place(x=95, y=335)
Button(root, text="3", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("3")).place(x=185, y=335)
Button(root, text="0", width=7, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show("0")).place(x=5, y=420)

Button(root, text=".", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: show(".")).place(x=185, y=420)
Button(root, text="=", width=3, height=2, font=("arial",30,"bold"), bd=1,fg="#ffffff", bg="#2a2d36", command=lambda: calculate()).place(x=275, y=335)

root.mainloop()