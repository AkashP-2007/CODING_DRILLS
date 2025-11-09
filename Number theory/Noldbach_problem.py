#CREATE A LIST OF PRIME NUMBERS (Corrected)
isprime = [True]*(n+1)
for p in range(2, int(n**0.5)+1):
    if isprime[p]:
        for x in range(p*p, n+1, p):
            isprime[x] = False
prime = [i for i in range(2, n+1) if isprime[i]]

# Search Noldbach Numbers
for i in range(len(prime)-1):
    if (prime[i]+prime[i+1]+1) in prime:
        print(prime[i]+prime[i+1]+1)
