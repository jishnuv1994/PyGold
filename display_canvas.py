# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 07:36:54 2020

@author: jishn
"""

import tkinter as tk
import gold_frame


class Display_Canvas(tk.Canvas):
    def __init__(self, container):
        super().__init__(container)
        container.columnconfigure(1, weight =1)
        self.grid(row = 1, column = 1, sticky ="NSEW")
        self.config(background = "white")
        
#--------------------------------------------------------------------------------------------      
        self.gold_object = gold_frame.Gold_Frame(self, background = "white")
        self.scrollable_window = self.create_window((0, 0), window=self.gold_object, anchor="nw")
        
         
        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))
        
        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.gold_object.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=1, column=2, sticky="NS")
        
        self.configure(yscrollcommand=scrollbar.set)
        
        self.yview_moveto(1.0)
#--------------------------------------------------------------------------------------------
        
    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")
        
        
        