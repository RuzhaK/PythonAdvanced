def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],

        ]
    else:
        size=input()
        matrix=[]
        for row in range(size):
            row=[int(x) for x in input().split()]
            matrix.append(row)
        return matrix


def get_sum_of_secondary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)

    for i in range(size):
        diagonal_sum += matrix[i][size-i-1]
    return diagonal_sum

def get_sum_above_primary_diagonal(matrix):
    the_sum=0
    size=len(matrix)
    for r in range(size):
        for c in range (r,size):
            the_sum+=matrix[r][c]
    return the_sum
print(get_sum_above_primary_diagonal(read_matrix(is_test=True)))
print(get_sum_of_secondary_diagonal(read_matrix(is_test=True)))