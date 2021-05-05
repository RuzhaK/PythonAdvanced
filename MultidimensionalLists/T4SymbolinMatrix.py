n=int(input())
matrix=[]
found=False
for i in range(n):
    row=input().split()
    matrix.append(row)
element=input()

for i in range(n):
    row=matrix[i]
    for el in row:
        for j in range(len(el)):
            if element==el[j]:
                if element==el[j]:

                    print(f"({i}, {j})")
                    found=True
if found==False:
    print(f"{element} does not occur in the matrix")


# todo 80/100