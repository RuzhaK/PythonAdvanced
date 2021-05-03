f=open('numbers.txt')
total_sum=0
for line in f:
    n=int(line.strip())
    total_sum+=n
print(total_sum)

# alternative

print((sum([int(line.strip() for line in open('numbers.txt'))])))
# създаване и презаписване на файл с w
f=open('baba.txt','w')
f.write('neshto')
f.close()
f=open('baba.txt','w')
f.write('drugo')
f.close()
f.read('baba.txt')
# това апендва нови редове:
f.writelines(['line one\n','line two\n'])

