#1672.Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts):
        '''max = 0  

        mysolutiion starts from here
        
        sum = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            if sum >= max:
                max = sum
        return max'''

        #found a cool way to solve the problem
        return max(map(sum, accounts))


s = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(s.maximumWealth(accounts))
