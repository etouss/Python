import tkinter
import time
fenetre=tkinter.Tk()
canvas = tkinter.Canvas(fenetre,width=400,height=400,background="white")
canvas.pack()
for i in range(0,400,10):
    for j in range(0,400,10):
        canvas.create_rectangle(i,j,i+10,j+10)
