def solve(numh, numl):
    for i in range(numh + 1):
        j = numh - i
        if 2 * j + 4 * i == numl:
            return i, j
    
numh, numl = int(input()), int(input())
print(solve(numh, numl))