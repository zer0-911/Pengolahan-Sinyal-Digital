# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:13:37 2022

@author: ASUS
"""

from sklearn import preprocessing
import numpy as np
x_array = np.array([0,7,2,1,1,9,4,0,0,0,0,0,2,6])
normalized_arr = preprocessing.normalize([x_array])
print(normalized_arr)