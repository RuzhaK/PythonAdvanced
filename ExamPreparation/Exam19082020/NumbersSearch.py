

def numbers_searching(*args):

    result=[]
    duplicates_found=[]
    for i in range(len(args)-1):
        if (args[i]+1) not in args and args[i]<max(args):
            missing_arg=(args[i]+1)
        if args[i] in args[i+1:]:
            duplicates_found.append(args[i])
    result.append(missing_arg)
    result.append(sorted(set(duplicates_found)))
    return result



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
#
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


