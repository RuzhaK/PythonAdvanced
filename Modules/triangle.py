def print_triangle(n):
    for row in range(n+2):
        print(*[i for i in range(1,row)])
    for row in range(n,0,-1):
        print(*[i for i in range(1,row)])

print_triangle(int(input()))