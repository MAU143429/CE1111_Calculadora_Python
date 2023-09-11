import tkinter as tk
import funtrans as ftrs
from tkinter import *
import sys
import os

'''
Este método permite crear una ruta predeterminada para el acceso de los 
recursos gráficos de la aplicación.
'''
def getAssetsPath(filename):
    # Obtener la ruta del ejecutable
    exe_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(exe_dir, 'assets', filename)

'''
Esta clase contiene la aplicación Funtras Calculator
'''
class CalculatorApp(tk.Tk):
    
    '''
    Método iniciador de la clase, permite crear las ventana inicial y sus recursos.
    '''
    def __init__(self):
        super().__init__()
        self.title("Calculadora FunTras")
        self.geometry("400x700")
        self.iconphoto(True, tk.PhotoImage(file=getAssetsPath("logo.png")))
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
        
        
    '''
    Método show_frame que permite llamar alternar frames de la ventana principal
    '''
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

'''
Esta clase contiene el frame principal de la aplicación Funtras Calculator
'''
class MainFrame(tk.Frame):
    
    '''
    Método iniciador de la clase MainFrame.
    '''
    def __init__(self, parent):
        super().__init__(parent, bg="#1CAC91")

        self.strimg = tk.PhotoImage(file=getAssetsPath("strbtn.png"))
        self.logo = tk.PhotoImage(file=getAssetsPath("logo.png"))
        tk.Label(self, image=self.logo, background="#1CAC91").pack()

        tk.Label(self, text="Welcome to", font=(
            "Berlin Sans FB", 30), bg="#1CAC91").pack()
        tk.Label(self, text="FunTras Calculator!", font=(
            "Berlin Sans FB", 30), bg="#1CAC91").pack()

        tk.Button(self, image=self.strimg, width=220, height=60, background="#1CAC91", borderwidth=0,
                  command=lambda: parent.show_frame(CalculatorFrame)).pack(pady=50)

