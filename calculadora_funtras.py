import tkinter as tk
from tkinter import *

# Función para mostrar la segunda ventana


def initCalculator():

    calculatorScreen = tk.Toplevel(mainScreen)
    calculatorScreen.title("Calculadora FunTras")
    calculatorScreen.geometry("400x700")
    calculatorScreen.iconphoto(True, icon)
    calculatorScreen.config(bg="#1CAC91")
    screen_width = calculatorScreen.winfo_screenwidth()
    screen_height = calculatorScreen.winfo_screenheight()
    x = (screen_width/2) - (400/2)
    y = (screen_height/2) - (700/2)
    calculatorScreen.geometry('%dx%d+%d+%d' % (400, 700, x, y))

    # Se inicializa la botonera
    tk.Button(calculatorScreen, image=help, width=40, height=40, background="#1CAC91", borderwidth=0).grid(
        row=0, column=0, sticky=W, pady=7, padx=20)
    tk.Label(calculatorScreen, text="FunTras Calculator", height=3, width=10, background="#1CAC91", font=("Berlin Sans FB", 15)).grid(
        row=0, column=1, sticky=W, pady=7)
    tk.Button(calculatorScreen, image=exit, width=40, height=40, background="#1CAC91", borderwidth=0, command=calculatorScreen.destroy).grid(
        row=0, column=2, sticky=W, pady=7, padx=7)
    tk.Label(calculatorScreen, text="x = ", width=13, height=1, background="#1CAC91").grid(
        row=1, column=0, sticky=W, pady=7, padx=7)
    x = tk.Entry(calculatorScreen, text="Enter a value...", width=17).grid(
        row=1, column=1, sticky=W, pady=7, padx=7)
    tk.Label(calculatorScreen,  text="y = ", width=13, height=1, background="#1CAC91").grid(
        row=2, column=0, sticky=W, pady=7, padx=7)
    y = tk.Entry(calculatorScreen, text="Enter a value...", width=17).grid(
        row=2, column=1, sticky=W, pady=7, padx=7)
    tk.Label(calculatorScreen, text="Answer = ", width=13, height=1, background="#1CAC91").grid(
        row=3, column=0, sticky=W, pady=7, padx=7)
    tk.Label(calculatorScreen, text="Answer Here!", width=14, height=1, background="#1CAC91").grid(
        row=3, column=1, sticky=W, pady=7, padx=7)

    tk.Button(calculatorScreen, text="senh(x)", width=13, height=1).grid(
        row=6, column=0, sticky=W, pady=2, padx=20)
    cosh = tk.Button(calculatorScreen, text="cosh(x)", width=13, height=1).grid(
        row=6, column=1, sticky=W, pady=2, padx=10,)
    tk.Button(calculatorScreen, text="tanh(x)", width=13, height=1).grid(
        row=6, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="asen(x)", width=13, height=1).grid(
        row=7, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="acos(x)", width=13, height=1).grid(
        row=7, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="atan(x)", width=13, height=1).grid(
        row=7, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="sec(x)", width=13, height=1).grid(
        row=8, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="csc(x)", width=13, height=1).grid(
        row=8, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="cot(x)", width=13, height=1).grid(
        row=8, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="sen(x)", width=13, height=1).grid(
        row=9, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="cos(x)", width=13, height=1).grid(
        row=9, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="tan(x)", width=13, height=1).grid(
        row=9, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="ln(x)", width=13, height=1).grid(
        row=10, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="log13(x)", width=13, height=1).grid(
        row=10, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="loga(x)", width=13, height=1).grid(
        row=10, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="1/x(x)", width=13, height=1).grid(
        row=11, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="sqrt(x)", width=13, height=1).grid(
        row=11, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="n_sqrt(x)", width=13, height=1).grid(
        row=11, column=2, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="exp(x)", width=13, height=1).grid(
        row=12, column=0, sticky=W, pady=2, padx=20)
    tk.Button(calculatorScreen, text="x^y", width=13, height=1).grid(
        row=12, column=1, sticky=W, pady=2, padx=10)
    tk.Button(calculatorScreen, text="x!", width=13, height=1).grid(
        row=12, column=2, sticky=W, pady=2, padx=10)

    tk.Button(calculatorScreen, text="7", width=13, height=2).grid(
        row=13, column=0, sticky=W, pady=10, padx=20)
    tk.Button(calculatorScreen, text="8", width=13, height=2).grid(
        row=13, column=1, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="9", width=13, height=2).grid(
        row=13, column=2, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="4", width=13, height=2).grid(
        row=14, column=0, sticky=W, pady=10, padx=20)
    tk.Button(calculatorScreen, text="5", width=13, height=2).grid(
        row=14, column=1, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="6", width=13, height=2).grid(
        row=14, column=2, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="1", width=13, height=2).grid(
        row=15, column=0, sticky=W, pady=10, padx=20)
    tk.Button(calculatorScreen, text="2", width=13, height=2).grid(
        row=15, column=1, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="3", width=13, height=2).grid(
        row=15, column=2, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text="π", width=13, height=2).grid(
        row=16, column=0, sticky=W, pady=10, padx=20)
    tk.Button(calculatorScreen, text="0", width=13, height=2).grid(
        row=16, column=1, sticky=W, pady=10, padx=10)
    tk.Button(calculatorScreen, text=".", width=13, height=2).grid(
        row=16, column=2, sticky=W, pady=10, padx=10)


# Configuración de la ventana principal
mainScreen = tk.Tk()
mainScreen.title("Calculadora FunTras")
mainScreen.geometry("400x700")
icon = tk.PhotoImage(file="assets/logo.png")
strimg = tk.PhotoImage(file="assets/strbtn.png")
help = tk.PhotoImage(file="assets/info.png")
exit = tk.PhotoImage(file="assets/exit.png")
mainScreen.iconphoto(True, icon)
screen_width = mainScreen.winfo_screenwidth()  # Width of the screen
screen_height = mainScreen.winfo_screenheight()  # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (400/2)
y = (screen_height/2) - (700/2)
mainScreen.geometry('%dx%d+%d+%d' % (400, 700, x, y))
mainScreen.config(bg="#1CAC91")


# Etiqueta y botón en la ventana principal
tk.Label(mainScreen, image=icon, background="#1CAC91").pack()
tk.Label(mainScreen, text="Welcome to", font=(
    "Berlin Sans FB", 30), background="#1CAC91").pack()
tk.Label(mainScreen, text="FunTras Calculator!", font=(
    "Berlin Sans FB", 30), background="#1CAC91").pack()
tk.Button(mainScreen, image=strimg,  width=220, height=60, pady=10, background="#1CAC91", borderwidth=0,
          command=initCalculator).pack(pady=50)

# Iniciar el bucle principal de la GUI
mainScreen.mainloop()
