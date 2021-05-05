# You will receive a command and a list of numbers:
# If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.
# If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list.
# Example
# Input	Output

def even_or_odd():
    command = input()
    line = [int(x) for x in input().split()]

    if command == 'Odd':
        result = sum(list(filter(lambda x: x % 2 != 0, line)))*len(line)
    else:
        result = sum(list(filter(lambda x: x % 2 == 0, line)))*len(line)
    print(result)
even_or_odd()