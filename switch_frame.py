# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:35:24 2020

@author: jishn
"""
import tkinter as tk
from tkinter import ttk

import config


class Switch_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row = 1, column = 0, sticky = "NS")
        
        
        
        
        gold_switch = tk.Button(self, text = "Gold Loan")
        gold_switch.grid(row = 0, column = 0)
        
        account_switch = tk.Button(self, text = "Accounts Manager")
        account_switch.grid(row = 1, column = 0)
        
        deposit_switch = tk.Button(self, text = "Deposit Details")
        deposit_switch.grid(row = 2, column = 0)
        
        cashbook_switch = tk.Button(self, text = "Cash Book")
        cashbook_switch.grid(row = 3, column = 0)
        
        report_swicth = tk.Button(self, text = "Reports")
        report_swicth.grid(row = 4, column = 0)
        
        
        
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=16)
            child.config(height = 4, width = 16, font = ("Arial", 15, "bold"))
        
