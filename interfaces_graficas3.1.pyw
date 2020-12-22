# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
root = Tk()
miFrame = Frame(root, width = 1200 ,height = 600, bg ="forest green")
miFrame.pack()


############################################################################
#  https://www.tutorialspoint.com/python3/tk_entry.htm >> opciones

cuadro_nombre = Entry(miFrame, bg ="light green", bd = 10, fg ="black", font = ("Forte", 20))
cuadro_nombre.grid (row = 0 , column = 1,  padx =15, pady =15) # posiciono el cuadro de texto en el frame 

cuadro_apellido= Entry(miFrame,bg ="light green", bd = 10, fg ="black" , font = ("Forte", 20))
cuadro_apellido.grid (row = 1 , column = 1,  padx =15, pady =15)# pad x y pad y sub espacion entre los cuadros de texto

cuadro_password = Entry(miFrame, bg ="light green", bd = 10, fg ="black", font = ("Forte", 20))
cuadro_password.grid (row = 2 , column = 1,  padx =15, pady =15)
cuadro_password.config(show = "*")

cuadro_direccion = Entry(miFrame, bg ="light green", bd = 10, fg ="black", font = ("Forte", 20))
cuadro_direccion.grid (row = 3 , column = 1,  padx =15, pady =15)

texto_comentario =Text(miFrame, width = 40 ,height =10) # para crear cuadros de texto largos
texto_comentario.grid(row = 4, column = 1, padx =15, pady =15)

scrollvar = Scrollbar(miFrame, command = texto_comentario.yview, bg = "papaya whip") # adicionar barra de desplazamiento simple
scrollvar.grid(row = 4 , column = 2, sticky = "nsew" )     # tutorialspoint.com/python/tk_text.htm

texto_comentario.config(yscrollcommand = scrollvar.set)


    
boton = Button(root, text = "Enviar", font = ("Forte", 15), command = "codigoBoton")
boton.pack()

##############]################################################################

nombreLabel = Label(miFrame, text = "Nombres ", font = ("Forte", 30), padx =15, pady =15, fg ="green")
nombreLabel.grid (row = 0 , column = 0, sticky = "e")# posiciono el  texto en el frame 

ApellidoLabel = Label(miFrame, text = "Apellidos", font= ("Forte", 30),  padx =15, pady =15, fg ="green")
ApellidoLabel.grid (row = 1 , column = 0, sticky = "e") # sticky trabaja con los puntos caridanes para posicionar el texto, 
                                                         #e east alineados a la izquierda
PassLabel = Label(miFrame, text = "Password", font = ("Forte", 30),  padx =15, pady =15, fg ="green")
PassLabel.grid (row = 2 , column = 0 , sticky = "e")

PassLabel = Label(miFrame, text = "Direccion", font = ("Forte", 30),  padx =15, pady =15, fg ="green")
PassLabel.grid (row = 3 , column = 0 , sticky = "e")

ComentLabel = Label(miFrame, text = "Comentarios", font = ("Forte", 30),  padx =15, pady =15, fg ="green")
ComentLabel.grid (row = 4 , column = 0 , sticky = "e")

root.mainloop()

