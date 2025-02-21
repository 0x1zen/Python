
nums=[1,2,3,1]

def containsDuplicates(nums):
    hashset=set(nums)
    if len(hashset)<len(nums):
        return True
    return False   

print(containsDuplicates(nums))

