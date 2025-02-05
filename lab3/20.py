prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

numb = list(range(1, 50))
prime_num = list(filter(prime, numb))
print(prime_num)
