n = 8


def read_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    return matrix


board = read_matrix(n)


def find_coordinates(symbol, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==symbol:
                return (i,j)

def check_for_collision(king_row,king_col,i,j,board):
    if i == king_row:  # prowerka dali e na reda
        row=board[i]
        if king_col>j:
            section=row[j+1:king_col]
        else:section=row[king_col:j]
        if "Q" not in section:
            return True

    elif j == king_col:  # prowerka dali e na colonata
        column_section=[]
        if king_row<i:
            for k in range(king_row+1,i):
                column_section.append(board[k][j])
        else:
            for k in range(i+1,king_row):
                column_section.append(board[k][j])

        if "Q" not in column_section:
            return True
    elif abs(king_col-j) == abs(king_row-i):  # prowerka dali e na diagonala
        section=[]

        if king_row<i:
            q = king_col
            for l in range(king_row, i):
                section.append(board[l][q])
                if j>king_col:
                    q += 1
                else:
                    q-=1

        else:


                if j > king_col:
                    q = j -1
                    for l in range(i + 1, king_row + 1):
                        section.append(board[l][q])
                        q -= 1
                else:
                    q=j+1
                    for l in range(i + 1, king_row + 1):
                        section.append(board[l][q])
                        q += 1

        if "Q" not in section:
            return True

king_row,king_col=find_coordinates("K",board)
dangerous_queens=[]
for i in range(n):
    for j in range(n):
        queen_in_the_way=False
        if board[i][j]=="Q":
            if check_for_collision(king_row,king_col,i,j,board):
                dangerous_queens.append([i, j])




if len(dangerous_queens)<=0:
    print("The king is safe!")
else:
    for q in dangerous_queens:
        print(q)
