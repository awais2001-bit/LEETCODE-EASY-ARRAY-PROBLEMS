#1672.Richest Customer Wealth

class Solution:
    def maximumWealth(self, nums):
        max = 0
        sum = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(len(nums[i])):
                sum += nums[i][j] 
            if sum >= max:
                max = sum
        return(max)

s = Solution()
nums = [[1,5],[7,3],[3,5]]
print(s.maximumWealth(nums))
        