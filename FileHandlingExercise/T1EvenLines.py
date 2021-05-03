symbols=['-', ',', '!', '.', ':']
i=0
with open('test.txt') as file:
    for line in file:

        if i%2!=0:
            i += 1
            continue
        for symbol in symbols:
            line.replace(symbol,'@')
            i += 1
        print(' '.join(reversed(line.split())))
print()
