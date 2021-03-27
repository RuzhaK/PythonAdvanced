program_stopped=False
n=int(input())
line=input().split()


def read_matrix(n):
    matrix = []
    for _ in range(n):
       matrix.append(input().split())

    return matrix


matrix=read_matrix(n)


def find_coordinates(symbol, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==symbol:
                return (i,j)


r,c=find_coordinates('s', matrix)
matrix[r][c]='*'


def index_is_valid(r, c, matrix):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False

coal_collected=0


def check_for_coal(matrix):
    coal_left=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]=='c':
                coal_left+=1
    if coal_left==0:
        return False
    else:
        return coal_left



for i in range(len(line)):
    if line[i]=="up":
        r_index=r-1
        c_index=c
    elif line[i]=="right":
        r_index=r
        c_index=c+1
    elif line[i]=="down":
        r_index=r+1
        c_index=c
    elif line[i]=="left":
        r_index=r
        c_index=c-1
    if index_is_valid(r_index,c_index,matrix):
        if matrix[r_index][c_index]=="*":
            r=r_index
            c=c_index
        elif matrix[r_index][c_index]=="e":
            program_stopped=True
            print(f"Game over! ({r_index}, {c_index})")
            break
        elif matrix[r_index][c_index] == "c":
            r = r_index
            c = c_index
            matrix[r_index][c_index] = "*"
            coal_collected+=1
            if check_for_coal(matrix)==False:
                print(f"You collected all coals! ({r}, {c})")
                program_stopped=True
                break
if not program_stopped:
    print(f"{check_for_coal(matrix)} coals left. ({r}, {c})")




