# fileDialog se usa para abrir o guardar.

#   Function	             Parameters	                               Purpose
# .askopenfilename	  >>  Directory, Title, Extension	    To open file: Dialog that requests selection of an existing file.
# .asksaveasfilename >>	  Directory, Title, Extension)	    To save file: Dialog that requests creation or replacement of a file.
# .askdirectory	    >>    None	                            To open directory
# llamamos la ventana emergente a traves de funciones
# https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/dialogs-dialogos/

from tkinter import *
from tkinter import messagebox, filedialog
root=Tk()


def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", 
	filetypes=(("Archivos de excel", "*xlsx"),("Archivos de texto","*.txt"),("Archivos de Word","*.docx"),("Archivos de pdf","*.pdf"),("Archivos de imagen","*.jpg"),("Todos los Archivos","*.*") ))#  initaldir=ABRIR EN EL C: y filestypes para que me muestre los tipos de archivo que quiero abrir pdf, txt, xls, jpg etc
	print(fichero)

Button(root,text="Abrir Fichero", command=abreFichero).pack()





root.mainloop()
