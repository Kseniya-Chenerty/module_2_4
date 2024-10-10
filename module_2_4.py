numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[1:]:
    is_primes = True
    for dividers in numbers[1:i-1]:
        if i % dividers == 0:
            is_primes = False
            break
    primes.append(i) if is_primes else not_primes.append(i)
print('Простые числа:', primes)
print('Не простые числа:', not_primes)