'''
Esta clase contiene el frame de la calculadora, este frame es desplegado despues del MainFrame(Pantalla de inicio)
en el se encuentran todas las funciones de la calculadora así como la botonera
'''
class CalculatorFrame(tk.Frame):
    '''
    Método iniciador del frame de la calculadora.
    '''
    def __init__(self, parent):
    
        super().__init__(parent, bg="#1CAC91")

        self.x_var = tk.StringVar()
        self.y_var = tk.StringVar()
        self.resultvar = tk.StringVar()
        self.resultvar.set("Answer Here!")
        
        # Cargando recursos gráficos para la calculadora.
        self.exit = tk.PhotoImage(file=getAssetsPath("exit.png"))
        self.info = tk.PhotoImage(file=getAssetsPath("info.png"))
        self.title = tk.PhotoImage(file=getAssetsPath("title.png"))
        self.trash = tk.PhotoImage(file=getAssetsPath("trash.png"))
        self.help = tk.PhotoImage(file=getAssetsPath("help.png"))

        # Sección de la botonera
        tk.Button(self, image=self.info, width=40, height=40, background="#1CAC91", borderwidth=0, command=self.displayInfo).grid(
            row=0, column=0, sticky=tk.W, pady=30, padx=20)
        tk.Label(self, image=self.title, height=40, width=100, font=("Berlin Sans FB", 15)).grid(
            row=0, column=1, sticky=tk.W, pady=7)
        tk.Button(self, image=self.exit, width=100, height=20, background="#1CAC91",  borderwidth=0, command=parent.destroy).grid(
            row=0, column=2, sticky=tk.W, pady=7, padx=7)

        tk.Label(self, text="X =", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=1, column=0, sticky=tk.W, pady=7, padx=7)
        self.x_entry = tk.Entry(self,textvariable=self.x_var, width=17)
        self.x_entry.grid(row=1, column=1, sticky=tk.W, pady=7, padx=7)

        tk.Button(self, image=self.trash, width=20, height=20, background="#1CAC91",  borderwidth=0, command=lambda: self.clearAll()).grid(
            row=1, column=2, sticky=tk.W, pady=7, padx=7)

        tk.Label(self, text="Y =", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=2, column=0, sticky=tk.W, pady=7, padx=7)
        self.y_entry = tk.Entry(self,textvariable=self.y_var, width=17)
        self.y_entry.grid(row=2, column=1, sticky=tk.W, pady=7, padx=7)

        tk.Label(self, text="Answer = ", font=("Berlin Sans FB", 10), width=13, height=1, background="#1CAC91").grid(
            row=3, column=0, sticky=tk.W, pady=20, padx=7)
        tk.Label(self, textvariable=self.resultvar, font=("Berlin Sans FB", 10), width=18, height=1, background="#1CAC91").grid(
            row=3, column=1, sticky=tk.W, pady=7, padx=7)
        

        tk.Button(self, text="senh(x)",command=lambda: self.resultvar.set(ftrs.sinh_t(float(eval(self.x_var.get())))), width=13, height=1).grid(
            row=6, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="cosh(x)",command=lambda: self.resultvar.set(ftrs.cosh_t(float(eval(self.x_var.get())))), width=13, height=1).grid(
            row=6, column=1, sticky=W, pady=2, padx=10,)
        tk.Button(self, text="tanh(x)",command=lambda: self.resultvar.set(ftrs.tanh_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=6, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="asen(x)",command=lambda: self.resultvar.set(ftrs.asin_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=7, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="acos(x)",command=lambda: self.resultvar.set(ftrs.acos_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=7, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="atan(x)",command=lambda: self.resultvar.set(ftrs.atan_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=7, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="sec(x)",command=lambda: self.resultvar.set(ftrs.sec_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=8, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="csc(x)",command=lambda: self.resultvar.set(ftrs.csc_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=8, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="cot(x)",command=lambda: self.resultvar.set(ftrs.cot_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=8, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="sen(x)",command=lambda: self.resultvar.set(ftrs.sin_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=9, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="cos(x)",command=lambda: self.resultvar.set(ftrs.cos_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=9, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="tan(x)",command=lambda: self.resultvar.set(ftrs.tan_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=9, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="ln(x)",command=lambda: self.resultvar.set(ftrs.ln_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=10, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="log10(x)",command=lambda: self.resultvar.set(ftrs.log_t(float(eval(self.x_entry.get())),10)), width=13, height=1).grid(
            row=10, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="loga(x)",command=lambda: self.resultvar.set(ftrs.log_t(float(eval(self.x_entry.get())),float(eval(self.y_entry.get())))), width=13, height=1).grid(
            row=10, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="1/x",command=lambda: self.resultvar.set(ftrs.div_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=11, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="sqrt(x)",command=lambda: self.resultvar.set(ftrs.sqrt_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=11, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, text="n_sqrt(x)",command=lambda: self.resultvar.set(ftrs.root_t(float(eval(self.x_entry.get())),float(eval(self.y_entry.get())))), width=13, height=1).grid(
            row=11, column=2, sticky=W, pady=2, padx=10)
        tk.Button(self, text="exp(x)",command=lambda: self.resultvar.set(ftrs.exp_t(float(eval(self.x_entry.get())))), width=13, height=1).grid(
            row=12, column=0, sticky=W, pady=2, padx=20)
        tk.Button(self, text="x^y",command=lambda: self.resultvar.set(ftrs.power_t(float(eval(self.x_entry.get())),float(eval(self.y_entry.get())))), width=13, height=1).grid(
            row=12, column=1, sticky=W, pady=2, padx=10)
        tk.Button(self, image=self.help, width=97, height=24, background="#1CAC91", borderwidth=0,command=self.displayHelp).grid(
            row=12, column=2, sticky=W, pady=2, padx=10)

        tk.Button(self, text="7", width=13, height=2, command=lambda: self.insertValues(7)).grid(
            row=13, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="8", width=13, height=2, command=lambda: self.insertValues(8)).grid(
            row=13, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="9", width=13, height=2, command=lambda: self.insertValues(9)).grid(
            row=13, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="4", width=13, height=2, command=lambda: self.insertValues(4)).grid(
            row=14, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="5", width=13, height=2, command=lambda: self.insertValues(5)).grid(
            row=14, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="6", width=13, height=2, command=lambda: self.insertValues(6)).grid(
            row=14, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="1", width=13, height=2, command=lambda: self.insertValues(1)).grid(
            row=15, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="2", width=13, height=2, command=lambda: self.insertValues(2)).grid(
            row=15, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text="3", width=13, height=2, command=lambda: self.insertValues(3)).grid(
            row=15, column=2, sticky=W, pady=10, padx=10)
        tk.Button(self, text="π", width=13, height=2, command=lambda: self.insertValues(ftrs.pi_t)).grid(
            row=16, column=0, sticky=W, pady=10, padx=20)
        tk.Button(self, text="0", width=13, height=2, command=lambda: self.insertValues(0)).grid(
            row=16, column=1, sticky=W, pady=10, padx=10)
        tk.Button(self, text=".", width=13, height=2, command=lambda: self.insertValues(".")).grid(
            row=16, column=2, sticky=W, pady=10, padx=10)

    '''
    Método displayInfo
    
    Realiza el display de una ventana emergente encargada de mostrar la información 
    sobre el uso de la calculadora así como otros aspectos relevantes de los autores.
    '''
    def displayInfo(self):
        infoScreen = tk.Toplevel(self)
        infoScreen.title("Calculadora FunTras")
        infoScreen.geometry("400x700")
        self.instructions = tk.PhotoImage(file=getAssetsPath("instructions.png"))
        self.logo = tk.PhotoImage(file=getAssetsPath("logo.png"))
        self.background_label = tk.Label(infoScreen, image=self.instructions)
        self.background_label.place(relwidth=1, relheight=1)
        infoScreen.iconphoto(True, self.logo)
        infoScreen.config(bg="#1CAC91")
        infoScreen.resizable(False, False)
        screen_width = infoScreen.winfo_screenwidth()
        screen_height = infoScreen.winfo_screenheight()
        x = (screen_width/2) - (400/2)
        y = (screen_height/2) - (700/2)
        infoScreen.geometry('%dx%d+%d+%d' % (400, 700, x, y))
        
    
    '''
    Método displayHelp
    
    Realiza el display de una ventana emergente encargada de mostrar la información 
    sobre la descripcion de todas las funciones que la calculadora puede emplear
    '''
    def displayHelp(self):
        
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        helpScreen = tk.Toplevel(self)
        helpScreen.title("Calculadora FunTras")
        helpScreen.geometry("410x700")
        
       
        canvas = tk.Canvas(helpScreen)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(helpScreen, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        frame_scrollable = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_scrollable, anchor='nw')
        
        self.help1 = tk.PhotoImage(file=getAssetsPath("help1.png"))
        self.help2 = tk.PhotoImage(file=getAssetsPath("help2.png"))
        self.help3 = tk.PhotoImage(file=getAssetsPath("help3.png"))
        self.help4 = tk.PhotoImage(file=getAssetsPath("help4.png"))
        self.help5 = tk.PhotoImage(file=getAssetsPath("help5.png"))

        labelHelp1 = tk.Label(frame_scrollable, image=self.help1)
        labelHelp2 = tk.Label(frame_scrollable, image=self.help2)
        labelHelp3 = tk.Label(frame_scrollable, image=self.help3)
        labelHelp4 = tk.Label(frame_scrollable, image=self.help4)
        labelHelp5 = tk.Label(frame_scrollable, image=self.help5)
        labelHelp1.pack(anchor='w')
        labelHelp2.pack(anchor='w')
        labelHelp3.pack(anchor='w')
        labelHelp4.pack(anchor='w')
        labelHelp5.pack(anchor='w')
  
        # Configurar el scroll para permitir desplazamiento
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        self.logo = tk.PhotoImage(file=getAssetsPath("logo.png"))
        helpScreen.iconphoto(True, self.logo)
        canvas.config(bg="#1CAC91")
        helpScreen.resizable(False, False)
        screen_width = helpScreen.winfo_screenwidth()
        screen_height = helpScreen.winfo_screenheight()
        x = (screen_width/2) - (410/2)
        y = (screen_height/2) - (700/2)
        helpScreen.geometry('%dx%d+%d+%d' % (410, 700, x, y))

    '''
    Método clearAll
    
    Permite borrar todos los datos ingresados en los inputs de la calucladora
    '''
    def clearAll(self):

        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)

    '''
    Método clc
    
  
    '''
    def clc(self):
        self.resultvar.set("mlp")

    '''
    Método insertValues
    
    Este método detecta el entry en el cual esta el focus para así ingresar los valores ingresados utilizando
     el teclado númerico facilitado por la app, esto nos permite conocer el entry al que se le desea ingresar
     el valor y posteriormente lo ingresa.
    '''
    def insertValues(self, value):

        focused_widget = self.focus_get()

        if focused_widget == self.x_entry:
            self.x_entry.insert(tk.END, value)
        elif focused_widget == self.y_entry:
            self.y_entry.insert(tk.END, value)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
