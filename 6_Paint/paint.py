#Requirements 
#Tkinter , PIL
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk, colorchooser
from PIL import Image,ImageTk
from tkinter.ttk import Style
import os

class main:
    def __init__(self,win):
        self.style = Style()
        self.style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'), foreground = 'red') 
        self.win = win
        self.fg = 'black'
        self.bg = 'white'
        self.oldx = None
        self.oldy = None
        self.width = 3
        self.draw()
        #Binding the events to the canvas widget
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
        self.win.config(cursor = 'pencil')
        

    #Paint method to draw on user input
    def paint(self,e):
        if self.oldx and self.oldy:
            self.c.create_line(self.oldx,self.oldy,e.x,e.y,width = self.width,fill = self.fg , capstyle = ROUND ,smooth = True)
        self.oldx = e.x
        self.oldy = e.y
    
    #Sets the cursor to inital state
    def reset(self,e):
        self.oldx = None
        self.oldy = None

    #Choose eraser
    def set_eraser(self):
        self.win.config(cursor = 'dot')
        self.fg = self.bg
    #Choose brush
    def set_brush(self):
        self.win.config(cursor = 'pencil')
        self.fg = 'black' 
        
    #Setting the Brush color
    def getPenColor(self):
        color = colorchooser.askcolor()
        if color != None:
            self.fg = (str(color)[-9:-2])

    #Fill tool 
    def fillbg(self):
        color = colorchooser.askcolor()
        if color != None:
            self.bg = (str(color)[-9:-2])
        self.c.config(background = self.bg)
    
    #Clears the content of the screen
    def clear(self):
        self.c.config(background = 'white')
        self.bg = 'white'
        self.c.delete(ALL)
    
    #Utility function for palette
    def setfg(self,color):
        self.fg = color
        

    #Method to dislpay all the sub widgets on the canvas    
    def draw(self):
        
        #Canvas
        self.c = Canvas(self.win,width = 800,height = 600,bg = self.bg)
        self.c.pack(side=LEFT)
        
        #Sidebar
        self.sideBar = Frame(self.win, padx=5, pady=5,height = 600,width = 350)
        self.sideBar.pack(side=RIGHT, fill=BOTH)
       
        #Buttons
        self.b1 = ttk.Button(self.sideBar,text = 'Exit',command = self.win.destroy)
        self.b1.pack()
        self.b2 = ttk.Button(self.sideBar,text = 'Clear',command = self.clear)
        self.b2.pack()
        
        self.eraser = ttk.Button(self.sideBar,text = 'Eraser',command = self.set_eraser)
        self.eraser.pack()
        self.brush = ttk.Button(self.sideBar,text = 'Brush',command = self.set_brush)
        self.brush.pack()
        
        self.color = ttk.Button(self.sideBar, text = "Pen Color" ,command=self.getPenColor)
        self.color.pack()
        
        self.fill = ttk.Button(self.sideBar, text = "Fill BG", command=self.fillbg)
        self.fill.pack()
        
        
#Main program to run the application
if __name__ == '__main__':
    win = Tk()
    main(win)
    win.title('PyPaint')
    win.mainloop()