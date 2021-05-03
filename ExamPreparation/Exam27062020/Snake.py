n=int(input())
territory=[list(input()) for _ in range(n)]
food=0
NEEDED_FOOD=10
game_over=False


def move(delta_y, delta_x):
    global snake_pos,game_over,food
    y,x =snake_pos
    territory[y][x]='.'
    new_y=y+delta_y
    new_x=x+delta_x
    if 0 >new_x or new_x>n-1 or 0 >new_y or new_y>n-1:
        game_over=True
        return
    at_pos=territory[new_y][new_x]
    if at_pos=="B":
        territory[new_y][new_x]='.'
        new_y,new_x=search_matrix(territory,'B')
    if at_pos == "*":
        food+=1
        if food>=NEEDED_FOOD:
            game_over=True
    territory[new_y][new_x]='S'
    snake_pos=(new_y,new_x)


ops={
    'up':lambda :move(-1,0),
    'down':lambda :move(1,0),
    'left':lambda :move(0,-1),
    'right':lambda :move(0,1),
     }

# todo enumerate


def search_matrix(matrix,search):
    for y, row in enumerate(matrix):
        for x,char in enumerate(row):
            if char==search:
                return y,x


snake_pos=search_matrix(territory,'S')


# todo осмисли принта:


def print_territory(territory):
    print('\n'.join([''.join(row) for row in territory]))


def are_coordinates_valid():
    pass
while not game_over:
    command=input()
    # todo tuk izvikwame taka funkciata move s razlichni koordinati
    move_fn=ops[command]
    move_fn()

if game_over and food<10:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
print_territory(territory)