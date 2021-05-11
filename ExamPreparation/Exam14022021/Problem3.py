from collections import deque

def stock_availability(*args):
    flavours=deque(args[0])
    if args[1]=="delivery":

        for i in range(len(args)-2):
            flavours.append(args[i+2])
    elif args[1]=="sell":
        if (len(args)-2)==0:
            if len(flavours)>0:
                flavours.popleft()
        elif (len(args)-2)>=1:
            try:
                n=int(args[2])
                cycles=min(n,len(flavours))
                for i in range(cycles):
                    flavours.popleft()
            except ValueError:
                for arg in args[2:]:
                    flavours=[flavour for flavour in flavours if flavour!=arg]



    return list(flavours)



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"), ['choco', 'vanilla', 'banana', 'caramel', 'berry'])
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"), ['chocolate', 'vanilla', 'banana', 'cookie', 'banana'])
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"), ['vanilla', 'banana'])
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3), [])
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", -4))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"), ['banana'])
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"), ['cookie', 'banana'])
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "cookie"), ['cookie', 'banana'])
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"), ['chocolate', 'vanilla', 'banana'])
print(stock_availability(["choco", "vanilla", "banana"], "delivery",3))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 4))
print(stock_availability(["choco", "vanilla", "banana"], "delivery","choco"))
print(stock_availability([], "sell"))
print(stock_availability([], "delivery"))

# print(stock_availability(["a", "b", "c"], "sell"))
# print(stock_availability(["a", "b", "c"], "sell", 3))
# print(stock_availability(["a", "b", "c"], "sell", "c"))
