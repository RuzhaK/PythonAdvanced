from collections import deque
materials_over=False
NEEDED=3
effects=deque([int(x) for x in input().split(", ")])
powers=[int(x) for x in input().split(", ")]
fireworks={"palm":0,"willow":0,"crossette":0}


def perfect_show(fireworks):
    if fireworks["crossette"]>=NEEDED and fireworks["willow"]>=NEEDED and fireworks["palm"]>=NEEDED:
        return True
    return False


while True:
    while effects[0] <= 0:
        effects.popleft()
        if len(effects) <= 0:
            materials_over=True
            break
    while powers[-1] <= 0:
        powers.pop()
        if len(powers) <= 0:
            materials_over = True
            break


    if materials_over==True:
        break

    current_sum = effects[0] + powers[-1]

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["crossette"] += 1
        effects.popleft()
        powers.pop()
        if perfect_show(fireworks):
            break
    elif current_sum % 3 == 0:
        fireworks["palm"] += 1
        effects.popleft()
        powers.pop()
        if perfect_show(fireworks):
            break
    elif current_sum % 5 == 0:
        fireworks["willow"] += 1
        effects.popleft()
        powers.pop()
        if perfect_show(fireworks):
            break
    else:
        effects[0] -= 1
        removed = effects.popleft()
        effects.append(removed)

    if len(effects) <= 0 or len(powers)<=0:
        break

if perfect_show(fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if len(effects)>0:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if len(powers)>0:
    print(f"Explosive Power left: {', '.join(str(x) for x in powers)}")
print(f"Palm Fireworks: {fireworks['palm']}")
print(f"Willow Fireworks: {fireworks['willow']}")
print(f"Crossette Fireworks: {fireworks['crossette']}")


# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

# -15, -8, 0, -16, 0, -22
# 10, 5



