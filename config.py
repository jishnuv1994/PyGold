# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:51:47 2020

@author: jishn
"""

import pandas as pd

def init():
    global custormer_data
    global active_data
    global closed_data
    custormer_data = pd.DataFrame()
    active_data = pd.DataFrame()
    closed_data = pd.DataFrame()
    pass