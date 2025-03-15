import os
import string

def solve(path):
    if not os.path.exists(path):
        print("This path doesn't exist")
        return

    for i in string.ascii_uppercase:
        name = f"{i}.txt"
        full = os.path.join(path, name)
        with open(full, 'a', encoding = 'utf-8') as ok:
            ok.write(f"{name}")
if __name__ == "__main__":
    user = input("Enter path: ")
    solve(user)
