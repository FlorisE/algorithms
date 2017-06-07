def solution(N, P, Q):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= N:
        #print sieve
        if sieve[i]:
            k = i * i
            while k <= N:
                sieve[k] = False
                k += i
        i += 1
    #print sieve
    primes = []

    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.append(i)
    print primes
    semiprimes = set()
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            semiprimes.add(primes[i] * primes[j])
    print semiprimes
    M = len(P)
    amounts = []
    for i in range(M):
        start = P[i]
        end = Q[i]
        count = 0
        for semiprime in sorted(semiprimes):
            if semiprime >= start and semiprime <= end:
                count += 1
            elif semiprime > end:
                break
        amounts.append(count)
    return amounts

print(solution(26, [1, 4, 16], [26, 10, 20]))
