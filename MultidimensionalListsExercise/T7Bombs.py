def index_is_valid(r, c, matrix):
    if 0<=r<len(matrix) and 0<=c<len(matrix):
        if matrix[r][c]>0:
            return True
    return False


def detonate_bomb(r_bomb, c_bomb, matrix):
    bomb=matrix[r_bomb][c_bomb]
    matrix[r_bomb][c_bomb]=0
    if index_is_valid(r_bomb-1,c_bomb, matrix):
        matrix[r_bomb-1][c_bomb]-=bomb
    if index_is_valid(r_bomb - 1, c_bomb+1, matrix):
        matrix[r_bomb-1][c_bomb+1]-=bomb
    if index_is_valid(r_bomb, c_bomb + 1, matrix):
        matrix[r_bomb][c_bomb+1]-=bomb
    if index_is_valid(r_bomb + 1, c_bomb + 1, matrix):
        # five_index=
        matrix[r_bomb+1][c_bomb+1]-=bomb

    if index_is_valid(r_bomb + 1, c_bomb, matrix):
        # six_index=
        matrix[r_bomb+1][c_bomb]-=bomb

    if index_is_valid(r_bomb +1, c_bomb - 1, matrix):
        # seven_index=
        matrix[r_bomb+1][c_bomb-1]-=bomb

    if index_is_valid(r_bomb, c_bomb - 1, matrix):
        # nine_index=
        matrix[r_bomb][c_bomb-1]-=bomb

    if index_is_valid(r_bomb - 1, c_bomb - 1, matrix):
        # eleven_index=
        matrix[r_bomb-1][c_bomb-1]-=bomb


n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list([int(x)  for x in input().split()]))

line=input().split()

for i in range(len(line)):

    r_bomb, c_bomb=[int(x) for x in line[i].split(',')]
    detonate_bomb(r_bomb,c_bomb,matrix)

sum_alive_cells=0
count_alive_cells=0
for i in range(n):
    for j in range(n):
        if matrix[i][j]>0:
            count_alive_cells+=1
            sum_alive_cells+=matrix[i][j]

print(f"Alive cells: {count_alive_cells}")
print(f"Sum: {sum_alive_cells}")

for i in range(n):
    # for j in range(n):
    print(' '.join(str(x) for x in matrix[i]))



