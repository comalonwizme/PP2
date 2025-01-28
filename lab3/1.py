def solve(grams):
    ounces = grams / 28.3495231
    return ounces
    
grams = int(input())
print(solve(grams))