numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for is_prime in numbers:
    if is_prime > 1:
        for i in range(2, is_prime):
        if (is_prime % i) == 0:
        Not_Primes.append(is_prime)
    break
    else:
    Primes.append(is_prime)
    else:
    Not_Primes.append(is_prime)
print('Primes:', Primes)
print('Not_Primes:', Not_Primes)
