import tkinter
from tkinter import *
calc = Tk()
calc.title("Pixel Calculator")

display = Text(calc,width="80",height="4")
display.grid(row="0",column="0",columnspan=5)
#function
def x():
    display.insert(1.0,"*")
def div():
    display.insert(1.0,"/")
def add():
    display.insert(1.0,"+")
def minus():
    display.insert(1.0,"-")
def clear():
    display.delete(1.0,END)
def one():
    display.insert(1.0,"1")
def two():
    display.insert(1.0,"2")
def three():
    display.insert(1.0,"3")
def four():
    display.insert(1.0,"4")
def five():
    display.insert(1.0,"5")
def six():
    display.insert(1.0,"6")
def seven():
    display.insert(1.0,"7")
def eight():
    display.insert(1.0,"8")
def nine():
    display.insert(1.0,"9")
def zero():
    display.insert(1.0,"0")
def equal():
    fun = display.get(1.0,END)
    global ans
    try:
     ans = str(eval(fun))
     display.delete(1.0,"end")
     display.insert(1.0,ans)
    except:
     ans = ""
     display.delete(1.0,"end")
     display.insert(1.0,">>MATH ERROR")
#row 1
btn = Button(calc,text="X",width="20",height="2",command=x)
btn.grid(row="1",column="1")
btn1 = Button(calc,text="/",width="20",height="2",command=div)
btn1.grid(row="1",column="2")
btn2 = Button(calc,text="+",width="20",height="2",command=add)
btn2.grid(row="1",column="3")
btn3 = Button(calc,text="-",width="20",height="2",command=minus)
btn3.grid(row="1",column="4") 
#row2
btn5 = Button(calc,text="C",width="20",height="2",command=clear)
btn5.grid(row="2",column="1")
btn6 = Button(calc,text="1",width="20",height="2",command=one)
btn6.grid(row="2",column="2")
btn7 = Button(calc,text="2",width="20",height="2",command=two)
btn7.grid(row="2",column="3")
btn8 = Button(calc,text="3",width="20",height="2",command=three)
btn8.grid(row="2",column="4")
#row 3
btn9 = Button(calc,text="4",width="20",height="2",command=four)
btn9.grid(row="3",column="1")
btn10 = Button(calc,text="5",width="20",height="2",command=five)
btn10.grid(row="3",column="2")
btn11 = Button(calc,text="6",width="20",height="2",command=six)
btn11.grid(row="3",column="3")
btn12 = Button(calc,text="7",width="20",height="2",command=seven)
btn12.grid(row="3",column="4")
#row4
btn13 = Button(calc,text="8",width="20",height="2",command=eight)
btn13.grid(row="4",column="1")
btn14 = Button(calc,text="9",width="20",height="2",command=nine)
btn14.grid(row="4",column="2")
btn15 = Button(calc,text="0",width="20",height="2",command=zero)
btn15.grid(row="4",column="3")
btn16 = Button(calc,text="=",width="20",height="2",command=equal)
btn16.grid(row="4",column="3")
calc.mainloop()