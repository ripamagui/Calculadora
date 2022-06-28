
from tkinter import *
from turtle import bgcolor, right


ventana = Tk()
ventana.geometry("300x225")
ventana.config(bg="#ff99c8")
ventana.title("Calculadora Magui")

mainLabel = Label(text = "Calculadora de Magui",bg="#fde2e4",font= ("Comic sens MC" , "18", "bold"),fg ="#ff5d8f")
mainLabel.grid(row = 0,columnspan = 6, sticky = E+W)

#Pantalla de ingreso
display = Entry(ventana, bg= "#fcf6bd", relief="groove", font= ("Comic sens MC" , "16", "bold italic"), fg ="#ff686b", justify= "right")
display.grid(row =1, columnspan = 6, sticky = E+W)
display.bind("<Enter>")

#hover

class HoverButton(Button):
    def __init__(self,master, **kw):
        Button.__init__(self, master = master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self,e):
        self["background"] = self.defaultBackground

i=0 #indice para agregar un numero al lado del otro

#funcion para obtener numero
def obtenerNum(n):
    global i
    display.insert(i , n)
    i+=1

def operacion(operador):
    global i 
    operadorLong =len(operador)
    display.insert(i, operador)
    i+=operadorLong

def clearDisplay():
    display.delete(0, END)

def undo():  #para borrar de a un valor
    estadoPantalla = display.get()
    if len(estadoPantalla):
        displayNuevoEstado = estadoPantalla[:-1]
        clearDisplay()
        display.insert(0, displayNuevoEstado)
    else: 
        clearDisplay()

def calcular():
    estadoPantalla = display.get()
    try:
        result = str(eval(estadoPantalla))
        #result = eval(mathExpresion)
        clearDisplay()
        display.insert(0, result)
    except:
        clearDisplay()
        display.insert(0,"ERROR")



#botones de numeros
Button1 = HoverButton (ventana, text ="1",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(1)).grid(row = 2, column = 0,sticky = E+W)
Button2 = HoverButton (ventana, text ="2", activebackground="#fcf6bd", bg="#ff99c8",command=lambda: obtenerNum(2)).grid(row = 2, column = 1,sticky = E+W)
Button3 = HoverButton (ventana, text ="3", activebackground="#fcf6bd", bg="#ff99c8", command=lambda: obtenerNum(3)).grid(row = 2, column = 2,sticky = E+W)

Button4 = HoverButton (ventana, text ="4", activebackground= "#fcf6bd", bg= "#ff99c8", command=lambda: obtenerNum(4)).grid(row = 3, column = 0,sticky = E+W)
Button5 = HoverButton (ventana, text ="5", activebackground= "#fcf6bd", bg= "#ff99c8", command=lambda: obtenerNum(5)).grid(row = 3, column = 1,sticky = E+W)
Button6 = HoverButton (ventana, text ="6",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(6)).grid(row = 3, column = 2,sticky = E+W)

Button7 = HoverButton (ventana, text ="7",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(7)).grid(row = 4, column = 0,sticky = E+W)
Button8 = HoverButton (ventana, text ="8",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(8)).grid(row = 4, column = 1,sticky = E+W)
Button9 = HoverButton (ventana, text ="9",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(9)).grid(row = 4, column = 2,sticky = E+W)

Button0 = HoverButton (ventana, text ="0",bg="#ff99c8", activebackground="#fcf6bd",command=lambda: obtenerNum(0)).grid(row = 5, column = 1,sticky = E+W)

#botones para operar
ButtonAC = HoverButton (ventana, text ="AC",bg="#E4C1F9", activebackground="#fcf6bd", command= lambda: clearDisplay()).grid(row = 5, column = 0,sticky = E+W)
ButtonCom = HoverButton (ventana, text =",",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion(".")).grid(row = 5, column = 2,sticky = E+W)

ButtonMas = HoverButton (ventana, text ="+",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("+")).grid(row = 3, column = 3,sticky = E+W)
ButtonMenos = HoverButton (ventana, text ="-",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("-")).grid(row = 4, column = 3,sticky = E+W)
ButtonDiv = HoverButton (ventana, text ="/",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("/")).grid(row = 5, column = 3,sticky = E+W)
ButtonPor = HoverButton (ventana, text ="*",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("*")).grid(row = 5, column = 3,sticky = E+W)
ButtonResto = HoverButton (ventana, text ="%",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("%")).grid(row = 5, column = 4,sticky = E+W)
ButtonParA = HoverButton (ventana, text ="(",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("(")).grid(row = 6, column = 3,sticky = E+W)
ButtonParC = HoverButton (ventana, text =")",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion(")")).grid(row = 6, column = 4,sticky = E+W)

ButtonFle = HoverButton (ventana, text ="⬅",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: undo()).grid(row = 2, column = 3, columnspan = 2,sticky = E+W) #borrar numero
ButtonExp = HoverButton (ventana, text ="exp",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("**")).grid(row = 3, column = 4,sticky = E+W)
ButtonExp2 = HoverButton (ventana, text ="^2",bg="#E4C1F9", activebackground="#fcf6bd", command = lambda: operacion("**2")).grid(row = 4, column = 4,sticky = E+W)
ButtonIgual = HoverButton (ventana, text ="=",bg="#D0F4DE", activebackground="#fcf6bd", relief = "raised", command= lambda: calcular()).grid(row = 6, column = 0, columnspan = 3,sticky = E+W)



ventana.mainloop()