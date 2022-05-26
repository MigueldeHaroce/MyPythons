from tkinter import *
#import time

windows = Tk()
windows.geometry("800x500")
windows.title("Perimetro calculator")
label = Label(windows, text="Calculadora de Perimetros 3000", font="Helvelica")
label.pack()
label4 = Label(windows, text="Que quiere calcular? Solo triangulo equilatero",font="Times")
label4.pack()
textEntry = Entry(windows)
textEntry.pack()
label2 = Label(windows)
label2.pack()

def textofbox():
    text20 = textEntry.get()
    label2["text"] = text20
    texto = text20
    if texto == "triangulo":
        label5 = Label(windows, text="Ingrese un lado de su tiangulo equilatero")
        label5.pack()
        textEntry2 = Entry(windows)
        textEntry2.pack()
        def calculator():
            text20 = textEntry2.get()
            texto2 = text20
            text2 = int(float(texto2))
            resultado = text2 * 3
            label6 = Label(windows, text=resultado)
            label6.pack()
        button2 = Button(windows, text="Insertar", command=calculator)
        button2.pack()



button = Button(windows, text="Insertar", command=textofbox)
button.pack()
windows.mainloop()
