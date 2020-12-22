from tkinter import *
#check buttons
root=Tk()

root.title("Ejemplo")

foto = PhotoImage(file="Avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()
Label(frame,text="Elige destinos",  width=50).pack()
Checkbutton(root, text="Playa").pack()
Checkbutton(root, text="Montaña").pack()
Checkbutton(root, text="Ciudad").pack()

root.mainloop()