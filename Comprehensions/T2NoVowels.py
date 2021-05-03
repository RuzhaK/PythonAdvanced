text=input()
VOWELS={'a','o','u','i','e'}
VOWELS=VOWELS.union(x.upper() for x in VOWELS)
# [VOWELS.add(x.upper()) for x in list(VOWELS)]

result=[ch for ch in text if ch not in VOWELS]
print(''.join(result))