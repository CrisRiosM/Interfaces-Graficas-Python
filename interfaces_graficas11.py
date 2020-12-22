#Creacion de interfaces graficas
#Menus: barras en la parte superior con opciones de sub-menus.

from tkinter import *

root=Tk()
barra_menu=Menu(root)
root.config(menu=barra_menu, width = 300, height= 300)

#creamos los menus

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar")
archivo_menu.add_command(label="Salir")
############
archivo_edicion=Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Pegar")
archivo_edicion.add_command(label="Cortar")

archivo_herramientas=Menu(barra_menu)
archivo_ayuda=Menu(barra_menu)

# Los organizamoc con add_cascade

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=archivo_edicion)
barra_menu.add_cascade(label="Herramientas", menu=archivo_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayuda)


root.mainloop()
