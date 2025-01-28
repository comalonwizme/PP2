a = list(map(int, input().split()))
ok = False
for i in range(len(a) - 1):
    if a[i] == 3 and a[i + 1] == 3:
        ok = True
        break
print(ok)
