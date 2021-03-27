def read_square_matrix(n):
    matrix=[]
    for r in range(n):
        row=[int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def sum_of_primary_diagonal(matrix):
    primary_sum=0
    for r in range(len(matrix)):

            primary_sum+=matrix[r][r]
    return primary_sum


def sum_of_secondary_diagonal(matrix):
    secondary_sum = 0
    for r in range(len(matrix)):
        secondary_sum += matrix[r][len(matrix)-r-1]
    return secondary_sum


n=int(input())
matrix=read_square_matrix(n)
result=abs(sum_of_primary_diagonal(matrix)-sum_of_secondary_diagonal(matrix))
print(result)