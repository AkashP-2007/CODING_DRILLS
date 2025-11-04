# Create suffix array
def build_suffix_array(string):
    suffixes = []   
    # Create list of suffix strings and sort it lexicographically
    for i in range(len(string)):
        suffixes.append((string[i:],i))
    suffixes.sort()
    
    # Storing the starting indexes in a list
    SA =[index for (suffix,index) in suffixes]
    return SA

# Compute LCP
def LCP(string):
    n = len(string)
    rank = [0] * n
    lcp = [0] * n
    for i in range(n):
        rank[Suffix_Array[i]] = i

    # loop in original order
    k = 0
    for i in range(n):
        # Last suffix in the suffix array does not have anything to compare it with
        if rank[i] == n-1:
            k = 0
            continue
        
        # next suffix in the lexicographical order
        j = Suffix_Array[rank[i] + 1]
        
        # comparing string[i:] and string[j:]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1                        
        #k is used to count the matches
        #Note: lcp[0] will always be zero
        lcp[rank[i]+1] = k
        
        #To avoid unnecessary comparisons
        if k>0:
            k-=1
    return lcp

s = input("Enter the string: ")
Suffix_Array = build_suffix_array(s)
print("Suffix Array : ",Suffix_Array)
print("Longest Common Prefix : ",LCP(s))
