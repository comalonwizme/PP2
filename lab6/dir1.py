import os

def contents(path):
    dirs = []
    files = []
    all_c = os.listdir(path)

    for i in all_c:
        full = os.path.join(path, i)
        if os.path.isdir(full):
            dirs.append(i)

        elif os.path.isfile(full):
            files.append(i)


    print(f"Directory contents: ")
    print(f"\nOnly files: ")
    for f in files:
        print(f"  {f}")

    print(f"\nOnly directory: ")
    for d in dirs:
        print(f"  {d}")

    print(f"\nAll contents: ")
    for i in all_c:
        print(f"  {i}")

if __name__ == "__main__":
    user = input("Enter Path: ")
    contents(user)
