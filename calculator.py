from tkinter import *

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnclear():
    global val
    val=""
    data.set("")
def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("calculator")
root.geometry("600x600+500+200")
data=StringVar()
val=""


#root.resizable(False,False)
display=Entry(root,bd=15,textvariable=data,bg="powder blue",justify="right",font=("ariel ",20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('+'))
btn_add.grid(row=1,column=3)
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('-'))
btn_sub.grid(row=2,column=3)
btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(3))
btn3.grid(row=3,column=2)
btn_pro=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('*'))
btn_pro.grid(row=3,column=3)
btn_c=Button(root,text="c",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btn_c.grid(row=4,column=0)
btn_0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(0))
btn_0.grid(row=4,column=1)
btn_div=Button(root,text="÷",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('/'))
btn_div.grid(row=4,column=2)
btn_equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEqual)
btn_equal.grid(row=4,column=3)
root.mainloop()
