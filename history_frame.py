# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:39:23 2020

@author: jishn
"""


import tkinter as tk
from tkinter import ttk


class History_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(background = "orange")
        self.grid(row = 0, column = 4, sticky = "NSEW")
        container.columnconfigure(4, weight = 1)
       
        
        tk.Label(self, text = "In Locker ").grid(row = 0, column = 0, sticky = "ew")
        
        self.locker_function()
        
                
        tk.Label(self, text  = "Total ").grid(row = 3, column = 0, pady = 3, sticky = "w", padx = 5)
        
        
        tk.Label(self, text = "Transation History ").grid(row = 4, column = 0)
        
        self.history_function()
        
        
#--------------------------------------------------------------------------------------
    def locker_function(self):
        
        
            self.locker_select_all_var = tk.IntVar()
            self.locker_select_all_var.set(0)
            
            
            def tree_all():
                items = locker_tree.get_children()
                if self.locker_select_all_var.get() == 1:
                    for select in items:
                        locker_tree.selection_add(select)
                        
                else:
                    for select in items:
                        locker_tree.selection_remove(select)
            
            def tree_selection(event):
                self.locker_select_all_var.set(0)
                print(locker_tree.selection())
                
            
            locker_select_all = tk.Checkbutton(self, text = "Select All", 
                                               variable = self.locker_select_all_var,
                                               command = tree_all)
            locker_select_all.grid(row = 1, column = 0, sticky = 'w', padx = 5)
            
            locker_canvas = tk.Canvas(self, background = "yellow")
            locker_canvas.grid(row = 2, column = 0, sticky = "nsew", padx = 5)
            self.columnconfigure(0, weight = 1)
            self.rowconfigure(2, weight = 1)
            
            
            locker_tree=ttk.Treeview(locker_canvas, height = 6, selectmode = "extended")
            locker_tree.grid(row = 0, column = 0, sticky = "nsew")
            locker_canvas.columnconfigure(0, weight = 1)
            
            
            
            locker_tree["columns"]=("one","two","three", "four", "five")
            locker_tree.column("#0", width=100, stretch=tk.NO)
            locker_tree.column("one", width=100, stretch=tk.NO)
            locker_tree.column("two", width=100, stretch=tk.NO)
            locker_tree.column("three", width=100, stretch=tk.NO)
            locker_tree.column("four", width=100, stretch=tk.NO)
            locker_tree.column("five", width=100, stretch=tk.NO)
            
            locker_tree.heading("#0",text="Pledge No.",anchor=tk.W, command = tree_selection)
            locker_tree.heading("one", text="Date",anchor=tk.W, command = tree_selection)
            locker_tree.heading("two", text="Weight",anchor=tk.W, command = tree_selection)
            locker_tree.heading("three", text="Capital",anchor=tk.W, command = tree_selection)
            locker_tree.heading("four", text="Intrest",anchor=tk.W, command = tree_selection)
            locker_tree.heading("five", text="Total",anchor=tk.W, command = tree_selection)
            
            
            
            locker_tree.insert("", 'end', text ="L1",  
                 values =("Nidhi", "F", "25")) 
            locker_tree.insert("", 'end', text ="L2", 
                 values =("Nisha", "F", "23")) 
            locker_tree.insert("", 'end', text ="L3", 
                 values =("Preeti", "F", "27")) 
            locker_tree.insert("", 'end', text ="L4", 
                 values =("Rahul", "M", "20")) 
            locker_tree.insert("", 'end', text ="L5",  
                 values =("Sonu", "F", "18")) 
            locker_tree.insert("", 'end', text ="L6", 
                 values =("Rohit", "M", "19")) 
            locker_tree.insert("", 'end', text ="L7",  
                 values =("Geeta", "F", "25")) 
            locker_tree.insert("", 'end', text ="L8",  
                 values =("Ankit", "M", "22")) 
            locker_tree.insert("", 'end', text ="L10",  
                 values =("Mukul", "F", "25")) 
            locker_tree.insert("", 'end', text ="L11", 
                 values =("Mohit", "M", "16")) 
            locker_tree.insert("", 'end', text ="L12", 
                 values =("Vivek", "M", "22")) 
            locker_tree.insert("", 'end', text ="L13", 
                 values =("Suman", "F", "30")) 
            
            
            locker_tree.bind("<ButtonRelease>",tree_selection)
            
            verscrlbar = ttk.Scrollbar(locker_canvas,  
                               orient ="vertical",  
                               command = locker_tree.yview)
            verscrlbar.grid(row = 0, column = 1, sticky = "ns")
            locker_tree.configure(yscrollcommand = verscrlbar.set) 
            
#------------------------------------------------------------------------------------
        
    def history_function(self):
            transation_canvas = tk.Canvas(self, background = "yellow")
            transation_canvas.grid(row = 5, column = 0, sticky = "nsew", padx = 5)
            
            self.rowconfigure(5, weight = 1)
            
            
            transation_tree=ttk.Treeview(transation_canvas, height = 5, selectmode = "none")
            transation_tree.grid(row = 0, column = 0, sticky = "nsew")
            transation_canvas.columnconfigure(0, weight = 1)
            
            transation_tree["columns"]=("one","two","three", "four", "five", "six")
            transation_tree.column("#0", width=100, stretch=tk.NO)
            transation_tree.column("one", width=100, stretch=tk.NO)
            transation_tree.column("two", width=90, stretch=tk.NO)
            transation_tree.column("three", width=80, stretch=tk.NO)
            transation_tree.column("four", width=75, stretch=tk.NO)
            transation_tree.column("five", width=70, stretch=tk.NO)
            transation_tree.column("six", width=85, stretch=tk.NO)
            
            transation_tree.heading("#0",text="Pledge No.",anchor=tk.W)
            transation_tree.heading("one", text="Date",anchor=tk.W)
            transation_tree.heading("two", text="Addition Pay",anchor=tk.W)
            transation_tree.heading("three", text="Capital Rec.",anchor=tk.W)
            transation_tree.heading("four", text="Intrest Rec.",anchor=tk.W)
            transation_tree.heading("five", text="Discount",anchor=tk.W)
            
            transation_tree.heading("six", text="Total",anchor=tk.W)
            
            transation_tree.insert("", 'end', text ="L1",  
                 values =("Nidhi", "F", "25")) 
            transation_tree.insert("", 'end', text ="L2", 
                 values =("Nisha", "F", "23")) 
            transation_tree.insert("", 'end', text ="L3", 
                 values =("Preeti", "F", "27")) 
            transation_tree.insert("", 'end', text ="L4", 
                 values =("Rahul", "M", "20")) 
            transation_tree.insert("", 'end', text ="L5",  
                 values =("Sonu", "F", "18")) 
            transation_tree.insert("", 'end', text ="L6", 
                 values =("Rohit", "M", "19")) 
            transation_tree.insert("", 'end', text ="L7",  
                 values =("Geeta", "F", "25")) 
            transation_tree.insert("", 'end', text ="L8",  
                 values =("Ankit", "M", "22")) 
            transation_tree.insert("", 'end', text ="L10",  
                 values =("Mukul", "F", "25")) 
            transation_tree.insert("", 'end', text ="L11", 
                 values =("Mohit", "M", "16")) 
            transation_tree.insert("", 'end', text ="L12", 
                 values =("Vivek", "M", "22")) 
            transation_tree.insert("", 'end', text ="L13", 
                 values =("Suman", "F", "30")) 
            
            
            verscrlbar = ttk.Scrollbar(transation_canvas,  
                               orient ="vertical",  
                               command = transation_tree.yview)
            verscrlbar.grid(row = 0, column = 1, sticky = "ns")
            transation_tree.configure(yscrollcommand = verscrlbar.set) 