from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Simple Calculator")
#root.iconbitmap("Dakirby309-Windows-8-Metro-Apps-Calculator-Metro.ico")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, str(f_num + int(second_number)))

    if math == "subtraction":
        e.insert(0, str(f_num - int(second_number)))

    if math == "multiplication":
        e.insert(0, str(f_num * int(second_number)))

    if math == "division":
        e.insert(0, str(f_num / int(second_number)))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#photo_plus = ImageTk.PhotoImage(Image.open("plus.png"))

photo_equal = ImageTk.PhotoImage(Image.open("equal.png"))

photo_mult = ImageTk.PhotoImage(Image.open("close.png"))

photo_minus = ImageTk.PhotoImage(Image.open("minus.png"))

photo_div = ImageTk.PhotoImage(Image.open("divide.png"))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4",font="Helvelatica", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", command=button_add, borderwidth=1, bg="grey")
button_equal = Button(root, image=photo_equal, command=button_equal, borderwidth=1, bg="grey")
button_clear = Button(root, text="A/C", padx=35, pady=20, command=button_clear)

button_subtract = Button(root, image=photo_minus, command=button_subtract, borderwidth=1, bg="grey")
button_multiply = Button(root, image=photo_mult, command=button_multiply, borderwidth=1, bg="grey")
button_divide = Button(root, image=photo_div, command=button_divide, borderwidth=1, bg="grey")

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=1, column=4)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)

root.mainloop()
