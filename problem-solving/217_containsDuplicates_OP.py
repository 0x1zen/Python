
nums=[3,3]

def containsDuplicates(nums):
    hashset=set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)     
    return False   

print(containsDuplicates(nums))

