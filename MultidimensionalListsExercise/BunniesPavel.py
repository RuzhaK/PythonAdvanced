from copy import deepcopy


def dead_situation(r, c, m):
    if m[r][c] == 'B':
        return True
    return False


def won_situation(r, c, m, command):
    if command == 'U' and r == 0:
        return True
    elif command == 'D' and r == len(m) - 1:
        return True
    elif command == 'L' and c == 0:
        return True
    elif command == 'R' and c == len(m[0]) - 1:
        return True
    return False


def entry_pos(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            if matrix[r][c] == 'P':
                matrix[r][c] = '.'
                return r, c


def command_parsing(r, c, initial_command):
    if initial_command == 'U':
        r -= 1
    elif initial_command == 'D':
        r += 1
    elif initial_command == 'L':
        c -= 1
    elif initial_command == 'R':
        c += 1
    return r, c


def moving_p(place_row, place_col, cmd_line, m):
    for cmd in cmd_line:
        m = bunny_producing(m)
        if won_situation(place_row, place_col, m, cmd):
            result = print_matrix(m)
            result += f'won: {place_row} {place_col}'
            return result
        place_row, place_col = command_parsing(place_row, place_col, cmd)
        if dead_situation(place_row, place_col, m) is True:
            result = print_matrix(m)
            result += f'dead: {place_row} {place_col}'
            return result


def bunny_producing(m):
    row_placeholder = [0, -1, 0, 1]
    col_placeholder = [-1, 0, 1, 0]
    new_matrix = deepcopy(m)
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 'B':
                for find in range(4):
                    row_finder = row + row_placeholder[find]
                    col_finder = col + col_placeholder[find]
                    if row_finder in range(len(m)) and col_finder in range(len(m[0])):
                        matrix[row_finder][col_finder] = 'B'
    return new_matrix


def print_matrix(m):
    result = ''
    for c in m:
        result += ''.join(c)
        result += '\n'
    return result


initial_row, initial_col = list(map(int, input().split()))
matrix = [list(input()) for c in range(initial_row)]
entry_row, entry_col = entry_pos(matrix)
command_line = list(input())
print(moving_p(entry_row, entry_col, command_line, matrix))
