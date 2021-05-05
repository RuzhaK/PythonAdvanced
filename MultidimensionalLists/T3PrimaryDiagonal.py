n=int(input())
sum_primary_diagonal=0
for i in range(n):
    row=[int(x) for x in input().split()]
    sum_primary_diagonal+=row[i]
print(sum_primary_diagonal)
# todo judge 