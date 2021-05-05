names = input().split(", ")
data = input()
heroes = {name:{} for name in names}


def update_heroes(name, item, price, heroes):

    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})
    return heroes


while not data == "End":
    name, item, price = data.split("-")
    heroes=update_heroes(name,item, price,heroes)
    data = input()

print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum([price for item, price in inventory.items()])}" for
        name, inventory in heroes.items()], sep="\n")
