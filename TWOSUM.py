#code which is givng integers
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
nums = [2,5,6,7,2]
target = 4
ret = Solution().twoSum(nums,target)
print(ret)   

        