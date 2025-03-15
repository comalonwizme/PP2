import os

def check(path):
    if os.path.exists(path):
        dirs = os.path.dirname(path)
        files = os.path.basename(path)
        print("Path exist")
        print(f"Directory: {dirs}")
        print(f"Files: {files}")
    else:
        print("Doesn't exist")


if __name__ == "__main__":
    user = input("Enter path: ")
    check(user)
