def solve(a):
    ok = False
    for i in range(len(a) - 2):
        if a[i] == 0:
            if a[i + 1] == 0:
                if a[i + 2] == 7:
                    ok = True
                    break
    return ok
a = list(map(int, input().split()))
print(solve(a))
