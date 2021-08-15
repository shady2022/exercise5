import random
import colorama
from colorama import
from colorama import Fore


game =[["_","_","_"],
       ["_","_","_"],
       ["_","_","_"]]

def show_game():
    for i in range(3):
        for j in range(3):
        print(game[i][j], end=" ")
    
    print()    
    
    print('player 1')
    row = int(input("satr ra wared konid:"))
    col = int(input("sotoon ravared konid:"))
    game[row][col] = "x" 
    
    show_game():
    
    print('player2')
    row = int(input("satr ra vared konid:"))
    col = int(input("sotoon ra vared konid:"))
    game[row][col]= "o"
    
    show_game():
        
    def winner():
        if player [0][0]=='x' and player[0][1]=='x' and player[0][2]=='x':
            print('player 1 winner')
            break
        
        elif player [0][0]=='o' and player[0][1]=='o' and player[0][2]=='o':
            print('player 2 winner')
            break
        
        elif player [1][0]=='x' and player[1][1]=='x' and player[1][2]=='x':
            print('player 1 winner')
            break
        
        elif player [1][0]=='o' and player[1][1]=='o' and player[1][2]=='o':
            print('player 2 winner')
            break
        
        
        elif player [2][0]=='x' and player[2][1]=='x' and player[2][2]=='x':
            print('player 1 winner')
            break
        
        elif player [2][0]=='o' and player[2][1]=='o' and player[2][2]=='o':
            print('player 2 winner')
            break
        
        elif player [0][0]=='x' and player[1][0]=='x' and player[2][0]=='x':
            print('player 1 winner')
            break
        
        elif player [0][0]=='o' and player[1][0]=='o' and player[2][0]=='o':
            print('player 2 winner')
            break
        
        elif player [0][1]=='x' and player[1][1]=='x' and player[2][1]=='x':
            print('player 1 winner')
            break
        
        elif player [0][1]=='o' and player[1][1]=='o' and player[2][1]=='o':
            print('player 2 winner')
            break
        
        elif player [0][2]=='x' and player[1][2]=='x' and player[2][2]=='x':
            print('player 1 winner')
            break
        
        
        elif player [0][2]=='o' and player[1][2]=='o' and player[2][2]=='o':
            print('player 2 winner')
            break
        
        elif player [0][0]=='x' and player[1][1]=='x' and player[2][2]=='x':
            print('player 1 winner')
            break
        
        elif player [0][0]=='o' and player[1][1]=='o' and player[2][2]=='o':
            print('player 2 winner')
            break
        
        elif player [0][2]=='x' and player[1][1]=='x' and player[2][0]=='x':
            print('player 1 winner')
            break
        
        elif player [0][2]=='x' and player[1][1]=='x' and player[2][0]=='x':
            print('player 2 winner')
            break
        
        
        
        
        
        
        
        
        
        
    