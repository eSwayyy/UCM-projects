from tkinter import *

def Funcion1():
    print("Puto el que lo lee")
ventana= Tk()
ventana.title("SI")
ventana.geometry("400x200")
lbl=Label(ventana,text="Label")
lbl.pack()
btn= Button(ventana, text="Presionar", command=Funcion1, fg="blue", bg="gray")
btn.pack()

ventana.mainloop()