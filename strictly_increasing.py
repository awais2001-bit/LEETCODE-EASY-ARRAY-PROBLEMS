#Strictly Increasing

class Solution:
    def can_be_increasing(self,nums):
        for i in range(len(nums)):
            result = True
            answer = nums[:i] + nums[i+1:]
            for j in range(len(answer)-1):
                if answer[j] >= answer[j+1]:
                    result = False
            if result:
                return True
        return False


s = Solution()
#nums = [1,2,10,5,7]
nums = [2,3,1,2]
print(s.can_be_increasing(nums))
