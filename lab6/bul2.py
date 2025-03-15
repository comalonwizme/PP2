from functools import reduce 
import string

s = input()
cnt1 = sum(1 for i in s if i in string.ascii_uppercase)
cnt2 = sum(1 for i in s if i in string.ascii_lowercase)
print(f"Uppercase: {cnt1}")
print(f"Lowercase: {cnt2}")
