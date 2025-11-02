n = int(input("Enter the limit : "))
prime = list(range(2,n+1))
for p in prime:
    for num in prime:
        if num%p==0 and num!=p:
            prime.remove(num)

# Search Noldbach Numbers
for i in range(len(prime)-1):
    if (prime[i]+prime[i+1]+1) in prime:
        print(prime[i]+prime[i+1]+1)
