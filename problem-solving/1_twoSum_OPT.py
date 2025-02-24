nums=[2,7,11,15]
target=9

def twoSum(nums,t):
    prevMap={}
    for i,n in enumerate(nums):
        diff=target-nums[i]
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n]=i

print(twoSum(nums,target))