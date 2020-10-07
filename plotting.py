# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:07:18 2020

@author: Surface
"""

import random
import matplotlib.pyplot as plt

for i in range(10000):
    x = random.random()
    y = random.random()
    d = (x - 0.5)**2 + (y - 0.5)**2
    if d<x**2 and d < y**2 and d<(1-x)**2 and d<(1-y)**2:
        plt.scatter(x, y)