def str_to_ints(strs):
    return [int(x) for x in strs]



def read_matrix():
    rows_count=int(input())
    return [str_to_ints(input().split(', ')) for _ in range(rows_count)]


matrix=read_matrix()
print([x for r in matrix for x in r])