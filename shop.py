from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.state("zoomed")
root.title("bill slip")
root.geometry('1280x720')
bg_color='#4D0039'

# Variables
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))

global l
l=[]

# Functions

def additm():
    try:
        n=Rate.get()
        m=quantity.get()*n
        l.append(m)
    except TclError:
        messagebox.showerror('Error','Enter Valid Values')
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please enter item')
def gbill():
    if len(c_name.get())<3 or len(c_phone.get())<10:
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n=====================================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n=====================================================")
        save_bill()
def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    F2.place_forget()
    F3.place_forget()
    getBill.config(state=NORMAL)
    cname_txt.config(state=NORMAL)
    cphone_txt.config(state=NORMAL)
def exitProgram():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
def save_bill():
    op=messagebox.askyesno("Save bill","Do you want to save the Bill?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill No. : {bill_no.get()} Saved Successfully")
    else:
        return
def welcome():
    if len(c_name.get())<3 or len(c_phone.get())<10:
        messagebox.showerror("Error", "Enter Valid Details")
        return -1
    try:
        temp=int(c_phone.get())
    except :
        messagebox.showerror("Error", "Enter Valid Details")
        return -1
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t  Welcome to Sri Anantha Sarees")
    textarea.insert(END,f"\n\nBill Number:\t\t\t{bill_no.get()}")
    textarea.insert(END,f"\nCustomer Name:\t\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n=====================================================")
    textarea.insert(END,"\nProduct\t\t\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n=====================================================\n")
    textarea.configure(font='arial 10 bold')
def fullScreen():
    root.attributes("-fullscreen", True)
    windowMenu.entryconfigure(0, label="Exit Full Screen", command=exitFullSCreen)
def exitFullSCreen():
    root.attributes("-fullscreen", False)
    windowMenu.entryconfigure(0, label="Full Screen", command=fullScreen)
def aboutF():
    win = Toplevel()
    win.title("About")
    about = "Made by Sai Krishna Using Python Tkinter"
    Label(win, text=about, width=100, height=10).pack()
    Button(win, text='OK', command=win.destroy).pack()
def showFrames():
    w=welcome()
    if w==-1:
        return
    F2.place(x=20, y=170,width=550,height=500)
    F3.place(x=570,y=170,width=455,height=500)
    getBill.config(state=DISABLED)
    cname_txt.config(state=DISABLED)
    cphone_txt.config(state=DISABLED)

title=Label(root,pady=2,text="Billing Software",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

# Menu Bar
menubar = Menu(root)

windowMenu = Menu(menubar, tearoff=0)
windowMenu.add_command(label="Full Screen", command=fullScreen)
windowMenu.add_separator()
windowMenu.add_command(label="Exit", command=exitProgram)

helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Help Topics")
helpMenu.add_separator()
helpMenu.add_command(label="About", command=aboutF)

menubar.add_cascade(label="Window", menu=windowMenu)
menubar.add_cascade(label="Help", menu=helpMenu)

#Product Frames
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bg=bg_color,pady=5)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new roman',14,'bold'),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt=Entry(F1,width=20,textvariable=c_name,font='arial 12 bold',relief=SUNKEN,bd=3)
cname_txt.grid(row=0,column=1,padx=10,pady=5,ipadx=3,ipady=3)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new roman',14,'bold'),bg=bg_color,fg='white')
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)
cphone_txt=Entry(F1,width=20,font='arial 12 bold',textvariable=c_phone,relief=SUNKEN,bd=3)
cphone_txt.grid(row=0,column=3,padx=10,pady=5,ipadx=3,ipady=3)

getBill=Button(F1,text='Get Bill',font='arial 12 bold',command=showFrames,padx=5,pady=3,bg='lime',width=15)
getBill.grid(row=0,column=5,padx=10,pady=5)

# Product Details
F2 = LabelFrame(root, text='Product Details', font=('times new roman', 14, 'bold'), fg='gold',bg=bg_color)
F2.pack_forget()

itm=Label(F2, text='Product Name', font=('times new roman',14, 'bold'), bg=bg_color, fg='lightgreen')
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt=Entry(F2, width=20,textvariable=item, font='arial 10 bold', relief=SUNKEN, bd=3)
itm_txt.grid(row=0, column=1, padx=10,pady=20,ipadx=3,ipady=3)

rate=Label(F2, text='Product Rate', font=('times new roman',14, 'bold'), bg=bg_color, fg='lightgreen')
rate.grid(row=1, column=0, padx=30, pady=20)
rate_txt=Entry(F2, width=20,textvariable=Rate, font='arial 10 bold', relief=SUNKEN, bd=3)
rate_txt.grid(row=1, column=1, padx=10,pady=20,ipadx=3,ipady=3)

n=Label(F2, text='Product Quantity', font=('times new roman',14, 'bold'), bg=bg_color, fg='lightgreen')
n.grid(row=2, column=0, padx=30, pady=20)
n_txt=Entry(F2, width=20,textvariable=quantity, font='arial 10 bold', relief=SUNKEN, bd=3)
n_txt.grid(row=2, column=1, padx=10,pady=20,ipadx=3,ipady=3)

# Bill Area
F3=Frame(root,relief=GROOVE,bd=5)
F3.place_forget()

bill_title=Label(F3,text='Bill Area',font='arial 10 bold',bd=3,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

#Buttons
btn1=Button(F2,text='Add item',font='arial 12 bold',command=additm,padx=5,pady=5,bg='lime',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate Bill',font='arial 12 bold',command=gbill,padx=5,pady=5,bg='lime',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 12 bold',padx=5,pady=5,command=clear,bg='lime',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 12 bold',padx=5,pady=5,command=exitProgram,bg='lime',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

root.config(menu=menubar)
root.mainloop()