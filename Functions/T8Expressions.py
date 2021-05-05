# import itertools
# numbers=[n for n in input().split(', ')]
# n=len(numbers)
# permutations=set(itertools.permutations(['-']*n +['+']*n,n))
#
# for permutation in permutations:
#     expr=''.join(itertools.chain(*zip(permutation,numbers)))
#     res=eval(expr)
#     print(f'{expr}={res}')

import itertools
numbers=[n for n in input().split(', ')]
n=len(numbers)
permutations=itertools.product('-+',repeat=n)

for permutation in permutations:
    expr=''.join(itertools.chain(*zip(permutation,numbers)))
    res=eval(expr)
    print(f'{expr}={res}')