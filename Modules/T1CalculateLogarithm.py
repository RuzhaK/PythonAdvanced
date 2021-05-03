import math
n=int(input())
base=input()
if base=="natural":
    print(f'{math.log(n):.2f}')
else:
    base=float(base)
    print(f'{math.log(n,base):.2f}')