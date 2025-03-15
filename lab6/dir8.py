import os

def solve(path):
    if not os.path.exists(path):
        print("This path doesn't exist")
        return

    if os.path.isdir(path):
        print("This is direct.")
        return

    if not os.access(path, os.W_OK):
        print("Don't have access")
        return

    os.remove(path)
    print("File is removed")


if __name__ == "__main__":
    user = input("Enter path: ")
    solve(user)
