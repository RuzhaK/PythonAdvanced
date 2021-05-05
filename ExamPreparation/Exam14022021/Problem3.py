from collections import deque

def stock_availablity(*args):
    flavours=deque(args[0])
    if args[1]=="delivery":
        for i in range(len(args)-2):
            flavours.append(args[i+2])
    else:
        if (len(args)-2)==0:
            flavours.popleft()
        elif (len(args)-2)==1:
            try:
                n=int(args[2])
                for i in range(n):
                    flavours.popleft()
            except ValueError:
                flavours=[flavour for flavour in flavours if flavour!=args[2]]

    return flavours

# todo  0 / 100 vsichki vhodove minavat

# print(stock_availablity(["a", "b", "c"], "delivery", "c", "b"))
#
#
# print(stock_availablity(["a", "b", "c"], "sell"))
# print(stock_availablity(["a", "b", "c"], "sell", 3))
# print(stock_availablity(["a", "b", "c"], "sell", "c"))
print(stock_availablity(["a", "b", "c"], "sell", "z"))