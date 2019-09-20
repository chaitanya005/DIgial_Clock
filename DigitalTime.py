from tkinter import * 
from tkinter.ttk import *
from time import strftime 
  
 
whole = Tk() 
whole.title('Clock') 
  
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
lbl = Label(whole, font = ('calibri', 40, 'bold'), 
            background = 'Black', 
            foreground = 'white')  
lbl.pack(anchor = 'center') 

time()
mainloop()
