def strs_to_ints(param):

    return [int(x) for x in param]




def read_matrix():
    n=int(input())
    return [strs_to_ints(input().split(" ")) for _ in range(n)]

matrix=read_matrix()
line=input()


def coordinates_valid(row, col,matrix):

    if 0<=row<len(matrix) and 0<=col<len(matrix[0]):
        return True
    return False


while line!="END":
    command, row, col, value=line.split()
    row=int(row)
    col=int(col)
    if coordinates_valid(row,col,matrix):
        if command=="Add":
            matrix[row][col]+=int(value)
        else:
            matrix[row][col]-=int(value)
    else:
        print("Invalid coordinates")
    line = input()

for i in range(len(matrix)):
    print(' '.join(str(x) for x in matrix[i]))

# todo printing and reading matrix!!!
