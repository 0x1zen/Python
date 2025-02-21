nums=[1,2,3,1]

def containsDuplicates(nums):
    my_arr=nums
    my_arr.sort()
    n=len(my_arr)
    for i in range(0,n-1):
        if(my_arr[i]==my_arr[i+1]):
            return True
    return False        
print(containsDuplicates(nums))