#2760. Longest Even Odd Subarray With Threshold

class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        max_length = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and len(nums) > 1 and nums[i] <= threshold:
                length = 1
                for j in range(i,len(nums)-1):
                    if nums[j+1] <= threshold and nums[j] % 2 != nums[j + 1] % 2: 
                        length += 1
                    else: 
                        break
                max_length = max(max_length, length)
            elif len(nums) == 1:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    max_length = 1
                    break
                else:
                    max_length = 0
                    break
        return max_length
s = Solution()
nums = [3,2,5,4]

#some test cases
'''[1,2]
[2,3,4,5]
[4]
[2]
[1,6]'''

threshold = 5
print(s.longestAlternatingSubarray(nums, threshold))