# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:28:01 2020 

@author: jishn
"""

import tkinter as tk
from tkinter import ttk
import switch_frame as switch
import display_canvas as display
import config



# Main class
class Finance(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Finance Software")      #Software Title
        self.state("zoom")                  #Maxmizes window
        
        
         
      
#------------------------------------------------------------------------------------------
        #Frame for heading
        head_frame = tk.Frame(self)
        head_frame.grid(row = 0, column = 1,  sticky = "EW")
        head_frame.columnconfigure(1, weight = 1)   #Expand with window
        head_label = tk.Label(head_frame, text = "Combined Finance", font = ("Segoe UI", 25, "bold"), justify = "center")
        head_label.grid(row = 0, column =1, sticky = "EW" )
#------------------------------------------------------------------------------------------
        backup_switch = tk.Button(self, text = "Backup", width = 16, height = 3, font = ("Arial", 9, "bold"))
        backup_switch.grid(row = 0, column = 0, pady = 5)
#------------------------------------------------------------------------------------------
        
        switch_object = switch.Switch_Frame(self)
      
        display_object = display.Display_Canvas(self)
        
        

if __name__ == "__main__":
    obj = Finance()
    obj.mainloop()