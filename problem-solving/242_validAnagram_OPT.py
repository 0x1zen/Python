# s='anagram'
# t='nagaram'
s='car'
t='rat'

def validAnagram(s,t):
    if len(s)!=len(t):
        return False
    else:
        sorted_s=sorted(s)
        sorted_t=sorted(t)
        for i in range(len(s)):
            if(sorted_s[i]!=sorted_t[i]):
                return False
    return True
print(validAnagram(s,t))