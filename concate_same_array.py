#concate array

def concatination(nums):
    for i in range(len(nums)):
            nums.append(nums[i])
    return nums
nums = [1,2,3,4]
print(concatination(nums))
        