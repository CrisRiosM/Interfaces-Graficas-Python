#LIBRERIA Tkinter . Widget Label
# PARA MOSTRAR TEXTO ESTATICO EN ALFUN SITIO DE LA INTERFAZ GRAFICA, NO TIENE INTERACION

# LABEL SINTAXIS 

# variable_label = Label(contenedor(puede ser tk() o un Frame()) , Opciones)

# Opciones pueden ser : Text(texto que se muestra en el label) , Anchor(controla piscion),  Bg(color de fondo)
# Bitmap(Mapas de bits que se mostraran como grafico), Bd(grosor del borde, pordefecto 2px), 
# Font(tipo de fuente a mostrar), Fg (color de la fuente), Widtgh( ancho) , Height( largo), 
# Image(muestra una imagen en el label en lugar de texto), justify(justificacion del texto en el label)

# Ejemplo

from tkinter import *

root = Tk()

miFrame = Frame(root, width = "500", height = "400") 
miFrame.pack()

miLabel = Label(miFrame, text = "Sierra Maestra Hidroponicos", fg = "green", font = ("Forte", 30), bg = "orange" )
miLabel.place(x=200, y=100)

root.mainloop()
