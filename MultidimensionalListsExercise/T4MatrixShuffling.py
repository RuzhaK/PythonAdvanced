def read_matrix(n,m):

    matrix = []
    for r in range(n):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


n, m = [int(x) for x in input().split()]
matrix = read_matrix(n,m)
data=input()


def check_if_index_is_valid(index_row,index_col,rows,cols):
    if 0<=index_row<rows and 0<=index_col<cols:
        return True
    return False

def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(f"{matrix[r][c]}", end=' ')
        print()

def check_if_command_is_valid(command,coordinates,n,m):
    if command=="swap" and len(coordinates)==4:
        for index in range(0,len(coordinates),2):
            if not check_if_index_is_valid(coordinates[index],coordinates[index+1],n,m):
                print("Invalid input!")
                return False
        return True
    print("Invalid input!")
    return False


while data!="END":
    splitted_data=data.split()
    try:
        command=splitted_data[0]
        coordinates=[int(x) for x in splitted_data[1:]]
    except:
        print("Invalid input!")
        continue
    if check_if_command_is_valid(command,coordinates,n,m):
        current_row=coordinates[0]
        current_col=coordinates[1]
        temp=matrix[current_row][current_col]
        matrix[current_row][current_col]=matrix[coordinates[2]][coordinates[3]]
        matrix[coordinates[2]][coordinates[3]]=temp
        print_matrix(matrix)
        # for r in range(n):
        #     print(' '.join(matrix[r]))

    data=input()
# todo  80 / 100