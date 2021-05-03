


def strs_to_ints(param):
    return [int(x) for x in param]


def read_matrix():
    n = int(input())
    return [strs_to_ints(input().split(", ")) for _ in range(n)]





def get_even_elements(row):
    return [x for x in row if x%2==0]


def get_even_matrix(matrix):
    return [get_even_elements(row) for row in matrix]




def print_result(even_matrix):
    print(even_matrix)

matrix=read_matrix()
even_matrix=get_even_matrix(matrix)
print_result(even_matrix)