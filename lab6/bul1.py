from functools import reduce 

n = list(map(int, input().split()))

print(reduce(lambda x, y: x * y, n)})
