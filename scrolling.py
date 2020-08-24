# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:12:53 2020

@author: jishn
"""

import tkinter as tk

class Vertical_Scroll(tk.Scrollbar):
    # Container = window
    # Control = canvas
    
    def __init__(self,window, canvas, frame):
        super().__init__(window)
        
        self.window = window
        self.canvas = canvas
        self.frame = frame
        
        self.scrollable_window = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        def configure_scroll_region(event):
            self.canvas.configure(scrollregion=self.bbox("all"))
        
        def configure_window_size(event):
            self.canvas.itemconfig(self.scrollable_window, width=self.canvas.winfo_width())
        
        self.canvas.bind("<Configure>", configure_window_size)
        self.frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=1, column=2, sticky="NS")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.yview_moveto(1.0)
        
    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")
    
    
        
        