nums=[3,3]

def containsDuplicates(nums):
    for i in range(len(nums)):
        currentNum=nums[i]
        for j in range(len(nums)):
            if(currentNum==nums[j] and i!=j):
                return True
    return False        
            
print(containsDuplicates(nums))

