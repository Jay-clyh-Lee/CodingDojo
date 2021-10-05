# Test

n = 10
sieve = set(range(2, n+1))
counter = 0
while sieve:
    prime = min(sieve)
    sieve -= set(range(prime, n+1, prime))
    
    counter += 1
print(counter)



def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
            #primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
            #print(primes[i * i: n: i])
    return sum(primes)




print(countPrimes(10))