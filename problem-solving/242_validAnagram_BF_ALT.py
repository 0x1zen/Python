s='anagram'
t='nagaram'

def validAnagram(s,t):
    return Counter(s)==Counter(t)
print(validAnagram(s,t))