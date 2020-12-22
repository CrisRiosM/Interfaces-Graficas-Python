from tkinter import *

# Widget Entry
# Widget utilizado para producir cuadros de texto

# root = Tk()
# miFrame = Frame(root, width = 1200 ,height = 600)
# miFrame.pack()



# cuadro_texto = Entry(root)
# cuadro_texto.place (x = 100 , y= 100) # posiciono el cuadro de texto en el frame 
# nombreLabel = Label(miFrame, text = "Nombre: ")
# nombreLabel.place(x=40 , y=100)


# root.mainloop()


# Metodo grid() dividiendo el frame en casillas alienadas donde se puede ubicar un texto o label
# s divide en Filas rows y columnas column desde la posicion 0 en adelante

root = Tk()
miFrame = Frame(root, width = 1200 ,height = 600)
miFrame.pack()



cuadro_texto = Entry(miFrame)
cuadro_texto.grid (row = 0 , column = 1) # posiciono el cuadro de texto en el frame 

nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid (row = 0 , column = 0)# posiciono el  texto en el frame 

root.mainloop()
