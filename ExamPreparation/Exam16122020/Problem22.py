string=input()
n=int(input())


def read_matrix(n):
    field=[]
    for i in range(n):
        row=[]
        text=input()
        for el in text:
            row.append(el)
        field.append(row)
    return field


field=read_matrix(n)


def initial_position(symbol, field):
    for i in range(len(field)):
        for j in range(len(field)):
            if symbol==field[i][j]:
                return (i, j)


row, col=initial_position("P",field)

m=int(input())


def coordinates_valid(row, col, field):
    if 0<=row<len(field) and 0<=col<len(field):
        return True
    return False


for i in range(m):
    command=input()
    if command=="left":
        if coordinates_valid(row, col - 1, field):
            field[row][col] = "-"
            col -= 1
            if field[row][col] != "-":
                string += field[row][col]
            field[row][col] = "P"

        else:
            if len(string) > 0:
                string = string[:-1]
    elif command=="right":
        if coordinates_valid(row,col+1,field):
            field[row][col] = "-"
            col += 1
            if field[row][col] != "-":
                string += field[row][col]
            field[row][col] = "P"

        else:
            if len(string)>0:
                string=string[:-1]


    elif command=="up":
        if coordinates_valid(row-1, col, field):
            field[row][col] = "-"
            row -= 1
            if field[row][col] != "-":
                string += field[row][col]
            field[row][col] = "P"

        else:
            if len(string) > 0:
                string = string[:-1]
    elif command=="down":
        if coordinates_valid(row+1, col, field):
            field[row][col] = "-"
            row+= 1
            if field[row][col] != "-":
                string += field[row][col]
            field[row][col] = "P"

        else:
            if len(string) > 0:
                string = string[:-1]
print(string)


def print_matrix(field):
    for i in range(len(field)):
        for j in range (len(field)):
            print(''.join(field[i][j]),end="")
        print()

print_matrix(field)