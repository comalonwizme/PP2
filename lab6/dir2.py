import os

def check(path):
    print(f"Existence: {os.access(path, os.F_OK)}")
    print(f"Readability: {os.access(path, os.R_OK)}")
    print(f"Writability: {os.access(path, os.W_OK)}")
    print(f"Executability: {os.access(path, os.X_OK)}")

if __name__ == "__main__":
    user = input("Enter path: ")
    check(user)
