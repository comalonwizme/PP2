import os

def check(path):
    if not os.path.exists(path):
        print("This path doesn't exist")
        return

    if not os.path.isfile(path):
        print("It's not a file")
        return

    cn = 0
    with open(path, 'r', encoding ='utf-8') as f:
        for i in f:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    user = input("Enter path to file: ")
    check(user)
