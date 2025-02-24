s='anagram'
t='nagaram'
# s='car'
# t='rat'

if len(s)==len(t):
    myHashS={}
    myHashT={}
    for i in range(len(s)):
        myHashS[s[i]]=1+myHashS.get(s[i],0)
        myHashT[t[i]]=1+myHashT.get(t[i],0)
    if myHashS.keys()==myHashT.keys():
        for i in myHashS:
            currValueS=myHashS[i]
            currValueT=myHashT[i]
            if currValueS!=currValueT:
                print("False")
    else:
        print("False")
else:
    print("False")

print("true")