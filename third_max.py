#414. Third Maximum Number

class Solution:
    def thirdMax(self, nums):
        l = list(set(nums))
        l.sort()
        if len(l)>=3:
            return l[len(l)-3]
        return max(l) 
s = Solution()
nums = [1,2,3,6,8,9,10]
print(s.thirdMax(nums))
        