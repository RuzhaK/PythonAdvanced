import itertools
people=input().split(', ')
n=int(input())
for combination in itertools.combinations(people,n):
    print(', '.join(combination))