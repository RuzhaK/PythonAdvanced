from collections import deque


orders=deque([int(x) for x in input().split(", ")])
employees=[int(x) for x in input().split(", ")]
made_pizzas=0
has_orders=True

while len(employees)>0:

    while orders[0]<=0 or orders[0]>10:
        orders.popleft()
        if len(orders) <= 0:
            has_orders = False
            break
    if has_orders==False:
        break
    if orders[0]<=employees[-1]:
        made_pizzas+=orders.popleft()
        employees.pop()

    else:
        orders[0]-=employees[-1]
        made_pizzas+=employees[-1]
        employees.pop()
    if len(orders)<=0:
        has_orders=False
        break
if has_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(order) for order in orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")




# Input

# All orders are successfully completed!
# Total pizzas made: 15
# Employees: 3, 1
# Not all orders are completed.
# Orders left: {left orders joined by ", "}

