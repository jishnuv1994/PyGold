# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:27:41 2020

@author: jishn
"""

import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry



class Intrest_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.grid(row = 0, column = 3, sticky = "nsew", padx  = 5)
        
        tk.Label(self, text = "Loan Manager", font = ("Arial", 12, "bold")).grid(row = 0,  column = 0, pady = 5, columnspan = 3)
#----------------------------------------------------------------------------------        
        date_canvas = tk.Canvas(self, width = 290, height = 85)
        date_canvas.grid(row = 1, column = 0, padx = 20, sticky = "w")
        date_canvas.grid_propagate(False)
        date_canvas.grid_columnconfigure(0, weight = 1)
        date_canvas.grid_columnconfigure(1, weight = 1)
        
        tk.Label(date_canvas, text = "Date ", width = 10, anchor = "w",
                  font = ("Arial", 12)).grid(row = 0, column = 0, pady = 2, sticky = "w")
        
        DateEntry(date_canvas,style='my.DateEntry',
                  font = ("Arial", 12), width = 10).grid(row = 0, column = 1, sticky = "w")
        tk.Label(date_canvas, text = "No. of Days ",  anchor = "w",
                 width = 10, font = ("Arial", 12)).grid(row = 1, column = 0, sticky = "w")
        tk.Label(date_canvas, text = "25 ", width = 10,
                 font = ("Arial", 12, "bold")).grid(row = 1, column = 1, pady = 2, sticky = "w")
        
        tk.Label(date_canvas, text = "Intrest ", width = 10, anchor = "w",
                 font = ("Arial", 12)).grid(row = 2, column = 0, sticky = "w")
        tk.Label(date_canvas, text = "2500 ", width = 10
                 , font = ("Arial", 12, "bold")).grid(row = 2, column = 1, pady = 2, sticky = "w")
        
        
        
#----------------------------------------------------------------------------------
        ttk.Separator(self, orient = "vertical").grid(row = 1, column = 1, sticky = "NS", padx = 4)
        
        addition_canvas = tk.Canvas(self, width = 280, height = 75)
        addition_canvas.grid(row = 1, column = 2, padx = 10)
        addition_canvas.grid_propagate(False)
        
        tk.Label(addition_canvas, text = "Addition ", width = 10, font = ("Arial", 12)).grid(row = 0, column = 0, pady = 5)
        
        addition_entry = tk.Entry(addition_canvas, width = 15, font = ("Arial", 15, "bold"))
        addition_entry.grid(row = 1, column = 0)
        
        addition_button = tk.Button(addition_canvas, text = "Save Addition", width = 10, height = 3,
                                    font = ("Arial", 12), wraplength = 65)
        addition_button.grid(row = 0, column = 1, rowspan = 2, padx = 5, pady = 5)
        
#----------------------------------------------------------------------------------
        
        ttk.Separator(self, orient = "horizontal").grid(row = 2, column = 0, sticky = "ew", columnspan = 3)
        
        receipt_canvas = tk.Canvas(self, width = 600, height = 75)
        receipt_canvas.grid(row = 3, column = 0, columnspan = 3)
        receipt_canvas.grid_propagate(False)
        
        tk.Label(receipt_canvas, text = "Capital Receipt", font = ("Arial", 12)).grid(row = 0, column = 0)
        captal_reciept_entry = tk.Entry(receipt_canvas, font = ("Arial", 15, "bold"))
        captal_reciept_entry.grid(row = 1, column = 0, padx = 10)
        
        tk.Label(receipt_canvas, text = "Intrest Receipt", font = ("Arial", 12)).grid(row = 0, column = 1)
        intrest_reciept_entry = tk.Entry(receipt_canvas, font = ("Arial", 15, "bold"))
        intrest_reciept_entry.grid(row = 1, column = 1, padx = 15)
        
        addition_button = tk.Button(receipt_canvas, text = "Save Receipt", width = 10, height = 3,
                                    font = ("Arial", 12), wraplength = 65)
        addition_button.grid(row = 0, column = 2, rowspan = 2, padx = 7, pady = 5)
        
        
#----------------------------------------------------------------------------------
        
        ttk.Separator(self, orient = "horizontal").grid(row = 4, column = 0, sticky = "ew", columnspan = 3)
        
        release_canvas = tk.Canvas(self, width = 600, height = 75)
        release_canvas.grid(row = 5, column = 0, columnspan = 3, sticky = "w", padx = 20)
        release_canvas.grid_propagate(False)
        
        tk.Label(release_canvas, text = "Service Charges ",  anchor = "w",
                 font = ("Arial", 12)).grid(row = 0, column = 0, sticky = "w")
        service_entry = tk.Entry(release_canvas, width = 16)
        service_entry.grid(row = 0, column = 1, padx = 10)
        
        
        tk.Label(release_canvas, text = "Discount ",  anchor = "w",
                 font = ("Arial", 12)).grid(row = 1, column = 0, sticky = "w")
        discount_entry = tk.Entry(release_canvas, width = 16)
        discount_entry.grid(row = 1, column = 1)
        
        tk.Label(release_canvas, text = "Total Amount ", font = ("Arial", 15, "bold")).grid(row = 0, column = 2)
        total_entry = tk.Entry(release_canvas, font = ("Arial", 15, "bold"))
        total_entry.grid(row = 1, column = 2, padx = 15)
        
        release_button = tk.Button(release_canvas, text = "Release", width = 10, height = 3,
                                    font = ("Arial", 12), wraplength = 65)
        release_button.grid(row = 0, column = 3, rowspan = 2, padx = 5, pady = 5)
        
#------------------------------------------------------------------------------------
        
        ttk.Separator(self, orient = "horizontal").grid(row = 6, column = 0, sticky = "ew", columnspan = 3)
        
        token_canvas = tk.Canvas(self, width = 600, height = 35)
        token_canvas.grid(row = 7, column = 0, columnspan = 3, sticky = "ew")
        token_canvas.grid_propagate(False)
        token_canvas.grid_columnconfigure(0, weight = 1)
        token_canvas.grid_columnconfigure(1, weight = 1)
        
        token_radio = tk.Radiobutton(token_canvas, text = "Token Presented", font = ("Arial", 12), anchor = "center")
        token_radio.grid(row = 0, column = 0, sticky = "ew")
        
        no_token_radio = tk.Radiobutton(token_canvas, text = "Token Not Presented", font = ("Arial", 12), anchor = "center")
        no_token_radio.grid(row = 0, column = 1, sticky = "ew")
        
#-----------------------------------------------------------------------------------
        
        ttk.Separator(self, orient = "horizontal").grid(row = 8, column = 0, sticky = "ew", columnspan = 3)
        
        bank_canvas = tk.Canvas(self, width = 600, height = 20)
        bank_canvas.grid(row = 9, column = 0, columnspan = 3)
        bank_canvas.grid_propagate(False)
        bank_canvas.grid_columnconfigure(0, weight = 1)
        bank_canvas.grid_columnconfigure(1, weight = 1)
        
        cash_radio = tk.Radiobutton(bank_canvas, text = "Cash", font = ("Arial", 12))
        cash_radio.grid(row = 0, column = 0)
        
        bank_radio = tk.Radiobutton(bank_canvas, text = "Bank", font = ("Arial", 12))
        bank_radio.grid(row = 0, column = 1)
        
        
        
        ttk.Separator(self, orient = "horizontal").grid(row = 10, column = 0, sticky = "ew", columnspan = 4)