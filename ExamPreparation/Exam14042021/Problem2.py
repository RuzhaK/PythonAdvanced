import math

size=int(input())


def read_matrix(size):
    matrix=[]
    for i in range(size):
        matrix.append(input().split())
    return matrix


field=read_matrix(size)
path=[]


def find_position(symbol, field):
    for i in range(len(field)):
        for j in range (len(field)):
            if symbol==field[i][j]:
                return i, j




P_position=find_position("P", field)

game_over=False
coins=0

def move(delta_row, delta_col):
    global game_over, P_position,path,size,coins
    y,x=P_position
    new_y=y+delta_row
    new_x=x+delta_col
    if 0>new_x or new_x>size-1 or 0>new_y or new_y>size-1 or field[new_y][new_x]=="X":
        game_over=True
        coins=math.floor(coins/2)
        return
    print()
    number=int(field[new_y][new_x])
    coins+=number

    path.append([new_y,new_x])
    P_position=(new_y,new_x)
    if coins>=100:
        game_over=True






ops={
    'up':lambda :move(-1,0),
    'down':lambda :move(1,0),
    'left':lambda :move(0,-1),
    'right':lambda :move(0,1),
     }

while True:

    if game_over==True:
        break
    command=input()
    if not command in ops:
        continue

    move_fn=ops[command]
    move_fn()

if coins>=100:
    print(f"You won! You've collected {math.floor(coins)} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins)} coins.")

print(f"Your path:")
for p in path:
    print(p)