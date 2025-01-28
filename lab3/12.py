def solve(a):
    for i in range(a):
        print('*', end = "")
a = list(map(int, input().split()))
for i in a:
    solve(i)
    print()
