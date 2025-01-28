def solve(s):
    ok = True
    for i in range((len(s) + 1) // 2):
        if s[i] != s[len(s) - 1 - i]:
            ok = False
            break
    return ok
s = input()
solve(s)
if solve(s) == True:
    print("Palindrome")
else:
    print("Not Palindrome")
