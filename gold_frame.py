# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:11:35 2020

@author: jishn
"""

import tkinter as tk
from tkinter import ttk
import address_frame
import history_frame
import intrest_frame
import detail_frame



from tkcalendar import DateEntry


class Gold_Frame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.grid(row = 0, column = 0)
#        for i in range(100):
#            tk.Label(self, text = i, background = "white").grid(row = i, column = 0, padx = 10)
        self.columnconfigure(0, weight = 1)
        
        self.rowconfigure(0, weight = 1)
        
        top_frame = tk.Frame(self, background = "red")
        top_frame.grid(row =0, column = 0, sticky = "NSEW")
  
#------------------------------------------------------------------------------------
        
        button_frame = tk.Frame(top_frame)
        button_frame.grid(row = 0, column = 0)
        
        add_button = tk.Button(button_frame, text = 'Add')
        add_button.grid(row = 0, column = 0)
        
        save_button = tk.Button(button_frame, text = "Save")
        save_button.grid(row = 1, column = 0)
        
        cancel_button = tk.Button(button_frame, text = "Canel")
        cancel_button.grid(row = 2, column = 0)
        
        print_button = tk.Button(button_frame, text = "Print")
        print_button.grid(row = 3, column = 0)
        
        delete_button = tk.Button(button_frame, text = "Delete")
        delete_button.grid(row = 4, column = 0)
        
        for child in button_frame.winfo_children():
            child.grid_configure(padx=4, pady=6)
            child.config(height = 3, width = 8, font = ("Arial", 10, "bold"))

#--------------------------------------------------------------------------------------
            
        ttk.Separator(top_frame, orient = "vertical").grid(row = 0, column = 1, sticky = "NS", padx = 4)
        
#--------------------------------------------------------------------------------------
        
        
        address_frame.Address_Frame(top_frame)
        
               
#--------------------------------------------------------------------------------------
        
        ttk.Separator(top_frame, orient = "vertical").grid(row = 0, column = 3, sticky = "NS", padx = 4)
        
#--------------------------------------------------------------------------------------
        
        history_frame.History_Frame(top_frame)
        
#--------------------------------------------------------------------------------------
#        
        ttk.Separator(top_frame, orient = "horizontal").grid(row = 1, column = 0, columnspan = 4, sticky = "EWS", padx = 4)
        
#--------------------------------------------------------------------------------------
        
        bottom_frame = tk.Frame(self, background = "cyan")
        bottom_frame.grid(row =1, column = 0, sticky = "NSEW")
        
        
        detail_frame.Detail_Frame(bottom_frame)
        
        ttk.Separator(bottom_frame, orient = "vertical").grid(row = 0, column = 2, sticky = "NS", padx = 4)
        
        intrest_frame.Intrest_Frame(bottom_frame)
      
        
       
      
        


        