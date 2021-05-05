from collections import deque

def list_manipulator(list_object, operation, position, *args):
    new_list=deque(list_object.copy())
    if operation=="add":
        assert  len(args)>0
        if position == "beginning":
            new_list = deque(args) + new_list
        elif position == "end":
            new_list = new_list + deque(args)
    elif operation=="remove":
        assert  0<=len(args)<=1
        # todo osmisli:
        n=args[0] if len(args)==1 else 1
        # dolu funkciite sa bez skobi!
        fn=new_list.popleft if position=="beginning" else new_list.pop
        for _ in range(n):
            fn()
    return list(new_list)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
