def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0:
        return False


    i = 3
    while i*i < num:
        if num%i == 0:
            return False
        i+=2
    return True

def filter_prime(nums: list[int]) -> list[int]:
    res = []
    for _ in nums:
        if is_prime(_): res.append(_)
    return res

running = 1

while running:
    try:
        l = map(int, input("Enter nums: ").split())
        t = filter_prime(l)
        print(t)
    except Exception as ex:
        break