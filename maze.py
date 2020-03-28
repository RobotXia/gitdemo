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
def solve(image, M):
    path = np.zeros((rows, cols, 2))
    vis = np.zeros((rows, cols))
    vis[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while(queue):
        temp = queue.popleft()
        nr = temp[0]
        nc = temp[1]
 
        if (nc == cols - 1) and (nr == rows - 1):
            plt.axis('off')
            trace(image, path)
            break
        if (nc > 0) and (not vis[nr][nc - 1]) and (M[nr][nc][0]):
            vis[nr][nc] = 1
            queue.append((nr, nc - 1))
            path[nr][nc - 1][0] = nr
            path[nr][nc - 1][1] = nc
        if (nr > 0) and (not vis[nr - 1][nc]) and (M[nr][nc][1]):
            vis[nr][nc] = 1
            queue.append((nr - 1, nc))
            path[nr - 1][nc][0] = nr
            path[nr - 1][nc][1] = nc
        if (nc < cols - 1) and (not vis[nr][nc + 1]) and (M[nr][nc][2]):
            vis[nr][nc] = 1
            queue.append((nr, nc + 1))
            path[nr][nc + 1][0] = nr
            path[nr][nc + 1][1] = nc
        if (nr < rows - 1) and (not vis[nr + 1][nc]) and (M[nr][nc][3]):
            vis[nr][nc] = 1
            queue.append((nr + 1, nc))
            path[nr + 1][nc][0] = nr
            path[nr + 1][nc][1] = nc

def trace(image, path):
    plt.axis('off')
    plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
    plt.ion()
    plt.pause(2)
    str = ""
    stack = []
    nr = rows - 1
    nc = cols - 1
    stack.append((nr, nc + 1))
    stack.append((nr, nc))
    while nr or nc:
        tr = nr
        tc = nc
        nr = (int)(path[tr][tc][0])
        nc = (int)(path[tr][tc][1])
        stack.append((nr, nc))
    pr = 0
    pc = 0
    dir = 2
    while(stack):
        temp = stack.pop()
        nr = temp[0]
        nc = temp[1]
        if nr or nc:
            if (nr == pr):
                if (nc > pc):

                   if (dir == 2):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 10)] = 128
                   elif (dir == 1):
                        image[10 * pr + 4,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 5] = 128
                   elif (dir == 3):
                        image[10 * pr + 4,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 5] = 128
                   dir = 2
                else:
                    if (dir == 0):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 10)] = 128
                    elif (dir == 1):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 5] = 128
                    elif (dir == 3):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 5] = 128
                    dir = 0
            elif (nc == pc):
                if (nr > pr):
                    if (dir == 3):
                        image[range(10 * pr + 0, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 10),10 * pc + 5] = 128
                    elif (dir == 0):
                        image[10 * pr + 4,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 5] = 128
                    elif (dir == 2):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 4, 10 * pr + 10),10 * pc + 5] = 2128
                    dir = 3
                else:
                    if (dir == 1):
                        image[range(10 * pr + 0, 10 * pr + 10),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 10),10 * pc + 5] = 128
                    elif (dir == 0):
                        image[10 * pr + 4,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[10 * pr + 5,range(10 * pc + 4, 10 * pc + 10)] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 5] = 128
                    elif (dir == 2):
                        image[10 * pr + 4,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[10 * pr + 5,range(10 * pc + 0, 10 * pc + 6)] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 4] = 128
                        image[range(10 * pr + 0, 10 * pr + 6),10 * pc + 5] = 128
                    dir = 1
            pr = nr
            pc = nc
            plt.axis('off')
            plt.clf()
            plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
            if not (stack):
                plt.axis('off')
                plt.show()

solve(image, M)
plt.show()

