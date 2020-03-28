# Script Name   : maze.py
# Author        : Robot Xia
# Created       : 19th June 2019
# Last Modified : 
# Version       : 1.0
# Modifications : 
# Description   : Homework


import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from collections import deque

 
rows = int(input("Width: "))
cols = int(input("Length: "))
lenminus=random.randint(cols//4,cols//3)
widminus=random.randint(rows//4,cols//3)
 

M = np.zeros((rows,cols,5), dtype=np.uint8)
image = np.zeros((rows*10,cols*10), dtype=np.uint8)
x = 0
y = 0
prev = [(x,y)]
for l in range(rows-lenminus,rows):
    for m in range(widminus):
        for n in range (5):
            M[l,m,n]=9
for p in range(lenminus):
    for q in range(cols-widminus,cols):
        for r in range (5):
            M[p,q,r]=9


