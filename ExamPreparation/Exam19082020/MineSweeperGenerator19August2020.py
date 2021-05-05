NEIGHBOURING_CELLS=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

board_size=int(input())
n=int(input())
minefield=[[0]*board_size for _ in range(board_size)]


def parse_mines_tuple(tuple_str):
    # това е един вариант евал обръща стринга в код
    return eval(tuple_str)
    # return tuple(tuple_str[1:-1].split(", "))


def add_mine_to_field(i, j):
    minefield[i][j]="*"


for _ in range(n):
    
    i,j=parse_mines_tuple(input())
    add_mine_to_field(i,j)
# update board


def is_valid_coordinates(i,j):
    if 0<=i<len(minefield) and 0<=j<len(minefield):
        return True
    return False


def get_sum_of_mines_nearby(i, j):
    num_mines=0

    for delta_i, delta_j in NEIGHBOURING_CELLS:
        if is_valid_coordinates(i + delta_i, j + delta_j):
            if is_mine(i+delta_i,j+delta_j):
                num_mines+=1
    return num_mines


def is_mine(i, j):
    return minefield[i][j]=="*"


for i in range(board_size):
    for j in range(board_size):
        if not is_mine(i,j):
            minefield[i][j]=get_sum_of_mines_nearby(i,j)

def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(f"{matrix[r][c]}", end=' ')
        print()

print_matrix(minefield)