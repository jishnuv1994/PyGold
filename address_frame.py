# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:30:37 2020

@author: jishn
"""


import tkinter as tk
from tkinter import ttk


from tkcalendar import DateEntry



class Address_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.config( background = "violet")
        self.grid(row = 0, column = 2, sticky = "NSEW")
#        top_frame.columnconfigure(2, weight = 1)
        
        #------------------------------------------------------------
        first_line_frame = tk.Frame(self)
        first_line_frame.grid(row = 0, column = 0, columnspan = 3, sticky = "W")
        
        tk.Label(first_line_frame, text = "Pledge No. ", width = 15).grid(row = 0, column = 0)
        pledge_no_entry = tk.Entry(first_line_frame, font = ("Arial", 15, "bold"), width = 25)
        pledge_no_entry.grid(row = 0, column = 1)
        
        tk.Label(first_line_frame, text = "Date ", width = 7).grid(row = 0, column = 2)
        DateEntry(first_line_frame,style='my.DateEntry', font = ("Arial", 12), width = 10).grid(row = 0, column = 3)
        
        #----------------------------------------------------------
        
        second_line_frame = tk.Frame(self)
        second_line_frame.grid(row = 1, column = 0, columnspan = 3, sticky = "W")
        
        tk.Label(second_line_frame, text = "Name ", width = 15).grid(row = 0, column = 0)
        name_entry = tk.Entry(second_line_frame,font = ("Arial", 15), width = 23)
        name_entry.grid(row = 0, column = 1)
        
        search_button = tk.Button(second_line_frame, text = "S", width = 2)
        search_button.grid(row = 0, column = 2)
        
        tk.Label(second_line_frame, text = "C Code ", width = 7).grid(row = 0, column = 3)
        customer_entry = tk.Entry(second_line_frame, font = ("Arial", 12), width = 12)
        customer_entry.grid(row = 0, column = 4)
        
        #---------------------------------------------------------
        
        tk.Label(self, text = "Phone No. ", width =15).grid(row = 2, column = 0, sticky = "w")
        phone_entry = tk.Entry(self, width = 49, font = ("Arial", 13))
        phone_entry.grid(row = 2, column = 1)
        
        tk.Label(self, text = "House ", width =15).grid(row = 3, column = 0, sticky = "w")
        house_entry = tk.Entry(self, width = 49, font = ("Arial", 13))
        house_entry.grid(row = 3, column = 1)
        #////////////////////////////////////////
        location_frame = tk.Frame(self)
        location_frame.grid(row = 4, column = 0, columnspan = 2)
        
        tk.Label(location_frame, text = "Location ", width =15).grid(row = 0, column = 0, sticky = "w")
        location_entry = tk.Entry(location_frame, width = 23, font = ("Arial", 13))
        location_entry.grid(row = 0, column = 1)
        
        tk.Label(location_frame, text = "KYC type ", width =10).grid(row = 0, column = 2, sticky = "w")
        kyc_type_entry = tk.Entry(location_frame, width = 17, font = ("Arial", 13))
        kyc_type_entry.grid(row = 0, column = 3)       
        #///////////////////////////////////////
        
        po_frame = tk.Frame(self)
        po_frame.grid(row = 5, column = 0, columnspan = 2)
        
        
        tk.Label(po_frame, text = "Post Office ", width =15).grid(row = 0, column = 0, sticky = "w")
        po_entry = tk.Entry(po_frame, width = 23, font = ("Arial", 13))
        po_entry.grid(row = 0, column = 1)
        
        tk.Label(po_frame, text = "KYC No. ", width =10).grid(row = 0, column = 2, sticky = "w")
        kyc_type_entry = tk.Entry(po_frame, width = 17, font = ("Arial", 13))
        kyc_type_entry.grid(row = 0, column = 3)   
        
        
        
        
         #----------------------------------------------------------
        
        nominee_line_frame = tk.Frame(self)
        nominee_line_frame.grid(row = 6, column = 0, columnspan = 3, sticky = "W")
        
        tk.Label(nominee_line_frame, text = "Nominee ", width = 15).grid(row = 0, column = 0)
        nominee_entry = tk.Entry(nominee_line_frame,font = ("Arial", 13), width = 28)
        nominee_entry.grid(row = 0, column = 1)
        
        nominee_search_button = tk.Button(nominee_line_frame, text = "S", width = 2)
        nominee_search_button.grid(row = 0, column = 2)
        
        tk.Label(nominee_line_frame, text = "C Code ", width = 7).grid(row = 0, column = 3)
        nominee_entry = tk.Entry(nominee_line_frame, font = ("Arial", 13), width = 12)
        nominee_entry.grid(row = 0, column = 4)
        
        #---------------------------------------------------------
        
        rating_frame = tk.Frame(self)
        rating_frame.grid(row = 7, column = 0, columnspan = 3, sticky = "w")
        
        rating_label = tk.Label(rating_frame, text = "Customer rating ", width = 15)
        rating_label.grid(row = 0, column = 0, sticky = "w")
        
        bad_radio = tk.Radiobutton(rating_frame, text = "Bad",font = ("Arial", 13))
        bad_radio.grid(row = 0, column = 1, sticky = "w", padx = 34)
        bad_radio = tk.Radiobutton(rating_frame, text = "Average",font = ("Arial", 13))
        bad_radio.grid(row = 0, column = 2, sticky = "w", padx = 34)
        bad_radio = tk.Radiobutton(rating_frame, text = "Excellent",font = ("Arial", 13))
        bad_radio.grid(row = 0, column = 3, sticky = "w", padx = 34)
        
        
        remark_label = tk.Label(rating_frame, text = "Remarks ", width = 15)
        remark_label.grid(row = 1, column = 0, sticky = "w")
        
        remark_entry = tk.Text(rating_frame, width = 55, height = 4)
        remark_entry.grid(row = 1, column = 1, columnspan = 3)
         
        
        
        for child in self.winfo_children():
            child.grid_configure(pady=6)