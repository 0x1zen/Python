nums=[1,1,1,2,2,3]
k=2
def topKFrequent(nums,k):
    myHash={}
    ans=[]
    for i in nums:
        if i in myHash:
            myHash[i]+=1
        else:
            myHash[i]=1
    print(myHash)
    while k>0:
        max_key=max(myHash,key=myHash.get)
        print(max_key)
        k-=1
    return ans

# print(topKFrequent(nums,k))
topKFrequent(nums,k)