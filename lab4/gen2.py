def solve(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(', '.join(map(str, list(solve(n)))))
