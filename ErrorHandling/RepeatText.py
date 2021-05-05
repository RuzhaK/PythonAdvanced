text=input()
try:
    times=int(input())

except ValueError:
    print("Variable should be integer")
else:
    print(text * times)