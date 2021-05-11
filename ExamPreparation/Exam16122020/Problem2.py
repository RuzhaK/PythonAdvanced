n=7
def change_player(A,B,current_player):
    if current_player==A:
        return B
    return A

dartboard=[]
# A_player_score=501
# B_player_score=501
A_player,B_player=input().split(', ')
players={}
players[A_player]=501
players[B_player]=501

for i in range(n):
    dartboard.append(input().split())
coordinates=input()
count_turns=0

current_player=A_player
while True:
    info = coordinates[1:-1]
    row, col = [int(x) for x in info.split(', ')]
    if current_player==A_player:
        count_turns += 1
    if 0>row or row>=7 or  0>col or col>=7:
        current_player=change_player(A_player,B_player, current_player)
        coordinates = input()

        continue

    if dartboard[row][col]=="B":
        if current_player==A_player:
            players[A_player]=0
        else:
            players[B_player] = 0


    elif dartboard[row][col]=="D":
        if current_player == A_player:
            players[A_player] -= 2*(int(dartboard[row][0])+int(dartboard[row][-1])+int(dartboard[0][col])+int(dartboard[n-1][col]))
        else:
            players[B_player] -= 2*(int(dartboard[row][0])+int(dartboard[row][-1])+int(dartboard[0][col])+int(dartboard[n-1][col]))
    elif dartboard[row][col]=="T":
        if current_player == A_player:
            players[A_player] -= 3 * (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[n - 1][col]))
        else:


            players[B_player] -= 3 * (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[n - 1][col]))
    else:

        if current_player == A_player:
            players[A_player] -= int(dartboard[row][col])
        else:
            players[B_player] -= int(dartboard[row][col])

    if players[A_player]<=0 or players[B_player]<=0:
        break
    current_player=change_player(A_player, B_player,current_player)

    coordinates = input()

if players[A_player]<=0:
    print(f"{A_player} won the game with {count_turns} throws!")
else:
    print(f"{B_player} won the game with {count_turns} throws!")




