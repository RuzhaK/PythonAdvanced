from collections import deque

jobs=deque([int(x) for x in input().split(", ")])
index=int(input())
cycles=0
current_index=0
value=jobs[index]
while True:
    current_index=jobs.index(min(jobs))
    current_job=min(jobs)
    jobs[current_index]=2147483647
    cycles+=current_job
    if current_index == index:
        break
print(cycles)

