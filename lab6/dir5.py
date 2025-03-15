import os

def writing(path):
    if not os.path.exists(path):
        print("This path doesn't exist")
        return
    if not os.path.isfile(path):
        print("It's not a file")
        return

    with open(path, 'a', encoding = 'utf-8') as f:
        ok = int(input("Enter lines to write: "))
        for i in range(ok):
            s = input()
            f.write(str(s) + '\n')

        print("Zapisano!")

if __name__ == "__main__":
    user = input("Enter path to file: ")
    writing(user)
