# SIEVE OF ERATOSTHENES ALGORITHM
n = int(input("Enter the limit : "))
l = list(range(2,n+1))
print(l)
for p in l:
    for num in l:
        if(num%p == 0 and num != p):
            l.remove(num)
print(l)
