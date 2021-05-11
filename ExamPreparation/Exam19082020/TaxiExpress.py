from collections import deque

customers=deque([int(x) for x in input().split(", ")])
taxis=[int(x) for x in input().split(", ")]
total_time=sum(customers)
while len(customers)>0 and len(taxis)>0:
    if customers[0]<=taxis[-1]:
        time=customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if len(customers)>0:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(str(x) for x in customers)}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")