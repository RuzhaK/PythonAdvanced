numbers=list(map(lambda number:int(number), input().split(' ')))
negatives=filter(lambda x:x<0,numbers)
positives=filter(lambda x:x>=0,numbers)
sum_neg=sum(negatives)
print(sum_neg)
sum_pos=sum(positives)
print(sum_pos)
if abs(sum_neg)>sum_pos:
    print("The negatives are stronger than the positives")
elif abs(sum_neg)<sum_pos:
    print("The positives are stronger than the negatives")
