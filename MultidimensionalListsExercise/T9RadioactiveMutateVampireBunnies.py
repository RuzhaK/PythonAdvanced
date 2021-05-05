n, m = [int(x) for x in input().split()]
alive=True
def read_matrix(n,m):
    matrix = []
    for _ in range(n):
        row=[]
        for el in input():
            row.append(el)
        matrix.append(row)

    return matrix


matrix=read_matrix(n,m)
commands=input()
def find_coordinates(symbol, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==symbol:
                return (i,j)


r,c=find_coordinates('P', matrix)
matrix[r][c]='.'
def find_bunnies(matrix):
    bunnies_coordinates=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]=="B":
                bunnies_coordinates.append((i,j))
    return bunnies_coordinates



def populate_with_bunnies(matrix):
    coordinates_of_bunnies=find_bunnies(matrix)
    for el in coordinates_of_bunnies:
        i=el[0]
        j=el[1]

        if index_in_range(i-1,j,len(matrix),len(matrix[i])):
            matrix[i-1][j]='B'
        if index_in_range(i,j+1,len(matrix),len(matrix[i])):
            matrix[i][j+1]='B'
        if index_in_range(i +1, j, len(matrix), len(matrix[i])):
            matrix[i+1][j]='B'
        if index_in_range(i, j-1, len(matrix), len(matrix[i])):
            matrix[i][j-1]='B'


def index_in_range(r, c, n,m):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


for command in commands:
    old_r=r
    old_c=c

    if command=="U":
        r=r-1
        c=c

    elif command=="R":
        r=r
        c=c+1
    elif command=="D":
        r=r+1
        c=c
    elif command=="L":
        r=r
        c=c-1
    populate_with_bunnies(matrix)
    if index_in_range(r, c, n, m):
        if matrix[r][c] == 'B':
            alive = False
            break
    else:
        break


for i in range(n):
    print(''.join(str(x) for x in matrix[i]))

if alive:
    print(f"won: {old_r} {old_c}")
else:
    print(f"dead: {r} {c}")
# todo  60 / 100

