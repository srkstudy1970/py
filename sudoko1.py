# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:11:29 2020

https://www.youtube.com/watch?v=G_UYXzGuqvM

@author: Ravi
"""

import numpy as np

#print("hello World")
grid0=[[12],[23]]
grid=[[1,2,3,0,0,0,0,6,0],
      [6,5,4,0,0,0,0,0,0],
      [7,8,9,0,0,0,0,0,0],
      [0,0,0,0,5,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]

#grid=np.matrix(grid1)

print (np.matrix(grid))

#print(grid)


def possible(x,y,n):
    global grid
    xcount=0
    ycount=0
    #print("x = " +str(x)+" y = " +str(y)+" the value of in that position is "+str(grid[x][y])+" value of n is "+str(n))
    
    for i in range(0,9):
        if grid[i][x] == n:
            xcount=xcount+1
            #print("xcount is "+str(xcount))
            #print(grid[x,i])
            return False
        
    for j in range(0,9):
        if grid[j][y] == n:
            ycount=ycount+1
            #print("ycount is "+str(ycount))
            #print("Yes")
            return False
        
    return True

def solve ():
    
    global grid    
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                for k in range(0,10):
                    if possible(i,j,k):
                        grid[i][j] = k
                        solve()
                        grid[i][j]=0
                        #print(grid[i][j])
                return
    print(np.matrix(grid))
    input("More?")
    

solve()
