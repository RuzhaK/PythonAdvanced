n=int(input())
removed_counter=0

matrix=[]
for _ in range(n):
    matrix.append(list(input()))


def is_valid_bound(potential_row, potential_column, matrix):
    if 0<=potential_row<len(matrix) and 0<=potential_column<len(matrix):
        return True
    return False


def calculate_kills(r_index, c_index, matrix):
    kills=0
    rows=[-2, -2, 2, 2, 1, 1, -1,-1]
    cols=[-1, 1, -1, 1,-2, 2, -2, 2]
    for index in range(len(rows)):
        potential_column=c_index+cols[index]
        potential_row=r_index+rows[index]
        if is_valid_bound(potential_row,potential_column,matrix):
            potential_position=matrix[potential_row][potential_column]
            if potential_position=="K":
                kills+=1
    return kills


while True:
    count_max_kills = 0
    killer_position = []
    for r_index in range(n):
        for c_index in range(n):
            if matrix[r_index][c_index] == "K":
                kills = calculate_kills(r_index, c_index, matrix)
                if count_max_kills <kills:
                    count_max_kills = kills
                    killer_position = [r_index, c_index]
    if killer_position:
        removed_counter+=1
        matrix[killer_position[0]][killer_position[1]]='0'
    else:
        break
print(removed_counter)





