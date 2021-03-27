def read_matrix(n):
    matrix = []
    for r in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


n, m = [int(x) for x in input().split()]
size = 3
matrix = read_matrix(n)

max_sum = 0
max_sum_r=0
max_sum_c=0


def find_sum(matrix, r, c,size):
    current_sum=0

    for i in range(r,r+size):
        for j in range(c, c+size):

            current_sum+=matrix[i][j]
    return current_sum


for r in range(n - size+1):
    for c in range(m - size+1):
        current_sum=find_sum(matrix, r,c,size)
        if current_sum>max_sum:
            max_sum=current_sum
            max_sum_c=c
            max_sum_r=r


print(f"Sum = {max_sum}")
for r in range(max_sum_r,max_sum_r+size):
    row=[]
    for c in range(max_sum_c,max_sum_c+size):
        row.append(matrix[r][c])
    print(' '.join(str(x) for x in row))