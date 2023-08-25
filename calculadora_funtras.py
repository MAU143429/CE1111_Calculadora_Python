import tkinter as tk
from tkinter import *


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora FunTras")
        self.geometry("400x700")
        self.iconphoto(True, tk.PhotoImage(file="assets/logo.png"))
        self.config(bg="#1CAC91")
        self.resizable(False, False)

        self.frames = {}  # Diccionario para almacenar los marcos

        for F in (MainFrame, CalculatorFrame):
            frame = F(self)
            self.frames[F] = frame
            # Asegurarse de que los marcos ocupen todo el espacio
            frame.place(relwidth=1, relheight=1)
            frame.grid_forget()  # Ocultar todos los marcos al inicio

        self.show_frame(MainFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1CAC91")

        self.strimg = tk.PhotoImage(file="assets/strbtn.png")
        self.logo = tk.PhotoImage(file="assets/logo.png")
        tk.Label(self, image=self.logo, background="#1CAC91").pack()

        tk.Label(self, text="Welcome to", font=(
            "Berlin Sans FB", 30), bg="#1CAC91").pack()
        tk.Label(self, text="FunTras Calculator!", font=(
            "Berlin Sans FB", 30), bg="#1CAC91").pack()

        tk.Button(self, image=self.strimg, width=220, height=60, background="#1CAC91", borderwidth=0,
                  command=lambda: parent.show_frame(CalculatorFrame)).pack(pady=50)


class CalculatorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1CAC91")

        self.exit = tk.PhotoImage(file="assets/exit.png")
        self.info = tk.PhotoImage(file="assets/info.png")
        self.title = tk.PhotoImage(file="assets/title.png")

        # Crear los widgets en el grid
        tk.Button(self, image=self.info, width=40, height=40, background="#1CAC91", borderwidth=0, command=self.displayInfo).grid(
            row=0, column=0, sticky=tk.W, pady=30, padx=20)
        tk.Label(self, image=self.title, height=40, width=100, font=("Berlin Sans FB", 15)).grid(
            row=0, column=1, sticky=tk.W, pady=7)
        tk.Button(self, image=self.exit, width=100, height=20, background="#1CAC91",  borderwidth=0, command=parent.destroy).grid(
            row=0, column=2, sticky=tk.W, pady=7, padx=7)
        tk.Label(self, text="X =", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=1, column=0, sticky=tk.W, pady=7, padx=7)
        x_entry = tk.Entry(self, width=17)
        x_entry.grid(row=1, column=1, sticky=tk.W, pady=7, padx=7)
        tk.Label(self, text="Y =", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=2, column=0, sticky=tk.W, pady=7, padx=7)
        y_entry = tk.Entry(self, width=17)
        y_entry.grid(row=2, column=1, sticky=tk.W, pady=7, padx=7)

        tk.Label(self, text="Answer = ", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=3, column=0, sticky=tk.W, pady=20, padx=7)
        tk.Label(self, text="Answer Here!", font=("Berlin Sans FB", 10), width=14, height=1, background="#1CAC91").grid(
            row=3, column=1, sticky=tk.W, pady=7, padx=7)

        tk.Button(self, text="senh(x)", width=13, height=1).grid(
            row=6, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="cosh(x)", width=13, height=1).grid(
            row=6, column=1, sticky=W, pady=2, padx=10,)
        tk.Button(self, text="tanh(x)", width=13, height=1).grid(
            row=6, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="asen(x)", width=13, height=1).grid(
            row=7, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="acos(x)", width=13, height=1).grid(
            row=7, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="atan(x)", width=13, height=1).grid(
            row=7, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="sec(x)", width=13, height=1).grid(
            row=8, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="csc(x)", width=13, height=1).grid(
            row=8, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="cot(x)", width=13, height=1).grid(
            row=8, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="sen(x)", width=13, height=1).grid(
            row=9, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="cos(x)", width=13, height=1).grid(
            row=9, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="tan(x)", width=13, height=1).grid(
            row=9, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="ln(x)", width=13, height=1).grid(
            row=10, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="log13(x)", width=13, height=1).grid(
            row=10, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="loga(x)", width=13, height=1).grid(
            row=10, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="1/x(x)", width=13, height=1).grid(
            row=11, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="sqrt(x)", width=13, height=1).grid(
            row=11, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="n_sqrt(x)", width=13, height=1).grid(
            row=11, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="exp(x)", width=13, height=1).grid(
            row=12, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="x^y", width=13, height=1).grid(
            row=12, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="x!", width=13, height=1).grid(
            row=12, column=2, sticky=W, pady=2, padx=10)

        tk.Button(self, text="7", width=13, height=2).grid(
            row=13, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="8", width=13, height=2).grid(
            row=13, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="9", width=13, height=2).grid(
            row=13, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="4", width=13, height=2).grid(
            row=14, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="5", width=13, height=2).grid(
            row=14, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="6", width=13, height=2).grid(
            row=14, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="1", width=13, height=2).grid(
            row=15, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="2", width=13, height=2).grid(
            row=15, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="3", width=13, height=2).grid(
            row=15, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="π", width=13, height=2).grid(
            row=16, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="0", width=13, height=2).grid(
            row=16, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text=".", width=13, height=2).grid(
            row=16, column=2, sticky=W, pady=10, padx=10)

    def displayInfo(self):
        infoScreen = tk.Toplevel(self)
        infoScreen.title("Calculadora FunTras")
        infoScreen.geometry("400x700")
        infoScreen.iconphoto(True, icon)
        infoScreen.config(bg="#1CAC91")
        infoScreen.resizable(False, False)
        screen_width = infoScreen.winfo_screenwidth()
        screen_height = infoScreen.winfo_screenheight()
        x = (screen_width/2) - (400/2)
        y = (screen_height/2) - (700/2)
        infoScreen.geometry('%dx%d+%d+%d' % (400, 700, x, y))


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
