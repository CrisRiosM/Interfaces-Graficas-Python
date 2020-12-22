from tkinter import *
from tkinter import messagebox
root=Tk()

# llamamos la ventana emergente a traves de funciones
# https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/dialogs-dialogos/


def infoAdicional():
	messagebox.showinfo("Procesador de Cris ", "Procesador de textos vesion 2020")
def avisoLicencia():
	messagebox.showwarning("Licencia","producto bajo licencia ")
def salirAplicacion():
	valor=messagebox.askquestion("Deseas salir de la aplicacion")
	if valor=="yes":
		root.destroy()

def cerrarPrograma():
	messagebox.askretrycancel("Reintentar,no es posible cerrar")

barra_menu=Menu(root)
root.config(menu=barra_menu, width = 300, height= 300)

#creamos los menusno es posible cerrar el programa, documento abiert")

archivo_menu=Menu(barra_menu, tearoff=0)

archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar",command=cerrarPrograma)
archivo_menu.add_command(label="Salir",command=salirAplicacion)
############
archivo_edicion=Menu(barra_menu, tearoff=0)

archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Pegar")
archivo_edicion.add_command(label="Cortar")
####
archivo_herramientas=Menu(barra_menu)
#####
archivo_ayuda=Menu(barra_menu)

archivo_ayuda.add_command(label="Licencia", command=avisoLicencia, font="Forte")
archivo_ayuda.add_command(label="Acerca de ...", command=infoAdicional)

# Los organizamoc con add_cascade

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=archivo_edicion)
barra_menu.add_cascade(label="Herramientas", menu=archivo_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayuda)


root.mainloop()
