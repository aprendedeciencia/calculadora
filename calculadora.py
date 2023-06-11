from tkinter import *

raiz = Tk()
raiz.title("Calculadora")

frame0 = Frame(raiz)
frame0.pack()

valor = StringVar()
operacion = ""
resultado = 0
operador=""
# ---------------Funciones---------------------
def valorPantalla(num):
    global operacion
    global operador
    if num == "0" and valor.get() == "0":
        valor.set("0")
    else:
        if valor.get() == "0":
            valor.set(num)
        else:
            if operacion == "suma":
                valor.set(num)
                operador = operacion
                operacion=""
            elif operacion == "resta":
                valor.set(num)
                operador = operacion
                operacion = ""
            elif operacion == "multiplicacion":
                valor.set(num)
                operador = operacion
                operacion = ""
            elif operacion == "division":
                valor.set(num)
                operador = operacion
                operacion = ""
            elif operacion == "igual":
                valor.set(num)
                operacion = ""
            else:
                valor.set(valor.get() + num)

def setAdd():
    global operacion
    global resultado
    resultado+=int(valor.get())
    operacion="suma"
    valor.set(str(resultado))

def setEquals():
    global operador
    global resultado
    global operacion

    if operador == "suma":
        resultado+=int(valor.get())
        valor.set(str(resultado))
        resultado = 0
        operacion = "igual"
    elif operador == "resta":
        resultado = resultado - int(valor.get())
        valor.set(str(resultado))
        resultado = 0
        operacion = "igual"
    elif operador == "multiplicacion":
        valor.set(str(resultado))
        resultado = 0
        operacion = "igual"

def setSustrac():
    global operacion
    global resultado
    if resultado == 0:
        resultado = int(valor.get())
    else:
        resultado = resultado - int(valor.get())

    operacion="resta"
    valor.set(str(resultado))

def setMult():
    global operacion
    global resultado
    resultado*=int(valor.get())
    operacion="multiplicacion"
    valor.set(str(resultado))

# ------------------PANTALLA------------------
pantalla = Entry(frame0, textvariable=valor)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#F8F8F8", fg="#28B7FF", justify="right")

# ------------------Botones 7-8-9-X------------------
siete = Button(frame0, text="7", width=5, height=5, command=lambda: valorPantalla("7"))
siete.grid(row=2, column=0)

ocho = Button(frame0, text="8", width=5, height=5, command=lambda: valorPantalla("8"))
ocho.grid(row=2, column=1)

nueve = Button(frame0, text="9", width=5, height=5, command=lambda: valorPantalla("9"))
nueve.grid(row=2, column=2)

multi = Button(frame0, text="X", width=5, height=5, command=lambda: setMult())
multi.grid(row=2, column=3)

# ------------------Botones 4-5-6-+------------------
cuatro = Button(frame0, text="4", width=5, height=5, command=lambda: valorPantalla("4"))
cuatro.grid(row=3, column=0)

cinco = Button(frame0, text="5", width=5, height=5, command=lambda: valorPantalla("5"))
cinco.grid(row=3, column=1)

seis = Button(frame0, text="6", width=5, height=5, command=lambda: valorPantalla("6"))
seis.grid(row=3, column=2)

add = Button(frame0, text="+", width=5, height=5, command=lambda: setAdd())
add.grid(row=3, column=3)

# ------------------Botones 1-2-3-------------------
uno = Button(frame0, text="1", width=5, height=5, command=lambda: valorPantalla("1"))
uno.grid(row=4, column=0)

dos = Button(frame0, text="2", width=5, height=5, command=lambda: valorPantalla("2"))
dos.grid(row=4, column=1)

tres = Button(frame0, text="3", width=5, height=5, command=lambda: valorPantalla("3"))
tres.grid(row=4, column=2)

sust = Button(frame0, text="-", width=5, height=5, command=lambda: setSustrac())
sust.grid(row=4, column=3)

# ------------------Botones 0-=-,-+------------------
cero = Button(frame0, text="0", width=5, height=5, command=lambda: valorPantalla("0"))
cero.grid(row=5, column=0)

coma = Button(frame0, text=",", width=5, height=5, command=lambda: valorPantalla(","))
coma.grid(row=5, column=1)

igual = Button(frame0, text="=", width=5, height=5, command=lambda: setEquals())
igual.grid(row=5, column=2)

div = Button(frame0, text="/", width=5, height=5)
div.grid(row=5, column=3)

raiz.mainloop()
