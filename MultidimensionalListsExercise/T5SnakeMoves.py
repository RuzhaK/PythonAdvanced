

def read_matrix(n,m):

    matrix = []
    for r in range(n):
        matrix.append([0 for el in range(m)])
    return matrix


n, m=[int(x) for x in input().split()]
snake=input()
matrix=read_matrix(n,m)
word_index=0
for r in range (n):
    for c in range(m):
        matrix[r][c]=snake[word_index]
        word_index+=1
        if word_index>=len(snake):
            word_index=0
for r in range(n):
    if r%2==1:
        matrix[r].reverse()
    print(''.join(matrix[r]))