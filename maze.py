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


while prev: 
    x,y = random.choice(prev)
    M[x,y,4] = 1 
    prev.remove((x,y))
    check = []
    if y > 0:
        if M[x,y-1,4] == 1:
            check.append('Left')
        elif M[x,y-1,4] == 0:
            prev.append((x,y-1))
            M[x,y-1,4] = 2
    if x > 0:
        if M[x-1,y,4] == 1: 
            check.append('Up') 
        elif M[x-1,y,4] == 0:
            prev.append((x-1,y))
            M[x-1,y,4] = 2
    if y < cols-1:
        if M[x,y+1,4] == 1: 
            check.append('Right')
        elif M[x,y+1,4] == 0:
            prev.append((x,y+1))
            M[x,y+1,4] = 2 
    if x < rows-1:
        if M[x+1,y,4] == 1: 
            check.append('Down') 
        elif  M[x+1,y,4] == 0:
            prev.append((x+1,y))
            M[x+1,y,4] = 2
    if len(check):
        direction = random.choice(check)
        if direction == 'Left':
            M[x,y,0] = 1
            y = y-1
            M[x,y,2] = 1
        if direction == 'Up':
            M[x,y,1] = 1
            x = x-1
            M[x,y,3] = 1
        if direction == 'Right':
            M[x,y,2] = 1
            y = y+1
            M[x,y,0] = 1
        if direction == 'Down':
            M[x,y,3] = 1
            x = x+1
            M[x,y,1] = 1
M[0,0,0] = 1
M[rows-1,cols-1,2] = 1

for row in range(0,rows):
    for col in range(0,cols):
        room = M[row,col]
        for i in range(10*row+2,10*row+8):
            image[i,range(10*col+2,10*col+8)] = 255
        if room[0] == 1 or room[0]==9: 
            image[range(10*row+2,10*row+8),10*col] = 255
            image[range(10*row+2,10*row+8),10*col+1] = 255
        if room[1] == 1 or room[1]==9: 
            image[10*row,range(10*col+2,10*col+8)] = 255
            image[10*row+1,range(10*col+2,10*col+8)] = 255
        if room[2] == 1 or room[2] == 9: 
            image[range(10*row+2,10*row+8),10*col+9] = 255
            image[range(10*row+2,10*row+8),10*col+8] = 255
        if room[3] == 1 or room[3] == 9: 
            image[10*row+9,range(10*col+2,10*col+8)] = 255
            image[10*row+8,range(10*col+2,10*col+8)] = 255

for row in range(rows-lenminus,rows):
    for col in range(widminus):
        for i in range(10*row,10*row+10):
            image[i,range(10*col,10*col+10)] = 255
for row in range(lenminus):
    for col in range(cols-widminus,cols):
        for i in range(10*row,10*row+10):
            image[i,range(10*col,10*col+10)] = 255

