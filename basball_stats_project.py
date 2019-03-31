# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:07:27 2019

@author: ddow2
"""

import pandas as pd
import numpy as np
import csv
import os

df = pd.read_csv(r'C:\\Stuff\\stats2010_2018.csv')
df2=df.loc[df.Team=='ange', 'Season':'Run']
df2.to_csv('angels.csv', encoding='utf-8', index=False)
    
print(df2)