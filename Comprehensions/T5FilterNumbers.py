start=int(input())
end=int(input())
def is_valid(x):
    return any(x%n==0 for n in range(2,11))

print([x for x in range(start,end+1) if is_valid(x)])