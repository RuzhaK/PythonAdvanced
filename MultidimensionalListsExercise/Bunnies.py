def find_player(matrix):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "P":
                return x, y


def find_bunnies(matrix):
    bunnies = []
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "B":
                bunnies.append((x, y))
    return bunnies


n, m = [int(x) for x in input().split(' ')]
lair = [list(input()) for _ in range(n)]
directions = input()
player_x, player_y = find_player(lair)
bunny_multiplications_directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

last_player_x, last_player_y = None, None

won = False
lost = False

for direction in directions:
    lair[player_y][player_x] = '.'
    last_player_x = player_x
    last_player_y = player_y

    if direction == 'U':
        player_y -= 1
    elif direction == 'D':
        player_y += 1
    elif direction == 'L':
        player_x -= 1
    elif direction == 'R':
        player_x += 1

    if player_x < 0 or player_x >= m or player_y >= n or player_y < 0:
        won = True
    else:
        at_position = lair[player_y][player_x]
        if at_position == 'B':
            lost = True
            last_player_x = player_x
            last_player_y = player_y
        else:
            lair[player_y][player_x] = 'P'

    for bunny_x, bunny_y in find_bunnies(lair):
        for delta_x, delta_y in bunny_multiplications_directions:
            new_bunny_x = bunny_x + delta_x
            new_bunny_y = bunny_y + delta_y
            if 0 <= new_bunny_x < m and 0 <= new_bunny_y < n:
                at_position = lair[new_bunny_y][new_bunny_x]
                lair[new_bunny_y][new_bunny_x] = 'B'
                if at_position == 'P':
                    lost = True

    if won:
        break
    if lost:
        break
for row in lair:
    print(''.join(row))

if won:
    print(f'won: {last_player_y} {last_player_x}')
elif lost:
    print(f'dead: {last_player_y} {last_player_x}')