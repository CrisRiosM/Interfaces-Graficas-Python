#radiobuttons

from tkinter import *

root=Tk()

varOption=IntVar()

def imprimir():

	#print(varOption.get())
	if varOption.get()==1:
		etiqueta.config(text="has elegido Masculino")
	elif varOption.get()==2:
		etiqueta.config(text="has elegido Femeneino")

Label(root, text="Genero: ").pack()

Radiobutton(root, text= "Masculino",variable=varOption, value=1, command=imprimir).pack()
Radiobutton(root, text= "Femenino", variable=varOption, value=2,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()