



n=int(input())


def str_to_int(param):
    return [int(x) for x in param]


def read_matrix(n):
    return [str_to_int(input().split(", ")) for i in range(n)]

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


matrix=read_matrix(n)


first_diagonal=[matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix)) if row==col]
second_diagonal=[matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix)) if len(matrix)-1-row==col]

print(f"First diagonal: {', '.join(map(str,first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str,second_diagonal))}. Sum: {sum(second_diagonal)}")

# # print(' '.join(' '.join(p) for p in matrix))
# for row in matrix:
#     print(' '.join(str(row)))
#
#
# print(f"First diagonal: {[matrix[r][r] for r in range(len(matrix))]}. Sum: {sum_of_primary_diagonal(matrix)}")
# print(f"First diagonal: {[matrix[r][r] for r in range(len(matrix))]}. Sum: {sum_of_primary_diagonal(matrix)}")
# print(f"Second diagonal: {[matrix[r][len(matrix)-r-1] for r in range(len(matrix))]}. Sum: {sum_of_secondary_diagonal(matrix)}")
# print(f"Second diagonal: {' '.join(' '.join(str([matrix[r][len(matrix)-r-1] for r in range(len(matrix))])))}. Sum: {sum_of_secondary_diagonal(matrix)}")