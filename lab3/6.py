def solve(s):
    w = s.split()
    ans = w[::-1]
    return ' '.join(ans)
    
s = input()
print(solve(s))