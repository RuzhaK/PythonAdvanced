





from collections import deque



def best_list_pureness(*args):
    numbers=deque(args[0])
    k=args[1]
    best_pureness_rotations=0
    pureness_value=0
    for i in range(len(numbers)):
        pureness_value+=i*numbers[i]
    best_pureness_value = pureness_value
    for i in range(k):
        value=numbers.pop()
        numbers.appendleft(value)
        pureness_value=0
        for j in range(len(numbers)):
            pureness_value += j * numbers[j]
        if pureness_value>best_pureness_value:
            best_pureness_value=pureness_value
            best_pureness_rotations=i+1




    return f"Best pureness {best_pureness_value} after {best_pureness_rotations} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
