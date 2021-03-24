

def read_matrix(n):
    matrix = []
    for r in range(n):
        row = [x for x in input().split()]
        matrix.append(row)


def find_submatrix(matrix_given, size):

    count = 0
    for r in range(len(matrix_given) - size):
        for c in range(size):
            current_element = matrix_given[r][c]
            if current_element == matrix_given[r][c + 1] and current_element == matrix_given[r + 1][c + 1] and current_element == matrix_given[r + 1][c]:
                count += 1
    return count

n, m = [int(x) for x in input().split()]

size = 2

matrix=read_matrix(n)
count=find_submatrix(matrix,size)
