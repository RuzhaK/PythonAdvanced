countries=input().split(", ")
capitals=input().split(", ")

result={countries[index]:capitals[index] for index in range (len(countries))}

print(*[f"{key} -> {value}" for key, value in result.items()], sep="\n")
# alternative:
print(*[f"{countries[index]} -> {capitals[index]}" for index in range(len(capitals))], sep="\n")

# alternative:
my_dict={country:capital for country,capital in tuple(zip(countries,capitals))}
[print(f"{country} -> {capital}")for country,capital in my_dict.items()]