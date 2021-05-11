from collections import deque

males=[int(x) for x in input().split()]
females=deque([int(x) for x in input().split()])
males_left=True
females_left=True
matches=0
def check_if_males(males):
    if len(males)<=0:
        return False
    return True

def check_if_females(females):
    if len(females)<=0:
        return False
    return True

while check_if_males(males) and check_if_females(females):

    while males[-1]<=0:
        males.pop()
        if not check_if_males(males):
            break
    while females[0] <= 0:
        females.popleft()
        if not check_if_females(females):
            break
    if not check_if_females(females):
        break
    if not check_if_males(males):
        break
    while len(females)>0 and females[0]%25==0:
        females.popleft()
        if not check_if_females(females):
            break
        females.popleft()


    while len(males)>0 and males[-1] % 25 == 0:
        males.pop()

        if not check_if_males(males):
            break
        males.pop()

    if not check_if_males(males):
        break
    if not check_if_females(females):
        break
    if males[-1]<=0 or females[0]<=0:
        continue
    if males[-1] == females[0]:
        matches+=1
        males.pop()

    else:
        males[-1] -= 2
    females.popleft()

print(f"Matches: {matches}")
if check_if_males(males)==False:
    print("Males left: none")
else:
    males=reversed(males)
    print(f"Males left: {', '.join(str(x) for x in males)}")

if check_if_females(females)==False:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(x) for x in females)}")

# 4 5 7 3 6 9 12
# 12 9 6 1
