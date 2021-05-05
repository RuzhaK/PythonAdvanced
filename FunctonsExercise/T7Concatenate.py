# def concatenate(*args):
#     result=''
#     for arg in args:
#         result+=arg
#     return result
# ----------------------
# def concatenate(*args):
#     return ''.join(args)
# ----------------------
# treti variant s rekursia:
def concatenate(*args):
    if len(args)==1:
        return args[0]
    return args[0]+concatenate(*args[1:])


print(concatenate("Soft", "Uni", "Is", "Great", "!"))