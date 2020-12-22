# creacion de interfaces graficas
# exportar la libreria de pythoon Tkinter WxPython PyQT PyGTK
# from tkinter import *

# raiz = Tk()
# raiz.title("Ventana de Pruebas") # metodo para ponerle titulo al frame

# raiz.resizable(1,0) # impedir que el ancho width y largo height varie bloquea icono de ampliar pantalla

# #para cambiar la imagen de la la pluma esta  en formato .ico, debo tener en el mismo directorio o carpeta 
# #una imagen en formato .ico, ver conversores en google

# raiz.iconbitmap("Hoja.ico")
#  ##

# raiz.geometry("650x350")

# raiz.config(bg = "salmon" )

# miFrame = Frame()
# miFrame.pack()

#raiz.mainloop() # siempre debe ir l finalpython Interfaces_graficas.py

##############################################################

# from tkinter import *

# raiz = Tk ()

# raiz.title("SIERRA MAESTRA")
# raiz.resizable(True, False)
# raiz.geometry("700x700")
# raiz.iconbitmap("Hoja.ico")
# raiz.config(bg = "light green")

# #CREEMOS UN FRAME DENTRO DE UNA RAIZ TK

# miFrame = Frame()
# # Con el metrdo pack() empaqueto el frame dentro de la raiz tk()
# miFrame.pack()
# # dandole tamaño al frame
# miFrame.config(bg = "orange")
# miFrame.config( width = "500", height = "350")
#  # ver la opciones del metodo pack () https://docs.python.org/3.3/library/tkinter.html#packer-options
# raiz.mainloop()

#opciones de pack( ejemplos)


from tkinter import *
from PIL import Image

raiz = Tk ()

raiz.title("SIERRA MAESTRA")
#raiz.resizable(True, False)
raiz.geometry("700x600")
raiz.iconbitmap("Hoja.ico")
raiz.config(bg = "green")


imagenF1 = PhotoImage(file ="SierraMaestra.gif" )
labImagen1 = Label(raiz, image = imagenF1).place(x=30,y =30)

imagenF = PhotoImage(file ="hierbas.gif" )
labImagen = Label(raiz, image = imagenF).place(x=700,y =0)


imagenF2 = PhotoImage(file ="frutas.gif" )
labImagen1 = Label(raiz, image = imagenF2).place(x=700,y =300)


#CREEMOS UN FRAME DENTRO DE UNA RAIZ TK

 # ver la opciones del metodo pack () https://docs.python.org/3.3/library/tkinter.html#packer-options
raiz.mainloop()

#LIBRERIA Tkinter . Widget Label
# PARA MOSTRAR TEXTO ESTATICO EN ALFUN SITIO DE LA INTERFAZ GRAFICA, NO TIENE INTERACION

# LABEL SINTAXIS 

# variable_label = Label(contenedor(puede ser tk() o un Frame()) , opciones)
# opciones pueden ser : Text(texto que se muestra en el label) , Anchor(controla piscion),  Bg(color de fondo)
# Bitmap(Mapas de bits que se mostraran como grafico), Bd(grosor del borde, pordefecto 2px), 
# Font(tipo de fuente a mostrar), Fg (color de la fuente), Widtgh( ancho) , Height( largo), 
# Image(muestra una imagen en el label en lugar de texto), justify(justificacion del texto en el label)





