

# result=[' '.join(list_as_str.split()) for list_as_str in input().split('|')[::-1]]
# print(*result)

lists=[outer_list.split() for outer_list in input().split('|')]
output_list=[el
    for list in reversed(lists)
    for el in list
]

print(' '.join(output_list))