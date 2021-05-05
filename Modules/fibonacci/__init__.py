def create_sequence(n):
    assert n>=1
    if n==1:
        sequence=[0]
    elif n==2:
        sequence=[0,1]
    else:
        sequence=[0,1]
        for _ in range(n-2):
            sequence.append(sequence[-1]+sequence[-2])

    return sequence