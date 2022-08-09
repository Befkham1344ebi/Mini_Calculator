from tkinter import * # pip install tkinter
import pyperclip # pip intall pyperclip


window = Tk()
window.title("Mini Calculator")
window.geometry("345x556")
window.config(bg="#2e495e")
window.resizable(0,0)

def mean():
    entry_s.config(state=NORMAL)
    entry_show_r.config(state=NORMAL)
    entry.config(state=NORMAL)
    entryPOP = entry.get()
    if "+" in entry_show.get():
        try:
            if entry_A.get() == "":
                pass
            else:
                entry.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry_show.insert(END,entryPOP)
                showed = float(entry_A.get()) + float(entry_B.get())
                entry.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_show.delete(0,END)
                entry_show_r.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"FORMAT ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    if "-" in entry_show.get():
        try:
            if entry_A.get() == "":
                pass
            else:
                entry.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry_show.insert(END,entryPOP)
                showed = float(entry_A.get()) - float(entry_B.get())
                entry.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_show.delete(0,END)
                entry_show_r.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"FORMAT ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    if "*" in entry_show.get():
        try:
            if entry_A.get() == "":
                pass
            else:
                entry.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry_show.insert(END,entryPOP)
                showed = float(entry_A.get()) * float(entry_B.get())
                entry.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_show.delete(0,END)
                entry_show_r.delete(0,END)
                entry_show_r.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"FORMAT ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    if "/" in entry_show.get():
            if entry_A.get() == "":
                pass
            else:
                entry.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry_show.insert(END,entryPOP)
                try:
                    showed = float(entry_A.get()) / float(entry_B.get())
                    entry.insert(END,str(showed))
                    entry_s.delete(0,END)
                    entry_s.insert(END,f"answer : {str(showed)}")
                    entry_A.delete(0,END)
                    entry_B.delete(0,END)
                    entry_show.delete(0,END)
                    entry_show_r.delete(0,END)
                    entry_show_r.delete(0,END)
                except:
                    entry.delete(0,END)
                    entry.insert(0,"ERROR")
                    entry_A.delete(0,END)
                    entry_B.delete(0,END)
                    entry_show.delete(0,END)
                    entry_show_r.delete(0,END)
    if "^" in entry_show.get():
        try:
            if entry_A.get() == "":
                pass
            else:
                entry.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry_show.insert(END,entryPOP)
                showed = float(entry_A.get()) ** float(entry_B.get())
                entry.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_show.delete(0,END)
                entry_show_r.delete(0,END)
                entry_show_r.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"FORMAT ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)

def point():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    entryPOP = entry.get()
    if "." in entryPOP:
        pass
    else:
        entry.insert(END,".")
    entry.config(state=DISABLED)

def pop():
    entry_s.config(state=NORMAL)
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    if entry_show.get() == "":
        entry_show.delete(0,END)
        entry_show.insert(0,"^")
        pop()
    elif "^" in entry_show.get(): 
        entryPOP = entry.get()
        entryB = entry_B.get()
        try:
            entry_show.delete(0,END)
            if entry_A.get() == "":
                entry_A.insert(END,entryPOP)
                entry.delete(0,END)
                entry.delete(0,END)
            else:
                entry_B.insert(END,entryPOP)
                entry.delete(0,END)
                showed = float(entry_A.get()) ** float(entry_B.get())
                entry.insert(END,str(showed))
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_A.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
            entry_show.insert(END,"^")
            entry_show_r.insert(END,f"{entryPOP}^{entryB}")
            if entry_show_r.get() == "^":
                entry_show_r.delete(0,END)
                entry_show.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    else:
        mean()
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)
        
def k():
    entry_s.config(state=NORMAL)
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    if entry_show.get() == "":
        entry_show.delete(0,END)
        entry_show.insert(0,"/")
        k()
    elif "/" in entry_show.get(): 
        entryPOP = entry.get()
        entryB = entry_B.get()
        try:
            entry_show.delete(0,END)
            if entry_A.get() == "":
                entry_A.insert(END,entryPOP)
                entry.delete(0,END)
                entry.delete(0,END)
            else:
                entry_B.insert(END,entryPOP)
                entry.delete(0,END)
                showed = float(entry_A.get()) / float(entry_B.get())
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_A.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
            entry_show.insert(END,"/")
            entry_show_r.insert(END,f"{entryPOP}/{entryB}")
            if entry_show_r.get() == "/":
                entry_show_r.delete(0,END)
                entry_show.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    else:
        mean()
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)

