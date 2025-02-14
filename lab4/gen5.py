def solve(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
print(' '.join(map(str, list(solve(n)))))

