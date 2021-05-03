numbers=map(lambda x:int(x),input().split(' '))
print(list(filter(lambda x:x%2==0,numbers)))