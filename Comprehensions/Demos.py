ll=[1, 2, 3, 14, 15]
def to_binary(number):
    bits=[]
    while number:
        bits.append(number%2)
        number//=2
    return ''.join(map(str,bits[::-1]))

print([to_binary(x) for x in ll])