def x():
    entry_s.config(state=NORMAL)
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    if entry_show.get() == "":
        entry_show.delete(0,END)
        entry_show.insert(0,"*")
        x()
    elif "*" in entry_show.get(): 
        entryPOP = entry.get()
        entryB = entry_B.get()
        try:
            entry_show.delete(0,END)
            if entry_A.get() == "":
                entry_A.insert(END,entryPOP)
                entry.delete(0,END)
                entry.delete(0,END)
            else:
                entry_B.insert(END,entryPOP)
                entry.delete(0,END)
                showed = float(entry_A.get()) * float(entry_B.get())
                entry.insert(END,str(showed))
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_A.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
            entry_show.insert(END,"*")
            entry_show_r.insert(END,f"{entryPOP}*{entryB}")
            if entry_show_r.get() == "*":
                entry_show_r.delete(0,END)
                entry_show.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    else:
        mean()
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)

def menha():
    entry_s.config(state=NORMAL)
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    if entry_show.get() == "":
        entry_show.delete(0,END)
        entry_show.insert(0,"-")
        menha()
    elif "-" in entry_show.get():
        entry_show.delete(0,END)
        try:
            entryPOP = entry.get()
            entryB = entry_B.get()
            if entry_A.get() == "":
                entry_A.insert(END,entryPOP)
                entry.delete(0,END)
            else:
                entry_B.insert(END,entryPOP)
                entry.delete(0,END)
                showed = float(entry_A.get()) - float(entry_B.get())
                entry.insert(END,str(showed))
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_A.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
            entry_show.insert(END,f"-")
            entry_show_r.insert(END,f"{entryPOP}-{entryB}")
            if entry_show_r.get() == "-":
                entry_show_r.delete(0,END)
                entry_show.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END) 
    else:
        mean()
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)

def plus():
    entry_s.config(state=NORMAL)
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    if entry_show.get() == "":
        entry_show.delete(0,END)
        entry_show.insert(0,"+")
        plus()
    elif "+" in entry_show.get():
        entryPOP = entry.get()
        entryB = entry_B.get()
        entry_show.delete(0,END)
        try:
            if entry_A.get() == "":
                entry_A.insert(END,entryPOP)
                entry.delete(0,END)
            else:
                entry_B.delete(0,END)
                entry_B.insert(END,entryPOP)
                entry.delete(0,END)
                showed = float(entry_A.get()) + float(entry_B.get())
                entry.insert(END,str(showed))
                entry_A.delete(0,END)
                entry_B.delete(0,END)
                entry_A.insert(END,str(showed))
                entry_s.delete(0,END)
                entry_s.insert(END,f"answer : {str(showed)}")
            entry_show.insert(END,f"+")
            entry_show_r.insert(END,f"{entryPOP}+{entryB}")
            if entry_show_r.get() == "+":
                entry_show_r.delete(0,END)
                entry_show.delete(0,END)
        except:
            entry.delete(0,END)
            entry.insert(0,"ERROR")
            entry_A.delete(0,END)
            entry_B.delete(0,END)
            entry_show.delete(0,END)
            entry_show_r.delete(0,END)
    else:
        mean()
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)
    entry_s.config(state=DISABLED)


def zero():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"0")
    entry.config(state=DISABLED)

def one():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"1")
    entry.config(state=DISABLED)
    
def two():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"2")
    entry.config(state=DISABLED)

def three():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"3")
    entry.config(state=DISABLED)

def four():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"4")
    entry.config(state=DISABLED)

def five():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"5")
    entry.config(state=DISABLED)

def six():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"6")
    entry.config(state=DISABLED)

def seven():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"7")
    entry.config(state=DISABLED)

def eight():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"8")
    entry.config(state=DISABLED)

def nine():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    entry.insert(END,"9")
    entry.config(state=DISABLED)

def C():
    entry_show_r .config(state=NORMAL)
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry_A.delete(0,END)
    entry_B.delete(0,END)
    entry_show.delete(0,END)
    entry_show_r.delete(0,END)
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)

