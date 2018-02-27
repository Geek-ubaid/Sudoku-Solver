def printboard(arr):
    for i in range(9):
        print (*arr[i],sep=" ")
       
def isfull(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
 

def check_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 

def check_column(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 

def check_cell(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
 

def check(arr,row,col,num):
     
    
    return not check_row(arr,row,num) and not check_column(arr,col,num) and not check_cell(arr,row//3*3,col//3*3,num)
 

def solveboard(arr):
     
    l=[0,0]
     
    if(not isfull(arr,l)):
        return True
     
    row=l[0]
    col=l[1]
     
    for num in range(1,10):
         
        if(check(arr,row,col,num)):
             
            arr[row][col]=num
 
            if(solveboard(arr)):
                return True
 
            arr[row][col] = 0
        else:
            break
             
    return False
 
def solve(puzzle):     
    
     
    if(solveboard(puzzle)):
        return puzzle
    else:
        return [-1]

def load1():
    return board

global board
board=[[0 for x in range(9)]for y in range(9)]
     
board=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]


 
