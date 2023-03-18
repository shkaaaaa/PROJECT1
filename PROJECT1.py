import tkinter
from tkinter import *
import math


# for creating main window
window = Tk()
window.title("CALCULATOR")
window.geometry('285x420+700+200')
window.resizable(False, False)
window.config(bg="#BDCDD6")

# creating button frame
button_frame = Frame(window, bg="#62CDFF", width=285, height=197)
button_frame.place(relx=0.629, rely=0.71, anchor=CENTER)

# creating screen

screen = LabelFrame(window, border=3, bg="white", width=250, height=100)
screen.place(relx=0.5, rely=0.25, anchor=CENTER)
# screen_name=LabelFrame(window,text="Screen")
# screen_name.place(relx=0.5, rely=0.25, anchor=CENTER)


# screen label
eq_label = Label(screen, text=f"{0}", bg='white', font=('times of roman', 50))
eq_label.place(relx=0.5, rely=0.5, anchor=CENTER)
ex_label = Label(
    window, text=f"backend-> {0}", bg='white', font=('times of roman', 10))
ex_label.place(relx=0.5, rely=0.075, anchor=CENTER)

# def press():
#     pass
# def add():
#     pass
# def sub():
#     pass
# def mul():
#     pass
# def div():
#     pass


# Expression
expression = ""
equation = ""

# set size of expression in label // exceptional if size is bigger font gets smaller


def font_size():
    if len(expression) < 8:
        eq_label.config(font=('times of roman', 50))
    elif len(expression) < 15:
        eq_label.config(font=('times of roman', 25))
    else:
        eq_label.config(font=('times of roman', 12))


# appending in global expression
def press(num):
    global expression
    global equation
    global last_pressed
    expression = expression + str(num)
    equation = equation+str(num)
    eq_label.config(text=f"{expression}")
    ex_label.config(text=f"backend-> {equation}")
    font_size()
    if last_pressed == 'sq':
        equation = equation+'**2'
    last_pressed = ""


# solving equation got from expression
def solve():
    global expression
    global equation
    global last_pressed
    try:

        total = str(eval(equation))
        equation = total
        expression = total
        eq_label.config(text=f"{total}")
        ex_label.config(text=f"backend-> {equation}")
        font_size()
    except:
        expression = ""
        equation = expression
        eq_label.config(text=f"ERROR")
    last_pressed = ""


# clear the screen, equation, expression
def cut():
    global expression
    global equation
    expression = ""
    equation = ""
    font_size()
    eq_label.config(text=f"{0}")
    ex_label.config(text=f"backend-> {equation}")

# backspace by decreasing size of expression by one from last


last_pressed = ""


def back_space():
    global expression
    global equation
    global last_pressed

    font_size()
    ex_len = len(expression)
    eq_len = len(equation)

    if ex_len <= 1:
        eq_label.config(text=f"{0}")
        equation = ""
        ex_label.config(text=f"backend-> {equation}")

    if last_pressed == "":
        equation = equation[:eq_len-1]
        expression = expression[:ex_len-1]
        last_pressed = ""

    elif last_pressed == "sin":
        equation = equation[:eq_len-23]
        expression = expression[:ex_len-4]
        last_pressed = ""

    elif last_pressed == "cos":
        equation = equation[:eq_len-23]
        expression = expression[:ex_len-4]
        last_pressed = ""

    elif last_pressed == "tan":
        equation = equation[:eq_len-23]
        expression = expression[:ex_len-4]
        last_pressed = ""

    elif last_pressed == "log":
        equation = equation[:eq_len-11]
        expression = expression[:ex_len-4]
        last_pressed = ""

    elif last_pressed == "sq":
        equation = equation[:eq_len-3]
        expression = expression[:ex_len-3]
        last_pressed = ""

    elif last_pressed == "sqr":
        equation = equation[:eq_len-10]
        expression = expression[:ex_len-4]
        last_pressed = ""

    eq_label.config(text=f"{expression}")
    ex_label.config(text=f"backend-> {equation}")


def advance():
    window.title("ADVANCE CALCULATOR")
    window.geometry('350x420+700+200')
    screen.config(width=300)
    button_frame.place(relx=0.5, rely=0.71, anchor=CENTER)
    key_adv.config(text='close adv', command=advance_close)


def advance_close():
    window.title("Strange's Calculator")
    window.geometry('285x420+700+200')
    screen.config(width=250)
    button_frame.place(relx=0.629, rely=0.71, anchor=CENTER)
    key_adv.config(text='open adv', command=advance)


def trig(sign):
    global expression
    global equation
    global last_pressed
    try:
        if sign == "sin":
            # converting rad to degree
            equation = equation+'math.sin(0.01745329251*'
            expression = expression+"sin("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "sin"
        elif sign == "cos":
            equation = equation+'math.cos(0.01745329251*'
            expression = expression+"cos("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "cos"
        elif sign == "tan":
            equation = equation+'math.tan(0.01745329251*'
            expression = expression+"tan("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "tan"
        elif sign == "log":
            equation = equation+'math.log10('
            expression = expression+"log("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "log"

        elif sign == "sq":
            equation = equation+'('
            expression = expression+"sq("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "sq"
        elif sign == "sqr":
            equation = equation+'math.sqrt('
            expression = expression+"sqrt("
            eq_label.config(text=expression)
            ex_label.config(text=f"backend-> {equation}")
            last_pressed = "sqr"

    except:
        expression = ""
        eq_label.config(text=f"ERROR")
        ex_label.config(text=f"backend-> {equation}")

