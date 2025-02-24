nums=[2,7,11,15]
target=9

def twoSum(nums,t):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return -1
print(twoSum(nums,target))