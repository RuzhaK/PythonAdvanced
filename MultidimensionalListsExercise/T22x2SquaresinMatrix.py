def read_matrix(n):
    matrix = []
    for r in range(n):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


def find_submatrix(matrix_given, r, c):
    current_element = matrix_given[r][c]
    if current_element == matrix_given[r][c + 1] and current_element == matrix_given[r + 1][
            c + 1] and current_element == matrix_given[r + 1][c]:

        return True
    return False


n, m = [int(x) for x in input().split()]

size = 2

matrix = read_matrix(n)

count = 0
for r in range(n - size+1):
    for c in range(m - size+1):
        if find_submatrix(matrix, r,c):
            count += 1

print(count)
