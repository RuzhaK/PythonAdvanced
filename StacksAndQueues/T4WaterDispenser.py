from collections import deque
quantity=int(input())
queue=deque()
START_COMMAND="Start"
END_COMMAND="End"
REFILL_COMMAND="refill"

while True:

    name=input()
    if name==START_COMMAND:
        break
    else:
        queue.append(name)

while True:

    command=input()
    if command==END_COMMAND:
        print(f"{quantity} liters left")
        break
    elif command.startswith(REFILL_COMMAND):
        command_params=command.split()
        refill_liters=int(command_params[1])
        quantity+=refill_liters

    else:
        person=queue.popleft()
        consumption = int(command)
        if consumption>quantity:
            print(f"{person} must wait")
        else:
            print(f"{person} got water")
            quantity-=consumption


