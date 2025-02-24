from collections import Counter
strs=['eat','tea','tan','ate','nat','bat']
def isAnagram(stringOne,stringTwo):
    return Counter(stringOne)==Counter(stringTwo)
def groupAnagrams(strs):
    arr=[0]*len(strs)
    ans=[]
    for i in range(len(strs)):
        currArr=[]
        if arr[i]==0:
            currArr.append(strs[i])
            arr[i]+=1
            for j in range(len(strs)):
                if i!=j and isAnagram(strs[i],strs[j]) and arr[j]==0:
                    currArr.append(strs[j])
                    arr[j]+=1
            ans.append(currArr)
    return ans

print(groupAnagrams(strs))