def m():
    entry.config(state=NORMAL)
    list_error = ["ERROR","Cannot Divide by Zero"]
    for i in list_error:
        if i in entry.get():
            entry.delete(0,END)
    pop = f"answer : {entry.get()}"
    if  pop == entry_s.get():
        entry.delete(0,END)
    if "-" in entry.get():
        pass
    else:
        entry.insert(0,"-")
    entry.config(state=DISABLED)
def E():
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.config(state=DISABLED)
    entry_show_r .config(state=DISABLED)


blue_1 = Label(window,bg="#3b5b68")
blue_1.place(x=0 , y=0 , width=358 , height=120)

entry = Entry(window , bg="white" , fg="#575656" , font = ("Agency FB",30),justify=RIGHT,state=DISABLED , bd=0)
entry.place(x=15 , y=36 , width =311 , height = 67)

entry_show = Entry(window)

entry_show_r = Entry(window , bg="white" , fg="#575656" , font = ("Agency FB",15),justify=RIGHT,state=DISABLED , bd=0)
entry_show_r.place(x=172 , y=10 , width =154 , height = 25)

entry_A = Entry(window)
entry_B = Entry(window)

entry_s = Entry(window , bg="white" , fg="black" , font = ("Agency FB",15),state=DISABLED , bd=0)
entry_s.place(x=15 , y=10 , width =155.5 , height = 25)

button_p = Button(text=".",bg="#5e7682",font = ("Century Gothic",30) , command=point)
button_p.place(x=95 , y=470 , height=70 , width=70)

button_pl = Button(text="+",bg="#5e7682",font = ("Century Gothic",30) , command=plus)
button_pl.place(x=175 , y=470 , height=70 , width=70)

button_m = Button(text="=",bg="#75bbf1",font = ("Century Gothic",30) , command=mean)
button_m.place(x=255 , y=390 , height=150 , width=70)

button_0 = Button(text="0",bg="#5e7682",font = ("Century Gothic",30) , command=zero)
button_0.place(x=15 , y=470 , height=70 , width=70)

button_1 = Button(text="1",bg="#5e7682",font = ("Century Gothic",30) , command=one)
button_1.place(x=15 , y=390 , height=70 , width=70)

button_2 = Button(text="2",bg="#5e7682",font = ("Century Gothic",30) , command=two)
button_2.place(x=95 , y=390 , height=70 , width=70)

button_3 = Button(text="3",bg="#5e7682",font = ("Century Gothic",30) , command=three)
button_3.place(x=175 , y=390 , height=70 , width=70)

button_4 = Button(text="4",bg="#5e7682",font = ("Century Gothic",30) , command=four)
button_4.place(x=15 , y=310 , height=70 , width=70)

button_5 = Button(text="5",bg="#5e7682",font = ("Century Gothic",30) , command=five)
button_5.place(x=95 , y=310 , height=70 , width=70)

button_6 = Button(text="6",bg="#5e7682",font = ("Century Gothic",30) , command=six)
button_6.place(x=175 , y=310 , height=70 , width=70)

button_7 = Button(text="7",bg="#5e7682",font = ("Century Gothic",30) , command=seven)
button_7.place(x=15 , y=230 , height=70 , width=70)

button_8 = Button(text="8",bg="#5e7682",font = ("Century Gothic",30) , command=eight)
button_8.place(x=95 , y=230 , height=70 , width=70)

button_9 = Button(text="9",bg="#5e7682",font = ("Century Gothic",30) , command=nine)
button_9.place(x=175 , y=230 , height=70 , width=70)

button_x = Button(text="×",bg="#5e7682",font = ("Century Gothic",30) , command=x)
button_x.place(x=255 , y=310 , height=70 , width=70)

button_k = Button(text="÷",bg="#5e7682",font = ("Century Gothic",30) , command=k)
button_k.place(x=255 , y=230 , height=70 , width=70)

button_C_1 = Button(text="C",bg="#ca1c20",font = ("Century Gothic",25) , command=C)
button_C_1.place(x=15 , y=150  , height=70 , width=35)

button_C_2 = Button(text="E",bg="#ca1c20",font = ("Century Gothic",25) , command=E)
button_C_2.place(x=50 , y=150  , height=70 , width=35)

