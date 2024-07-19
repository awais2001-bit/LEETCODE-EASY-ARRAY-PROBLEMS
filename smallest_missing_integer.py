#2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

class Solution:
    def missingInteger(self, nums):
        longest_seq_prefix = []
        current_seq_prefix = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_seq_prefix.append(nums[i])
            else:
                break
        longest_seq_prefix = current_seq_prefix
        seq_sum = sum(longest_seq_prefix)
        x = seq_sum
        while x in nums:
            x += 1
        return x

s = Solution()
nums = [1,2,3,2,5]
#nums = [3,4,5,1,12,14,13]
print(s.missingInteger(nums)) 