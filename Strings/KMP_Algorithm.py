#Longest Prefix Suffix
def lps(pat):
    lps = [0] * len(pat)
    length = 0
    i = 1
    while i < len(pat) :
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0 :
                length = lps[length-1]
            else :
                lps[i] = 0
                i += 1
    return lps
            
string = input("STRING: ")
pattern = input("PATTERN: ")
LPS = lps(pattern)
i=0
j=0
while i<len(string) :
    # Checking for character match 
    if i < len(string) and pattern[j] == string[i] :                
        i+=1
        j+=1
        
    # Pattern match found condition
    if j == len(pattern):
        print("PATTERN MATCH FOUND AT INDEX : ", i-j)
        j = LPS[j-1]
    
    # Checking for character mismatch 
    if i < len(string) and pattern[j] != string[i] :
        if j!=0:
            j=LPS[j-1]
        else:
            i+=1
            
