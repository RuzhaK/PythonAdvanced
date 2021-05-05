from collections import deque
kids=input().split()
n=int(input())
kids_queue=deque(kids)

counter=0
while len(kids_queue)>1:
    counter+=1
    current_player=kids_queue.popleft()
    if counter==n:
        print(f"Removed {current_player}")
        counter=0
    else:
        kids_queue.append(current_player)
print(f"Last is {kids_queue.popleft()}")







