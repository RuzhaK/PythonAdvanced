n, m = [int(x) for x in input().split()]
def read_matrix(n):
    matrix = []
    for _ in range(n):
       matrix.append(input().split())

    return matrix


matrix=read_matrix(n)
commands=input()
a=5
