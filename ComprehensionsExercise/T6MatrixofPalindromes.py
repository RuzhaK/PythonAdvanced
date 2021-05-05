row,col=[int(x) for x in input().split()]
# alternative
# r,c=map(int,input().split())
result=[[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num,num+col)] for num in range(97,97+row)]

[print(*row) for row in result]