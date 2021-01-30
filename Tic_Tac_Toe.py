
'''
---
---
---
'''

grid_dict = {1 : '1' , 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
'''

   |   |
   |   |
   |   |
============
   |   |
   |   |
   |   |
============
   |   |
   |   |
   |   |
'''

def display_row(grid_dict,row_num):
    print('   |   |   ')
    print(' {} | {} | {} '.format(grid_dict[1 + 3*(row_num-1)],grid_dict[2 + 3*(row_num-1)], grid_dict[3 + 3*(row_num-1)]))
    print('   |   |   ')
    
def display_line(n):
    print('='*n)
    
def display_board(grid_dict):
    for i in range(1,4):
        display_row(grid_dict,i)
        if i < 3 :
            display_line(12)
        
            
#display_board(grid_dict)    

# HW - Write a function that takes name of first player and asks them what symbol they want (only x or o), do the same for 2nd player. Print all the info.
def roles():
    p1 = str(input('enter your name '))
    p1s = str(input('Choose between x and o '))
    p2 = str(input('enter your name '))
    if p1s == 'x':
             p2s = 'o'
    else:
        p2s = 'x'
    return ((p1,p1s),(p2,p2s))

((p1 , p1s) , (p2 , p2s)) = roles()

def row_win(grid_dict,row_num,symbol):
    
    if grid_dict[1 + 3*(row_num)] == symbol and grid_dict[2 + 3*(row_num)] == symbol and grid_dict[1 + 3*(row_num-1)] == symbol:
        return True
    else:
        return False
def column_win(grid_dict,col_num,symbol):
    if grid_dict[col_num+1] == symbol and grid_dict[col_num+4] == symbol and grid_dict[col_num+7] == symbol:
        return True
    else:
        return False
    

def ldiagnol_win(grid_dict,symbol):
    if grid_dict[1] == symbol and grid_dict[5] == symbol and grid_dict[9] == symbol:
        return True
    else:
        return False
def rdiagnol_win(grid_dict,symbol):
    if grid_dict[3] == symbol and grid_dict[5] == symbol and grid_dict[7] == symbol:
        return True
    else:
        return False

def win(symbol,grid):
    for i in range(3):
        if row_win(grid,i,symbol) == True or column_win(grid,i,symbol) == True:
            return True
    if ldiagnol_win(grid,symbol) == True or rdiagnol_win(grid,symbol) == True:
        return True
    
    return False

def draw_game(grid_dict):
    for i in grid_dict.values():
        if i != 'x' and i != 'o':
            return False
    return True
while True:    
    current_player = 1
    grid_dict = {1 : '1' , 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
    display_board(grid_dict)
    while True:
        
        if current_player == 1:
            position = int(input(' {} pls enter the position of your symbol {} from 1 to 9 '.format(p1,p1s)))
            if position > 0 and position < 10:
                 if grid_dict[position] != 'x' and grid_dict[position] != 'o':
                     grid_dict[position] = p1s
                     display_board(grid_dict)
                 else:
                     print('Sorry, the position is already occupied')
                     continue
            else:
                print('Pls enter a valid position')
                continue
            if win(p1s,grid_dict) :
                print('{} has won'.format(p1))
                break
            if draw_game(grid_dict):
                print('The game has ended in a draw')
                break
            current_player += 1

        if current_player == 2:
            position = int(input(' {} pls enter the position of your symbol {} from 1 to 9 '.format(p2,p2s)))
            if position > 0 and position < 10:
                 if grid_dict[position] != 'x' and grid_dict[position] != 'o':
                     grid_dict[position] = p2s
                     display_board(grid_dict)
                 else:
                     print('Sorry, the position is already occupied')
                     continue
            else:
                print('Pls enter a valid position')
                continue
            if win(p2s,grid_dict) :
                print('{} has won'.format(p2))
                break
            if draw_game(grid_dict):
                print('The game has ended in a draw')
                break
            current_player -= 1
        
    play_again = int(input('If you want to play again press 1, To exit press 2 '))
    if play_again == 1:
        continue
    else:
        break
                     
