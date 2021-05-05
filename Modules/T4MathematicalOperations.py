import mathops
expr=input()
res=mathops.exec(*mathops.parse_expression(expr))
print(res)