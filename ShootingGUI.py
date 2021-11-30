from tkinter import Entry, font
from tkinter.constants import  CENTER
import Shooting
import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


app = tk.Tk()
app.geometry('1000x1000')
app.state('zoomed')
a = tk.Label(app, text= 'Start Throwing!')
# a.grid(row= 1, column = 0)
TextAndButton = tk.Frame(app,highlightbackground="red", highlightthickness=1)
TextAndButton.place(relx= 0.2, rely= 0.5)
buttonFrame = tk.Frame(TextAndButton,highlightbackground="blue", highlightthickness=1)
buttonFrame.grid()

VelocityText = tk.Label(buttonFrame, text= 'Velocity',  font = ('', 15)).grid()
VelocityEntry = tk.Entry(buttonFrame, font = ('',15))
VelocityEntry.grid(pady= 10, padx= 10)

TimeText = tk.Label(buttonFrame, text= 'Time', font = ('', 15)).grid()
TimeEntry = tk.Entry(buttonFrame, font = ('',15))
TimeEntry.grid(pady= 10, padx= 10)

AngleText = tk.Label(buttonFrame, text= 'Angle', font = ('', 15)).grid()
AngleEntry = tk.Entry(buttonFrame, font = ('',15))
AngleEntry.grid(pady= 10, padx= 10)
t = tk.Entry(app, text = 'Entry:')



def ShowSim():
    time = TimeEntry.get()
    velocity = VelocityEntry.get()
    angle = AngleEntry.get() 
    InnerCanvas = tk.Canvas(app, height= 800, width= 800)
    InnerCanvas.place(rely= 0.5, relx= 0.8, anchor= CENTER)
    Throw = Shooting.simShooting(int(velocity), float(time), float(angle))
    canvas = FigureCanvasTkAgg(Throw, master = InnerCanvas)
    canvas.get_tk_widget().pack(expand= 1)
    toolbar = NavigationToolbar2Tk(canvas, InnerCanvas)
    toolbar.update()
    
def _quit():
    app.quit()
    app.destroy()
a = tk.Button(TextAndButton, text= 'Start Throwing!', command= ShowSim)
a.grid(row = 0,column= 1)

quitButton = tk.Button(TextAndButton, text = 'Quit', command= _quit)
quitButton.grid(row= 1, column=1)

app.mainloop()

