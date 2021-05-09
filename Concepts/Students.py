from functools import reduce
students = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
filtered = list(filter(lambda n:n%3==0,students))
grace =list(map(lambda n:n+5,filtered))
sum_grace = reduce(lambda a,b:a+b,grace)
print(sum_grace)