button_B = Button(text="^",bg="#5e7682",font = ("Century Gothic",30) , command=pop)
button_B.place(x=175 , y=150 , height=70 , width=70)

button_m = Button(text="-M",bg="#5e7682",font = ("Century Gothic",20) , command=m)
button_m.place(x=95 , y=150 , height=70 , width=70)

button_quit = Button(text="-",bg="#5e7682",font = ("Century Gothic",20) , command=menha)
button_quit.place(x=255 , y=150 , height=70 , width=70)

_label = Label(window,fg="black", bg="light blue")
copy_ = Label(window,text="Copy" , bg="light blue" , font=("",12))
cut_ = Label(window,text="Cut" , bg="light blue" , font=("",12))
paste_ = Label(window,text="Paste" , bg="light blue" , font=("",12))

def press(event):
    _label.place(x=event.x - 50  , y=event.y+20 , height=100 , width=100)
    copy_.place(x=event.x - 50 +5 , y=event.y+20 + 5  , width=90)
    cut_.place(x=event.x - 50 +5 , y=event.y+20 + 5 + 30  , width=90)
    paste_.place(x=event.x - 50 +5 , y=event.y+20 + 5 + 60  , width=90)
def copy(event):
    _label.place_forget()
    copy_.place_forget()
    cut_.place_forget()
    paste_.place_forget()
    pyperclip.copy(entry.get())
def cut(event):
    _label.place_forget()
    copy_.place_forget()
    cut_.place_forget()
    paste_.place_forget()
    pyperclip.copy(entry.get())
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.config(state=DISABLED)
def paste(event):
    _label.place_forget()
    copy_.place_forget()
    cut_.place_forget()
    paste_.place_forget()
    entry.config(state=NORMAL)
    try:
        entry.delete(0,END)
        pasteIT = float(pyperclip.paste())
        entry.insert(0,pasteIT)
    except:
        pass
    entry.config(state=DISABLED)
def hide(event):
    _label.place_forget()
    copy_.place_forget()
    cut_.place_forget()
    paste_.place_forget()

entry.bind("<ButtonPress-3>",press)
copy_.bind("<ButtonPress-1>",copy)
cut_.bind("<ButtonPress-1>",cut)
paste_.bind("<ButtonPress-1>",paste)
window.bind("<ButtonPress-1>" , hide)
def showchar(event):
    entry.config(state=NORMAL)
    try:
        char = int(event.keysym)
        list_error = ["ERROR","Cannot Divide by Zero"]
        for b in list_error:
            if b in entry.get():
                entry.delete(0,END)
        pop = f"answer : {entry.get()}"
        if  pop == entry_s.get():
            entry.delete(0,END)
        entry.insert(END,char)
    except:
        pass
    pop = []
    char_1 = event.keysym
    pop.append(char_1)
    for i in pop:
        if "plus" in i:
            plus()
        if "asterisk" in i:
            x()
        if "slash" in i:
            k()
        if "period" in i:
            point()
        if "m" in i.lower():
            m()
        ppp = ["Return","equal"]
        for p in ppp:
            if p in i:
                mean()
        if "Escape" in i:
            C()
        if "underscore" in i:
            menha()
        if "BackSpace" in i:
            num = len(entry.get())
            entry.delete(num - 1 , END)

    entry.config(state=DISABLED)
window.bind("<Key>",showchar)
def enter_copy_E(event):
    copy_.config(bg="blue")
def enter_copy_L(event):
    copy_.config(bg="light blue")
copy_.bind("<Enter>" , enter_copy_E)
copy_.bind("<Leave>" , enter_copy_L)
#---------------------------------------------#
def enter_cut_E(event):
    cut_.config(bg="blue")
def enter_cut_L(event):
    cut_.config(bg="light blue")
cut_.bind("<Enter>" , enter_cut_E)
cut_.bind("<Leave>" , enter_cut_L)
#---------------------------------------------#
def enter_paste_E(event):
    paste_.config(bg="blue")
def enter_paste_L(event):
    paste_.config(bg="light blue")
paste_.bind("<Enter>" , enter_paste_E)
paste_.bind("<Leave>" , enter_paste_L)

window.mainloop()
