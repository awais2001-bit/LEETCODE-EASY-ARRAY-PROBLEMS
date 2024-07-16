#remove Duplicates

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    del nums[j]
                else:
                    j += 1
            i += 1
        return len(nums)

s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = s.removeDuplicates(nums)
print(new_length)  
print(nums[:new_length])  
