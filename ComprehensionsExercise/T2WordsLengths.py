text=input().split(", ")
# result=[f"{x} -> {len(x)}" for x in text]
# print(', '.join(result))

print(*[f"{x} -> {len(x)}" for x in text], sep=", ")