n = int(input("Enter the limit: "))
l = list(range(2,n+1))
count = [0 for _ in range(n+1)]
lucky_number = []

#CREATE A LIST OF PRIME NUMBERS
for p in l:
    for num in l:
        if num%p == 0 and num!=p :
            l.remove(num)

#COUNT PRIME FACTORS          
for p in l:
    for num in range(p, n+1, p):              
        count[num] += 1

#ADD LUCKY NUMBERS TO LIST
c = 0                                    
for i in range(2,n+1) :
    if count[i] == 3 :
        lucky_number.append(i)
        c=c+1
        
print("LUCKY NUMBERS: ")
print(lucky_number)
