'''  * Archivo:   Interfaz.py
     * Dispositivo: PIC16F887
     * Autor: Margareth Vela 
     * Programa: SPI
     * Creado: Agosto 04, 2021
     * Última modificación: Agosto 05, 2021'''

'''------------------------------------------------------------------------------
                            Importación de librerías
-------------------------------------------------------------------------------- '''
import tkinter as tk
from tkinter import *
import serial

'''------------------------------------------------------------------------------
                            Definición de objetos
------------------------------------------------------------------------------'''
root = Tk()

'''------------------------------------------------------------------------------
                            Definición del puerto serial
------------------------------------------------------------------------------'''
com_serial = serial.Serial(port='COM3', baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1)

'''------------------------------------------------------------------------------
                            Definición del puerto serial
------------------------------------------------------------------------------'''
def Conectar():
        var1 = []
        n=0
        flag = False
        flag1=False
        while(flag == False):
            var = com_serial.read().decode('ascii')
            if var == '\r':
                flag = True
            if (flag):
                while(n<9):
                    var = com_serial.read().decode('ascii')
                    var_temp = var
                    var1.append(var_temp)    
                    n = n+1
                    flag = False
                    flag1 = True
        label_pots1=tk.Label(root, text=var1[0])
        label_pots1.place(x=50, y=150)
        label_pots2=tk.Label(root, text=var1[1])
        label_pots2.place(x=60, y=150)
        label_pots3=tk.Label(root, text=var1[2])
        label_pots3.place(x=70, y=150)
        label_pots4=tk.Label(root, text=var1[3])
        label_pots4.place(x=80, y=150)
        label_pots5=tk.Label(root, text=var1[4])
        label_pots5.place(x=110, y=150)
        label_pots6=tk.Label(root, text=var1[5])
        label_pots6.place(x=140, y=150)
        label_pots7=tk.Label(root, text=var1[6])
        label_pots7.place(x=150, y=150)
        label_pots7=tk.Label(root, text=var1[7])
        label_pots7.place(x=160, y=150)
        label_pots7=tk.Label(root, text=var1[8])
        label_pots7.place(x=170, y=150)
        
def Enviar():       
        lista = [];            
        var_temp = root.name.get()
        for i in var_temp:
            lista.append(i)
        if len(lista) ==1:
            unidad = str(hex(int(48)+int(str(lista[0])))) 
            enter = bytes('13', 'utf-8')
            com_serial.write(unidad.encode('ascii'))
            com_serial.write(b'\r')           
        
        elif len(lista)==2:
            decena = str(hex(int(48)+int(str(lista[0]))))
            unidad = str(hex(int(48)+int(str(lista[1]))))
            enter = bytes('13', 'utf-8')
            com_serial.write(decena)
            com_serial.write(unidad)
            com_serial.write(b'\r')
            
        elif len(lista)==3:
            centena = str(hex(int(48)+int(str(lista[0]))))
            decena = str(hex(int(48)+int(str(lista[1]))))
            unidad = str(hex(int(48)+int(str(lista[2]))))
            enter = bytes('13', 'utf-8')
            com_serial.write(centena)
            com_serial.write(decena)
            com_serial.write(unidad)
            com_serial.write(b'\r')

'''------------------------------------------------------------------------------
                               Interfaz
------------------------------------------------------------------------------'''
name = None
x=50
var1 = []
root.title("Serial")
# allowing the widget to take the full space of the root window
root.geometry("230x200") 
# Botón para conectar la comunicación serial
ConectarButton = Button(root, text="Conectar", command = lambda:Conectar())
#Ubicación del botón
ConectarButton.place(x=10, y=10)

#Botón para enviar datos por USART
EnviarButton = Button(root, text="Enviar", command = lambda:Enviar())
#Ubicación del botón
EnviarButton.place(x=160, y=80)

#Texto del Contador
text = tk.Label(root, text="Contador: ").place(x=10, y=50)
root.name = Entry(text)
root.name.focus()
root.name.place(x=10, y=80)

Pot1= tk.Label(root, text="POT1")
Pot1.place(x=50, y=120)
Pot2 = tk.Label(root, text="POT2")
Pot2.place(x=150, y=120)

'''------------------------------------------------------------------------------
                               Main loop
------------------------------------------------------------------------------'''
root.mainloop()