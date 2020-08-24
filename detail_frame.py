# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:44:59 2020

@author: jishn
"""

import tkinter as tk
from tkinter import ttk

class Detail_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.grid(row = 0, column = 0)
        
        tk.Label(self, text = "Pledge Details", font = ("Arial", 12, "bold")).grid(row = 0,  column = 0, pady = 5, columnspan = 4)
        
       
#        
        
        
        tk.Label(self, text = "Pledge No.", relief = "groove", width = 18).grid(row = 1, column = 0)
        tk.Label(self, text = "Item", relief = "groove", width = 24).grid(row = 1, column = 1)
        tk.Label(self, text = "Discription", relief = "groove", width = 30).grid(row = 1, column = 2)
        tk.Label(self, text = "Quantity", relief = "groove", width = 15).grid(row = 1, column = 3)
        
        self.item_canvas = tk.Canvas(self, bg = "white", height = 120, bd  = 2, width = 200)
        self.item_canvas.grid(row= 2, column = 0 , sticky = "nsew", columnspan = 4)
        self.item_canvas.grid_propagate(False)
#        
        
#        
        item_frame = tk.Frame(self.item_canvas, bg = "yellow")
        item_frame.grid(row = 1, column = 0, sticky = "nsew")
        
        items = ("Ring", "Bangle", "Chain") 
        
        
        item_one_pledge = tk.Label(item_frame, text = "A805/15", relief ="sunken", width = 18)
        item_one_pledge.grid(row  = 0, column = 0)
        item_one_list = ttk.Combobox(item_frame, values = items , width = 25)
        item_one_list.grid(row  = 0, column = 1)
        item_one_dec = ttk.Entry(item_frame, width = 35)
        item_one_dec.grid(row  = 0, column = 2)
        item_one_dec = ttk.Entry(item_frame, width = 17)
        item_one_dec.grid(row  = 0, column = 3)
#------------------------------------------------------------------------------------------------------------       
        self.scrollable_window = self.item_canvas.create_window((0, 0), window=item_frame, anchor="nw")
        
        def configure_scroll_region(event):
            self.item_canvas.configure(scrollregion=self.bbox("all"))
        
        def configure_window_size(event):
            self.item_canvas.itemconfig(self.scrollable_window, width=self.item_canvas.winfo_width())

        self.item_canvas.bind("<Configure>", configure_window_size)
        item_frame.bind("<Configure>", configure_scroll_region)
#        self.item_canvas.bind_all("<MouseWheel>", self.item_canvas._on_mousewheel)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.item_canvas.yview)
        scrollbar.grid(row=2, column=5, sticky="NS")
        
        self.item_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.item_canvas.yview_moveto(1.0)
#-----------------------------------------------------------------------------------------------------------
        
        value_frame = tk.Frame(self)
        value_frame.grid(row = 3, column = 0, columnspan = 5, sticky = "w")
        
        tk.Label(value_frame, text = "Total Weight ", font = ("Arial", 14)).grid(row = 0, column = 0, padx = 5, sticky = "w")
        
        
        weight_entry = tk.Entry(value_frame, width = 15, font = ("Arial", 14))
        weight_entry.grid(row = 0, column = 1, padx = 5)
        
        tk.Label(value_frame, text = "Total Quantity ", font = ("Arial", 12)).grid(row = 0, column = 2, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "3 ", font = ("Arial", 12),
                 relief ="sunken",
                 width = 18).grid(row = 0, column = 3, padx = 5, sticky = "w")
        
        
        
        tk.Label(value_frame, text = "Rate :", font = ("Arial", 10)).grid(row = 1, column = 0, padx = 5, sticky = "w")
        tk.Label(value_frame, text = "3500 ", font = ("Arial", 10),
                 relief ="sunken",
                 width = 20).grid(row = 1, column = 1, padx = 5, sticky = "w")
        
        
        
        tk.Label(value_frame, text = "Maximum Amount", font = ("Arial", 10),).grid(row = 1, column = 2, padx = 5, sticky = "w")
        tk.Label(value_frame, text = "3500 ", font = ("Arial", 10),relief ="sunken",
                 width = 20).grid(row = 1, column = 3, padx = 5, sticky = "w")
        
        
        tk.Label(value_frame, text = "Loan Amount ", font = ("Arial", 16)).grid(row = 2, column = 0, padx = 5, sticky = "w")
        
        
        weight_entry = tk.Entry(value_frame, width = 13, font = ("Eras", 18,'bold'))
        weight_entry.grid(row = 2, column = 1, padx = 5)
        
        tk.Label(value_frame, text = "Current Rate ", font = ("Arial", 10)).grid(row = 2, column = 2, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "3500 ", font = ("Arial", 10),
                 relief ="sunken",
                 width = 20).grid(row = 2, column = 3, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "Actual Loan ", font = ("Arial", 10)).grid(row = 3, column = 0, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "3500 ", font = ("Arial", 10),
                 relief ="sunken",
                 width = 20).grid(row = 3, column = 1, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "Addition ", font = ("Arial", 10)).grid(row = 3, column = 2, padx = 5, sticky = "w")
        
        tk.Label(value_frame, text = "3500 ", font = ("Arial", 10),
                 relief ="sunken",
                 width = 20).grid(row = 3, column = 3, padx = 5, sticky = "w")
        
        
        
        
        
        for child in value_frame.winfo_children():
            child.grid_configure(pady=5)
#            child.config(height = 4, width = 16, font = ("Arial", 15, "bold"))
        
        ttk.Separator(self, orient = "horizontal").grid(row = 4, column = 0, sticky = "ew", columnspan = 4)
        
        pledge_bank_canvas = tk.Canvas(self, width = 500, height = 20)
        pledge_bank_canvas.grid(row = 5, column = 0, columnspan = 4)
        pledge_bank_canvas.grid_propagate(False)
        pledge_bank_canvas.grid_columnconfigure(0, weight = 1)
        pledge_bank_canvas.grid_columnconfigure(1, weight = 1)
        
        cash_radio = tk.Radiobutton(pledge_bank_canvas, text = "Cash", font = ("Arial", 12))
        cash_radio.grid(row = 0, column = 0)
        
        bank_radio = tk.Radiobutton(pledge_bank_canvas, text = "Bank", font = ("Arial", 12))
        bank_radio.grid(row = 0, column = 1)
        
        ttk.Separator(self, orient = "horizontal").grid(row = 6, column = 0, sticky = "ew", columnspan = 4)
        
        
        
        
        
        
        
        
        
        