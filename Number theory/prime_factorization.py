# PRIME NUMBER listing using sieve of eratosthenes
n = int(input("Enter the limit: "))
l = list(range(2,n+1))
for p in l:
    for num in l:
        if(num%p == 0 and num != p):
            l.remove(num)
print(l)

# prime factorization
x = int(input("Number: "))
factors = []
for p in l:
    while x%p == 0:
        if(x%p == 0):
            factors.append(p)
        x = x/p
print(factors)
