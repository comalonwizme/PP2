import shutil

def solve(inp, out):
    shutil.copy(inp, out)

if __name__ == "__main__":
    inp = input()
    out = input()
    solve(inp, out)