# creating Key Buttons


key_bracket_open = Button(button_frame, bg='#7B8FA1', border=2, text="(", width=9,
                          height=2, command=lambda: press('('))
key_bracket_open.grid(row=0, column=0)

key_bracket_close = Button(button_frame, bg='#7B8FA1', border=2, text=")", width=9,
                           height=2, command=lambda: press(')'))
key_bracket_close.grid(row=0, column=1)

key_adv = Button(button_frame, bg='#7B8FA1', border=2, text="open adv", width=9,
                 height=2, command=advance)
key_adv.grid(row=0, column=2)

key_bc = Button(button_frame, bg='#7B8FA1', border=2, text="<", width=9,
                height=2, command=back_space)
key_bc.grid(row=0, column=3)

key_sin = Button(button_frame, bg='#7B8FA1', border=2, text="sin", width=9,
                 height=2, command=lambda: trig('sin'))
key_sin.grid(row=0, column=4)

key1 = Button(button_frame, bg='#7B8FA1', border=2, text="1", width=9,
              height=2, command=lambda: press(1))
key1.grid(row=1, column=0)

key2 = Button(button_frame, bg='#7B8FA1', border=2, text="2", width=9,
              height=2, command=lambda: press(2))
key2.grid(row=1, column=1)

key3 = Button(button_frame, bg='#7B8FA1', border=2, text="3", width=9,
              height=2, command=lambda: press(3))
key3.grid(row=1, column=2)

key_add = Button(button_frame, bg='#7B8FA1', border=2, text="+", width=9,
                 height=2, command=lambda: press('+'))
key_add.grid(row=1, column=3)

key_cos = Button(button_frame, bg='#7B8FA1', border=2, text="cos", width=9,
                 height=2, command=lambda: trig('cos'))
key_cos.grid(row=1, column=4)

key4 = Button(button_frame, bg='#7B8FA1', border=2, text="4", width=9,
              height=2, command=lambda: press(4))
key4.grid(row=2, column=0)

key5 = Button(button_frame, bg='#7B8FA1', border=2, text="5", width=9,
              height=2, command=lambda: press(5))
key5.grid(row=2, column=1)

key6 = Button(button_frame, bg='#7B8FA1', border=2, text="6", width=9,
              height=2, command=lambda: press(6))
key6.grid(row=2, column=2)

key_sub = Button(button_frame, bg='#7B8FA1', border=2, text="-", width=9,
                 height=2, command=lambda: press('-'))
key_sub.grid(row=2, column=3)

key_tan = Button(button_frame, bg='#7B8FA1', border=2, text="tan", width=9,
                 height=2, command=lambda: trig('tan'))
key_tan.grid(row=2, column=4)

key7 = Button(button_frame, bg='#7B8FA1', border=2, text="7", width=9,
              height=2, command=lambda: press(7))
key7.grid(row=3, column=0)

key8 = Button(button_frame, bg='#7B8FA1', border=2, text="8", width=9,
              height=2, command=lambda: press(8))
key8.grid(row=3, column=1)

key9 = Button(button_frame, bg='#7B8FA1', border=2, text="9", width=9,
              height=2, command=lambda: press(9))
key9.grid(row=3, column=2)

key_mul = Button(button_frame, bg='#7B8FA1', border=2, text="x", width=9,
                 height=2, command=lambda: press('*'))
key_mul.grid(row=3, column=3)

key_root = Button(button_frame, bg='#7B8FA1', border=2, text="root", width=9,
                  height=2, command=lambda: trig('sqr'))
key_root.grid(row=3, column=4)

key_cut = Button(button_frame, bg='#7B8FA1', border=2,
                 text="Clear", width=9, height=2, command=cut)
key_cut.grid(row=4, column=0)

key0 = Button(button_frame, bg='#7B8FA1', border=2, text="0", width=9,
              height=2, command=lambda: press(0))
key0.grid(row=4, column=1)

key_dec = Button(button_frame, bg='#7B8FA1', border=2, text=".",
                 width=9, height=2, command=lambda: press('.'))
key_dec.grid(row=4, column=2)

key_div = Button(button_frame, bg='#7B8FA1', border=2, text="/", width=9,
                 height=2, command=lambda: press('/'))
key_div.grid(row=4, column=3)

key_square = Button(button_frame, bg='#7B8FA1', border=2, text="square", width=9,
                    height=2, command=lambda: trig('sq'))
key_square.grid(row=4, column=4)

key_equal = Button(button_frame, bg='#7B8FA1', border=2, text="=", width=40,
                   height=2, command=solve)
key_equal.grid(row=5, column=0, columnspan=4)

key_log = Button(button_frame, bg='#7B8FA1', border=2, text="log", width=9,
                 height=2, command=lambda: trig('log'))
key_log.grid(row=5, column=4)

window.mainloop()
